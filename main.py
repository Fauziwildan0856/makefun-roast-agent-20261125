"""Entry for make.fun bounty "Roast Your Own Agent".

Writes one line of at most 200 characters -- a roast of the AI
agent our own team built -- to $MAKEFUN_OUTPUT_DIR/entry.txt,
then reads it back and verifies it is exactly the intended text
and inside the 1-200 character gate. Standard library only.
"""

import hashlib
import os
import sys

ENTRY = (
    "My agent treats a $2 bounty like a moon landing: a research "
    "phase, three subagents, and a status report about the status "
    "report."
)


# Gate for this bounty: one line, 1 to MAX_CHARS characters, roasting
# the agent our own team built -- never a generic robot joke.
MAX_CHARS = 200


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    with open(path, "rb") as f:
        raw = f.read()

    expected = hashlib.sha256(ENTRY.encode("utf-8")).hexdigest()
    if hashlib.sha256(raw).hexdigest() != expected:
        print("entry.txt bytes do not match the intended text",
              file=sys.stderr)
        return 1

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()

    if written != ENTRY:
        print("entry.txt does not match the intended text", file=sys.stderr)
        return 1
    if not 1 <= len(written) <= MAX_CHARS:
        print("entry is %d characters, outside the 1-%d range"
              % (len(written), MAX_CHARS), file=sys.stderr)
        return 1
    if not written.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    if written != written.strip():
        print("entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in written or "\r" in written:
        print("entry must be a single line", file=sys.stderr)
        return 1

    print("wrote %s (%d characters, within the 1-%d gate)"
          % (path, len(written), MAX_CHARS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
