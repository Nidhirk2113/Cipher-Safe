"""
CipherSafe Steganography Module (lsb_stego.py)
----------------------------------------------
Implements Least Significant Bit (LSB) steganography for hiding and
extracting encrypted text within PNG images. Suitable for combining 
with Vernam Cipher (OTP) to achieve covert communication.
"""

from PIL import Image
import binascii

class LSBSteganography:
    """
    Handles text-based steganography through LSB modification.
    
    Uses the least significant bits (1 bit per RGB channel) to embed or
    extract messages from lossless images like PNG or BMP.

    Limitations:
    - Avoid lossy formats (e.g. JPEG) — compression destroys data.
    - Image must have enough pixels to store all bits (8 bits per char).
    """

    def __init__(self):
        pass

    # ---------------------
    # Internal Utilities
    # ---------------------

    @staticmethod
    def _text_to_bits(text):
        """Convert string message to binary representation."""
        return ''.join(format(ord(c), '08b') for c in text)

    @staticmethod
    def _bits_to_text(bits):
        """Convert binary string back to plaintext message."""
        chars = [bits[i:i+8] for i in range(0, len(bits), 8)]
        return ''.join(chr(int(b, 2)) for b in chars if len(b) == 8)

    # ---------------------
    # Encoding
    # ---------------------

    def encode(self, input_image_path, output_image_path, secret_text):
        """
        Embed a secret message inside an image using LSB method.

        Args:
            input_image_path (str): Path to base (cover) image.
            output_image_path (str): Path to save stego image.
            secret_text (str): Data to hide (usually Vernam ciphertext).

        Returns:
            str: Confirmation message on success.
        """
        image = Image.open(input_image_path)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        encoded = image.copy()
        width, height = image.size
        binary_data = self._text_to_bits(secret_text + "#####")  # delimiter for stop
        binary_index = 0

        for y in range(height):
            for x in range(width):
                pixel = list(image.getpixel((x, y)))
                for channel in range(3):
                    if binary_index < len(binary_data):
                        pixel[channel] = (pixel[channel] & ~1) | int(binary_data[binary_index])
                        binary_index += 1
                encoded.putpixel((x, y), tuple(pixel))
                if binary_index >= len(binary_data):
                    encoded.save(output_image_path, 'PNG')
                    return f"Message successfully encoded into {output_image_path}"

        raise ValueError("Message too long for selected image capacity.")

    # ---------------------
    # Decoding
    # ---------------------

    def decode(self, stego_image_path):
        """
        Extract hidden message from a stego image.

        Args:
            stego_image_path (str): Path of image containing hidden data.

        Returns:
            str: The decoded plaintext (hidden message).
        """
        image = Image.open(stego_image_path)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        binary_data = ""
        width, height = image.size

        for y in range(height):
            for x in range(width):
                pixel = list(image.getpixel((x, y)))
                for channel in range(3):
                    binary_data += str(pixel[channel] & 1)
                    if binary_data.endswith("0010001100100010001000110010001100100011"):  # binary("#####")
                        text = self._bits_to_text(binary_data)
                        return text.split("#####")[0]
        return "No hidden message found."

    # ---------------------
    # Capacity Check
    # ---------------------

    def estimate_capacity(self, image_path):
        """
        Estimate max number of characters that can be safely hidden in an image.

        Args:
            image_path (str): Path to input image.

        Returns:
            int: Max characters storable without overflow.
        """
        image = Image.open(image_path)
        width, height = image.size
        total_pixels = width * height
        max_bits = total_pixels * 3  # 3 channels, 1 bit per channel
        return max_bits // 8  # 8 bits = 1 char


# ---------------------
# Standalone Demo
# ---------------------
if __name__ == "__main__":
    stego = LSBSteganography()

    print("=== CipherSafe LSB Steganography Demo ===")
    base_image = "assets/images/sample_input.png"
    stego_image = "assets/stego_output/sample_output.png"
    message = "OPERATION BLACK DAWN SUCCESS"

    capacity = stego.estimate_capacity(base_image)
    print(f"Max capacity: {capacity} characters")

    if len(message) > capacity:
        print("Message too large for this image.")
    else:
        print("Encoding message...")
        print(stego.encode(base_image, stego_image, message))
        print("Decoding message...")
        print(stego.decode(stego_image))
