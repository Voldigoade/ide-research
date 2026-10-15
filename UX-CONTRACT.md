# UX contract

- The site is static. The chooser, score explorer, and comparator run entirely in the browser.
- No analytics, cookies, accounts, backend, third-party scripts, remote fonts, or network requests are used by interactive tools.
- Controls work with keyboard and screen readers. State changes are announced in a polite live region.
- A visitor can compare 2 to 4 environments and inspect the criterion ranges behind each result.
- Scenario changes use explicit stack composition and criterion weights. They do not merely increase one generic score.
- Local state is not persisted. No query string is written.
- Provide a link to the method and evidence near every result.
- Never present a computed ranking as an empirical probability.
