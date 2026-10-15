---
description: "Las integraciones nativas, plugins, protocolos y CLI externos tienen costes y límites de confianza distintos."
---

# Agentes, IA y modelos

Las integraciones nativas, plugins, protocolos y CLI externos tienen costes y límites de confianza distintos. «Compatible» significa que la documentación actual describe la conexión, no que garantice calidad o seguridad equivalentes.

## IntelliJ IDEA Ultimate 2026.2

IDEA reúne Codex, Claude Agent, Junie y agentes ACP en AI Assistant, además de JetBrains Air in IDEs para varias sesiones y agentes locales/ACP. JetBrains documenta ejecutar un agente ACP desde WSL. GitHub Copilot es un plugin separado de Marketplace. El servidor MCP integrado está desactivado por defecto para agentes ACP; se pueden limitar las herramientas. BYOK existe para ciertos agentes y proveedores.

Ollama y LM Studio pueden alimentar algunas funciones de AI Assistant. Límite actual: los agentes no pueden usar modelos locales, y los modelos locales no pueden invocar herramientas MCP configuradas. «Modelo local» no significa «agente totalmente local».

## Otros entornos

| Entorno | Agentes y protocolos | Uso útil sin IA |
|---|---|---|
| VS Code | Copilot integrado; MCP documentado; Codex/Claude Code por CLI o extensión | Sí, editor y extensiones completos |
| RustRover / PyCharm | JetBrains AI/ACP/MCP; plugin Copilot | Sí, fuertes en su especialidad |
| VSCodium | Open VSX y CLI; Copilot Marketplace de Microsoft no viene por defecto | Sí, con diferencias de marketplace |
| Cursor | Agente nativo, herramientas y modelos según plan; ACP no confirmado | Sí, editor completo |
| Zed | Agentes ACP, herramientas MCP y modelos locales | Sí, editor nativo |
| Neovim | Agentes CLI y plugins configurables | Sí, control local amplio |
| Sublime Text 4 | LSP/DAP mediante paquetes; agente por CLI o extensión de terceros | Sí, editor potente sin IA |
| Devin Desktop | Agente Cognition e integraciones externas documentadas | Sí como editor, producto centrado en agentes |
| Kiro | Agente y MCP documentados; ACP/BYOK/local no confirmados aquí | Sí, workflow agentico |
| Antigravity | Orquestación de agentes y extensiones; ACP/BYOK/local no confirmados | Sí, menor madurez |

Consulta la [matriz completa con fuentes](https://github.com/Voldigoade/ide-research/blob/main/research/agent-compatibility.md), que separa soporte demostrado e incertidumbre.

## Seguridad y privacidad

Un agente puede leer el repositorio, modificar archivos, ejecutar comandos y contactar un proveedor. Revisa proveedor, retención, cuotas, permisos, herramientas MCP y plan comercial. ACP/MCP estandarizan conexiones, no la seguridad del agente. Cada extensión tiene licencia y cadena de suministro propias.
