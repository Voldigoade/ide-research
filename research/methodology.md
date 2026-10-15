# Research methodology

## Evidence hierarchy

Official documentation, release notes, license terms, security advisories, and source repositories establish documented claims. Independent technical reporting may corroborate observed behavior. Forums and issue tickets are field reports, not representative samples. Ranking is an explicit inference from these sources and the target workflow.

Evidence labels: SOURCED, CORROBORATED, INFERENCE, UNCERTAIN, UNKNOWN, and MEASURED. A measurement is labeled MEASURED only when an actual controlled measurement is conducted or sourced. JetBrains publishes a five-run, vendor-side WSL comparison of IJent and 9P on IntelliJ IDEA; this is scoped evidence about file transport, not a cross-IDE benchmark.

## Decision model

Candidates have editorial ranges from 1 to 10 for 27 scored criteria, separating capabilities, UX, price, lock-in, and operating systems. Pairwise duels compare the 23 requested product dimensions; Docker and Dev Containers are combined in the containers row, while operating-system scores remain in platform scenarios. The balanced profile weights stack mix 55 percent and workflow 45 percent. Specialist profiles change this split: Rust/Tauri uses 75 percent stack, Python uses 68 percent, remote/OS profiles around 38 to 40 percent, and agent/privacy profiles 15 to 30 percent. The exact mix and weights are stored in data/scenarios.json; score ranges and per-rating evidence confidence are in data/environments.json. Ranges are plausible editorial bounds, not statistical confidence intervals or measurements.

The model performs 20,000 seeded Monte Carlo draws for ratings-only, weights-only, and combined uncertainty. High-confidence scores are center-weighted, medium-confidence scores are uniform, and low-confidence scores randomly emphasize the optimistic or pessimistic edge. Confidence classifies evidence quality, not objective winner probability. Win frequencies show stability inside the stated model and are not objective market probabilities.

## Currentness and cost

The source register date is 2026-10-15. Product versions, prices, terms, plugin support, marketplace access, AI provider behavior, and privacy policies change. Recheck before purchase or commercial deployment.
