# Agents, AI, and models

Native integrations, plugins, protocols, and external CLIs have different costs and trust boundaries. "Supported" means current documentation describes a connection, not equal quality or safety.

## IntelliJ IDEA Ultimate 2026.2

IDEA can bring Codex, Claude Agent, Junie, and ACP agents into AI Assistant, plus JetBrains Air in IDEs for multiple sessions and local/ACP agents. JetBrains documents running a custom ACP executable from WSL. GitHub Copilot is a separate Marketplace plugin. The built-in MCP server is off by default for ACP agents; tool access can be restricted. BYOK is available for selected agents/providers.

Ollama and LM Studio can power some AI Assistant features. Current limitation: agents cannot use local models, and local models cannot call configured MCP tools. "Local model" therefore does not mean "fully local agent."

## Other environments

| Environment | Agents and protocols | Useful without AI |
|---|---|---|
| VS Code | Copilot integration; documented MCP; Codex/Claude Code through CLI or extensions | Yes, complete editor and extensions |
| RustRover / PyCharm | JetBrains AI/ACP/MCP; Copilot plugin | Yes, strong in their specialty |
| VSCodium | Open VSX extensions and CLI; Microsoft Copilot Marketplace integration is not default | Yes, with marketplace differences |
| Cursor | Native agent, tools and models by plan; ACP not established in reviewed sources | Yes, complete editor |
| Zed | ACP agents, MCP tools, local models | Yes, native editor |
| Neovim | CLI agents and plugins; user-configured | Yes, strong local control |
| Sublime Text 4 | LSP/DAP through packages; agent via CLI or third-party extension | Yes, strong editor without AI |
| Devin Desktop | Cognition agent and documented external integrations | Yes as editor, but agent-centric |
| Kiro | Agent and MCP documented; ACP/BYOK/local not established here | Yes, agent-led workflow |
| Antigravity | Agent orchestration and extensions; ACP/BYOK/local not confirmed | Yes, lower maturity |

See the [full source-linked matrix](https://github.com/Voldigoade/ide-research/blob/main/research/agent-compatibility.md). It separates documented support from unknowns.

## Security and privacy

An agent may read repository files, change code, run commands, and contact a provider. Check provider, retention, quotas, permissions, MCP tools, and commercial plan. ACP/MCP standardize connections, not agent security. Extensions have their own licenses and supply chains.
