---
description: "Verdict précédent : CONFIRMÉ AVEC RÉSERVES."
---

# Résultat de l'audit

## Décision

**Verdict précédent : CONFIRMÉ AVEC RÉSERVES.** Le premier choix tient pour une personne qui alterne Rust/Tauri, TypeScript/React, Python, GitHub, WSL2, SSH et conteneurs. Son avantage est l'étendue de l'écosystème, la documentation multiplateforme et un bon niveau sans agents IA. Ce n'est pas une victoire robuste sur toutes les notes : les fourchettes recouvrent souvent le deuxième candidat.

**Le concurrent le plus susceptible de battre le premier choix est IntelliJ IDEA Ultimate 2026.2.** Il combine officiellement les plugins Rust et Python avec TypeScript, React, Next.js, outils SQL, Docker, Dev Containers, WSL et Remote Development. Le plugin Rust réutilise le moteur et les fonctions centrales de RustRover. La parité produit complète n'est toutefois pas démontrée pour chaque workflow; les agents ACP peuvent être configurés dans WSL via le plugin JetBrains Air in IDEs. IDEA reste commercial et probablement plus lourd, mais JetBrains a amélioré son mode WSL en 2026.2, avec une mesure fournisseur sur l'accès fichiers qui ne vaut pas comparaison entre IDEs.

Dans le mod?le d'incertitude de cette ?tude, VS Code arrive en t?te dans 59 % des simulations de sensibilit? combin?es et IntelliJ IDEA Ultimate dans 41 %. Ces fr?quences d?crivent la stabilit? du mod?le ?ditorial retenu; elles ne sont pas des probabilit?s objectives qu'un IDE soit le meilleur en situation r?elle.

## Nouveaux finalistes

Les douze finalistes sont conservés pour réduire le risque de manquer un gagnant de scénario :

1. VS Code: meilleure couverture généraliste et remote/WSL.
2. IntelliJ IDEA Ultimate: intégration polyglotte JetBrains sérieuse, réintégrée dans la finale.
3. RustRover: meilleur choix Rust/Tauri dominant.
4. PyCharm Professional: Python, SQL et web fortement intégrés.
5. VSCodium: voie locale et communautaire basée sur Code OSS.
6. Cursor: IDE complet avec agents IA parmi les plus intégrés.
7. Zed: éditeur natif moderne, modèles locaux et agents externes.
8. Neovim: voie terminal configurable, locale et très extensible.
9. Sublime Text: éditeur mature dont les paquets LSP/DAP couvrent les langues, mais avec un assemblage et un remote moins intégrés.
10. Devin Desktop: surface d'édition complète avec agent central.
11. Kiro: IDE complet avec workflow de spécifications et agents.
12. Google Antigravity: IDE agentique autonome avec support d'extensions en expansion.

La présence dans la finale ne signifie pas que les douze sont équivalents comme IDE. Neovim et Sublime Text nécessitent un assemblage; Cursor, Kiro, Devin et Antigravity ont des arbitrages de fournisseur, confidentialité, stabilité ou coût propres aux plateformes IA. JetBrains Air est une couche d'agents multi-surface intégrée à IDEA, pas un moteur de code distinct.

## JetBrains: produits séparés, pile combinable

| Produit | Forces pour cette pile | Écarts et coûts |
|---|---|---|
| IntelliJ IDEA Ultimate | Plugin Rust officiel; plugin Python qui apporte les fonctions Python de PyCharm; JavaScript/TypeScript, React, Next.js; bases de données; Docker; Dev Containers; WSL; remote/SSH; Git; agents ACP/MCP | Produit commercial plus lourd; mesurer la mémoire sur le dépôt réel; vérifier la version précise du plugin et les différences de configuration et de fonctionnalité entre produits. C'est le challenger généraliste. |
| RustRover | Moteur Rust dédié, Cargo, debugging, tests, analyse et refactorings; JavaScript/TypeScript utile pour l'interface Tauri | N'établit pas la même couverture Next.js que l'IDE généraliste. Python moins intégré. Licence commerciale en usage commercial. |
| PyCharm Professional | Meilleure expérience Python; web, bases de données, Docker, WSL et remote | Rust via plugin, donc moins ciblé que RustRover. Licence Pro. |

