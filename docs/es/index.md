# IDE Research: auditoría contradictoria

**Estado: 15 de octubre de 2026.** Las puntuaciones son intervalos editoriales con fuentes, no benchmarks ni probabilidades objetivas.

## Veredicto

**Veredicto anterior: CONFIRMADO CON RESERVAS.** VS Code sigue siendo la opción equilibrada más defendible para un flujo multiplataforma con Windows/WSL2, Linux y macOS. IntelliJ IDEA Ultimate es el rival más fuerte y merece estar en la final: sus plugins oficiales de Rust y Python se combinan con herramientas web, bases de datos, contenedores y acceso remoto. RustRover gana si Rust y Tauri dominan; VSCodium gana si prima el control local y reducir la telemetría del proveedor.

La ventaja es estrecha. Los intervalos se solapan y el ganador cambia según el escenario. Consulta la [auditoría completa](audit.md), el [método](method.md) y los [escenarios](scenarios.md).

## Explorar escenarios

<div class="tool-panel" data-lang="es">
  <label for="scenario-select">Perfil de trabajo</label>
  <select id="scenario-select">
    <option value="balanced">Políglota equilibrado</option><option value="rust">Rust y Tauri dominantes</option><option value="web">Web y full stack</option><option value="python">Python intensivo</option><option value="agents">Agentes de IA dominantes</option><option value="privacy">Privacidad y local primero</option><option value="remote">Remote y WSL</option><option value="windows">Windows</option><option value="linux">Linux</option><option value="macos">macOS</option>
  </select>
  <p id="scenario-summary" aria-live="polite"></p><div id="scenario-results"></div>
</div>

## Alcance

La final incluye VS Code, IntelliJ IDEA Ultimate, RustRover, PyCharm Professional, VSCodium, Cursor, Zed, Neovim, Sublime Text 4, Devin Desktop, Kiro y Google Antigravity.

- [Comparar de 2 a 4 entornos](compare.md)
- [Perfiles y configuraciones realistas](products.md)
- [Fuentes y registro estructurado](sources.md)
