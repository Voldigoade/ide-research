# IDE comparison: adversarial audit

**Audit date:** 2026-10-15  
**Previous verdict:** CONFIRMED WITH RESERVATIONS  
**Balanced recommendation:** Visual Studio Code, with an overlapping and model-sensitive lead over IntelliJ IDEA Ultimate.

This is a continuation of the earlier approximately 40-candidate scan. The existing source set and user profile are retained. The main correction is that IntelliJ IDEA Ultimate 2026.2 can combine JetBrains' official Rust and Python plugins with web, database, container, WSL, remote, Git, and agent tooling. The first verdict survives, but its reasoning and margin need correction.

## Previous finalists, reinstatements, and exits

The updated shortlist deliberately has twelve candidates to preserve likely scenario winners: VS Code, IntelliJ IDEA Ultimate, RustRover, PyCharm Professional, VSCodium, Cursor, Zed, Neovim, Sublime Text 4, Devin Desktop, Kiro, and Google Antigravity. IDEA is restored as a leading challenger. RustRover and PyCharm remain because their dedicated language workflows can win specialist profiles. Agentic products are retained only as complete editing environments, not on agent quality alone. VSCodium, Zed, Neovim, and Sublime Text remain for local control, native editing, terminal workflows, or extensibility.

Fleet is a confirmed exit because standalone distribution ended. Nova is macOS-only, so it cannot serve the cross-platform Windows/WSL/Linux profile. Lapce, Helix, Emacs, and an independent Air entry have larger gaps or represent an agent layer rather than a code IDE. Theia remains outside the final because its distribution-dependent capability profile is not one installable product. Sublime Text was reinstated after checking its current LSP and DAP packages; see `market-scan.md`.

## JetBrains, evaluated separately

IntelliJ IDEA Ultimate 2026.2 deserves a final place. JetBrains states that the IDEA Rust plugin maintains feature parity with RustRover, while its comparison documentation lists setup, debugger, and profiler differences. LLDB/GDB debugging requires the free Native Debugging Support plugin. The official Python plugin implements PyCharm functionality. IDEA also documents TypeScript, React, Next.js, database tools, Docker, Dev Containers, WSL, SSH/Remote Development, and Git. This makes a single IDE configuration capable of combining most of the relevant JetBrains language and workflow features. It does not prove identical ergonomics across products or equivalent performance on the user's repository.

AI integrations have materially changed: AI Assistant documents Codex, Claude Agent, Junie, and ACP-compatible agents; JetBrains Air can run ACP agents and documents a Linux agent executable inside WSL; the official GitHub Copilot plugin is separate. IDEA provides an MCP server/client workflow. BYOK is available for selected providers and agents. Ollama and LM Studio can power supported AI Assistant features, but current documentation says agents cannot use local models and local models cannot call configured MCP tools. A local model option therefore does not make the agent workflow fully local. Confirm current commercial licensing and separate AI service costs before purchase.

RustRover remains the strongest dedicated Rust/Cargo contender, but its broader Python and Next.js fit is weaker than IDEA or VS Code. PyCharm Professional remains the Python specialist with Rust as a secondary plugin workflow. Product-level plugins, price, rights, and practical dependencies are detailed in `extensions.md` and `agent-compatibility.md`.

## Updated top five

| Rank | Candidate | Combined model win frequency | Median rank | Score p10 to p90 |
|---:|---|---:|---:|---:|
| 1 | Visual Studio Code | 59% | 1.0 | 8.5 to 8.8 |
| 2 | IntelliJ IDEA Ultimate | 41% | 2.0 | 8.5 to 8.7 |
| 3 | VSCodium | 0% | 3.0 | 8.2 to 8.4 |
| 4 | PyCharm Professional | 0% | 4.0 | 8.2 to 8.4 |
| 5 | Neovim | 0% | 5.0 | 7.9 to 8.3 |

The 20,000-draw frequencies describe stability of this editorial model, not market probability or user satisfaction. The score ranges are subjective bounds, not confidence intervals from a benchmark. VS Code and IDEA overlap materially; the lead is real in the chosen model but not decisive evidence of a universal winner.

## Profile scenarios

| Scenario | Stack mix: Rust / Tauri / web / Python / other | Median winner range | Runner-up range | Overlap |
|---|---|---|---|---|
| Balanced polyglot | 25% / 10% / 30% / 20% / 15% | Visual Studio Code (8.0 to 9.3) | IntelliJ IDEA Ultimate (8.0 to 9.2) | yes |
| Rust and Tauri dominant | 55% / 25% / 10% / 5% / 5% | RustRover (8.1 to 9.3) | Visual Studio Code (7.9 to 9.2) | yes |
| Web and full stack | 8% / 10% / 60% / 15% / 7% | Visual Studio Code (8.2 to 9.5) | IntelliJ IDEA Ultimate (8.3 to 9.4) | yes |
| Python heavy | 10% / 5% / 15% / 60% / 10% | IntelliJ IDEA Ultimate (8.4 to 9.5) | PyCharm Professional (8.6 to 9.3) | yes |
| AI agents dominant | 15% / 7% / 30% / 20% / 28% | Devin Desktop (7.5 to 9.3) | IntelliJ IDEA Ultimate (7.7 to 9.0) | yes |
| Privacy and local first | 25% / 10% / 25% / 20% / 20% | Neovim (7.3 to 9.3) | VSCodium (7.3 to 9.1) | yes |
| Remote and WSL | 18% / 8% / 28% / 20% / 26% | Visual Studio Code (8.1 to 9.4) | IntelliJ IDEA Ultimate (7.9 to 9.0) | yes |
| Windows first | 20% / 8% / 28% / 20% / 24% | Visual Studio Code (8.0 to 9.4) | IntelliJ IDEA Ultimate (7.9 to 9.1) | yes |
| Linux first | 25% / 8% / 25% / 20% / 22% | Visual Studio Code (7.9 to 9.3) | IntelliJ IDEA Ultimate (7.8 to 9.1) | yes |
| macOS first | 20% / 8% / 28% / 20% / 24% | Visual Studio Code (7.9 to 9.3) | IntelliJ IDEA Ultimate (7.8 to 9.1) | yes |

