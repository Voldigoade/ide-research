from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen
import json

ROOT = Path(__file__).resolve().parents[1]
sources = json.loads((ROOT / "data/sources.json").read_text(encoding="utf-8"))

def check(source):
    request = Request(source["url"], method="HEAD", headers={"User-Agent":"ide-research-link-check/1.0"})
    try:
        with urlopen(request, timeout=15) as response:
            return source["id"], response.status, ""
    except Exception as exc:
        return source["id"], 0, str(exc)

failures = []
with ThreadPoolExecutor(max_workers=8) as pool:
    for source_id, status, message in pool.map(check, sources):
        if status and status < 400:
            continue
        # Some publishers deny HEAD or automated requests. Report for review rather than
        # treating access controls as proof that the source page has disappeared.
        print(f"REVIEW {source_id}: HTTP {status or 'unavailable'} {message}")
        failures.append(source_id)
print(f"Checked {len(sources)} URLs; {len(failures)} need human review.")
