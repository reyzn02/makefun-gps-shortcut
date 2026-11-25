"""The GPS Swears It Was a Shortcut.

Writes the GPS's one-line excuse to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Stdlib only, no network, deterministic.
"""

import os

LINE = (
    "The map swore this was a shortcut, so I took us through a wedding, "
    "a cul-de-sac, and \u2014 technically \u2014 a lake."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
