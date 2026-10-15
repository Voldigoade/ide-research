from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen
import json

ROOT = Path(__file__).resolve().parents[1]
sources = json.loads((ROOT / "data/sources.json").read_text(encoding="utf-8"))
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
)


def fetch(url, method, headers=None):
    request_headers = {"User-Agent": USER_AGENT}
    if headers:
        request_headers.update(headers)
    request = Request(url, method=method, headers=request_headers)
    with urlopen(request, timeout=20) as response:
        return response.status, response.geturl()


def check(source):
    url = source["url"]
    head_status = 0
    head_message = ""
    try:
        status, final_url = fetch(url, "HEAD")
        if status < 400 and status != 202:
            return source["id"], status, "HEAD", final_url
        head_status = status
    except HTTPError as exc:
        head_status = exc.code
        head_message = str(exc)
    except Exception as exc:
        head_message = str(exc)

    try:
        status, final_url = fetch(url, "GET", {"Range": "bytes=0-0"})
        if status < 400 and status != 202:
            return source["id"], status, "GET", final_url
        if status == 202:
            return source["id"], status, "LIMITED", final_url
        return source["id"], status, "REVIEW", final_url
    except HTTPError as exc:
        detail = f"GET after HEAD {head_status}: {exc}"
        return source["id"], exc.code, "REVIEW", detail
    except Exception as exc:
        detail = f"GET after HEAD {head_status}: {exc}"
        if head_message:
            detail += f"; HEAD error: {head_message}"
        return source["id"], 0, "REVIEW", detail


observations = {}
reviews = []
limited = []
with ThreadPoolExecutor(max_workers=2) as pool:
    for source_id, status, via, detail in pool.map(check, sources):
        if via == "LIMITED":
            observations[source_id] = f"content_not_retrieved_http_{status}"
            print(f"LIMITED {source_id}: HTTP {status} for HEAD and GET; publisher accepted the request without serving page content.")
            limited.append(source_id)
            continue
        if status and status < 400 and via != "REVIEW":
            observations[source_id] = f"reachable_via_{via.lower()}_http_{status}"
            if via != "HEAD":
                print(f"OK {source_id}: HTTP {status} via GET fallback (HEAD was not usable)")
            continue
        observations[source_id] = f"needs_review_http_{status or 'unavailable'}"
        print(f"REVIEW {source_id}: {detail}")
        reviews.append(source_id)

report = {
    "checked_on": datetime.now(timezone.utc).date().isoformat(),
    "method": (
        "HTTP HEAD with a browser-like user agent; when HEAD is rejected, "
        "rate-limited, or unavailable, retry GET with Range bytes=0-0. "
        "HTTP 202 responses are recorded as content not retrieved. "
        "Reachability does not establish that page content supports the claim."
    ),
    "status": observations,
}
(ROOT / "research/source-accessibility.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(
    f"Checked {len(sources)} URLs; "
    f"{len(sources)-len(reviews)-len(limited)} returned a page response, "
    f"{len(limited)} returned HTTP 202 without page content, "
    f"{len(reviews)} need human review."
)
import sys
sys.path.insert(0, str(ROOT / "scripts"))
from build_reports import build_manifest
build_manifest()
print("Updated research/manifest.json.")
