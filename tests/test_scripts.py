import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "skills/lean-output/scripts/token_audit.py"


class ScriptTests(unittest.TestCase):
    def test_token_audit_runs(self):
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md") as f:
            f.write("hello world\n")
            f.flush()
            result = subprocess.run(["python3", str(AUDIT), f.name], capture_output=True, text=True, check=True)
            self.assertIn("approx_tokens:", result.stdout)
            self.assertIn("heuristic estimate", result.stdout)


if __name__ == "__main__":
    unittest.main()
