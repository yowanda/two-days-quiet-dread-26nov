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
    # Runtime validation: the file must exist, hold 1-140 UTF-8
    # characters, and match the expected bytes exactly.
    with open(path, "rb") as handle:
        data = handle.read()
    text = data.decode("utf-8")
    if not 1 <= len(text) <= 140 or text.strip() == "":
        raise SystemExit("entry.txt failed validation: length out of range")
    if data != COMMENT.encode("utf-8"):
        raise SystemExit("entry.txt failed validation: bytes differ from expected")


if __name__ == "__main__":
    main()
