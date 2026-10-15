---
description: "Previous verdict: CONFIRMED WITH RESERVATIONS."
---

# Audit result

## Decision

**Previous verdict: CONFIRMED WITH RESERVATIONS.** Visual Studio Code remains the balanced model winner for Rust/Tauri, TypeScript/React, Python, GitHub, WSL2, SSH and containers. Its score range overlaps IntelliJ IDEA Ultimate 2026.2, the strongest realistic challenger. This result supports the prior choice without treating its lead as robust.

The updated shortlist has 12 products: VS Code, IntelliJ IDEA Ultimate, RustRover, PyCharm Professional, VSCodium, Cursor, Zed, Neovim, Sublime Text 4, Devin Desktop, Kiro and Google Antigravity. The most important change is restoring IDEA after checking the 2026.2 plugin combination. Sublime Text takes the finalist place previously considered for Theia. Eclipse Theia IDE is itself a downloadable desktop product for Windows, Linux, and macOS; it remains screened out because this source set does not establish low-friction coverage of the full Rust/Tauri, web, Python, database, WSL/SSH, container, and external-agent workflow in its packaged extension set.

Under the uncertainty model used in this study, VS Code ranked first in 59% of combined sensitivity runs and IntelliJ IDEA Ultimate in 41%. These frequencies describe the stability of the chosen editorial model; they are not objective probabilities that either IDE is the best in real use.

## Scenario winners

| Profile | Indicative winner | Main reason |
|---|---|---|
| Balanced polyglot | VS Code | Broad stack and consistent remote workflow |
| Rust and Tauri dominant | RustRover | Focused Rust/Cargo engine and debugging |
| Web/full stack | VS Code | Web ecosystem, extensions and remote support |
| Python heavy | PyCharm Professional | Python analysis, refactoring, tests and debugging |
| AI-agent dominant | Devin Desktop by model midpoint; IDEA close | A complete editor with a central agent leads; intervals overlap |
| Privacy/local-first | Neovim by model midpoint; VSCodium for a GUI | Local control with a higher setup cost |
| Remote/WSL | VS Code | Broadest documented WSL, SSH and Dev Containers path |
| Windows | VS Code | WSL and ecosystem integration |
| Linux | VS Code | Broad fit; RustRover for Rust-only work |
| macOS | VS Code | Balanced; Zed is a native alternative |

## JetBrains reassessment

IntelliJ IDEA Ultimate 2026.2 can combine official Rust and Python plugins with JavaScript/TypeScript, React, Next.js, databases, Docker, Dev Containers, WSL, remote development and Git. JetBrains states that its Rust plugin maintains feature parity with RustRover; its comparison identifies debugger, profiler and setup differences. IDEA requires the free Native Debugging Support plugin for LLDB/GDB. The official Python plugin implements PyCharm functionality. This is a strong single-IDE configuration, but plugin feature parity does not establish identical ergonomics or performance on a real monorepo. See the [price and license table](pricing.md): IDEA Ultimate is $199/year for the first individual annual term, then $159 and $119/year; All Products Pack is $299/$239/$179 per year and includes the separate IDEs and AI Pro.

AI Assistant documents Codex, Claude Agent and Junie, BYOK for selected providers, local Ollama/LM Studio models for supported features, and MCP client/server functionality. Local models cannot run agents or call the configured MCP tools. GitHub Copilot is a separate official Marketplace plugin.

JetBrains Air is now an agent system across JetBrains IDE, web, CLI and mobile surfaces. Air in IDEs became a separate early-access plugin in October 2026. It supports local agents and ACP and documents a WSL execution setup. This strengthens IDEA's agent workflow; Air is not counted as a separate language IDE or code engine. Its model/provider permissions and terms remain separate.

RustRover remains the Rust specialist, while PyCharm Professional is the Python specialist. Both remain separate candidates rather than treating JetBrains as one product.

## Agentic environments

Cursor, Devin Desktop, Kiro and Antigravity are complete editing environments, not agent-only command wrappers. The comparison still checks language support, Git, debugging, extensions, WSL/remote, platforms, maturity, privacy, pricing and usefulness with AI off. A capable agent alone does not make an otherwise weak IDE the winner. See the [agent and protocol matrix](agents.md).

## Rechecked exclusions

| Candidate | 2026 check and decision |
|---|---|
| Fleet | Standalone downloads ended in December 2025; JetBrains says Fleet became Air in May 2026. Air is evaluated as an agent layer. |
| Air | Air in IDEs is an EAP agent plugin, not a separate Rust/Python/TypeScript IDE; count it with IDEA. |
| Nova | Still an active native Mac editor with 2026 docs, but macOS-only for a one-environment cross-platform profile. |
| Lapce | Version 0.4.6 and October nightlies; Rust, TypeScript, Python and SQLite plugins plus SSH remote exist. The current remote docs still require a terminal command for opening workspaces after the UI rewrite, WSL folder-picker support remains a reported gap, and integrated DAP/database/container breadth is weaker. Exclusion is confirmed with a corrected rationale, not poor polyglot coverage. |
| Helix | Latest stable release announcement found is 25.07; built-in LSP/tree-sitter are strong, but DAP is experimental and remote/database/container tooling is weaker for this profile. |
| Eclipse Theia IDE | A concrete desktop IDE with Windows, Linux, and macOS downloads. Excluded on evidence and fit: its packaged feature set is selected and the retained sources do not establish the full required stack and remote/container integrations. |
| Sublime Text | Reinstated: Build 4215 and current Rust/TypeScript LSP and DAP/Python-debug packages justify a final place. First-party WSL, Dev Containers and Remote SSH workspace coverage remains weaker. |
| Emacs | Technically capable but requires a large custom package/configuration stack; Neovim already represents the local terminal path for this shortlist. |

## Performance and field reports

No cross-IDE controlled benchmark was found or run. JetBrains publishes a scoped five-run WSL comparison on Windows 11, Ubuntu 24.04 under WSL2, IDEA Ultimate 263.SNAPSHOT and Spring Framework (23 subprojects, 8,191 files), comparing IJent with the older 9P path. It reports improvements to cold open, traversal, indexing and file reads. This is a vendor measurement of its WSL transport change, not a comparison between IDEs.

Recent community reports describe JetBrains refactoring/debugger strengths, VS Code startup/configuration and extension trade-offs, PyCharm migration in both directions, Neovim configuration and VS Code migrations, and specific Zed WSL/memory issues. These are self-selected field reports, not prevalence or controlled measurements. VSCodium migration reports are sparse.

The AWS advisory for Kiro CVE-2026-95985 affects versions before 1.0.242 and says it was fixed in 1.0.242. The reviewed Kiro 1.3.0 version is later; this is a patched historical issue, not evidence of current exposure. Users of affected versions should review global configuration as AWS recommends.

Detailed [candidate decisions](https://github.com/Voldigoade/ide-research/blob/main/research/market-scan.md), [scores and scenarios](../scenarios.md), [sensitivity](https://github.com/Voldigoade/ide-research/blob/main/research/sensitivity.md), [duels](https://github.com/Voldigoade/ide-research/blob/main/research/duels-top-five.md), and [sources](../sources.md) are available.
