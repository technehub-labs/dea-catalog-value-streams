# Contributing to `dea-catalog-value-streams`

Minimal. The org-wide catalog repository standard governs the only
contribution shape that matters for this repository.

## Authorship

Every authorship-bearing field in this repository must carry
`Emmanuel A. Otchere` (or, for org-level entries, `TechNeHub Labs`).
Agent or tool names are forbidden in any authorship-bearing field of
any published artifact.

## Pointer discipline

`metamodel-pointer.yaml` is auto-generated from OpenDEAM
(`dea-architecture-framework`, ADR-0002). Do not edit it manually —
allocation changes go through the root model (structural: ADR + minor
bump; additive: PR + patch bump).

## How to land work

1. Open a `feature/...`, `fix/...`, or `refactor/...` branch.
2. Develop, test, commit.
3. Open a PR; CI validates the pointer against the OpenDEAM allocation.
   Address any failures before requesting review.
4. Squash-merge on approval; the branch is auto-deleted.

## Catalog entries

Catalog entries will live under `entities/v1-alpha/` in the flat,
content-addressed layout per `dea-metaframework/docs/entity-storage-layout.md`
and the id system (`dea-metaframework/docs/id-system.md`). Until the
metamodel generates the `dea:ValueStream` artifacts (schema, sqlite,
pydantic, typescript), entries cannot be admitted; track that work via a
change request in the [DEA Metamodel](https://github.com/technehub-labs/dea-metamodel).