Stack composition changes per scenario. Rust/Tauri is explicitly 55% Rust plus 25% Tauri; web/full-stack assigns 60% web; the AI-agent scenario changes the agent workflow weight; local-first emphasizes privacy and security. Windows, Linux, and macOS are separate profiles. Full scenario weights and results are reproducible from `data/scenarios.json` and `model-results.json`.

## Agentic editors are complete IDE candidates

Cursor, Devin Desktop, Kiro, and Antigravity are assessed as editing environments as well as agent products. They differ in architecture, extensions, debugging, Git, OS and WSL/remote fit, maturity, privacy, pricing, and usefulness with AI disabled. VS Code, JetBrains IDEs, Zed, Neovim, and other extensible editors can also host agents or agent protocols. The feature matrix in `agent-compatibility.md` distinguishes native features, plugins, external CLIs, ACP, MCP, BYOK, and local models.

## Performance evidence

- **MEASURED:** JetBrains reports five runs on Windows 11, WSL2 Ubuntu 24.04, IntelliJ IDEA Ultimate 263.SNAPSHOT, and the Spring Framework tree (23 subprojects, 8,191 files). For native IJent versus the previous 9P file path it reports cold open 18.5 to 11.5 seconds, tree traversal 8.1 to 3.7 seconds, indexing 10.8 to 8.4 seconds, and file read 12.2 to 5.7 seconds. This is a vendor measurement of its WSL transport change, not an independent IDE comparison.
- **CORROBORATED:** official product documentation establishes which language engines, indexers, debuggers, remote hosts, and containers are supported. It does not establish comparative startup, RAM, CPU, input latency, search, monorepo, or branch-switch performance.
- **RECURRING TESTIMONY:** reports from Rust users describe trade-offs between RustRover analysis/refactoring and Rust Analyzer startup or resource use. Zed issues report specific WSL memory, project-search memory, and ACP memory problems. These reports are self-selected and do not establish prevalence.
- **INFERENCE:** local repository size, extension set, language-server version, filesystem placement, and OS can dominate the experience. A short controlled trial on the actual project is the best remaining performance evidence.

Selected field reports and issue threads are indexed in `data/sources.json` and `evidence-register.md`. They are leads, not vote counts.

## Security, privacy, cost, and dependency burden

Treat editor extensions, language servers, MCP tools, ACP agents, shell CLIs, and cloud agents as separate trust boundaries. Any of them can receive source context or execute code depending on configuration. Local model support reduces some provider exposure but does not secure the endpoint or plugins. Open source and privacy modes do not prove zero telemetry or safety.

The source register records AWS advisory CVE-2026-95985 for Kiro versions before 1.0.242. AWS states it was fixed in 1.0.242; the reviewed Kiro 1.3.0 release is later. This is a patched historical issue, not evidence that the current reviewed version remains vulnerable. Users who ran affected versions with untrusted workspaces should follow the vendor's configuration review guidance.

Minimal extension/plugin configurations and estimated critical dependency counts are in `extensions.md`. The dated price snapshot and commercial-license distinctions are in `pricing.md`. At the checked individual annual rate, IDEA Ultimate is $199 in year one; JetBrains' All Products Pack is $299 in year one and includes RustRover, PyCharm, Air, and AI Pro. VS Code is free for commercial use, Sublime Text is $99 one-time for a personal license with three years of updates, and agent products have separate quota/usage charges. The model's price criterion remains a broad editorial range and does not assume a paid AI subscription or estimate token use.

## Sensitivity and direct duels

`duels-top-five.md` compares the five best balanced candidates pairwise across all 23 criteria, then adds VS Code/RustRover and IDEA/RustRover. The former #1 versus its strongest challenger, VS Code versus IDEA, is included. Equal ranges are marked Equal; disjoint ranges produce A wins or B wins; overlapping ranges remain Uncertain. The sensitivity report separately varies weights, ratings, and both together.

## Final answer

**If I had to install one environment today for the balanced polyglot profile and stop searching, I would choose: Visual Studio Code.**

It gives the broadest, most consistent cross-platform workflow for Rust/Tauri, TypeScript/React, Python, Git, WSL, SSH, containers, and optional external agents, while remaining fully useful with AI off. IntelliJ IDEA Ultimate 2026.2 is the closest and strongest challenger: its lead deficit is small, the ranges overlap, and JetBrains' official plugin combination now covers far more of the stack than the first report credited. The verdict would most likely reverse if the user's own Rust-heavy monorepo shows IDEA's refactoring/debugging advantage without unacceptable memory or indexing cost, or if the user's workflows rely more heavily on JetBrains integrations than on VS Code remote/extension breadth.
