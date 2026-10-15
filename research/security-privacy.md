# Security, privacy, and trust boundaries

This is a product comparison, not a security audit or certification. Security depends on OS configuration, extensions, model provider, account, repository contents, network path, and agent permissions.

## Threat model

Assets include source code, credentials, local build artifacts, and repository metadata. Relevant adversaries include malicious or compromised extensions, malicious repository instructions, compromised model/tool providers, account takeover, and compromised endpoints.

| Boundary | Main concern | Practical control |
|---|---|---|
| Editor and extension | Extensions can run code, read files, launch processes, and make network requests | Verify publisher/source/license/permissions; minimize extensions; update deliberately |
| Agent and repository | Malicious repository instructions can trigger unsafe actions or disclosure | Review diffs; require approval for destructive/network operations; limit workspace permissions |
| Model provider | Requests, code context, retention, telemetry, and subprocessors vary | Read current terms; use privacy controls; keep secrets out of context; consider local models |
| Remote host/container | Credentials and local/remote trust boundaries differ | Least-privilege SSH keys, isolated containers, signed images, scoped tokens |
| Marketplace/build | Publisher, supply chain, and distribution differ | Check exact publisher and marketplace; VSCodium Open VSX differs from Microsoft's marketplace |

## Product notes

- VS Code: telemetry settings, Copilot and other cloud features have separate terms.
- VSCodium: community build without Microsoft telemetry defaults; extension network activity still matters.
- JetBrains: distinguish IDE telemetry, AI Assistant data sharing, and third-party providers.
- Cursor, Devin, Kiro, Antigravity: cloud agents may need broad repository access; review privacy mode, retention, model, plan, and enterprise terms.
- Zed: local models are possible, while hosted services and agent protocols have distinct trust boundaries.
- Neovim: local core does not make third-party plugins or language servers trustworthy by default.
- Theia: the downloadable desktop IDE differs from its experimental self-hosted Docker deployment; operating the latter makes the operator responsible for patching and service security.

A disclosed product vulnerability is not automatically present-day risk. Verify affected versions, prerequisites, fixes, exposure, and deployment. AWS advisory CVE-2026-95985 describes agentic writes to global configuration from untrusted workspaces in Kiro releases before 1.0.242; AWS says it was fixed in 1.0.242. The reviewed Kiro 1.3.0 release is later. This is a patched historical issue, not evidence of an unpatched flaw in the current release. AWS advises users of affected versions to review the global Kiro configuration directory.
