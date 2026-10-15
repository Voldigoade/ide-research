# Resultado de la auditoría

## Decisión

**Veredicto anterior: CONFIRMADO CON RESERVAS.** Visual Studio Code sigue siendo el ganador equilibrado del modelo para Rust/Tauri, TypeScript/React, Python, GitHub, WSL2, SSH y contenedores. Su rango se solapa con IntelliJ IDEA Ultimate 2026.2, el rival real con más opciones de superarlo. Se confirma la recomendación anterior, pero su ventaja no es robusta.

La nueva shortlist tiene 12 productos: VS Code, IntelliJ IDEA Ultimate, RustRover, PyCharm Professional, VSCodium, Cursor, Zed, Neovim, Sublime Text 4, Devin Desktop, Kiro y Google Antigravity. El cambio principal es reincorporar IDEA tras comprobar sus plugins en 2026.2. Sublime Text sustituye a Theia porque es un editor instalable concreto; Theia sigue en el análisis como framework dependiente de la distribución.

## Ganadores por escenario

| Perfil | Ganador indicativo | Motivo |
|---|---|---|
| Políglota equilibrado | VS Code | Stack amplio y flujo remoto uniforme |
| Rust y Tauri dominantes | RustRover | Motor Rust/Cargo y depuración especializados |
| Web/full stack | VS Code | Ecosistema web, extensiones y remoto |
| Python intensivo | PyCharm Professional | Análisis, refactorización, tests y depuración Python |
| Agentes IA dominantes | Devin Desktop por mediana; IDEA cerca | IDE y agente central, con rangos solapados |
| Privacidad/local primero | Neovim según el modelo; VSCodium para GUI | Control local con mayor configuración |
| Remote/WSL | VS Code | Ruta más amplia documentada para WSL, SSH y Dev Containers |
| Windows | VS Code | Integración WSL y ecosistema |
| Linux | VS Code | Cobertura amplia; RustRover para Rust puro |
| macOS | VS Code | Equilibrado; Zed como alternativa nativa |

## Revisión de JetBrains

IntelliJ IDEA Ultimate 2026.2 combina los plugins oficiales Rust y Python con JavaScript/TypeScript, React, Next.js, bases de datos, Docker, Dev Containers, WSL, desarrollo remoto y Git. JetBrains afirma que el plugin Rust mantiene paridad funcional con RustRover; su comparación documenta diferencias de depuración, perfilado y configuración. IDEA requiere el plugin gratuito Native Debugging Support para LLDB/GDB. El plugin oficial Python implementa las funciones de PyCharm. La combinación es sólida, pero la paridad del plugin no demuestra idéntica ergonomía o rendimiento en un monorepo real. Consulta la [tabla de precios y licencias](pricing.md): IDEA Ultimate cuesta $199/año el primer periodo individual, luego $159 y $119/año; All Products Pack cuesta $299/$239/$179 al año e incluye los IDE separados y AI Pro.

AI Assistant documenta Codex, Claude Agent y Junie, BYOK para proveedores seleccionados, modelos Ollama/LM Studio para funciones compatibles, y cliente/servidor MCP. Los agentes no pueden usar modelos locales ni los modelos locales llamar a herramientas MCP configuradas. GitHub Copilot es un plugin oficial separado del Marketplace.

JetBrains Air es ahora un sistema de agentes para IDE, web, CLI y móvil. Air in IDEs pasó a ser un plugin EAP separado en octubre de 2026. Admite agentes locales y ACP y documenta ejecución desde WSL. Esto amplía el flujo agente de IDEA; Air no se cuenta como otro IDE o motor de código. Proveedor, autorización y permisos siguen siendo límites separados.

RustRover sigue siendo especialista de Rust; PyCharm Professional, de Python. Se valoran como productos separados.

## Entornos agenticos

Cursor, Devin Desktop, Kiro y Antigravity son entornos completos de edición, no solo wrappers de agentes. La comparación incluye lenguajes, Git, depurador, extensiones, WSL/remoto, plataformas, madurez, privacidad, precio y utilidad sin IA. Un agente bueno no basta para ganar si el IDE es débil. Consulta la [matriz de agentes y protocolos](agents.md).

## Exclusiones revisadas

| Candidato | Revisión de 2026 y decisión |
|---|---|
| Fleet | Las descargas independientes terminaron en diciembre de 2025; JetBrains afirma que Fleet pasó a Air en mayo de 2026. Air se evalúa como capa de agentes. |
| Air | Air in IDEs es un plugin EAP de agentes, no un IDE Rust/Python/TypeScript separado; se cuenta con IDEA. |
| Nova | Sigue activo como editor nativo para Mac con documentación de 2026, pero solo cubre macOS en un perfil multiplataforma. |
| Lapce | Versión 0.4.6 y nightlies de octubre; hay plugins Rust, TypeScript, Python y SQLite, además de SSH remoto. La documentación remota aún requiere abrir workspaces desde el terminal tras la reescritura de interfaz; WSL tiene una brecha reportada y el DAP/bases/contenedores están menos integrados. Se confirma su salida con una razón corregida, no por falta de lenguajes. |
| Helix | El último anuncio estable hallado es 25.07; LSP y tree-sitter integrados, pero DAP experimental y menos gestión remota, bases o contenedores para este perfil. |
| Theia | Framework activo, pero la distribución elegida define funciones, licencia, privacidad y rendimiento; no es un solo producto instalable comparable. |
| Sublime Text | Reincorporado: Build 4213 y paquetes actuales LSP Rust/TypeScript y DAP/Python justifican una plaza. WSL, Dev Containers y Remote SSH oficiales siguen siendo más débiles. |
| Emacs | Técnicamente capaz, pero requiere montar muchos paquetes y configuración; Neovim ya representa el camino local de terminal de esta shortlist. |

## Rendimiento y opiniones

No encontramos ni ejecutamos un benchmark controlado entre IDEs. JetBrains publica una prueba limitada de cinco ejecuciones con Windows 11, Ubuntu 24.04 en WSL2, IDEA Ultimate 263.SNAPSHOT y Spring Framework (23 subproyectos, 8.191 archivos), comparando IJent con la antigua ruta 9P. Informa mejoras en apertura, recorrido, indexación y lectura. Es una medición del proveedor sobre su transporte WSL, no una comparación entre IDEs.

Opiniones recientes describen ventajas de refactorización y depuración en JetBrains, inicio y configuración/extensiones en VS Code, migraciones PyCharm↔VS Code, migraciones a Neovim y problemas puntuales de memoria/WSL en Zed. Son informes autoseleccionados, no prevalencia ni pruebas controladas. Hay pocos informes de migración específica de VSCodium.

El aviso AWS para Kiro CVE-2026-95985 afecta versiones anteriores a 1.0.242 e indica que se corrigió en 1.0.242. La versión Kiro 1.3.0 revisada es posterior; es un problema histórico corregido, no prueba de exposición actual. Quienes usaron versiones afectadas deben revisar la configuración global según AWS.

Consulta las [decisiones por candidato](../../research/market-scan.md), [notas y escenarios](../scenarios.md), [sensibilidad](../../research/sensitivity.md), [duelos](../../research/duels-top-five.md) y [fuentes](../sources.md).