**Réponse à la question de parité :** IntelliJ IDEA Ultimate peut combiner officiellement les capacités Rust du plugin Rust, le plugin Python, l'outillage JavaScript/TypeScript, les bases et le développement distant. JetBrains indique que le plugin Rust maintient la parité des fonctionnalités avec RustRover; son comparatif officiel détaille les différences de débogueur, de profilage et de configuration. IDEA exige le plugin gratuit Native Debugging Support pour LLDB/GDB. Cela justifie sa réintégration. Il faut distinguer la parité annoncée du plugin et l'égalité de chaque flux produit; certaines fonctions ou limites sont spécifiques à l'IDE. Les sources ne démontrent pas que l'IDE généraliste soit plus léger ou plus rapide sur le monorepo de l'utilisateur.

Pour une licence individuelle annuelle vérifiée le 15 octobre 2026, IDEA Ultimate est affiché à 199 USD la première année, puis 159 USD et 119 USD/an à partir de la troisième. Le All Products Pack, qui comprend IDEA, PyCharm, RustRover, Air et AI Pro, est à 299/239/179 USD par an selon l'ancienneté de l'abonnement. Le pack peut être rentable si l'on utilise les IDE séparés, mais les plugins Rust et Python permettent de réunir la pile dans IDEA sans les acheter. Voir le détail de [prix et licence](pricing.md); taxes, région et quotas IA s'ajoutent ou changent le montant.

### IA, ACP, MCP, BYOK et modèles locaux

IDEA 2026.2 permet d'utiliser Codex, Claude Agent et Junie dans AI Assistant, en plus des agents ACP. JetBrains Air in IDEs est un plugin EAP distinct au 15 octobre 2026; il lance des agents locaux ou ACP et documente une configuration WSL avec exécutable Linux. Le plugin officiel GitHub Copilot est disponible dans le Marketplace JetBrains. AI Assistant expose un serveur MCP intégré et accepte des serveurs MCP externes. BYOK est proposé pour des providers et agents compatibles; Ollama et LM Studio peuvent fournir des modèles locaux pour AI Assistant. Limite : les agents ne peuvent pas utiliser les modèles locaux, et les modèles locaux ne peuvent pas appeler les serveurs MCP configurés. Certaines fonctions cloud/agents dépendent d'un abonnement ou d'une authentification fournisseur. Sources : [agents Codex/Claude/ACP](https://www.jetbrains.com/help/ai-assistant/activate-agents.html), [MCP](https://www.jetbrains.com/help/ai-assistant/mcp.html), [modèles locaux](https://www.jetbrains.com/help/ai-assistant/use-custom-models.html), [BYOK](https://www.jetbrains.com/help/ai-assistant/bring-your-own-key-byok.html), [JetBrains Air](https://www.jetbrains.com/help/idea/air-in-jetbrains-ides.html), [ACP sous WSL](https://www.jetbrains.com/help/air-ides/air-manage-agents.html), [Copilot](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer).

## Scénarios

| Profil | Gagnant indicatif | Pourquoi le choix change |
|---|---|---|
| Polyglotte actuel | VS Code | Extensions et remote uniformes, faible coût, comportement similaire sur les OS. |
| Rust/Tauri dominant | RustRover | Moteur et intégration Cargo plus profonds; VS Code reste proche et plus léger. |
| Web/full stack | VS Code | Support web mature, extensions, remote et coût. IDEA Ultimate reste finaliste si l'intégration SQL compte beaucoup. |
| Python dominant | PyCharm Professional | Analyse, refactoring, tests et debug Python au coeur du produit. |
| Agents IA dominants | Devin Desktop selon la médiane; IDEA et Antigravity suivent | Le produit combine un vrai environnement d'édition et un agent central; les plages se chevauchent. |
| Privacy/local-first | Neovim selon le modèle; VSCodium pour un IDE graphique | Neovim maximise le contrôle local si l'on accepte la configuration; VSCodium reste plus accessible en GUI. |
| Remote/WSL | VS Code | Chemin WSL/SSH/Dev Containers le mieux documenté et le plus homogène. |
| Windows | VS Code | WSL et extensions Microsoft intégrés; IDEA Ultimate peut gagner selon préférence IDE. |
| Linux | VS Code | Large couverture et même workflow que WSL/macOS; RustRover devient préférable pour Rust pur. |
| macOS | VS Code | Choix équilibré; Zed est une alternative native si les besoins SQL/containers sont limités. |

Les scores changent en direct dans le [sélecteur de scénarios](scenarios.md). Les nombres sont des jugements structurés, pas une mesure empirique.

## Agents et éditeurs agentiques

