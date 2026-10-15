# Contributing

Thanks for improving the evidence.

## Research changes

1. Edit canonical records in `data/`, then update the research pages derived from them.
2. Add or revise the source in `data/sources.json`. Prefer official documentation, release notes, source repositories, terms, pricing pages, and advisories.
3. Attach source IDs to material product claims. Record the page title, publisher, URL, date checked, scope, and evidence class.
4. Keep claims version and platform specific. Mark missing evidence as UNKNOWN.
5. Treat forum posts and issue reports as field reports, not prevalence measurements.
6. Do not infer security from open source status, privacy from encryption alone, or performance from vendor claims.
7. Keep translations aligned in meaning. English is the canonical research language.

## Local validation

```sh
python scripts/check_repo.py
python -m unittest discover -s tests
node --test tests/*.test.cjs
python -m mkdocs build --strict
```

External-link checks are scheduled separately because vendor sites can rate-limit CI and move pages.

## Style

- No U+2014 EM DASH character in authored files.
- Commit messages are ASCII, English, and describe one coherent change.
- No fabricated dates, benchmark results, source material, or authorship.
- Avoid adding dependencies to the public site.
