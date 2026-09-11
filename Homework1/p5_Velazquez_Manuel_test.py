import unittest

from p5_Velazquez_Manuel import (
    caesar_cipher,
    caesar_decipher,
    letter_frequency
)


class TestCaesarCipher(unittest.TestCase):

    def test_cipher(self):
        self.assertEqual(caesar_cipher("abc", 3), "def")

    def test_uppercase(self):
        self.assertEqual(caesar_cipher("ABC", 3), "DEF")

    def test_wraparound(self):
        self.assertEqual(caesar_cipher("xyz", 3), "abc")

    def test_spaces(self):
        self.assertEqual(
            caesar_cipher("hello world", 1),
            "ifmmp xpsme"
        )

    def test_decipher(self):
        self.assertEqual(
            caesar_decipher("def", 3),
            "abc"
        )

    def test_frequency(self):
        result = letter_frequency("Hello")

        self.assertEqual(result["h"], 1)
        self.assertEqual(result["e"], 1)
        self.assertEqual(result["l"], 2)
        self.assertEqual(result["o"], 1)


if __name__ == "__main__":
    unittest.main()