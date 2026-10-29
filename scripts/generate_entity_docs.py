#!/usr/bin/env python3
"""Per-stream documentation generator (CR-VS-13).

Regenerates every entity subtree under entities/v1-alpha/ so each value
stream folder is both human- and machine-readable:

  value-stream-<slug>-<hash6>/
  ├── value-streams-value-stream-<slug>-<hash6>.yaml  (authoritative record)
  ├── README.md                                      (front-mattered, visual)
  └── research/
      ├── evidence.md                                (source-backed notes)
      └── README.md                                  (folder contract)

The README carries YAML front matter (machine-extractable summary: id,
name, category, industries, stages, metrics, links), a GitHub-rendered
at-a-glance table, a mermaid stage-flow diagram, and full section
rendering of every record block. Cross-stream links point at the sibling
folder. All content derives from the record + the catalog-wide evidence
register; nothing is hand-authored per stream.

Usage:
  python3 scripts/generate_entity_docs.py [--check] [--dry-run] [--only <slug>]

`--check` (CI mode): regenerate in memory and exit 1 if any committed
README.md / research/ file differs from what the records+register
produce. This is the docs-freshness gate wired into validate-entries.yml
(CR-VS-14): any record change must regenerate its entity docs in the
same PR.
"""
from __future__ import annotations

import argparse
import glob
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
ENT = REPO / "entities" / "v1-alpha"

CAP_REPO = "https://github.com/technehub-labs/dea-catalog-business-capabilities"
BP_REPO = "https://github.com/technehub-labs/dea-catalog-business-processes"
MET_REPO = "https://github.com/technehub-labs/dea-catalog-metrics"


def load_evidence_register() -> dict[str, dict]:
    reg_path = REPO / "catalog-research" / "evidence-register.yaml"
    if not reg_path.is_file():
        return {}
    data = yaml.safe_load(reg_path.read_text(encoding="utf-8")) or {}
    return {s.get("id"): s for s in data.get("sources", []) if isinstance(s, dict) and s.get("id")}


def load_records() -> list[tuple[Path, dict]]:
    out = []
    for f in sorted(ENT.glob("value-stream-*/value-streams-*.yaml")):
        out.append((f, yaml.safe_load(f.read_text(encoding="utf-8"))))
    return out


def slug_of(rec: dict) -> str:
    return rec["id"].split("value-stream-", 1)[1].rsplit("-", 1)[0]


def folder_of(slug: str) -> str:
    """Resolve the folder name for a cross-stream slug.

    Cross-stream refs store slugs in the `value-stream-<slug>` form; the
    folder is `value-stream-<slug>-<hash6>`. Slugs are prefixes of other
    slugs (e.g. value-stream-trial-... vs value-stream-trial-to-readout-...),
    so the match anchors the slug followed by '-' and exactly 6 hash chars.
    """
    import re
    body = slug[len("value-stream-"):] if slug.startswith("value-stream-") else slug
    pat = re.compile(rf"^value-stream-{re.escape(body)}-[a-z2-9]{{6}}$")
    for p in sorted(ENT.iterdir()):
        if p.is_dir() and pat.match(p.name):
            return p.name
    return f"value-stream-{body}-unknown"


def front_matter(rec: dict) -> str:
    fm = {
        "documentation_generated_from": rec["id"].replace(":", "-") + ".yaml",
        "id": rec["id"],
        "name": rec["name"],
        "type": rec["type"],
        "version": rec["version"],
        "lifecycle_status": rec.get("lifecycle_status", "active"),
        "value_stream_category": rec.get("value_stream_category"),
        "industries": rec.get("applicability", {}).get("industries", []),
        "specificity": rec.get("applicability", {}).get("specificity"),
        "entry_criterion": rec["entry_criterion"],
        "exit_criterion": rec["exit_criterion"],
        "outcome": rec["outcome"],
        "stages": [s["name"] for s in rec.get("value_stages", [])],
        "capabilities": sorted(set(rec.get("aggregated_capability_refs", []))),
        "processes": sorted(set(rec.get("process_refs", []))),
        "metrics": [m["name"] for m in rec.get("metrics", [])],
        "upstream": [u["slug"] for u in rec.get("upstream_refs", [])],
        "downstream": [d["slug"] for d in rec.get("downstream_refs", [])],
        "evidence_sources": rec.get("evidence", {}).get("sources", []),
    }
    return yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=200).strip()


