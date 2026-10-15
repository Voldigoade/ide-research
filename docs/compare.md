---
description: "Sélectionner de 2 à 4 produits."
---

# Comparateur

Sélectionner de 2 à 4 produits. Les valeurs montrent l'intervalle plausible, pas un score mesuré. Les critères restent visibles pour que le classement soit inspectable.

<div class="tool-panel" data-lang="fr">
  <fieldset>
    <legend>Environnements à comparer</legend>
    <div id="compare-controls"></div>
  </fieldset>
  <label for="compare-scenario">Scénario de pondération</label>
  <select id="compare-scenario">
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
  <p id="compare-summary" aria-live="polite"></p>
  <div id="compare-results"></div>
</div>

Aucune sélection n'est envoyée au serveur ou conservée dans le navigateur. Voir les [hypothèses et limites](method.md).
