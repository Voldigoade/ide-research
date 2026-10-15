---
description: "The 12 finalists are VS Code, IntelliJ IDEA Ultimate, RustRover, PyCharm Professional, VSCodium, Cursor, Zed, Neovim, Sublime Text 4, Devin Desktop, Kiro..."
---

# Products and setups

The 12 finalists are VS Code, IntelliJ IDEA Ultimate, RustRover, PyCharm Professional, VSCodium, Cursor, Zed, Neovim, Sublime Text 4, Devin Desktop, Kiro, and Antigravity.

For VS Code, a realistic baseline uses rust-analyzer, CodeLLDB, Python, Python Debugger, Remote WSL, Remote SSH, Dev Containers, and Tauri, with ESLint/Prettier and GitHub PRs as needed. IntelliJ IDEA Ultimate needs official Rust and Python plugins; JS/TS, React, Next.js, SQL/database tools, Git, containers and remote features are integrated by edition. RustRover needs fewer plugins for Rust but is less broad for Python/web. PyCharm Pro is strongest for Python and adds Rust through a plugin.

VSCodium uses Open VSX and needs compatibility checks for Microsoft extensions. Cursor integrates its agent, but verify data mode, quotas, and provider terms. Zed uses LSPs and external agents but database/container tooling is less integrated. Neovim needs an actively maintained LSP, Rust, DAP, Treesitter, Git, SQL, and formatter stack.

Sublime Text 4 Build 4215 uses separately maintained packages such as LSP, rust-analyzer, TypeScript LSP, Debugger/DAP and Python Debugger. Its built-in terminal helps, but WSL file-share limitations and the lack of an established first-party Dev Containers/Remote SSH workspace make it less integrated; estimate 6 to 9 critical packages or tools.

An extension can execute code, read files, spawn processes, and contact services. Verify its maintainer, source, license, permissions, and update channel. See the [detailed product profiles](../products.md).
