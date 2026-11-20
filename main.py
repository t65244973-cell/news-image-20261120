"""Entry program for make.fun news-image-20261120.

Sums up the world's news of Friday 20 November 2026 in one image.

The image is held in this repository as entry.png (a 1024x1024 PNG
newspaper front page). This program copies it, byte for byte, to
/output/entry.png. It uses only the Python standard library, reads
nothing from the network, and writes exactly the same bytes on every
run, so repeated runs are deterministic.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.png")


def _sha256(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    os.makedirs(DEST_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    # Verify the copy is byte-identical, so a repeated run is
    # provably deterministic: same input bytes, same output bytes.
    if _sha256(SOURCE) != _sha256(DEST):
        print("error: /output/entry.png differs from entry.png", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (DEST, os.path.getsize(DEST)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
