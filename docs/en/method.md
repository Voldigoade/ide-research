---
description: "Research state: 15 October 2026."
---

# Method and uncertainty

Research state: 15 October 2026. This audit retains the previous market scan and collected sources, then revisits early exclusions and current product changes. Official product sources establish documented capabilities, not independent proof of quality, privacy, security, or speed. Forums and issues are field reports, not representative samples.

The model scores 27 criteria, separating capabilities, UX, price, lock-in and operating systems. Pairwise duels cover the 23 requested dimensions; Docker and Dev Containers share one containers row, while OS scores remain in platform scenarios. Ratings are editorial ranges from 1 to 10, not statistical confidence intervals. The balanced model uses 55% stack and 45% workflow. Specialist splits are Rust/Tauri 75% stack, web 65%, Python 68%, agents 15%, privacy 30%, remote 38%, and OS profiles 40%. Stack mix also changes explicitly: Rust/Tauri dominant assigns 55% of work to Rust and 25% to Tauri. Exact weights are in data/scenarios.json. The exact stack mixture and weights are public in `data/scenarios.json`.

The reproducible sensitivity script draws high-confidence ratings around the interval midpoint, medium-confidence ratings uniformly, and low-confidence ratings with a randomly optimistic or pessimistic triangular mode. It varies stack composition and cross-cutting weights by +/-20%. It reports median rank, p10-p90 score range, and win frequency rounded to whole percentages. These are model stability diagnostics, not objective odds.

## Performance evidence

- **MEASURED:** no cross-IDE benchmark was conducted. JetBrains publishes five WSL IJent-versus-9P runs on IDEA Ultimate and Spring Framework; this is scoped vendor evidence about its architecture, not an IDE product comparison.
- **CORROBORATED:** official documents describe LSPs, indexing, remote workflows, and debugging, not comparative speed.
- **RECURRING TESTIMONY:** public user reports mention startup, RAM/CPU, large repositories, WSL, or latency. They are self-selected and uncounted.
- **INFERENCE:** native rendering may reduce UI overhead, but language servers and indexing can dominate. Architecture alone does not establish relative performance.

Prices change by region and plan. The source register links official pricing and licensing pages. Verify commercial-use rights, agent/model costs, and extension terms at purchase time.
