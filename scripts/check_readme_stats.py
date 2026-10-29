#!/usr/bin/env python3
"""Root-README statistics gate (CR-VS-14).

Validates that every derived number in the landing README matches the
records: stream counts (badges, glance table, intro), the per-industry
table, and the ECF overlay matrix (via the vendored
tools/id-sets/capability-ecf-coordinates.txt map). CI runs this on every
PR (validate-entries.yml) so the README can never drift from the catalog
silently.

Exit codes: 0 pass; 1 mismatch found.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
ENT = REPO / "entities" / "v1-alpha"

DOMS = ["strategy-direction", "party-relationship", "product-value", "finance-accounting",
        "agency-organization", "enablement-operations", "governance-existence"]
STAGES = ["conceive", "design", "build", "activate", "operate", "improve", "retire"]


def load_ecf_map() -> dict[str, str]:
    m = {}
    p = REPO / "tools" / "id-sets" / "capability-ecf-coordinates.txt"
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        cid, coord = line.split()
        m[cid] = coord
    return m


def main() -> int:
    records = []
    for f in sorted(ENT.glob("value-stream-*/value-streams-*.yaml")):
        records.append(yaml.safe_load(f.read_text(encoding="utf-8")))
    readme = (REPO / "README.md").read_text(encoding="utf-8")
    failures = 0

    total = len(records)
    generic = sum(1 for r in records if r.get("applicability", {}).get("specificity") == "generic")
    industry = total - generic
    stage_count = sum(len(r.get("value_stages", [])) for r in records)
    cats = Counter(r.get("value_stream_category") for r in records)
    inds = Counter()
    for r in records:
        for i in r.get("applicability", {}).get("industries", []):
            inds[i] += 1

    def expect(name: str, present: bool, detail: str = ""):
        nonlocal failures
        if not present:
            print(f"  MISMATCH {name}{(': ' + detail) if detail else ''}")
            failures += 1

    # badges + intro counts
    expect("Streams badge", f"Streams-{total}-blue" in readme)
    expect("Industries badge", f"Industries-{len(inds)}-green" in readme)
    expect("intro total", f"{total} admitted streams" in readme)
    expect("intro split", f"{total} admitted streams — {generic} enterprise-generic and {industry} industry-specific" in readme
           or f"{total} admitted streams \u2014 {generic} enterprise-generic and {industry} industry-specific" in readme)

    # glance table
    expect("glance streams", f"| **Streams** | {total} ({generic} cross-industry \u00b7 {industry} industry-specific across {len(inds) - 1} industries) |" in readme)
    expect("glance stages", f"| **Value stages** | {stage_count}," in readme)
    expect("glance categories",
           f"| **Categories** | {cats['operational']} operational \u00b7 {cats['governance']} governance \u00b7 {cats['support']} support \u00b7 {cats['development']} development |" in readme)

    # industry summary table rows
    for dom, cnt in sorted(inds.items()):
        m = re.search(rf"\| {re.escape(dom)} \| (\d+) \|", readme)
        expect(f"industry row {dom}", bool(m) and m.group(1) == str(cnt),
               f"want {cnt}, readme has {m.group(1) if m else 'no row'}")

    # ECF matrix
    ecf = load_ecf_map()
    cell = Counter()
    for r in records:
        for c in r.get("aggregated_capability_refs", []):
            coord = ecf.get(c)
            if coord:
                cell[coord] += 1
    for d in DOMS:
        m = re.search(rf"\*\*{re.escape(d)}\*\*\s*\|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\|", readme)
        expect(f"ECF row {d}", bool(m), "row missing")
        if not m:
            continue
        for s, got in zip(STAGES, m.groups()):
            want = cell.get(f"{d}/{s}", 0)
            raw = got.strip().replace("**", "")
            got_n = 0 if raw in ("·", "—", "-", "") else int(raw)
            expect(f"ECF cell {d}/{s}", got_n == want, f"want {want}, readme has {got_n}")

    if failures:
        print(f"readme-stats: FAILED ({failures} mismatch(es)); update README.md derived numbers")
        return 1
    print(f"readme-stats: OK ({total} streams, {stage_count} stages, {len(inds)} industries, ECF matrix current)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
