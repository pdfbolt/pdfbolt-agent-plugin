#!/usr/bin/env python3
"""Package the current plugin source without including old releases or local files."""
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def main():
    root = Path(__file__).resolve().parents[1]
    manifests = [root / name / "plugin.json" for name in (".claude-plugin", ".codex-plugin")]
    metadata = [json.loads(path.read_text(encoding="utf-8")) for path in manifests]
    if len({(item["name"], item["version"]) for item in metadata}) != 1:
        raise SystemExit("Claude and OpenAI plugin names and versions must match")
    name, version = metadata[0]["name"], metadata[0]["version"]
    files = manifests + [root / path for path in (".mcp.json", "README.md", "LICENSE")]
    for directory in ("skills", "assets"):
        files.extend(path for path in (root / directory).rglob("*") if path.is_file())
    for path in files:
        if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(root):
            raise SystemExit(f"Invalid package source: {path}")
    output = root / f"{name}-{version}.zip"
    temporary = output.with_suffix(".zip.tmp")
    try:
        with ZipFile(temporary, "w", ZIP_DEFLATED) as archive:
            for path in sorted(files):
                archive.write(path, Path(name) / path.relative_to(root))
        with ZipFile(temporary) as archive:
            if archive.testzip() is not None:
                raise SystemExit("Package integrity check failed")
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)
    print(f"Created {output} ({len(files)} files)")


if __name__ == "__main__":
    main()
