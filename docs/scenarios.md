# Profils de travail

Les scénarios modifient la composition de la pile et l'importance des dimensions transversales. Le scénario Rust met bien plus de poids sur Rust et Tauri que sur le web; ce n'est pas une simple hausse de poids d'un critère généraliste.

<div class="tool-panel" data-lang="fr">
  <label for="scenario-select">Choisir un scénario</label>
  <select id="scenario-select">
    <option value="balanced">Polyglotte équilibré</option>
    <option value="rust">Rust et Tauri dominants</option>
    <option value="web">Web et full stack</option>
    <option value="python">Python dominant</option>
    <option value="agents">Agents IA dominants</option>
    <option value="privacy">Confidentialité et local-first</option>
    <option value="remote">Remote et WSL</option>
    <option value="windows">Windows</option>
    <option value="linux">Linux</option>
    <option value="macos">macOS</option>
  </select>
  <p id="scenario-summary" aria-live="polite"></p>
  <div id="scenario-results"></div>
</div>

## Règles

Le profil équilibré donne 55% au stack et 45% au workflow. Rust monte à 75% de stack, Python à 68%, tandis que les profils agents et privacy descendent à 15% et 30%. Les notes restent des plages de jugement, pas des observations de benchmark. Pour lire les écarts, consulter [la méthode](method.md). Les profils Windows, Linux et macOS donnent un poids explicite à l'OS et conservent une composition de pile visible.
