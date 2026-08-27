#!/usr/bin/env python3
"""Run MkDocs while keeping the atlas content at the repository root."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "mkdocs.yml"


def main() -> int:
    mkdocs = shutil.which("mkdocs")
    if mkdocs is None:
        print(
            "MkDocs is unavailable. Install it with: "
            "uv tool install mkdocs --with mkdocs-material",
            file=sys.stderr,
        )
        return 1

    arguments = sys.argv[1:] or ["serve"]
    source = CONFIG.read_text(encoding="utf-8")
    marker = "docs_dir: ."
    if source.count(marker) != 1:
        print(f"Expected exactly one {marker!r} entry in {CONFIG}", file=sys.stderr)
        return 1

    source = source.replace(marker, f'docs_dir: "{ROOT}"', 1)

    with tempfile.TemporaryDirectory(prefix="atlas-mkdocs-") as temporary:
        generated_config = Path(temporary) / "mkdocs.yml"
        generated_config.write_text(source, encoding="utf-8")
        command = [mkdocs, *arguments, "--config-file", str(generated_config)]
        return subprocess.run(command, cwd=ROOT, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