| Environnement | IDE complet ? | Agent, architecture et limites principales |
|---|---|---|
| Cursor | Oui | Éditeur propriétaire basé sur technologie VS Code. Agent intégré, worktrees et choix de modèles; coût, confidentialité et consommation variables. |
| Devin Desktop | Oui | Éditeur complet dérivé de VS Code et agent Cognition. Intégrations externes en évolution; verrouillage et maturité plus élevés qu'un éditeur neutre. |
| Kiro | Oui | Éditeur Code OSS avec agent et specs. Extensions Open VSX/compatibilité à vérifier; Rust via extensions et écosystème AWS. |
| Antigravity | Oui | IDE autonome et orchestration agentique, support d'extensions croissant. Plateforme jeune; contrôler permissions, termes, confidentialité et stabilité. |
| Zed | Oui | Éditeur natif et agents externes via protocoles; modèle local disponible. Moins intégré pour bases et conteneurs; retours Windows/WSL encore mixtes. |
| VS Code | Oui | IDE/éditeur complet, fonctionnalités agentiques et GitHub Copilot en supplément. Forte dépendance au compte et aux services Microsoft pour Copilot. |
| IntelliJ IDEA | Oui | IDE intégré avec ACP, MCP et fournisseurs; JetBrains Air documente l'exécution d'un agent ACP dans WSL via un binaire Linux. |
| Sublime Text | Oui | Éditeur complet; LSP et DAP via paquets, sans remote/WSL/containers intégrés comparables. |
| Neovim | Éditeur/IDE configuré | Agent externe via plugins/terminal, pas de couche IA native nécessaire. Qualité sans IA excellente pour utilisateurs expérimentés. |

Un agent intégré excellent ne remplace pas automatiquement le débogueur, les refactorings, la navigation, Git, les plugins ou la stabilité d'un IDE. Les quatre produits agentiques restent donc comparés comme environnements complets.

## Avis de terrain et performance

Aucun benchmark contrôlé comparant plusieurs IDE sur mêmes machines, dépôts et versions n'a été trouvé. **Une mesure fournisseur existe pour JetBrains WSL :** cinq exécutions sur Windows 11, WSL2 Ubuntu 24.04 et IDEA Ultimate 263.SNAPSHOT, comparant IJent natif à l'ancien accès 9P sur spring-framework (23 sous-projets, 8 191 fichiers). JetBrains rapporte -38% sur l'ouverture à froid, -54% sur le parcours, -22% sur l'indexation et -53% sur la lecture des fichiers. Il s'agit d'une mesure MESURÉE du fournisseur sur son architecture, pas d'une comparaison d'IDE indépendante.

- **CORROBORÉ par documentation :** VS Code, IDEA/PyCharm, RustRover et Neovim documentent language servers, remote et analyse; cela n'établit pas la vitesse relative.
- **TÉMOIGNAGES RÉCURRENTS, non représentatifs :** des utilisateurs apprécient les outils Cargo/Rust de RustRover et le workflow léger/modulaire de VS Code; d'autres quittent l'un pour l'autre selon la profondeur d'analyse, le démarrage et la mémoire.
- Des tickets Zed en 2026 rapportent pointes mémoire WSL, fuite liée à la recherche et consommation ACP. Ils prouvent des problèmes reproduits par les auteurs de tickets dans certains environnements, pas une fréquence pour la population.
- VS Code, les IDE JetBrains et les outils basés sur Code OSS peuvent chacun consommer beaucoup lors de l'indexation, de TypeScript ou de grands workspace. L'architecture seule ne donne pas une mesure exploitable.

