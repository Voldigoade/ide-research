from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "research"
products = json.loads((DATA / "environments.json").read_text(encoding="utf-8"))
criteria = json.loads((DATA / "criteria.json").read_text(encoding="utf-8"))
scenarios = json.loads((DATA / "scenarios.json").read_text(encoding="utf-8"))
sources = json.loads((DATA / "sources.json").read_text(encoding="utf-8"))
results = json.loads((OUT / "model-results.json").read_text(encoding="utf-8"))
source_by_id = {x["id"]: x for x in sources}
criterion_ids = [x["id"] for x in criteria]
EXCLUDED = {".git", "site", "node_modules", "__pycache__", ".playwright", "test-results", "playwright-report", ".venv"}

def stable_bytes(path):
    raw = path.read_bytes()
    try:
        return raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
    except UnicodeDecodeError:
        return raw

def scores_for(product):
    return {key: tuple(float(n) for n in value.split("-")) for key, value in zip(criterion_ids, product["scores"].split(","), strict=True)}

def mdlink(source_id):
    source = source_by_id[source_id]
    return f"[{source_id}]({source['url']})"

def build_duels():
    sys.path.insert(0, str(ROOT / "scripts"))
    import analyze
    ranked = analyze.evaluate(analyze.RATINGS, next(x for x in scenarios if x["id"]=="balanced"))
    top = [row[0] for row in ranked[:5]]
    by_id = {p["id"]: p for p in products}
    pairs = [(top[i], top[j]) for i in range(len(top)) for j in range(i+1,len(top))]
    for aid,bid in (("vscode","rustrover"),("idea","rustrover")):
        pair = (by_id[aid],by_id[bid])
        if not any((a["id"],b["id"])==(aid,bid) for a,b in pairs): pairs.append(pair)
    keywords = {
        "rust":["rust"],"tauri":["tauri"],"web":["typescript","javascript","react","next","web"],
        "python":["python"],"databases":["database","sql"," db"],"docker":["docker"],"containers":["docker","devcontainer","container"],
        "devcontainers":["devcontainer"],"wsl":["wsl"],"remote":["remote","ssh"],
        "git":["git","github"],"terminal":["terminal","shell"],"debugging":["debug","dap"],
        "code_intelligence":["language support","rust","python","typescript","lsp"],
        "refactoring":["refactor","rust","python","typescript"],
        "plugins":["extension","plugin","marketplace","openvsx"],
        "ai":["agent","copilot","ai","model","byok"],
        "external_agents":["agent","acp","mcp","codex","claude"],
        "security":["security","cve","sandbox","privacy","license","terms","permissions","execution"],"privacy":["privacy","telemetry","data handling"],
        "performance":["benchmark","performance","memory","wsl-benchmark"],
        "stability":["release","changelog"],"ux":["ux","experience","community"],
        "windows":["windows"],"linux":["linux"],"macos":["macos"],
        "price":["price","pricing"],"lockin":["license","terms","openvsx","privacy"]
    }
    prefixes = {
        "vscode":("vscode.","tauri.vscode","codex.","claude.","pricing.vscode"),
        "idea":("idea.","pricing.jetbrains-idea","pricing.jetbrains-ai","pricing.jetbrains-pack"),
        "rustrover":("rustrover.","idea.rust","tauri.","pricing.jetbrains-rustrover","pricing.jetbrains-pack"),
        "pycharm":("pycharm.","idea.python","idea.web","idea.db","idea.docker","idea.wsl","pricing.jetbrains-pycharm","pricing.jetbrains-pack"),
        "vscodium":("vscodium.","vscode.","tauri.vscode","pricing.vscodium"),
        "cursor":("cursor.","vscode.","community.cursor","pricing.cursor"),
        "zed":("zed.","community.zed","community.vscode-zed","tauri.","pricing.zed"),
        "neovim":("nvim.","community.neovim-rust","pricing.neovim"), "theia":("theia.",),
        "devin":("devin.","vscode.","pricing.devin"), "kiro":("kiro.","cve.kiro","vscode.","pricing.kiro"),
        "antigravity":("antigravity.","vscode.wsl","pricing.antigravity","pricing.antigravity-change"),
        "sublime":("sublime.","pricing.sublime")
    }
    def source_trail(product,key):
        if key=="price":
            current_price_source={
                "vscode":"pricing.vscode","idea":"pricing.jetbrains-idea",
                "rustrover":"pricing.jetbrains-rustrover","pycharm":"pricing.jetbrains-pycharm",
                "vscodium":"pricing.vscodium","cursor":"pricing.cursor","zed":"pricing.zed",
                "neovim":"pricing.neovim","sublime":"pricing.sublime","devin":"pricing.devin",
                "kiro":"pricing.kiro","antigravity":"pricing.antigravity"
            }.get(product["id"])
            if current_price_source in source_by_id:
                return mdlink(current_price_source)
        terms=keywords.get(key,[])
        candidates=[s for s in sources if s["id"].startswith(prefixes.get(product["id"],()))]
        hits=[s["id"] for s in candidates if any(term in (s["id"]+" "+s["title"]).lower() for term in terms)]
        if not hits:
            return "No criterion-specific source in the retained register; relative rating is an editorial inference"
        return ", ".join(mdlink(sid) for sid in hits[:2])
    duel_dimensions = [
        ("Code intelligence", ["code_intelligence"], "code_intelligence"),
        ("Refactoring", ["refactoring"], "refactoring"),
        ("Debugging", ["debugging"], "debugging"),
        ("Rust", ["rust"], "rust"),
        ("TypeScript, React and Next.js", ["web"], "web"),
        ("Python", ["python"], "python"),
        ("Tauri", ["tauri"], "tauri"),
        ("Git and GitHub", ["git"], "git"),
        ("Database tooling", ["databases"], "databases"),
        ("Terminal", ["terminal"], "terminal"),
        ("WSL2", ["wsl"], "wsl"),
        ("Remote SSH", ["remote"], "remote"),
        ("Containers (Docker and Dev Containers)", ["docker", "devcontainers"], "containers"),
        ("Plugins", ["plugins"], "plugins"),
        ("Integrated AI", ["ai"], "ai"),
        ("External agents and protocols", ["external_agents"], "external_agents"),
        ("Security", ["security"], "security"),
        ("Privacy", ["privacy"], "privacy"),
        ("Performance", ["performance"], "performance"),
        ("Stability", ["stability"], "stability"),
        ("UX", ["ux"], "ux"),
        ("Price and commercial license", ["price"], "price"),
        ("Vendor lock-in and portability", ["lockin"], "lockin")
    ]
    lines=["# Direct duels: balanced top five and Rust specialists","","The first five are sorted by balanced median score. Every pair is compared across the 23 requested dimensions. Docker and Dev Containers are averaged in the single containers row; OS-specific scores remain in the scenario model. A win requires non-overlapping editorial ranges; overlapping ranges are uncertain; identical ranges are equal. The direct VS Code/IDEA duel tests the previous #1 against the strongest challenger. Additional VS Code/RustRover and IDEA/RustRover tables test the Rust specialist. Sources support documented capabilities; ranges and relative ordering remain editorial inference, not a controlled product trial.","","## Balanced top five",""]
    for rank,product in enumerate(top,1): lines.append(f"{rank}. **{product['name']}**")
    lines += ["","## Pairwise tables",""]
    for a,b in pairs:
        lines += [f"### A: {a['name']} vs B: {b['name']}","","| Criterion | A range | B range | Outcome | Basis and sources |","|---|---:|---:|---|---|"]
        av,bv=scores_for(a),scores_for(b)
        for label,keys,evidence_key in duel_dimensions:
            alo= sum(av[key][0] for key in keys)/len(keys); ahi=sum(av[key][1] for key in keys)/len(keys)
            blo= sum(bv[key][0] for key in keys)/len(keys); bhi=sum(bv[key][1] for key in keys)/len(keys)
            if (alo,ahi)==(blo,bhi): outcome,reason="Equal","The editorial ranges are identical; evidence does not distinguish them."
            elif alo>bhi: outcome,reason="A wins",f"A's lower bound exceeds B's upper bound; the modeled advantage is on {label.lower()}."
            elif blo>ahi: outcome,reason="B wins",f"B's lower bound exceeds A's upper bound; the modeled advantage is on {label.lower()}."
            else: outcome,reason="Uncertain","Ranges overlap; documentation does not establish comparative implementation quality."
            trails=source_trail(a,evidence_key)+"; "+source_trail(b,evidence_key)
            lines.append(f"| {label} | {alo:.1f} to {ahi:.1f} | {blo:.1f} to {bhi:.1f} | {outcome} | {reason} Evidence trail: {trails}. |")
        lines.append("")
    lines += ["## Interpretation","","Many results are uncertain because plausible intervals overlap. Sources establish advertised or documented capabilities; performance, UX, and stability remain weakly measured. The Rust specialist duels matter for the Rust/Tauri scenario even when RustRover is below the balanced top five.",""]
    (OUT/"duels-top-five.md").write_text("\n".join(lines),encoding="utf-8")
