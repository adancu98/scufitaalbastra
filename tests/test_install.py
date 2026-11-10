"""Installer tests use synthetic skills and temporary destinations only."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "install.py"
spec = importlib.util.spec_from_file_location("scufita_install", MODULE_PATH)
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repository = self.root / "package"
        for name in installer.SKILLS:
            (self.repository / name).mkdir(parents=True)
            (self.repository / name / "SKILL.md").write_text("# Synthetic skill\n")
        (self.repository / "scufita-albastra" / "sibling-link.txt").write_text("../photoshop-mcp-techniques/SKILL.md")
        self.destination = self.root / "destination"

    def run_install(self, **kwargs):
        return installer.install(self.destination, repository=self.repository, **kwargs)

    def test_dry_run_creates_nothing(self):
        result = self.run_install(dry_run=True)
        self.assertTrue(result["ok"])
        self.assertFalse(self.destination.exists())

    def test_installs_both_siblings_and_relative_link(self):
        result = self.run_install()
        self.assertEqual(result["skills"], list(installer.SKILLS))
        text = (self.destination / "scufita-albastra" / "sibling-link.txt").read_text()
        self.assertTrue((self.destination / "scufita-albastra" / text).is_file())

    def test_existing_skill_refuses_before_partial_installation(self):
        old = self.destination / "scufita-albastra"
        old.mkdir(parents=True)
        (old / "old.txt").write_text("preserve")
        with self.assertRaises(ValueError):
            self.run_install()
        self.assertEqual((old / "old.txt").read_text(), "preserve")
        self.assertFalse((self.destination / "photoshop-mcp-techniques").exists())

    def test_replace_keeps_original_backup(self):
        self.run_install()
        (self.destination / "scufita-albastra" / "old.txt").write_text("preserve")
        result = self.run_install(replace=True)
        self.assertEqual(len(result["backups"]), 2)
        self.assertTrue(all(Path(path).parent != self.destination for path in result["backups"].values()))
        self.assertEqual((Path(result["backups"]["scufita-albastra"]) / "old.txt").read_text(), "preserve")
        self.assertFalse((self.destination / "scufita-albastra" / "old.txt").exists())

    def test_missing_source_does_not_create_destination(self):
        (self.repository / "photoshop-mcp-techniques" / "SKILL.md").unlink()
        with self.assertRaises(ValueError):
            self.run_install()
        self.assertFalse(self.destination.exists())

    def test_source_destination_collision_is_rejected(self):
        with self.assertRaises(ValueError):
            installer.install(self.repository, repository=self.repository, replace=True)

    def test_rollback_restores_both_old_skills(self):
        self.run_install()
        for name in installer.SKILLS:
            (self.destination / name / "old.txt").write_text(name)
        original_rename = Path.rename

        def fail_second_commit(path, target):
            if path.name == "photoshop-mcp-techniques" and path.parent.name.startswith(".scufita-install-"):
                raise OSError("Synthetic second-install failure")
            return original_rename(path, target)

        with patch.object(Path, "rename", fail_second_commit), self.assertRaises(OSError):
            self.run_install(replace=True)
        for name in installer.SKILLS:
            self.assertEqual((self.destination / name / "old.txt").read_text(), name)
        self.assertEqual(list(self.destination.parent.glob("destination-backups/*.backup-*")), [])


if __name__ == "__main__":
    unittest.main()
