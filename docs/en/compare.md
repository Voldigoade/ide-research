# Comparator

Select 2 to 4 products. Scores display plausible ranges, not measurements.

<div class="tool-panel" data-lang="en">
<fieldset><legend>Environments to compare</legend><div id="compare-controls"></div></fieldset>
<label for="compare-scenario">Scenario</label>
<select id="compare-scenario"><option value="balanced">Balanced polyglot</option><option value="rust">Rust and Tauri dominant</option><option value="web">Web and full stack</option><option value="python">Python heavy</option><option value="agents">AI agents dominant</option><option value="privacy">Privacy and local first</option><option value="remote">Remote and WSL</option><option value="windows">Windows</option><option value="linux">Linux</option><option value="macos">macOS</option></select>
<p id="compare-summary" aria-live="polite"></p><div id="compare-results"></div>
</div>

Selections are processed locally and not persisted. Read the [assumptions](method.md).
