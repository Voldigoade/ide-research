# Agent and AI integration audit

A product's built-in agent, an extension, a protocol adapter, and a shell CLI have different dependency and trust models. "Yes" means current docs describe the integration, not that the agent is equally capable or safe. "Not established" means reviewed sources do not prove support.

## Current integration status

| Environment | Complete IDE? | Architecture | Codex | Claude Agent/Code | Copilot | ACP | MCP | BYOK/local | Useful with AI off? |
|---|---|---|---|---|---|---|---|---|---|
| VS Code | Yes | Microsoft Code OSS distribution | External CLI/MCP | External CLI/extension | First-party integration | No first-party ACP established | Documented tools | Provider/extension dependent | Yes |
| IntelliJ IDEA Ultimate | Yes | JetBrains integrated IDE with official Rust/Python plugins | AI Assistant; Air in IDEs EAP and ACP | Claude Agent and external Claude Code | Official Marketplace plugin | AI Assistant; Air in IDEs EAP | Built-in server and client | BYOK; Ollama/LM Studio for features, not agents | Yes |
| RustRover | Yes | JetBrains Rust IDE | JetBrains AI/ACP options, verify product version | JetBrains AI/ACP options | Official plugin | AI Assistant/Air | JetBrains MCP | Local models for features, not agents | Strong Rust IDE |
| PyCharm Pro | Yes | JetBrains Python IDE | JetBrains AI/ACP options, verify product version | JetBrains AI/ACP options | Official plugin | AI Assistant/Air | JetBrains MCP | Local models for features, not agents | Strong Python IDE |
| VSCodium | Yes | Community Code OSS, Open VSX | CLI or compatible extension | CLI or compatible extension | Microsoft Marketplace integration not available by default | No first-party ACP established | Extension dependent | Extension dependent | Yes |
| Cursor | Yes | Proprietary VS Code-derived editor | External CLI workflow | External CLI workflow | Not native product integration | Not established in reviewed docs | Agent/tool integration documented | Model options depend on plan | Yes |
| Zed | Yes | Native editor, open source client | External ACP/terminal | External ACP/terminal | No native integration established | Documented | Agent tools | BYOK/provider options and local models documented | Yes |
| Neovim | Configured IDE | Open source terminal editor and LSP | External CLI | External CLI | Community plugin | Plugin dependent | Plugin/agent dependent | CLI/provider dependent | Yes |
| Sublime Text 4 | Yes | Native proprietary editor; Package Control | External CLI | External CLI | No first-party integration established | No native ACP established | No native MCP established | External CLI/extension dependent | Strong text editing; LSP and DAP require packages |
| Devin Desktop | Yes | VS Code-derived editor and Cognition services | External ACP/agent workflow | External ACP/agent workflow | Not established | Documented external agents | Agent dependent | Plan/provider dependent | Editor works; agent-centric |
| Kiro | Yes | Code OSS-derived editor | Current external support needs verification | Current external support needs verification | Not established | Not established in reviewed sources | MCP documented | Plan/provider needs recheck | Yes |
| Antigravity | Yes | Standalone editor; exact codebase architecture unknown | Not confirmed | Not confirmed | Extension support varies | Not confirmed | Agent tool integrations documented | BYOK/local not confirmed | Yes, with lower maturity |

## JetBrains 2026.2: materially stronger than the older picture

IntelliJ IDEA 2026.2 combines official Rust and Python plugins with web tooling, database support, Docker, Dev Containers, WSL, remote development, Git, AI Assistant, JetBrains Air in IDEs, Copilot through Marketplace, and MCP. JetBrains states that the IDEA Rust plugin maintains feature parity with RustRover; the comparison page also lists debugger, profiler, and setup differences. The Python plugin implements PyCharm functionality.

AI Assistant exposes Codex, Claude Agent, Junie, and ACP-compatible agents. JetBrains Air in IDEs became a separate EAP plugin in October 2026; its plugin is free, but model/provider use and agent terms remain separate. Authentication can use JetBrains AI, supported provider accounts, or API keys for selected agents. The IDE's MCP server is opt-in for agents by default, and tool access can be restricted. Air in IDEs documents running a custom ACP agent inside WSL using its Linux executable and WSL execution environment.

Local Ollama and LM Studio models can be assigned to supported AI Assistant features. Current docs explicitly state that agents cannot use local models, and local models cannot call configured MCP tools. Local model support therefore does not mean fully local agent execution. GitHub Copilot is a separate official Marketplace plugin with its own account, terms, and provider boundary.

This combination reverses early elimination and makes IDEA Ultimate a serious #2. It does not prove identical ergonomics to RustRover/PyCharm, zero provider exposure, or equal performance. Verify plugin compatibility, license, AI plan, data terms, and permissions.

## Minimal configurations and trust

- VS Code: Rust and Python extensions, Rust debugger, Tauri, remote, containers, and optional Copilot/MCP. About 6 to 10 critical extensions.
- IDEA Ultimate: Rust/Python plugins, AI Assistant and Air if needed, Copilot as a separate plugin, and deliberate ACP/MCP configuration. About 3 to 6 plugins/configurations.
- VSCodium: Open VSX alternatives; verify publisher identity and Microsoft service dependencies.
- Zed: language servers, agent, local model or remote provider; SQL and containers may need external tools.
- Neovim: LSP, DAP, completion, formatter, Git, SQL, and optional CLI agent. About 8 to 12 components.
- Devin, Kiro, and Antigravity: verify distribution, agent source, permission defaults, provider, quota, and data terms. Eclipse Theia IDE is a standalone desktop product based on Theia Platform with a selected feature set; this review did not establish full stack coverage for its packaged defaults. JetBrains Air remains an agent layer, not an independent code engine.

Extensions and agents can read files, execute code, launch processes, and contact services. Check their publisher, source, license, update channel, and scope. MCP and ACP standardize connections; they do not certify agent security.
