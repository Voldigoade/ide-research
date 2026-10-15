# Agents, IA et modèles

Les intégrations natives, plugins, protocoles et CLI externes ont des coûts et frontières de confiance différents. Une marque « supporté » signifie uniquement que la documentation actuelle décrit le branchement.

## JetBrains IDEA Ultimate 2026.2

IDEA peut rassembler Codex, Claude Agent, Junie et agents ACP dans AI Assistant, plus JetBrains Air in IDEs, plugin EAP distinct en octobre 2026, pour plusieurs sessions et agents locaux/ACP. JetBrains documente un exécutable ACP hébergé dans WSL. GitHub Copilot est un plugin distinct du Marketplace. Le serveur MCP intégré est désactivé par défaut pour les agents ACP; la liste d'outils peut être restreinte. BYOK existe pour certains agents/fournisseurs.

Ollama et LM Studio peuvent alimenter certaines fonctions AI Assistant. Limite actuelle: les agents ne peuvent pas utiliser de modèles locaux; les modèles locaux ne peuvent pas appeler les outils MCP configurés. « Modèle local » ne signifie donc pas « agent entièrement local ».

## Les autres environnements

| Environnement | Agents et protocoles | Usage utile sans IA |
|---|---|---|
| VS Code | Copilot intégré; MCP documenté; Codex/Claude Code via CLI ou extensions | Oui, éditeur et extensions complets |
| RustRover / PyCharm | Intégrations JetBrains AI/ACP/MCP; Copilot en plugin | Oui, solides dans leur spécialité |
| VSCodium | Extensions Open VSX et CLI; pas de Copilot Microsoft Marketplace par défaut | Oui, avec différences de marketplace |
| Cursor | Agent natif, outils et modèles selon plan; ACP non établi dans les sources examinées | Oui, éditeur complet |
| Zed | Agents ACP, outils MCP, modèles locaux | Oui, éditeur natif |
| Neovim | Agents CLI et plugins; configuration au choix | Oui, fort contrôle local |
| Sublime Text 4 | LSP/DAP via paquets; agent seulement par CLI ou extension tierce | Oui, puissant éditeur sans IA |
| Devin Desktop | Agent Cognition et intégrations externes documentées | Oui comme éditeur, mais produit centré agents |
| Kiro | Agent et MCP documentés; support ACP/BYOK/local non établi ici | Oui, workflow agentique important |
| Antigravity | Orchestration agentique et extensions; ACP/BYOK/local non confirmés | Oui, maturité inférieure |

Voir la [matrice complète sourcée](https://github.com/Voldigoade/ide-research/blob/main/research/agent-compatibility.md). Elle distingue les fonctions établies des inconnues.

## Sécurité et vie privée

Un agent peut lire le dépôt, modifier des fichiers, lancer des commandes et contacter un fournisseur. Vérifier le provider, la rétention, les quotas, les permissions, les outils MCP et le plan commercial. ACP/MCP standardisent le branchement, pas la sécurité. Les extensions exécutables gardent leur propre licence et chaîne d'approvisionnement.
