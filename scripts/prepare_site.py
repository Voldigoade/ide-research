from pathlib import Path
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TARGET = DOCS / "assets" / "data"
TARGET.mkdir(parents=True, exist_ok=True)
for name in ("criteria.json", "environments.json", "scenarios.json"):
    shutil.copyfile(ROOT / "data" / name, TARGET / name)