def mermaid_stages(rec: dict) -> str:
    lines = ["flowchart LR"]
    stages = rec.get("value_stages", [])
    for i, s in enumerate(stages, 1):
        safe = s["name"].replace('"', "'")
        lines.append(f'  S{i}["{i}. {safe}"]')
    for i in range(1, len(stages)):
        lines.append(f"  S{i} --> S{i + 1}")
    if len(stages) >= 2:
        lines.append(f"  TRIGGER((\"⏺ Entry\")) --> S1")
        lines.append(f"  S{len(stages)} --> EXIT1(((\"✔ Exit\"))")
    return "\n".join(lines)


def render_stage_table(rec: dict) -> list[str]:
    out = ["| # | Stage | Entry criterion | Exit criterion | Enabling capabilities (count) | Realizing processes (count) | Visible |",
           "|---|---|---|---|---|---|---|"]
    for i, s in enumerate(rec.get("value_stages", []), 1):
        out.append(f"| {i} | **{s['name']}** | {s['entry_criterion']} | {s['exit_criterion']} | {len(s.get('capability_refs', []))} | {len(s.get('process_refs', []))} | {'yes' if s.get('customer_visible') else 'no'} |")
    return out


def render(rec: dict, register: dict) -> str:
    name = rec["name"]
    vid = rec["id"]
    file_name = vid.replace(":", "-") + ".yaml"
    app = rec.get("applicability", {})
    inds = ", ".join(app.get("industries", []))

    L: list[str] = []
    L.append("---")
    L.append(front_matter(rec))
    L.append("---")
    L.append("")
    L.append(f"# {name}")
    L.append("")
    L.append(f"`{vid}` · **{rec.get('value_stream_category', '')}** · {inds} · {app.get('specificity', '')}")
    L.append("")
    L.append(f"> {rec['definition']}")
    L.append("")
    L.append(f"**Outcome:** {rec['outcome']}")
    L.append("")
    L.append("**Machine-readable:** this page is generated from — and must stay in sync with — "
              f"the authoritative record [`{file_name}`](./{file_name}). "
              "The front matter above is YAML-extractable metadata.")
    L.append("")
    L.append("## Stage flow")
    L.append("")
    L.append("```mermaid")
    L.append(mermaid_stages(rec))
    L.append("```")
    L.append("")
    L.append("## Value stages")
    L.append("")
    L.extend(render_stage_table(rec))
    L.append("")
    for i, s in enumerate(rec.get("value_stages", []), 1):
        L.append(f"### {i}. {s['name']}")
        L.append("")
        L.append(f"{s['definition']}")
        L.append("")
        L.append("| Aspect | Value |")
        L.append("|---|---|")
        L.append(f"| Entry criterion | {s['entry_criterion']} |")
        L.append(f"| Exit criterion | {s['exit_criterion']} |")
        L.append(f"| Outcome | {s['outcome']} |")
        if "customer_visible" in s:
            L.append(f"| Customer visible | {s['customer_visible']} |")
        L.append(f"| Enabling capabilities | {' · '.join(f'`{c}`' for c in s.get('capability_refs', []))} |")
        if s.get("process_refs"):
            L.append(f"| Realizing processes | {' · '.join(f'`{p}`' for p in s['process_refs'])} |")
        if s.get("actor_refs"):
            L.append(f"| Participating actors | {' · '.join(f'`{a}`' for a in s['actor_refs'])} |")
        L.append("")
    # scope
    L.append("## Scope boundary")
    L.append("")
    L.append(f"**Entry:** {rec['entry_criterion']}")
    L.append("")
    L.append(f"**Exit:** {rec['exit_criterion']}")
    L.append("")
    sc = rec.get("scope", {})
    if sc:
        L.append("**In scope**")
        L.append("")
        L.extend(f"- {i}" for i in sc.get("includes", []))
        L.append("")
        if sc.get("excludes"):
            L.append("**Out of scope** (owned by the named neighbour)")
            L.append("")
            L.extend(f"- {e}" for e in sc["excludes"])
            L.append("")
    # traceability
    L.append("## Traceability")
    L.append("")
    L.append("**Capabilities** (`aggregated_capability_refs`, resolving in "
             f"[business-capabilities]({CAP_REPO})):")
    L.append("")
    L.extend(f"- `{c}`" for c in rec.get("aggregated_capability_refs", []))
    L.append("")
    if rec.get("process_refs"):
        L.append(f"**Processes** (`process_refs`, resolving in [business-processes]({BP_REPO})):")
        L.append("")
        L.extend(f"- `{p}`" for p in rec["process_refs"])
        L.append("")
    # links
    L.append("## Cross-stream links")
    L.append("")
    ups = rec.get("upstream_refs", [])
    downs = rec.get("downstream_refs", [])
    if ups:
        L.append("**Upstream** (their exit feeds this stream's entry):")
        L.append("")
        for u in ups:
            L.append(f"- [{u['slug'].replace('value-stream-', '').replace('-', ' ')}](../{folder_of(u['slug'])}/README.md) — {u.get('note', '')}")
        L.append("")
    else:
        L.append("**Upstream:** none recorded.")
        L.append("")
    if downs:
        L.append("**Downstream** (this stream's exit feeds their entry):")
        L.append("")
        for d in downs:
            L.append(f"- [{d['slug'].replace('value-stream-', '').replace('-', ' ')}](../{folder_of(d['slug'])}/README.md) — {d.get('note', '')}")
        L.append("")
    else:
        L.append("**Downstream:** none recorded.")
        L.append("")
    # metrics
    L.append("## Measurement")
    L.append("")
    if rec.get("metrics"):
        for m in rec["metrics"]:
            scope = f" (stage: {m['applies_to_stage']})" if m.get("applies_to_stage") else " (stream-level)"
            ref = f" → [`{m['metric_ref']}`]({MET_REPO})" if m.get("metric_ref") else ""
            L.append(f"- **{m['name']}**{scope} — {m['definition']}{ref}")
        L.append("")
    # evidence
    L.append("## Evidence")
    L.append("")
    srcs = rec.get("evidence", {}).get("sources", [])
    if srcs:
        L.append("| Source | Class | Reference |")
        L.append("|---|---|---|")
        for sid in srcs:
            s = register.get(sid, {})
            L.append(f"| {sid} | {s.get('class', '—')} | {s.get('name', '—')} |")
        L.append("")
        L.append(f"**Rationale:** {rec['evidence'].get('rationale', '')}")
        L.append("")
        L.append(f"See [research/evidence.md](./research/evidence.md) for the source-backed notes.")
        L.append("")
    # provenance
    L.append("## Provenance ladder")
    L.append("")
    L.append("| Stage | Date | Actor |")
    L.append("|---|---|---|")
    for p in rec["provenance"]["ladder_passage"]:
        L.append(f"| {p['stage']} | {p['date']} | {p['actor']} |")
    L.append("")
    L.append("---")
    L.append("")
    L.append(f"*Generated by [`scripts/generate_entity_docs.py`](../../../scripts/generate_entity_docs.py) "
              f"(CR-VS-13) from the authoritative record. Do not edit by hand; regenerate.*")
    L.append("")
    return "\n".join(L)