def build_register():
    lines = ["# Evidence register", "", f"Records checked for this audit: 2026-10-15. Total: {len(sources)}. The checked date means a source was included in the current source set; it does not guarantee future URL availability or independent verification.", "", "| ID | Publisher | Type | Evidence | Title | URL |", "|---|---|---|---|---|---|"]
    for s in sources: lines.append(f"| {s['id']} | {s['publisher']} | {s['kind']} | {s['evidence']} | {s['title']} | [open]({s['url']}) |")
    (OUT / "evidence-register.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    access_path = OUT / "source-accessibility.json"
    expected_ids = {source["id"] for source in sources}
    source_date = max((source.get("checked", "") for source in sources), default="")
    try:
        previous = json.loads(access_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        previous = {}
    if previous.get("checked_on") == source_date and set(previous.get("status", {})) == expected_ids:
        access = previous
    else:
        access = {
            "checked_on": source_date,
            "method": "Not checked in this build. Run scripts/check_links.py for HTTP reachability checks.",
            "status": {source["id"]: "not_checked" for source in sources},
        }
    access_path.write_text(json.dumps(access, indent=2)+"\n", encoding="utf-8")

def build_scenarios():
    names = {p["id"]:p["name"] for p in products}
    lines = ["# Scenario results", "", "Explicit stack mixtures and workflow weights are in data/scenarios.json. Midpoints sort the list; ranges remain visible.", "", "| Scenario | Stack mix: Rust / Tauri / Web / Python / other | Winner | Score range | Runner-up | Score range | Overlap |", "|---|---|---|---:|---|---:|---|"]
    for s in scenarios:
        r=results["scenario_results"][s["id"]]
        mix=" / ".join(f"{s['stack'][k]}%" for k in ("rust","tauri","web","python","other"))
        lo=" to ".join(f"{x:.1f}" for x in r["winner_range"]); rlo=" to ".join(f"{x:.1f}" for x in r["runner_up_range"])
        lines.append(f"| {s['label']} | {mix} | {names[r['winner']]} | {lo} | {names[r['runner_up']]} | {rlo} | {'yes' if r['overlap'] else 'no'} |")
    lines += ["", "A scenario winner is an indicative recommendation, not a universal result.", ""]
    (OUT / "scenario-results.md").write_text("\n".join(lines),encoding="utf-8")

def build_sensitivity():
    modes=results["balanced_sensitivity"]
    lines=["# Sensitivity to ratings and weights","","Each Monte Carlo view has 20,000 draws with a fixed seed. Score intervals are subjective plausibility ranges, not statistical confidence intervals. High-confidence scores are center-weighted, medium-confidence scores uniform, and low-confidence scores use a random optimistic or pessimistic triangular mode within the declared interval. Weight draws multiply stack shares, workflow dimensions, and stack/workflow balance by declared random factors and renormalize. Win frequencies describe stability of this editorial model only, not objective odds.",""]
    for mode,title in (("combined","Combined uncertainty"),("weights","Weights varied, ratings fixed"),("ratings","Ratings varied, weights fixed")):
        lines += [f"## {title}","","| Environment | Rounded model win frequency | Median rank | Score p10 to p90 |","|---|---:|---:|---:|"]
        rows=modes[mode]["candidates"]
        for p in sorted(products,key=lambda x:rows[x["id"]]["median_rank"]):
            r=rows[p["id"]]; lines.append(f"| {p['name']} | {r['win_frequency_percent_rounded']}% | {r['median_rank']:.1f} | {r['score_p10_p90'][0]:.1f} to {r['score_p10_p90'][1]:.1f} |")
        lines.append("")
    lines += ["Interpretation: frequencies depend on subjective ranges, chosen weights, randomization, and seed. They do not estimate user satisfaction or market probability."]
    (OUT/"sensitivity.md").write_text("\n".join(lines)+"\n",encoding="utf-8")

def build_final_report():
    names={p["id"]:p["name"] for p in products}
    scenario_lines=[]
    for scenario in scenarios:
        row=results["scenario_results"][scenario["id"]]
        wr=" to ".join(f"{x:.1f}" for x in row["winner_range"])
        rr=" to ".join(f"{x:.1f}" for x in row["runner_up_range"])
        mix=" / ".join(f"{scenario['stack'][k]}%" for k in ("rust","tauri","web","python","other"))
        scenario_lines.append(f"| {scenario['label']} | {mix} | {names[row['winner']]} ({wr}) | {names[row['runner_up']]} ({rr}) | {'yes' if row['overlap'] else 'no'} |")
    sensitivity=results["balanced_sensitivity"]["combined"]["candidates"]
    ranked=sorted(products,key=lambda p:sensitivity[p["id"]]["median_rank"])
    top_lines=[]
    for i,p in enumerate(ranked[:5],1):
        r=sensitivity[p["id"]]
        top_lines.append(f"| {i} | {p['name']} | {r['win_frequency_percent_rounded']}% | {r['median_rank']:.1f} | {r['score_p10_p90'][0]:.1f} to {r['score_p10_p90'][1]:.1f} |")
    text="""# IDE comparison: adversarial audit

**Audit date:** 2026-10-15  
**Previous verdict:** CONFIRMED WITH RESERVATIONS  
**Balanced recommendation:** Visual Studio Code, with an overlapping and model-sensitive lead over IntelliJ IDEA Ultimate.

This is a continuation of the earlier approximately 40-candidate scan. The existing source set and user profile are retained. The main correction is that IntelliJ IDEA Ultimate 2026.2 can combine JetBrains' official Rust and Python plugins with web, database, container, WSL, remote, Git, and agent tooling. The first verdict survives, but its reasoning and margin need correction.

## Previous finalists, reinstatements, and exits

The updated shortlist deliberately has twelve candidates to preserve likely scenario winners: VS Code, IntelliJ IDEA Ultimate, RustRover, PyCharm Professional, VSCodium, Cursor, Zed, Neovim, Sublime Text 4, Devin Desktop, Kiro, and Google Antigravity. IDEA is restored as a leading challenger. RustRover and PyCharm remain because their dedicated language workflows can win specialist profiles. Agentic products are retained only as complete editing environments, not on agent quality alone. VSCodium, Zed, Neovim, and Sublime Text remain for local control, native editing, terminal workflows, or extensibility.

Fleet is a confirmed exit: JetBrains ended standalone Fleet downloads on 2025-12-22 and said in May 2026 that Fleet had evolved into Air. Air remains an agent system, with Air in IDEs only an early-access plugin in October 2026, rather than a replacement Rust/Python/TypeScript language engine. Nova is macOS-only, so it cannot serve the cross-platform Windows/WSL/Linux profile. Lapce, Helix, Emacs, and an independent Air entry have larger gaps or represent an agent layer rather than a code IDE. Eclipse Theia IDE is a real downloadable desktop product for Windows, Linux, and macOS. It remains outside the final twelve because the retained sources do not establish low-friction coverage of the complete required stack and remote/container integrations in the packaged product. Sublime Text was reinstated after checking its current LSP and DAP packages; see `market-scan.md`.

## JetBrains, evaluated separately

IntelliJ IDEA Ultimate 2026.2 deserves a final place. JetBrains states that the IDEA Rust plugin maintains feature parity with RustRover, while its comparison documentation lists setup, debugger, and profiler differences. LLDB/GDB debugging requires the free Native Debugging Support plugin. The official Python plugin implements PyCharm functionality. IDEA also documents TypeScript, React, Next.js, database tools, Docker, Dev Containers, WSL, SSH/Remote Development, and Git. This makes a single IDE configuration capable of combining most of the relevant JetBrains language and workflow features. It does not prove identical ergonomics across products or equivalent performance on the user's repository.

AI integrations have materially changed: AI Assistant documents Codex, Claude Agent, Junie, and ACP-compatible agents; JetBrains Air can run ACP agents and documents a Linux agent executable inside WSL; the official GitHub Copilot plugin is separate. IDEA provides an MCP server/client workflow. BYOK is available for selected providers and agents. Ollama and LM Studio can power supported AI Assistant features, but current documentation says agents cannot use local models and local models cannot call configured MCP tools. A local model option therefore does not make the agent workflow fully local. Confirm current commercial licensing and separate AI service costs before purchase.

RustRover remains the strongest dedicated Rust/Cargo contender, but its broader Python and Next.js fit is weaker than IDEA or VS Code. PyCharm Professional remains the Python specialist with Rust as a secondary plugin workflow. Product-level plugins, price, rights, and practical dependencies are detailed in `extensions.md` and `agent-compatibility.md`.

## Updated top five

| Rank | Candidate | Combined model win frequency | Median rank | Score p10 to p90 |
|---:|---|---:|---:|---:|
"""+"\n".join(top_lines)+"""

The 20,000-draw frequencies describe stability of this editorial model, not market probability or user satisfaction. The score ranges are subjective bounds, not confidence intervals from a benchmark. VS Code and IDEA overlap materially; the lead is real in the chosen model but not decisive evidence of a universal winner.

## Profile scenarios

| Scenario | Stack mix: Rust / Tauri / web / Python / other | Median winner range | Runner-up range | Overlap |
|---|---|---|---|---|
"""+"\n".join(scenario_lines)+"""

Stack composition changes per scenario. Rust/Tauri is explicitly 55% Rust plus 25% Tauri; web/full-stack assigns 60% web; the AI-agent scenario changes the agent workflow weight; local-first emphasizes privacy and security. Windows, Linux, and macOS are separate profiles. Full scenario weights and results are reproducible from `data/scenarios.json` and `model-results.json`.

## Agentic editors are complete IDE candidates

Cursor, Devin Desktop, Kiro, and Antigravity are assessed as editing environments as well as agent products. They differ in architecture, extensions, debugging, Git, OS and WSL/remote fit, maturity, privacy, pricing, and usefulness with AI disabled. VS Code, JetBrains IDEs, Zed, Neovim, and other extensible editors can also host agents or agent protocols. The feature matrix in `agent-compatibility.md` distinguishes native features, plugins, external CLIs, ACP, MCP, BYOK, and local models.

## Performance evidence

- **MEASURED:** JetBrains reports five runs on Windows 11, WSL2 Ubuntu 24.04, IntelliJ IDEA Ultimate 263.SNAPSHOT, and the Spring Framework tree (23 subprojects, 8,191 files). For native IJent versus the previous 9P file path it reports cold open 18.5 to 11.5 seconds, tree traversal 8.1 to 3.7 seconds, indexing 10.8 to 8.4 seconds, and file read 12.2 to 5.7 seconds. This is a vendor measurement of its WSL transport change, not an independent IDE comparison.
- **CORROBORATED:** official product documentation establishes which language engines, indexers, debuggers, remote hosts, and containers are supported. It does not establish comparative startup, RAM, CPU, input latency, search, monorepo, or branch-switch performance.
- **RECURRING TESTIMONY:** reports from Rust users describe trade-offs between RustRover analysis/refactoring and Rust Analyzer startup or resource use. Zed issues report specific WSL memory, project-search memory, and ACP memory problems. These reports are self-selected and do not establish prevalence.
- **INFERENCE:** local repository size, extension set, language-server version, filesystem placement, and OS can dominate the experience. A short controlled trial on the actual project is the best remaining performance evidence.

Selected field reports and issue threads are indexed in `data/sources.json` and `evidence-register.md`. They are leads, not vote counts.

## Security, privacy, cost, and dependency burden

Treat editor extensions, language servers, MCP tools, ACP agents, shell CLIs, and cloud agents as separate trust boundaries. Any of them can receive source context or execute code depending on configuration. Local model support reduces some provider exposure but does not secure the endpoint or plugins. Open source and privacy modes do not prove zero telemetry or safety.

The source register records AWS advisory CVE-2026-95985 for Kiro versions before 1.0.242. AWS states it was fixed in 1.0.242; the reviewed Kiro 1.3.0 release is later. This is a patched historical issue, not evidence that the current reviewed version remains vulnerable. Users who ran affected versions with untrusted workspaces should follow the vendor's configuration review guidance.

Minimal extension/plugin configurations and estimated critical dependency counts are in `extensions.md`. The dated price snapshot and commercial-license distinctions are in `pricing.md`. At the checked individual annual rate, IDEA Ultimate is $199 in year one; JetBrains' All Products Pack is $299 in year one and includes RustRover, PyCharm, Air, and AI Pro. VS Code is free for commercial use, Sublime Text is $99 one-time for a personal license with three years of updates, and agent products have separate quota/usage charges. The model's price criterion remains a broad editorial range and does not assume a paid AI subscription or estimate token use.

## Sensitivity and direct duels

`duels-top-five.md` compares the five best balanced candidates pairwise across all 23 criteria, then adds VS Code/RustRover and IDEA/RustRover. The former #1 versus its strongest challenger, VS Code versus IDEA, is included. Equal ranges are marked Equal; disjoint ranges produce A wins or B wins; overlapping ranges remain Uncertain. The sensitivity report separately varies weights, ratings, and both together.

## Final answer

**If I had to install one environment today for the balanced polyglot profile and stop searching, I would choose: Visual Studio Code.**

It gives the broadest, most consistent cross-platform workflow for Rust/Tauri, TypeScript/React, Python, Git, WSL, SSH, containers, and optional external agents, while remaining fully useful with AI off. IntelliJ IDEA Ultimate 2026.2 is the closest and strongest challenger: its lead deficit is small, the ranges overlap, and JetBrains' official plugin combination now covers far more of the stack than the first report credited. The verdict would most likely reverse if the user's own Rust-heavy monorepo shows IDEA's refactoring/debugging advantage without unacceptable memory or indexing cost, or if the user's workflows rely more heavily on JetBrains integrations than on VS Code remote/extension breadth.
"""
    (OUT/"final-report.md").write_text(text,encoding="utf-8")

def build_manifest():
    records=[]
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or any(x in path.parts for x in EXCLUDED): continue
        if path.relative_to(ROOT).as_posix()=="research/manifest.json": continue
        records.append({"path":path.relative_to(ROOT).as_posix(),"sha256":hashlib.sha256(stable_bytes(path)).hexdigest()})
    (OUT/"manifest.json").write_text(json.dumps({"version":"1.0.0","updated":"2026-10-15","files":records},indent=2)+"\n",encoding="utf-8")

build_register(); build_scenarios(); build_sensitivity(); build_duels(); build_final_report(); build_manifest()
print("Generated evidence register, scenario results, sensitivity, duels, and manifest.")
