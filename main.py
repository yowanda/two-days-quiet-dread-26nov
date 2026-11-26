#!/usr/bin/env python3
"""Write one code review comment to entry.txt.

The comment approves a pull request while carrying quiet existential
dread. Deterministic, stdlib-only, no network access. It writes exactly
one line (no trailing newline) to $MAKEFUN_OUTPUT_DIR/entry.txt, or
/output/entry.txt when MAKEFUN_OUTPUT_DIR is unset.
"""

import os

COMMENT = (
    "LGTM. This code will outlive us all, which is the nicest thing "
    "I can say about either of us."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(COMMENT)


if __name__ == "__main__":
    main()
