"""Rename the Planet entry.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13 stdlib only, deterministic: no randomness, network, or clock.
"""

import os


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Winner-pattern: insider-specific concrete truth (Saturn's rings),
    # twist lands in the last words ("can't travel light"), no generic cliche.
    line = (
        "Saturn is now 'Baggage Claim,' because it drags 100,000 "
        "glittering rings around everywhere and still can't travel light."
    )
    # Exactly one line, no trailing newline: the gate counts characters.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
