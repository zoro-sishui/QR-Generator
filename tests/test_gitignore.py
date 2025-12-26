import unittest
import subprocess
import os

class TestGitIgnore(unittest.TestCase):
    def test_ignores_virtual_env(self):
        """Test that the virtual environment directory is ignored."""
        result = subprocess.run(
            ["git", "check-ignore", "myenv/"], 
            capture_output=True, 
            text=True
        )
        self.assertEqual(result.returncode, 0, "myenv/ should be ignored")

    def test_ignores_pycache(self):
        """Test that __pycache__ directories are ignored."""
        result = subprocess.run(
            ["git", "check-ignore", "__pycache__/"], 
            capture_output=True, 
            text=True
        )
        self.assertEqual(result.returncode, 0, "__pycache__/ should be ignored")
    
    def test_ignores_generated_images(self):
        """Test that generated PNG files are ignored."""
        result = subprocess.run(
            ["git", "check-ignore", "qr_code.png"], 
            capture_output=True, 
            text=True
        )
        self.assertEqual(result.returncode, 0, "*.png files should be ignored")

    def test_does_not_ignore_source_code(self):
        """Test that source code files are NOT ignored."""
        result = subprocess.run(
            ["git", "check-ignore", "main.py"], 
            capture_output=True, 
            text=True
        )
        # git check-ignore returns 1 if the file is NOT ignored
        self.assertNotEqual(result.returncode, 0, "main.py should NOT be ignored")

if __name__ == "__main__":
    unittest.main()
