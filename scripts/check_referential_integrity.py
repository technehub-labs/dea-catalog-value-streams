#!/usr/bin/env python3
"""Referential-integrity checker for dea-catalog-value-streams (CR-VS-07).

Validates every cross-catalog reference in every catalog entry:

  capabilities:<id>   -> must resolve in dea-catalog-business-capabilities
                        (entities/v1-alpha/**.yaml `id:` fields)
  processes:<id>      -> must resolve in dea-catalog-business-processes
                        (entities/v1-alpha/**.yaml `id:` fields)
  metrics:<id>        -> must resolve in dea-catalog-metrics (when present)
  actors:<id>         -> must resolve in dea-catalog-actors (when present)
  upstream_refs/downstream_refs slugs -> must resolve to a sibling entry
                        slug in this catalog

Sibling catalogs are looked up, in order, at:
  1. --sibling-root/<repo> (local clones, one directory per repo)
  2. env VIB_<REPO_VAR uppercase> path (CI checkout paths)
  3. ../<repo> relative to this catalog (monorepo-style checkouts)

The capability id set is built from CATALOG.yaml of the sibling when a
clone is unavailable (index-driven mode), falling back to a vendored
id-set snapshot under tools/id-sets/ so the gate still runs fully
offline (last refreshed date recorded in the snapshot header).

Exit codes:
  0 success
  1 unresolved references found
  2 sibling catalog unavailable (missing for a namespace in use)
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent

SIBLINGS = {
    "capabilities": "dea-catalog-business-capabilities",
    "processes": "dea-catalog-business-processes",
    "metrics": "dea-catalog-metrics",
    "actors": "dea-catalog-actors",
}

ID_SET_SNAPSHOTS = {
    "capabilities": REPO / "tools" / "id-sets" / "business-capabilities-ids.txt",
    "processes": REPO / "tools" / "id-sets" / "business-processes-ids.txt",
}

NS_OF_INTEREST = ("capabilities", "processes", "metrics", "actors")


def find_sibling(namespace: str) -> Path | None:
    """Locate a sibling catalog checkout by convention."""
    repo = SIBLINGS[namespace]
    candidates = []
    env = os.environ.get("VIB_SIBLING_" + repo.replace("-", "_").upper())
    if env:
        candidates.append(Path(env))
    candidates.append(REPO.parent / repo)
    for cand in candidates:
        if cand.is_dir():
            return cand
    return None


def collect_ids_from_clone(clone: Path) -> set[str]:
    """All `id:` values in YAML files under entities/ of a sibling clone."""
    ids: set[str] = set()
    entities = clone / "entities"
    if not entities.is_dir():
        return ids
    for f in entities.rglob("*.yaml"):
        try:
            data = yaml.safe_load(f.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError):
            continue
        if isinstance(data, dict) and isinstance(data.get("id"), str):
            ids.add(data["id"])
    return ids


def collect_ids_from_catalog_index(clone: Path) -> set[str]:
    """Entity ids from a sibling CATALOG.yaml (index-driven fallback)."""
    index = clone / "CATALOG.yaml"
    if not index.is_file():
        return set()
    try:
        data = yaml.safe_load(index.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return set()
    if not isinstance(data, dict):
        return set()
    catalog = data.get("catalog", data)
    entities = catalog.get("entities", []) if isinstance(catalog, dict) else []
    return {e.get("id") for e in entities if isinstance(e.get("id"), str)}


def load_id_set(namespace: str, errors: list[str]) -> set[str] | None:
    """Resolve the id universe for a namespace; None = unavailable."""
    clone = find_sibling(namespace)
    if clone is not None:
        ids = collect_ids_from_clone(clone) or collect_ids_from_catalog_index(clone)
        if ids:
            return ids
    snapshot = ID_SET_SNAPSHOTS.get(namespace)
    if snapshot is not None and snapshot.is_file():
        return {
            line.strip().lstrip("id: ")
            for line in snapshot.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.startswith("#")
        }
    return None


def entry_files() -> list[Path]:
    root = REPO / "entities" / "v1-alpha"
    if not root.is_dir():
        return []
    return sorted(
        f
        for f in root.rglob("*.yaml")
        if "research" not in f.parts and "candidates" not in f.parts and "retired" not in f.parts
    )


def refs_in(record: dict) -> list[tuple[str, str]]:
    """Extract (json-pointer-ish location, reference) pairs from a record."""
    out: list[tuple[str, str]] = []

    def walk(node, path):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in ("capability_refs", "process_refs", "actor_refs", "metric_ref") or k in (
                    "customer_ref",
                    "source_id",
                    "target_id",
                ):
                    if isinstance(v, str):
                        out.append((f"{path}/{k}", v))
                    elif isinstance(v, list):
                        for i, item in enumerate(v):
                            if isinstance(item, str):
                                out.append((f"{path}/{k}/{i}", item))
                walk(v, f"{path}/{k}")
        elif isinstance(node, list):
            for i, item in enumerate(node):
                walk(item, f"{path}/{i}")

    walk(record, "")
    return out


SLUG_RE = re.compile(r"^value-stream-[a-z0-9-]+$")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--sibling-root", type=Path, default=None, help="Directory containing sibling catalog clones")
    args = parser.parse_args()
    if args.sibling_root:
        os.environ["VIB_SIBLING_ROOT"] = str(args.sibling_root)

    if args.sibling_root:
        for ns, repo in SIBLINGS.items():
            cand = args.sibling_root / repo
            if cand.is_dir():
                os.environ["VIB_SIBLING_" + repo.replace("-", "_").upper()] = str(cand)

    files = entry_files()
    if not files:
        print("referential-integrity: no catalog entries; nothing to check")
        return 0

    # Determine which namespaces are actually in use before requiring siblings.
    used: dict[str, set[str]] = {ns: set() for ns in NS_OF_INTEREST}
    records: dict[Path, dict] = {}
    for f in files:
        try:
            data = yaml.safe_load(f.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as exc:
            print(f"  \u2717 {f}: cannot parse ({exc})")
            return 1
        if not isinstance(data, dict):
            continue
        records[f] = data
        for _, ref in refs_in(data):
            ns = ref.split(":", 1)[0]
            if ns in used:
                used[ns].add(ref)

    universes: dict[str, set[str] | None] = {}
    unavailable: list[str] = []
    for ns in NS_OF_INTEREST:
        if not used[ns]:
            universes[ns] = None
            continue
        ids = load_id_set(ns, unavailable)
        if ids is None:
            unavailable.append(ns)
        universes[ns] = ids

    if unavailable:
        for ns in sorted(set(unavailable)):
            print(
                f"  \u2717 sibling catalog for namespace '{ns}:' not locatable "
                f"({SIBLINGS[ns]} clone, CATALOG.yaml index, and vendored snapshot all absent)"
            )
        return 2

    failures = 0
    local_slugs = {
        str(data.get("id", "")).split("value-streams:", 1)[-1].rsplit("-", 1)[0]
        if isinstance(data.get("id"), str) and data["id"].count("-") >= 1
        else None
        for data in records.values()
    }
    local_slugs = {s for s in local_slugs if s}

    for f, data in records.items():
        for loc, ref in refs_in(data):
            ns = ref.split(":", 1)[0]
            if ns in universes and universes[ns] is not None and ref not in universes[ns]:
                print(f"  \u2717 {f}: unresolved {ns} reference at {loc}: {ref}")
                failures += 1
        for key in ("upstream_refs", "downstream_refs"):
            for i, link in enumerate(data.get(key) or []):
                slug = link.get("slug") if isinstance(link, dict) else None
                if not slug or not SLUG_RE.match(slug):
                    print(f"  \u2717 {f}: {key}/{i}: malformed slug {slug!r}")
                    failures += 1
                elif slug not in local_slugs:
                    print(f"  \u2717 {f}: {key}/{i}: unknown sibling value-stream slug {slug!r}")
                    failures += 1
        for i, m in enumerate(data.get("metrics") or []):
            stage = m.get("applies_to_stage") if isinstance(m, dict) else None
            if stage:
                stage_names = {s.get("name") for s in data.get("value_stages") or [] if isinstance(s, dict)}
                if stage not in stage_names:
                    print(f"  \u2717 {f}: metrics/{i}: applies_to_stage {stage!r} matches no value stage")
                    failures += 1

    print(f"referential-integrity: {'FAILED' if failures else 'passed'} ({len(files)} entries checked)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