Voir les [retours utilisateurs et limites](sources.md#retours-de-terrain) et les [critères de performance](method.md#performance).

## Configuration réaliste et dépendances critiques

| Environnement | Assemblage minimal réaliste | Dépendances critiques approximatives |
|---|---|---:|
| VS Code | rust-analyzer, CodeLLDB, Python, Python Debugger, ESLint/Prettier selon projet, Tauri, Remote WSL, Remote SSH, Dev Containers, GitHub Pull Requests si besoin | 6 à 10 extensions |
| IntelliJ IDEA Ultimate | Plugins Rust/Python; web, DB, Docker, remote; AI Assistant, JetBrains Air in IDEs, Copilot plugin, MCP/ACP et modèles | 3 à 6 plugins/configs |
| RustRover | Configuration Rust intégrée; Tauri et outils web; plugin Python si Python devient important; remote/DB selon besoins | 0 à 3 plugins |
| PyCharm Pro | Python/web/DB intégrés; plugin Rust; Docker/WSL/remote si non activés par défaut | 1 à 3 plugins |
| VSCodium | Extensions équivalentes installées via Open VSX; valider éditeur, source et compatibilité | 6 à 10 extensions |
| Cursor | Fonctions d'édition/agent intégrées; extensions Rust, Python et environnement selon besoin | 4 à 8 extensions |
| Zed | LSP Rust/Python/TypeScript; adaptateurs agents; outils externes SQL et conteneurs | 4 à 8 extensions/outils |
| Neovim | LSP, rust-analyzer, DAP, Treesitter, complétion, fichiers, Git, formatters, SQL, plugins agents optionnels | 8 à 12 plugins |

Le nombre dépend de l'usage. Les droits de chaque extension sont distincts de la licence de l'éditeur; vérifier la licence, le mainteneur, les permissions, le canal de mise à jour et l'éditeur exact avant installation. Marketplace officiel ne signifie pas absence de risque de chaîne d'approvisionnement.

## Sécurité, confidentialité, prix et licence

- Agent local ou cloud: traiter le code comme une donnée sensible. Vérifier les destinations de modèle, la rétention, le mode privacy, les journaux, les fichiers ignorés et le recours humain.
- Les permissions, approbations d'outils et sandbox réduisent certains risques; elles ne neutralisent pas les instructions malveillantes dans un dépôt ni les extensions compromises.
- VS Code, IntelliJ, Cursor, Zed, Kiro et Antigravity ont des composants/services propriétaires même si certaines couches sont open source. VSCodium et Neovim améliorent l'auditabilité locale mais ne garantissent pas la sécurité.
- VS Code et VSCodium sont utilisables gratuitement; IDE JetBrains Pro/Ultimate et les plans d'agents peuvent être payants; les quotas changent. Cursor/Kiro/Devin/Antigravity dépendent d'offres et crédits évolutifs. Les liens de prix sont dans le registre.
- Usage commercial: vérifier la licence exacte du produit, les conditions des modèles et les licences d'extensions. RustRover/IDE JetBrains, services IA et plugins n'ont pas un régime unique.

Kiro: AWS advisory CVE-2026-95985 affects versions before 1.0.242 and says the issue was fixed in 1.0.242. The reviewed 1.3.0 release is later; this is a patched historical issue, not evidence of current exposure. Prior users of affected versions should review the global configuration directory as AWS recommends.

## Sensibilité des notes et des poids

L'analyse reproductible tire les notes dans leurs intervalles plausibles et fait varier les poids dans une plage déclarée. Elle publie médiane de rang, plage p10-p90 des scores et fréquence de victoire du modèle arrondie au pourcent le plus proche. Cette fréquence est **une stabilité du modèle éditorial**, pas la probabilité objective qu'un produit soit le meilleur.

Les deux principales variables qui changent le classement sont la profondeur Rust/Tauri (RustRover/IDEA) et la priorité donnée à l'intégration des agents ou à la confidentialité (Cursor/VSCodium/Neovim). Avec les notes incertaines, l'écart VS Code / IDEA doit être lu comme faible.

## Sorties confirmées du balayage

| Candidat | Motif de sortie |
|---|---|
| Fleet | JetBrains a annoncé la fin de distribution autonome; ce n'est plus un candidat actuel. |
| Nova | Réservé à macOS et moins convaincant pour un workflow Windows/WSL/Linux. |
| Lapce | Projet intéressant, mais l'intégration debugger, bases, conteneurs et extensions reste trop incertaine pour le profil; pas de preuve de parité multi-OS complète. |
| Sublime Text | Ancien motif infirmé: Build 4215 (2026-09-25) et paquets LSP/DAP actuels justifient sa réintégration; WSL/remote et containers restent ses lacunes. |
| Helix | Bon éditeur terminal et LSP, mais le débogage et les services intégrés de workflow ne couvrent pas assez la pile. |
| Air | Environnement d'agents/outils, pas un IDE desktop complet comparable dans ce périmètre. |
| Emacs | Très capable après configuration; pour ce profil, la charge d'assemblage et le recouvrement avec Neovim réduisent sa probabilité d'être le gagnant. |
| Zed, Kiro, Antigravity, Devin, Neovim | Réintégrés dans cette shortlist élargie car ils peuvent gagner un scénario distinct ou apporter une comparaison de contrôle/agents. |
| Eclipse Theia IDE | Application de bureau réellement distribuée sur Windows, Linux et macOS. Exclue pour couverture intégrée et compatibilité de pile insuffisamment établies dans les sources retenues, pas parce que le produit serait un simple framework. |

