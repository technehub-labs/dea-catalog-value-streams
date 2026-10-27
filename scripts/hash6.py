#!/usr/bin/env python3
"""hash6: content-derived id suffix per the org-wide id system (dea-metaframework
docs/id-system.md section 2.5): first 4 bytes of the record file's SHA-256,
big-endian, rendered as 6 base-31 digits over the visually-unambiguous alphabet
abcdefghjkmnpqrstuvwxyz23456789. Matches the reference implementation in
dea-catalog-business-capabilities/scripts/migrate_to_new_ids.py."""
import hashlib
import sys

ALPHABET = "abcdefghjkmnpqrstuvwxyz23456789"


def hash6(text: str) -> str:
    h = hashlib.sha256(text.encode("utf-8")).digest()
    val = int.from_bytes(h[:4], "big")
    chars = []
    for _ in range(6):
        chars.append(ALPHABET[val % 31])
        val //= 31
    return "".join(reversed(chars))


if __name__ == "__main__":
    for path in sys.argv[1:]:
        with open(path) as fh:
            print(f"{hash6(fh.read())}  {path}")
