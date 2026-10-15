---
description: "Research state: 15 October 2026."
---

# IDE Research: adversarial audit

**Research state: 15 October 2026.** Ratings are sourced editorial ranges, not benchmarks or objective probabilities.

## Audit verdict

**Previous verdict: CONFIRMED WITH RESERVATIONS.** VS Code remains the most defensible balanced choice for a polyglot Windows/WSL2, Linux, and macOS workflow. IntelliJ IDEA Ultimate is the strongest challenger and belongs in the final: its official Rust and Python plugins can now combine with web, database, container, and remote tooling. RustRover wins if Rust and Tauri dominate; VSCodium wins when local control and reduced vendor telemetry matter most.

The lead is narrow. Rating ranges overlap and scenario winners change. Read the [full audit](audit.md), [method](method.md), and [scenarios](scenarios.md).

## Explore scenarios

<div class="tool-panel" data-lang="en">
  <label for="scenario-select">Work profile</label>
  <select id="scenario-select">
    <option value="balanced">Balanced polyglot</option><option value="rust">Rust and Tauri dominant</option><option value="web">Web and full stack</option><option value="python">Python heavy</option><option value="agents">AI agents dominant</option><option value="privacy">Privacy and local first</option><option value="remote">Remote and WSL</option><option value="windows">Windows</option><option value="linux">Linux</option><option value="macos">macOS</option>
  </select>
  <p id="scenario-summary" aria-live="polite"></p><div id="scenario-results"></div>
</div>

## Scope

The final includes VS Code, IntelliJ IDEA Ultimate, RustRover, PyCharm Professional, VSCodium, Cursor, Zed, Neovim, Sublime Text 4, Devin Desktop, Kiro, and Google Antigravity. The wider scan and exclusions appear in the audit.

- [Compare 2 to 4 environments](compare.md)
- [Product profiles and realistic setups](products.md)
- [Sources and structured register](sources.md)
