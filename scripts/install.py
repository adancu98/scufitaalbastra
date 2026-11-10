#!/usr/bin/env python3
"""Install both sibling skills without configuring accounts or MCP servers."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import shutil
import tempfile
import uuid

SKILLS = ("scufita-albastra", "photoshop-mcp-techniques")
REPOSITORY = Path(__file__).resolve().parents[1]


def exists(path: Path) -> bool:
    return path.exists() or path.is_symlink()


def install(skills_dir: Path, *, replace: bool = False, dry_run: bool = False,
            repository: Path = REPOSITORY) -> dict:
    repository = repository.resolve()
    skills_dir = skills_dir.expanduser().absolute()
    sources = {name: repository / name for name in SKILLS}
    destinations = {name: skills_dir / name for name in SKILLS}
    for name, source in sources.items():
        if not (source / "SKILL.md").is_file():
            raise ValueError(f"Missing required skill: {name}")
        if source.is_symlink() or any(item.is_symlink() for item in source.rglob("*")):
            raise ValueError(f"Source skill must contain regular files/directories: {name}")
        if destinations[name].resolve() == source.resolve():
            raise ValueError("The installation destination cannot be the source package")
    conflicts = [name for name, path in destinations.items() if exists(path)]
    if conflicts and not replace:
        raise ValueError("Existing skills preserved: " + ", ".join(conflicts) +
                         ". Use --replace to install with backups.")
    plan = {"skills": list(SKILLS), "skills_dir": str(skills_dir),
            "destinations": {name: str(path) for name, path in destinations.items()},
            "existing_skills": conflicts, "dry_run": dry_run, "backups": {}}
    if dry_run:
        return {"ok": True, **plan}

    skills_dir.mkdir(parents=True, exist_ok=True)
    # Backups sit outside the scanned skill directory to avoid duplicate skill discovery.
    backup_root = skills_dir.parent / (skills_dir.name + "-backups")
    installed: list[str] = []
    backups: dict[str, Path] = {}
    with tempfile.TemporaryDirectory(prefix=".scufita-install-", dir=skills_dir) as staging:
        staging = Path(staging)
        for name, source in sources.items():
            shutil.copytree(source, staging / name,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"))
        # Recheck after copying so a concurrently created destination is not overwritten.
        if not replace and any(exists(path) for path in destinations.values()):
            raise ValueError("A destination appeared during preparation; existing files preserved")
        try:
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            for name, destination in destinations.items():
                if exists(destination):
                    backup_root.mkdir(parents=True, exist_ok=True)
                    backup = backup_root / f"{name}.backup-{stamp}-{uuid.uuid4().hex[:8]}"
                    destination.rename(backup)
                    backups[name] = backup
                (staging / name).rename(destination)
                installed.append(name)
        except Exception:
            # Only remove the new directories this transaction installed.
            for name in reversed(installed):
                shutil.rmtree(destinations[name])
            for name, backup in backups.items():
                if not exists(destinations[name]):
                    backup.rename(destinations[name])
            raise
    plan["backups"] = {name: str(path) for name, path in backups.items()}
    return {"ok": True, **plan}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-dir", type=Path, default=Path.home() / ".codex" / "skills",
                        help="Destination skill directory (default: ~/.codex/skills)")
    parser.add_argument("--replace", action="store_true",
                        help="Replace existing skills after preserving timestamped backups")
    parser.add_argument("--dry-run", action="store_true", help="Show the plan without writing files")
    args = parser.parse_args()
    try:
        result = install(args.skills_dir, replace=args.replace, dry_run=args.dry_run)
    except (OSError, ValueError) as error:
        print(json.dumps({"ok": False, "error": str(error)}, ensure_ascii=False))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
