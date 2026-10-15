---
description: "État de la recherche : 15 octobre 2026."
---

# IDE Research: audit contradictoire

**État de la recherche : 15 octobre 2026.** Les notes sont des plages d'appréciation sourcées, pas des benchmarks ni des probabilités.

## Verdict de l'audit

**Verdict précédent : CONFIRMÉ AVEC RÉSERVES.** VS Code reste le choix équilibré le plus défendable pour le profil polyglotte Windows/WSL2, Linux et macOS. IntelliJ IDEA Ultimate est le challenger le plus crédible et mérite la finale : ses plugins officiels Rust et Python permettent désormais de réunir presque toute la pile JetBrains dans un seul IDE. RustRover gagne si Rust et Tauri dominent vraiment; VSCodium gagne quand le contrôle local et la réduction de télémétrie priment.

La marge du premier choix est limitée. Les intervalles de notes se chevauchent et les résultats changent selon le scénario. Voir [l'audit complet](audit.md), [la méthode](method.md) et [les scénarios](scenarios.md).

## Explorer les scénarios

<div class="tool-panel" data-lang="fr">
  <label for="scenario-select">Votre composition de travail</label>
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

## Portée

La finale comprend 12 environnements : VS Code, IntelliJ IDEA Ultimate, RustRover, PyCharm Professional, VSCodium, Cursor, Zed, Neovim, Sublime Text 4, Devin Desktop, Kiro et Google Antigravity. Le balayage plus large et les sorties sont détaillés dans l'audit.

Le comparateur couvre le langage, le débogage, Git, le terminal, WSL, le remote, les conteneurs, l'IA, les permissions, la confidentialité, les performances, la stabilité, les systèmes, le coût et le verrouillage.

- [Comparer 2 à 4 environnements](compare.md)
- [Profils et configurations réalistes](products.md)
- [Sources et registre structuré](sources.md)
