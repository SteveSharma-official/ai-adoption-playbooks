#!/usr/bin/env python3
"""Series-wide check.

  python scripts/check_series.py              structure, registry, lab.json contract, naming, writing rules
  python scripts/check_series.py --run-tests  also runs each active book's lab proof sequence
"""
import argparse, json, re, subprocess, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
FOLDER = re.compile(r"^(chapter-\d{2}/lab-\d{2}-[a-z0-9-]+|capstone/[a-z0-9-]+)$")
REQUIRED = {"id", "title", "starter_status", "tenant_steps", "has_solution_after_break"}
TEXT = {".md", ".py", ".yaml", ".yml", ".json", ".jsonl", ".csv", ".txt", ".kql", ".template"}
problems = []


def bad(msg):
    problems.append(msg)
    print("  FAIL", msg)


def check_book(b):
    path = ROOT / b["submodule_path"]
    print(f"Book {b['number']}: {b['title']} ({path.relative_to(ROOT)})")
    if not (path / "README.md").exists():
        bad(f"Book {b['number']}: submodule not initialised. Run git submodule update --init --recursive")
        return
    ids = {}
    for lj in sorted(path.glob("**/lab.json")):
        if "workspace" in lj.parts:
            continue
        rel = lj.parent.relative_to(path).as_posix()
        meta = json.loads(lj.read_text())
        if set(meta) != REQUIRED:
            bad(f"{rel}/lab.json keys {sorted(meta)} do not match the schema")
        if meta.get("starter_status") not in ("PASS", "FAIL"):
            bad(f"{rel}: starter_status must be PASS or FAIL")
        if not FOLDER.match(rel):
            bad(f"{rel}: folder does not follow chapter-NN/lab-NN-slug")
        if meta["id"] in ids:
            bad(f"Duplicate lab id {meta['id']} in {rel} and {ids[meta['id']]}")
        ids[meta["id"]] = rel
        m = re.match(r"chapter-(\d{2})/lab-(\d{2})", rel)
        if m and meta["id"] != f"{int(m[1])}.{int(m[2])}":
            bad(f"{rel}: id {meta['id']} does not match its folder")
        for sub in ("starter", "solution", "lab-changes"):
            if not (lj.parent / sub).is_dir():
                bad(f"{rel}: missing {sub}/")
        if not (lj.parent / "starter" / "run.py").exists():
            bad(f"{rel}: missing starter/run.py")
    print(f"  {len(ids)} labs")
    return path


def writing_rules(base):
    for p in base.rglob("*"):
        if p.is_file() and p.suffix in TEXT and ".git" not in p.parts:
            if "\u2014" in p.read_text(encoding="utf-8", errors="ignore"):
                bad(f"em dash in {p.relative_to(ROOT)}")


def empty_dirs(base):
    for p in base.rglob("*"):
        if p.is_dir() and ".git" not in p.parts and not any(p.iterdir()):
            bad(f"empty folder {p.relative_to(ROOT)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-tests", action="store_true")
    a = ap.parse_args()
    reg = yaml.safe_load((ROOT / "series" / "books.yaml").read_text())["books"]
    active = [b for b in reg if b["status"] in ("labs-active", "published")]
    for b in reg:
        sp = b.get("submodule_path")
        if b["status"] in ("planned", "methodology") and sp and (ROOT / sp).exists():
            bad(f"Book {b['number']} is {b['status']} but {sp} exists")
    books = [p for b in active if (p := check_book(b))]
    writing_rules(ROOT)
    empty_dirs(ROOT)
    if a.run_tests:
        for p in books:
            print(f"Running lab tests in {p.relative_to(ROOT)}")
            r = subprocess.run([sys.executable, "-m", "pytest", "-q"], cwd=p)
            if r.returncode:
                bad(f"lab tests failed in {p.relative_to(ROOT)}")
    print("Series check:", "PASS" if not problems else f"FAIL ({len(problems)} problems)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
