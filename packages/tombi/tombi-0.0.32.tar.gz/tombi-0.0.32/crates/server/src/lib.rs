mod backend;
mod document;
mod handler;
mod hover;
mod semantic_tokens;
mod toml;

use backend::Backend;
use config::TomlVersion;

/// Run TOML Language Server
#[derive(Debug)]
#[cfg_attr(feature = "clap", derive(clap::Args))]
pub struct Args {
    /// TOML version.
    #[cfg_attr(feature = "clap", arg(long, value_enum, default_value = None))]
    toml_version: Option<TomlVersion>,
}

pub async fn serve(args: impl Into<Args>) {
    tracing::info!(
        "Tombi LSP Server Version \"{}\" will start.",
        env!("CARGO_PKG_VERSION")
    );

    let stdin = tokio::io::stdin();
    let stdout = tokio::io::stdout();
    let args = args.into();

    let (service, socket) = tower_lsp::LspService::build(|client| {
        crate::backend::Backend::new(client, args.toml_version)
    })
    .custom_method("tombi/getTomlVersion", Backend::get_toml_version)
    .finish();

    tower_lsp::Server::new(stdin, stdout, socket)
        .serve(service)
        .await;

    tracing::info!("Tombi LSP Server did shut down.");
}
