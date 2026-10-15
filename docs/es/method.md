---
description: "La investigación refleja el 15 de octubre de 2026."
---

# Método e incertidumbre

La investigación refleja el 15 de octubre de 2026. Conserva el barrido previo y las fuentes recopiladas, y vuelve a examinar candidatos descartados y cambios recientes. Las fuentes oficiales prueban las funciones documentadas, no la calidad real, privacidad, seguridad o velocidad. Los foros e issues son testimonios, no muestras representativas.

Las puntuaciones son intervalos de 1 a 10, no intervalos estadísticos. El modelo equilibrado usa 55% de stack y 45% de workflow. Los escenarios especializados usan 75% Rust/Tauri, 65% web, 68% Python, 15% agentes IA, 30% privacidad, 38% remote y 40% en perfiles por sistema operativo. La composición también cambia: Rust/Tauri dominante asigna 55% del trabajo a Rust y 25% a Tauri. Pesos en data/scenarios.json. La mezcla y los pesos están en `data/scenarios.json`.

El análisis reproducible muestrea notas dentro de sus intervalos y modifica pesos de stack y workflow en +/-20%. Publica rango mediano, intervalo p10-p90 y frecuencia de victoria redondeada al porcentaje. Son diagnósticos del modelo, no probabilidades objetivas.

## Evidencia de rendimiento

- **MEDIDO:** no se realizó benchmark entre IDEs. JetBrains publica cinco pruebas WSL de IJent contra 9P en IDEA Ultimate y Spring Framework; es evidencia del proveedor sobre su arquitectura, no comparación de productos.
- **CORROBORADO:** la documentación describe LSP, indexación, remoto y debugging, no velocidad relativa.
- **TESTIMONIOS RECURRENTES:** usuarios comentan inicio, RAM/CPU, repositorios grandes, WSL y latencia. Son muestras voluntarias sin recuento.
- **INFERENCIA:** el renderizado nativo puede reducir carga de UI, pero language servers e indexación pueden dominar.

Los precios cambian por región y plan. Comprueba licencias comerciales, costes de agentes/modelos y términos de extensiones.
