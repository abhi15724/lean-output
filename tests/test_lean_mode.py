import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "hooks" / "lean_mode.py"


class LeanModeTests(unittest.TestCase):
    def run_hook(self, prompt, env):
        result = subprocess.run(
            ["python3", str(SCRIPT)],
            input=json.dumps({"prompt": prompt}),
            text=True,
            capture_output=True,
            env=env,
            check=True,
        )
        return result.stdout.strip()

    def test_default_mode_is_standard(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = os.environ.copy()
            env["LEAN_CONFIG_DIR"] = tmp
            output = self.run_hook("hello", env)
            self.assertIn("active mode: standard", output)

    def test_mode_persists(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = os.environ.copy()
            env["LEAN_CONFIG_DIR"] = tmp
            self.run_hook("/lean ultra", env)
            output = self.run_hook("continue", env)
            self.assertIn("active mode: ultra", output)

    def test_fast_build_persists(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = os.environ.copy()
            env["LEAN_CONFIG_DIR"] = tmp
            self.run_hook("/lean-fast-build make an app", env)
            output = self.run_hook("continue", env)
            self.assertIn("active mode: fast-build", output)

    def test_off_is_silent(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = os.environ.copy()
            env["LEAN_CONFIG_DIR"] = tmp
            self.run_hook("/lean off", env)
            self.assertEqual(self.run_hook("hello", env), "")


if __name__ == "__main__":
    unittest.main()
