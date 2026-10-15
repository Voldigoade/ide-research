# Produits et assemblages

La shortlist comprend douze environnements distincts. L'outil compare les plages stockées dans [les données structurées](https://github.com/Voldigoade/ide-research/tree/main/data).

## Configurations minimales

### VS Code
Installer les extensions officielles Rust Analyzer, CodeLLDB, Python, Python Debugger, Remote - WSL, Remote - SSH, Dev Containers et Tauri; ajouter ESLint, Prettier et GitHub Pull Requests selon le dépôt. Vérifier chaque identifiant d'éditeur et les permissions. VS Code utilise son Marketplace Microsoft; certaines extensions ont des licences et conditions différentes de l'éditeur.

### IntelliJ IDEA Ultimate
Activer les plugins officiels Rust et Python. JavaScript/TypeScript, React, Next.js, outils base de données et Git sont fournis par l'IDE/édition. Docker, Dev Containers et Remote Development sont documentés. Configurer le fournisseur ACP/MCP séparément. C'est un assemblage plus intégré, avec abonnement commercial et prise en charge ACP sous WSL via Air; les limites des modèles locaux restent distinctes.

### RustRover
Le moteur Rust, Cargo et debugging forment le coeur du produit. Les outils TypeScript aident sur l'interface Tauri; les preuves de parité Next.js complète restent incertaines. Ajouter des outils Python et SQL si ces domaines deviennent importants.

### PyCharm Professional
Python est natif; bases de données, Docker, WSL et remote sont documentés. Installer le plugin Rust officiel pour Rust secondaire. Prix Pro à vérifier selon plan et région.

### VSCodium
Utiliser Open VSX et vérifier les éditeurs de chaque extension. Une partie des extensions Microsoft n'est pas distribuée de la même façon ou dépend de services Microsoft. La configuration demande plus de travail que l'installation de VS Code.

### Cursor
IDE complet avec agent intégré. Ajouter extensions Rust/Python selon besoin. Revoir mode de confidentialité, rétention, quotas, modèles inclus, BYOK et éventuels coûts additionnels avant d'ouvrir un dépôt propriétaire.

### Zed
Configurer rust-analyzer, pyright/pylsp, TypeScript et l'agent choisi. Les modèles locaux et connexions distantes existent; SQL, Dev Containers et outils de base peuvent réclamer des extensions ou outils externes. Consulter les notes Windows/WSL actuelles.

### Neovim
Pile possible: LSP client plus nvim-lspconfig, rustaceanvim, nvim-dap, nvim-treesitter, complétion, navigation, formatter, Git, SQL. Choisir des mainteneurs actifs et consulter licence, permissions et activité du dépôt. Les besoins agents sont optionnels.

### Sublime Text 4
LSP Rust/TypeScript/Python et débogage DAP sont disponibles via des paquets séparés. Le terminal intégré est utile; WSL par partage UNC et fichiers distants n'offrent pas le même workflow que Remote SSH/Dev Containers. Compter environ 6 à 9 dépendances critiques.

### Devin Desktop, Kiro et Antigravity
Les profils sont complets mais leurs extensions, accès distant, politique de données, agent et compatibilité doivent être vérifiés par distribution et plan. Le modèle de score les pénalise lorsqu'une fonction n'est pas établie par une source actuelle.

## Extensions, maintenance et droits

Une extension peut exécuter du code local, accéder aux fichiers, démarrer des processus et contacter un service. Le nom d'un éditeur réputé n'est pas une preuve suffisante. Vérifier dépôt source, licence, mises à jour, permissions, marketplace, dépendances et traitement des données. Les licences de produits tiers ne sont pas remplacées par les licences MIT et CC de ce dépôt.
