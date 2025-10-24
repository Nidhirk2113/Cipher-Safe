"""
Test Suite: Steganography (LSB)
Validates text encoding and decoding within images.
"""

import unittest
import os
from steganography.lsb_stego import LSBSteganography
from PIL import Image

class TestLSBSteganography(unittest.TestCase):

    def setUp(self):
        """Prepare base test image and steganography instance."""
        self.stego = LSBSteganography()
        self.input_path = "assets/images/test_input.png"
        self.output_path = "assets/stego_output/test_output.png"
        os.makedirs("assets/images/", exist_ok=True)
        os.makedirs("assets/stego_output/", exist_ok=True)

        # Create small sample image
        Image.new("RGB", (100, 100), color="white").save(self.input_path, "PNG")

    def test_capacity_estimation(self):
        """Ensure calculated capacity > 0."""
        capacity = self.stego.estimate_capacity(self.input_path)
        self.assertGreater(capacity, 0)

    def test_encode_and_decode_text(self):
        secret = "SECRET MISSION CODE"
        result = self.stego.encode(self.input_path, self.output_path, secret)
        self.assertIn("Message successfully encoded", result)
        decoded = self.stego.decode(self.output_path)
        self.assertEqual(decoded, secret)

    def test_message_too_large(self):
        """Raise ValueError when message exceeds image capacity."""
        large_text = "X" * 999999
        with self.assertRaises(ValueError):
            self.stego.encode(self.input_path, self.output_path, large_text)

    def tearDown(self):
        """Remove temp files."""
        import shutil
        shutil.rmtree("assets/", ignore_errors=True)

if __name__ == "__main__":
    unittest.main(verbosity=2)
