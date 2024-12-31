use anyhow::{bail, Context};
use archive_to_parquet::Converter;
use archive_to_parquet::{
    new_record_batch_channel, ConvertionOptions, IncludeType, ProgressBarConverter,
};
use byte_unit::Byte;
use clap::Parser;
use indicatif::MultiProgress;
pub use parquet::basic::Compression as ParquetCompression;
use std::fs::File;
use std::io::{stderr, BufRead, BufWriter, Stderr, Write};
use std::num::NonZeroUsize;
use std::path::PathBuf;
use tracing::{error, info, Level};
use tracing_subscriber::fmt::MakeWriter;
use tracing_subscriber::{fmt, layer::SubscriberExt, util::SubscriberInitExt, EnvFilter};

pub fn default_threads() -> NonZeroUsize {
    std::thread::available_parallelism().unwrap_or(NonZeroUsize::new(1).unwrap())
}

const DEFAULT_OPTS: ConvertionOptions = ConvertionOptions::const_default();

#[derive(Debug, Clone, Parser)]
struct Args {
    /// Output Parquet file to create
    output: PathBuf,

    /// Input paths to read. Pass "-" to read paths from stdin
    #[clap(required = true)]
    paths: Vec<PathBuf>,

    /// Min file size to output.
    /// Files below this size are skipped
    #[clap(long)]
    min_size: Option<Byte>,

    /// Max file size to output.
    /// Files above this size are skipped.
    #[clap(long)]
    max_size: Option<Byte>,

    /// Only output unique files by hash
    #[clap(long)]
    unique: bool,

    /// Only output text files, skipping binary files
    #[clap(long, value_enum, default_value_t=DEFAULT_OPTS.include)]
    include: IncludeType,

    /// Number of threads to use when extracting.
    /// Defaults to number of CPU cores
    #[clap(long, default_value_t = default_threads())]
    threads: NonZeroUsize,

    /// Compression to use
    #[clap(long, default_value_t = DEFAULT_OPTS.compression)]
    compression: ParquetCompression,

    /// Number of batches to buffer in memory at once.
    #[clap(long, default_value_t = DEFAULT_OPTS.batch_count)]
    batch_count: usize,

    /// Maximum size of each batch in memory.
    #[clap(long, default_value = "100MB")]
    batch_size: Byte,

    /// Log file to write messages to
    #[clap(long)]
    log_file: Option<PathBuf>,
}
fn main() -> anyhow::Result<()> {
    let args = Args::parse();
    do_main(args)?;
    Ok(())
}
fn do_main(args: Args) -> anyhow::Result<()> {
    let options = ConvertionOptions::new(
        args.threads,
        args.include,
        args.unique,
        args.compression,
        args.min_size,
        args.max_size,
        args.batch_count,
        args.batch_size,
    );

    let channel = new_record_batch_channel(options.batch_count);

    let mut converter = ProgressBarConverter::new(options);
    let (tracing_writer, _guard) = match args.log_file {
        None => {
            let writer = TracingProgressWriter::new(converter.progress().clone(), stderr());
            tracing_appender::non_blocking(writer)
        }
        Some(p) => {
            let file = File::create(&p).with_context(|| format!("Creating log file {:?}", p))?;
            tracing_appender::non_blocking(BufWriter::new(file))
        }
    };
    setup_tracing(tracing_writer)?;

    let paths = if args.paths.len() == 1 && args.paths[0].to_string_lossy() == "-" {
        info!("Reading paths from stdin");
        std::io::stdin()
            .lock()
            .lines()
            .map(|line| line.map(PathBuf::from))
            .collect::<Result<Vec<_>, _>>()
            .context("Reading paths from stdin")?
    } else {
        args.paths
    };

    let limit = rlimit::increase_nofile_limit((paths.len() * 100) as u64)?;
    info!("Increased open file limit to {}", limit);
    info!("Converting {} files to Parquet", paths.len());
    info!("Options: {}", converter.options());

    for path in paths {
        converter
            .add_paths([&path], &channel)
            .with_context(|| format!("Adding path {path:?}"))?;
    }

    let output_file =
        File::create(&args.output).with_context(|| format!("Creating file {:?}", args.output))?;

    let counts = converter
        .convert(output_file, channel)
        .context("Converting")?;
    if counts.output_rows == 0 {
        error!("No rows written to output file. Raw stats: {counts:#?}");
        bail!("No rows written to output file");
    }

    Ok(())
}

fn setup_tracing(writer: impl Write + Sync + Send + Clone + 'static) -> anyhow::Result<()> {
    let env_filter = EnvFilter::builder()
        .with_default_directive(Level::INFO.into())
        .from_env()
        .context("Setting up tracing environment filter")?;
    tracing_subscriber::registry()
        .with(
            fmt::layer()
                .compact()
                .with_file(false)
                .with_thread_ids(true)
                .with_writer(move || writer.clone()),
        )
        .with(env_filter)
        .init();
    Ok(())
}

// Utils for making tracing and indicatif work together
#[derive(derive_new::new)]
struct TracingProgressWriter {
    progress: MultiProgress,
    writer: Stderr,
}

impl Clone for TracingProgressWriter {
    fn clone(&self) -> Self {
        Self {
            progress: self.progress.clone(),
            writer: stderr(),
        }
    }
}

impl MakeWriter<'_> for TracingProgressWriter {
    type Writer = TracingProgressWriter;

    fn make_writer(&self) -> Self::Writer {
        self.clone()
    }
}

impl Write for TracingProgressWriter {
    fn write(&mut self, buf: &[u8]) -> std::io::Result<usize> {
        self.progress.suspend(|| self.writer.write(buf))
    }

    fn flush(&mut self) -> std::io::Result<()> {
        self.progress.suspend(|| self.writer.flush())
    }
}
