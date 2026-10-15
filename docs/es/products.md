# Productos y configuraciones

Los doce finalistas son VS Code, IntelliJ IDEA Ultimate, RustRover, PyCharm Professional, VSCodium, Cursor, Zed, Neovim, Sublime Text 4, Devin Desktop, Kiro y Antigravity.

Para VS Code, una base realista usa rust-analyzer, CodeLLDB, Python, Python Debugger, Remote WSL, Remote SSH, Dev Containers y Tauri; añade ESLint/Prettier y GitHub PR según el proyecto. IntelliJ IDEA Ultimate requiere los plugins oficiales Rust y Python; JavaScript/TypeScript, React, Next.js, SQL, Git, contenedores y remoto se integran según edición. RustRover necesita menos plugins para Rust, pero ofrece menos amplitud Python/web. PyCharm Pro es fuerte en Python y añade Rust mediante plugin.

VSCodium usa Open VSX; hay que verificar compatibilidad de extensiones Microsoft. Cursor incluye un agente, pero hay que comprobar privacidad, cuotas y proveedores. Zed usa LSP y agentes externos, con menos integración SQL/containers. Neovim requiere configurar LSP, Rust, DAP, Treesitter, Git, SQL y formatos.

Sublime Text 4 Build 4213 usa paquetes mantenidos por separado como LSP, rust-analyzer, TypeScript LSP, Debugger/DAP y Python Debugger. Su terminal integrada ayuda, pero los límites de WSL por carpeta compartida y la falta de un workspace Dev Containers/Remote SSH oficial y demostrado reducen la integración; estima 6 a 9 paquetes o herramientas críticas.

Una extensión puede ejecutar código, leer archivos, lanzar procesos y contactar servicios. Revisa mantenedor, código, licencia, permisos y actualizaciones.
