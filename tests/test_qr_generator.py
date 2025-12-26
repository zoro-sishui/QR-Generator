import unittest
import os
import shutil
from src.qr_generator.validator import validate_data
from src.qr_generator.utilis import prepare_outputpath
from src.qr_generator.generator import generate_qr

class TestQRGenerator(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_output"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        # Clean up any files created in current directory if any tests leak
        if os.path.exists("test_qr.png"):
            os.remove("test_qr.png")

    def test_validator_valid(self):
        """Test validator with valid data."""
        is_valid, error = validate_data("https://example.com")
        self.assertTrue(is_valid)
        self.assertEqual(error, "")

    def test_validator_empty(self):
        """Test validator with empty string."""
        is_valid, error = validate_data("")
        self.assertFalse(is_valid)
        self.assertIn("cannot e empty", error) # Note: Typo in original code "cannot e empty"

    def test_validator_whitespace(self):
        """Test validator with whitespace only."""
        is_valid, error = validate_data("   ")
        self.assertFalse(is_valid)
        self.assertIn("cannot e empty", error)

    def test_validator_too_long(self):
        """Test validator with data exceeding limit."""
        long_data = "a" * 3000
        is_valid, error = validate_data(long_data)
        self.assertFalse(is_valid)
        self.assertIn("exceeds the QR code size limit", error)

    def test_utils_prepare_outputpath(self):
        """Test output path preparation and sanitization."""
        # Test basic filename
        path = prepare_outputpath("test")
        self.assertTrue(path.endswith("test.png"))
        
        # Test with extension
        path = prepare_outputpath("test.png")
        self.assertTrue(path.endswith("test.png"))
        
        # Test sanitization (uppercase to lowercase, spaces to underscores)
        path = prepare_outputpath("Test File")
        filename = os.path.basename(path)
        self.assertEqual(filename, "test_file.png")

    def test_generator_success(self):
        """Test successful QR code generation."""
        output_file = os.path.join(self.test_dir, "test_qr.png")
        result = generate_qr("https://example.com", output_file)
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(output_file))
        self.assertGreater(os.path.getsize(output_file), 0)

    def test_generator_invalid_path(self):
        """Test generator with invalid path."""
        # Trying to save to a directory that doesn't exist (nested)
        output_file = os.path.join(self.test_dir, "non_existent_dir", "test.png")
        result = generate_qr("data", output_file)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
