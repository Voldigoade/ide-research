from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []
EXCLUDED = {".git", "site", "node_modules", "__pycache__", ".playwright", "test-results", "playwright-report", ".venv"}

def stable_hash(path):
    raw=path.read_bytes()
    try:
        raw=raw.decode("utf-8").replace("\r\n","\n").replace("\r","\n").encode("utf-8")
    except UnicodeDecodeError:
        pass
    return hashlib.sha256(raw).hexdigest()

def fail(message):
    ERRORS.append(message)

def json_file(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return None

def iter_files():
    for path in ROOT.rglob("*"):
        if any(part in EXCLUDED for part in path.parts):
            continue
        if path.is_file():
            yield path

all_files=list(iter_files())
for path in all_files:
    try:
        text=path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    if chr(0x2014) in text:
        fail(f"{path.relative_to(ROOT)} contains U+2014 EM DASH")
    if path.name != "check_repo.py" and re.search(r"(?i)\b(?:TODO|FIXME|Lorem ipsum|placeholder text)\b",text):
        fail(f"{path.relative_to(ROOT)} contains a placeholder")
    if re.search(r"(?i)(gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,})",text):
        fail(f"{path.relative_to(ROOT)} may contain a credential")

criteria=json_file(ROOT/"data/criteria.json") or []
products=json_file(ROOT/"data/environments.json") or []
scenarios=json_file(ROOT/"data/scenarios.json") or []
sources=json_file(ROOT/"data/sources.json") or []
agents=json_file(ROOT/"data/agents.json") or []
for name,rows in (("criteria",criteria),("environments",products),("scenarios",scenarios),("sources",sources),("agents",agents)):
    ids=[x.get("id") for x in rows]
    if len(set(ids))!=len(ids):fail(f"duplicate {name} IDs")
criterion_ids=[x["id"] for x in criteria]; source_ids={x["id"] for x in sources}
product_ids={x["id"] for x in products}
if {x.get("id") for x in agents}!=product_ids:fail("agents matrix IDs must match finalist IDs")
for row in agents:
    for key in ("name","ide_complete","architecture","copilot","codex","claude","acp","mcp","byok","local_models","without_ai"):
        if not row.get(key):fail(f"agents/{row.get('id')}: missing {key}")
    missing=set(row.get("sources",[]))-source_ids
    if missing:fail(f"agents/{row.get('id')}: missing source IDs {sorted(missing)}")
for product in products:
    values=product.get("scores","").split(",")
    if len(values)!=len(criterion_ids):fail(f"{product.get('id')}: expected {len(criterion_ids)} scores, found {len(values)}")
    for key,value in zip(criterion_ids,values):
        try:
            low,high=[float(part) for part in value.split("-")]
            if not (1<=low<=high<=10):fail(f"{product['id']}/{key}: invalid range {value}")
        except Exception:fail(f"{product.get('id')}/{key}: malformed range {value}")
    missing=set(product.get("sources",[]))-source_ids
    if missing:fail(f"{product['id']}: missing source IDs {sorted(missing)}")
    confidence=product.get("confidence",{})
    if set(confidence)!=set(criterion_ids):fail(f"{product['id']}: confidence map must cover every scored criterion")
    if set(confidence.values())-{"high","medium","low"}:fail(f"{product['id']}: invalid confidence level")
    for key in ("id","name","type","version","checked","architecture","notes"):
        if not product.get(key):fail(f"{product.get('id')}: missing {key}")
for scenario in scenarios:
    if set(scenario.get("stack",{}))!={"rust","tauri","web","python","other"}:fail(f"{scenario.get('id')}: stack keys mismatch")
    if round(sum(scenario.get("stack",{}).values()))!=100:fail(f"{scenario.get('id')}: stack mix must total 100")
    if sum(scenario.get("dimensions",{}).values())<=0:fail(f"{scenario.get('id')}: workflow dimensions must be positive")
    if not 10<=scenario.get("stack_weight",55)<=80:fail(f"{scenario.get('id')}: invalid stack weight")
    missing=set(scenario.get("dimensions",{}))-set(criterion_ids)
    if missing:fail(f"{scenario.get('id')}: unknown dimensions {sorted(missing)}")
    if not scenario.get("dimensions"):fail(f"{scenario.get('id')}: no workflow dimensions")
for source in sources:
    if not re.match(r"^https://",source.get("url","")):fail(f"{source.get('id')}: source must use HTTPS")
    if source.get("checked")!="2026-10-15":fail(f"{source.get('id')}: stale audit check date")
pages={}
for locale,directory in (("fr",ROOT/"docs"),("en",ROOT/"docs/en"),("es",ROOT/"docs/es")):
    pages[locale]={p.stem for p in directory.glob("*.md")}
if not (pages["fr"]==pages["en"]==pages["es"]):fail(f"translation page parity mismatch: {pages}")
for path in all_files:
    if path.suffix!=".md":continue
    text=path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)",text):
        if target.startswith(("http://","https://","mailto:","#")):continue
        local=target.split("#",1)[0]
        if not local:continue
        resolved=(path.parent/local).resolve()
        if not resolved.exists():fail(f"{path.relative_to(ROOT)}: broken local link {target}")
manifest=json_file(ROOT/"research/manifest.json") or {}
manifest_rows=manifest.get("files",[])
manifest_map={row.get("path"):row.get("sha256") for row in manifest_rows}
expected={path.relative_to(ROOT).as_posix():stable_hash(path) for path in all_files if path.relative_to(ROOT).as_posix()!="research/manifest.json"}
if set(manifest_map)!=set(expected):
    fail(f"manifest paths differ: missing={sorted(set(expected)-set(manifest_map))}, extra={sorted(set(manifest_map)-set(expected))}")
for name,digest in expected.items():
    if manifest_map.get(name)!=digest:fail(f"manifest hash mismatch: {name}")
if ERRORS:
    print("\n".join(f"ERROR: {item}" for item in ERRORS));sys.exit(1)
print(f"Repository checks passed: {len(products)} environments, {len(agents)} agent profiles, {len(criteria)} criteria, {len(scenarios)} scenarios, {len(sources)} sources, {len(pages['fr'])} translated pages.")