RESEARCH_FOLDER_README = """# research/ — {name}

Per-entity research artifacts ([`{vid}`](../{file_name})).

Per the catalog repository standard (CR-CATALOG-STRUCT-01 §5), research
artifacts that are about a single entity live in that entity's `research/`
subtree. The catalog-wide registers (evidence register, candidate
universe, admission register) stay in
[`catalog-research/`](../../../../catalog-research/README.md).

Contents:

- `evidence.md` — source-backed evidence notes for this stream, expanded
  from the catalog-wide evidence register entries it cites. Generated;
  regenerate with `scripts/generate_entity_docs.py`.
"""


def evidence_md(rec: dict, register: dict) -> str:
    srcs = rec.get("evidence", {}).get("sources", [])
    L = [f"# Evidence notes — {rec['name']}", ""]
    L.append(f"Record: [`{rec['id']}`](../{rec['id'].replace(':', '-') + '.yaml'}) · "
             "Expanded from [`catalog-research/evidence-register.yaml`](../../../../catalog-research/evidence-register.yaml). "
             "Generated file (CR-VS-13); do not edit by hand.")
    L.append("")
    L.append(f"**Admission rationale (from the record):** {rec.get('evidence', {}).get('rationale', '')}")
    L.append("")
    for sid in srcs:
        s = register.get(sid)
        if not s:
            continue
        L.append(f"## {sid} — {s.get('name', '')}")
        L.append("")
        L.append(f"- **Class:** {s.get('class', '—')}")
        L.append(f"- **Reference:** {s.get('reference', '—')}")
        L.append(f"- **Retrieved:** {s.get('retrieved', '—')} ({s.get('retrieval', '')})")
        L.append("")
        for obs in s.get("observations", []):
            L.append(f"**Observation:** {obs.get('observation', '')}")
            L.append("")
            supports = obs.get("supports", [])
            if supports:
                L.append("*Supports:*")
                L.append("")
                L.extend(f"- {x}" for x in supports)
                L.append("")
            imp = obs.get("implication")
            if imp:
                L.append(f"*Implication:* {imp}")
                L.append("")
        note = s.get("evidence_note")
        if note:
            L.append(f"> **Evidence note:** {note}")
            L.append("")
    return "\n".join(L)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--only", help="Regenerate a single slug")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--check", action="store_true",
                    help="Exit 1 if any committed entity doc differs from the generated output (CI freshness gate)")
    args = ap.parse_args(argv)

    register = load_evidence_register()
    records = load_records()
    if args.only:
        records = [(f, r) for f, r in records if slug_of(r) == args.only]
    if not records:
        print("no records found")
        return 1

    drift = 0
    for f, rec in records:
        sub = f.parent
        readme = render(rec, register)
        rdir = sub / "research"
        emd = evidence_md(rec, register)
        rreadme = RESEARCH_FOLDER_README.format(
            name=rec["name"], vid=rec["id"],
            file_name=rec["id"].replace(":", "-") + ".yaml")
        if args.dry_run:
            print(f"[dry-run] {sub.name}: README {len(readme)}B, research/evidence.md {len(emd)}B")
            continue
        if args.check:
            for rel, want in (("README.md", readme),
                              ("research/evidence.md", emd),
                              ("research/README.md", rreadme)):
                have_path = sub / rel
                have = have_path.read_text(encoding="utf-8") if have_path.exists() else None
                if have != want:
                    print(f"  STALE {have_path.relative_to(REPO)}: differs from generated output")
                    drift += 1
            continue
        (sub / "README.md").write_text(readme, encoding="utf-8")
        rdir.mkdir(exist_ok=True)
        (rdir / "evidence.md").write_text(emd, encoding="utf-8")
        (rdir / "README.md").write_text(rreadme, encoding="utf-8")

    if args.check:
        if drift:
            print(f"entity-docs freshness: FAILED ({drift} stale file(s)); "
                  "run `python3 scripts/generate_entity_docs.py` and commit the result")
            return 1
        print(f"entity-docs freshness: OK ({len(records)} record docs current)")
        return 0
    print(f"generated docs for {len(records)} record(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
