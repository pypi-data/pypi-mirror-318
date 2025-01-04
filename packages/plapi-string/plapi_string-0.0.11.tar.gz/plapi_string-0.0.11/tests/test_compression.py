import unittest
from plapi.string.compression import compress_string

class TestStringCompression(unittest.TestCase):
    def test_compress_string(self):
        self.assertEqual(compress_string("aaabbcc"), "a3b2c2")
        self.assertEqual(compress_string("a"), "a1")
        self.assertEqual(compress_string(""), "")
        self.assertEqual(compress_string("abc"), "a1b1c1")
        self.assertEqual(compress_string("aabcccccaaa"), "a2b1c5a3")

if __name__ == '__main__':
    unittest.main()