# Sources et retours de terrain

Les sources sont gardées dans [`data/sources.json`](https://github.com/Voldigoade/ide-research/blob/main/data/sources.json). Le fichier associe un identifiant stable, un titre, un éditeur, un type, une URL, une date de vérification et une classe d'évidence. Les sources constructeur établissent les capacités documentées, pas une preuve indépendante de sécurité, confidentialité ou performance.

## Sources centrales

- [Nouveautés VS Code 1.142](https://code.visualstudio.com/updates/v1_142), plus documentation [Remote](https://code.visualstudio.com/docs/remote/remote-overview), [WSL](https://code.visualstudio.com/docs/remote/wsl) et [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers).
- JetBrains 2026.2: [Rust and RustRover parity](https://www.jetbrains.com/help/idea/rust-plugin.html), [Codex/Claude Agent and ACP](https://www.jetbrains.com/help/ai-assistant/activate-agents.html), [MCP](https://www.jetbrains.com/help/ai-assistant/mcp.html), [BYOK](https://www.jetbrains.com/help/ai-assistant/bring-your-own-key-byok.html), [local models](https://www.jetbrains.com/help/ai-assistant/use-custom-models.html), [Air agents in WSL](https://www.jetbrains.com/help/air-ides/air-manage-agents.html), and the [WSL architecture measurement](https://blog.jetbrains.com/platform/2026/09/the-evolution-of-wsl-support-in-jetbrains-ides/).
- JetBrains: [Rust](https://www.jetbrains.com/help/idea/rust-plugin.html), [Python](https://www.jetbrains.com/help/idea/python.html), [TypeScript](https://www.jetbrains.com/help/idea/javascript.html), [React](https://www.jetbrains.com/help/idea/react.html), [base de données](https://www.jetbrains.com/help/idea/database-tool-window.html), [Dev Containers](https://www.jetbrains.com/help/idea/dev-containers.html) et [ACP](https://www.jetbrains.com/help/idea/acp.html).
- VSCodium: [build source](https://github.com/VSCodium/vscodium) et [extensions](https://github.com/VSCodium/vscodium/blob/master/docs/extensions.md).
- Cursor: [changelog](https://cursor.com/changelog), [prix](https://cursor.com/pricing), [utilisation des données](https://cursor.com/en-US/data-use).
- Zed: [versions stables](https://zed.dev/releases/stable), [privacy IA](https://zed.dev/docs/ai/privacy-and-security), [modèles locaux](https://github.com/zed-industries/zed/blob/main/docs/src/ai/use-a-local-model.md), [remote](https://github.com/zed-industries/zed/blob/main/docs/src/remote-development.md).
- [Neovim LSP](https://neovim.io/doc/user/lsp), [Theia](https://theia-ide.org/docs/), [Kiro](https://kiro.dev/docs/), [Antigravity](https://antigravity.google/docs), [Tauri](https://v2.tauri.app/).

## Retours de terrain

Les pages Reddit, Hacker News et GitHub Issues sont des exemples qualitatifs sélectionnés pour couvrir des migrations et problèmes opposés. Aucun nombre de commentaires ou de votes n'est traité comme mesure d'adoption ou de fréquence.

| Sujet | Page | Lecture prudente |
|---|---|---|
| RustRover vers VS Code | [r/rust](https://www.reddit.com/r/rust/comments/1wepy3p/about_rust_rover/) | Signale l'avantage des infos Cargo et une recherche manuelle plus fréquente sous VS Code; témoignage individuel. |
| VS Code et RustRover | [r/rust](https://www.reddit.com/r/rust/comments/16hiw6o/introducing_rustrover_a_standalone_rust_ide_by/) | Contraste vitesse/error messages d'un utilisateur avec refactorings JetBrains. Page ancienne, pas un test version 2026. |
| Workflow Rust 2026 | [r/rust](https://www.reddit.com/r/rust/comments/1r4jz1b/my_rust_development_workflow_in_2026/) | Compare configurations d'éditeur; opinions divergentes et contexte individuel. |
| VS Code et Zed | [r/vscode](https://www.reddit.com/r/vscode/comments/1thib4i/i_still_dont_understand_the_hype_around_zed_over/) | Évoque vitesse/recherche versus extensions et habitudes; non représentatif. |
| Mémoire Zed | [Issue 49168](https://github.com/zed-industries/zed/issues/49168), [Issue 46434 WSL](https://github.com/zed-industries/zed/issues/46434), [Issue 60134 ACP](https://github.com/zed-industries/zed/issues/60134) | Problèmes circonstanciés; les issues ne prouvent pas la fréquence ni qu'un problème reste ouvert dans la version la plus récente. |
| Cursor et agents | [Hacker News](https://news.ycombinator.com/item?id=47618084) | Montre certains workflows Cursor vers Claude Code/Zed et le maintien d'un éditeur classique; échantillon volontaire. |



Les retours qualitatifs et migrations pour le top 5 sont résumés dans [les avis de terrain](../research/community-field-reports.md). Ils servent de pistes, pas de décompte de préférence.
