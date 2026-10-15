---
description: "Scenarios change the actual stack mix and the cross-cutting workflow weights."
---

# Work profiles

Scenarios change the actual stack mix and the cross-cutting workflow weights. Rust-dominant work gives Rust and Tauri most of the stack share, while TypeScript and Python become secondary.

<div class="tool-panel" data-lang="en">
<label for="scenario-select">Choose a scenario</label>
<select id="scenario-select"><option value="balanced">Balanced polyglot</option><option value="rust">Rust and Tauri dominant</option><option value="web">Web and full stack</option><option value="python">Python heavy</option><option value="agents">AI agents dominant</option><option value="privacy">Privacy and local first</option><option value="remote">Remote and WSL</option><option value="windows">Windows</option><option value="linux">Linux</option><option value="macos">macOS</option></select>
<p id="scenario-summary" aria-live="polite"></p><div id="scenario-results"></div>
</div>

The balanced model gives stack fit 55% and workflow 45%. Rust raises stack weight to 75%; Python uses 68%; agent-first uses 15%; privacy-first uses 30%. Ratings are sourced judgments, not benchmark measurements. See the [method](method.md).
