# IDE Research

A source-linked comparison of development environments for Rust, Tauri, TypeScript/React/Next.js, Python, databases, containers, remote work, and AI agents.

**As of:** 2026-10-15  
**Current verdict:** VS Code is the strongest balanced default in this model. IntelliJ IDEA Ultimate is the closest integrated-IDE challenger; RustRover wins Rust/Tauri-heavy work; VSCodium leads when local control and reduced vendor telemetry matter most.

The verdict is conditional. Scores are editorial ranges, not benchmark results or objective probabilities. Product versions, platform behavior, licensing, and AI terms change. Read the evidence and scenario fit before relying on a rank.

- [Open the trilingual research site](https://voldigoade.github.io/ide-research/)
- [Method and decision model](research/methodology.md)
- [Full audit](research/final-report.md)
- [Agent compatibility audit](research/agent-compatibility.md)
- [Structured data](data/)
- [Sources](research/evidence-register.md)

## Scope

The shortlist covers VS Code, IntelliJ IDEA Ultimate, RustRover, PyCharm Professional, VSCodium, Cursor, Zed, Neovim, Sublime Text 4, Devin Desktop, Kiro, and Google Antigravity. The wider market scan and exclusions are documented in [the audit](research/final-report.md).

This project compares complete working environments, not just code completion. It considers language intelligence, refactoring, debugging, Git, terminal, WSL/SSH, containers, extensions, AI agents, security, privacy, performance evidence, stability, operating systems, usability, price, and lock-in.

## Reproduce checks

Requirements: Python 3.12+ and Node.js 20+. Build dependencies are pinned in `requirements.txt`.

```sh
python scripts/check_repo.py
python -m unittest discover -s tests
node --test tests/*.test.cjs
python -m mkdocs build --strict
```

The CI workflow also runs a browser smoke test. No telemetry or network calls are used by the site's chooser or comparator.

## Licensing

Research text and data: CC BY-SA 4.0.  
Code, styles, scripts, and configuration: MIT.  
Third-party product names and marks remain with their respective owners.

See [LICENSE-CC-BY-SA-4.0.txt](LICENSE-CC-BY-SA-4.0.txt) and [LICENSE-MIT.txt](LICENSE-MIT.txt).
