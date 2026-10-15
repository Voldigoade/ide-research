# Realistic extension configurations

## VS Code

| Need | Extension or built-in feature | Installation | Publisher/rights review |
|---|---|---|---|
| Rust language intelligence | rust-analyzer | Install extension; Rust toolchain and rust-analyzer required | Verify official Rust project publisher and extension license |
| Rust debugging | CodeLLDB | Install extension and LLDB toolchain as needed | Third-party extension; inspect repository and rights |
| Python | Python and Python Debugger | Install extensions; interpreter/environment configuration remains | Microsoft publisher; extension terms differ from VS Code license |
| TypeScript, React, Next.js | TypeScript/JavaScript support built in; framework additions optional | No core TS extension required | Add only project-specific formatter/linter |
| Tauri | Tauri extension | Install if its commands improve workflow | Tauri project publisher and extension license |
| WSL / SSH / containers | Remote WSL, Remote SSH, Dev Containers | Install required extensions; configure WSL, SSH, Docker | Microsoft-published extensions |
| Database | SQL or vendor driver extension | Choose by DB engine | High variation in maintenance, telemetry, and license |
| GitHub | GitHub Pull Requests | Optional extension | GitHub-specific permissions and account scope |
| AI | GitHub Copilot or external CLI/ACP/MCP agent | Optional/configured separately | Separate subscription, provider, privacy, quota and tool permissions |

Estimate: 6 to 10 critical extensions for the full requested stack. TypeScript and Git basics are built into VS Code, but Rust debug, Python, Tauri, remote, containers and project-specific quality tools expand the extension surface.

## IntelliJ IDEA Ultimate 2026.2

- Install/enable official Rust and Python plugins.
- JS/TS, React, Next.js and Node tools are provided by the IDE edition.
- Database tools, Docker, Git, Dev Containers and remote development are integrated or supported through JetBrains tooling.
- AI Assistant provides Codex, Claude Agent, Junie and ACP agents. JetBrains Air in IDEs is a separate EAP plugin as of 2026-10-15; its docs describe local/ACP agents and WSL execution for custom agents. GitHub Copilot is installed as a separate Marketplace plugin. MCP client/server, BYOK and local models are documented; local models cannot run agents. Review model and subscription terms.
- Review AI Assistant provider/data terms separately from the IDE license.

Estimate: 2 to 4 essential plugin/configuration additions. This is the strongest one-product native composition in JetBrains for the polyglot stack. Product feature parity and performance still require testing on the user's actual project.

## RustRover and PyCharm

RustRover's Rust engine is integrated. Add Python plugin/tooling only if Python becomes regular; JS/TS support exists, while complete Next.js parity was not established in reviewed docs. PyCharm Pro integrates Python, DB and remote workflows; install the official Rust plugin for secondary Rust work. Check plugin compatibility after version upgrades.

## VSCodium

Use Open VSX by default. Extension ID and publisher must match expected code. Some Microsoft extensions and service-bound components may be absent or require a manual distribution flow. Do not assume marketplace parity with VS Code.

## Cursor, Zed, Kiro, Devin, Antigravity

These ship more agent/editor features natively, but language intelligence still depends on embedded language servers, extensions, adapters or external tools. Confirm marketplace source, update cadence, license, privacy, model choice, data retention and permission boundaries per plan.

## Sublime Text 4 Build 4213

Install Package Control packages LSP, LSP-rust-analyzer, LSP-typescript, a Python LSP such as pyright, Debugger and the Python Debugger package; add adapter/configuration for the desired Rust/Python debugger. Tauri uses the Rust and TypeScript LSPs plus external Cargo/npm tasks. Docker syntax is available by package; no first-party Dev Containers/Remote SSH/WSL workspace service or integrated database suite was established. The SFTP package transfers files and is not equivalent to VS Code Remote SSH. WSL folder access over the Windows share has community-reported file notification limitations.

Estimate: 6 to 9 packages/tools, with more manual maintenance than VS Code and IDEA. Package Control is a distribution/maintenance channel, not a guarantee that all packages have one publisher or license.

## Neovim

A likely stack includes nvim-lspconfig, rustaceanvim or equivalent Rust support, nvim-dap, nvim-treesitter, a completion engine, formatter, Git interface, file navigation, SQL plugin, and optional agent integration. 8 to 12 components is a practical estimate. Each plugin is a separate executable dependency. Verify owner, license, release/activity, transitive tools and permissions.

## JetBrains Air is not a separate code engine

JetBrains Air is evaluated as an agent system and Air in IDEs as an EAP plugin, not as another language IDE. Air in IDEs runs local or ACP agents inside IntelliJ-based IDEs; it does not replace Rust, Python, web or database language tooling. Treat agent/provider authorization and workspace permissions separately from the JetBrains IDE license.

## Supply chain and license rule

An extension marketplace is a distribution path, not a security certification. Install the minimum set, verify exact publisher/repository, examine update and permission behavior, and keep a rollback path. Plugin licenses do not inherit the IDE license.

For date-stamped software and AI plan prices, personal versus commercial terms, and token-cost caveats, see [`pricing.md`](pricing.md).
