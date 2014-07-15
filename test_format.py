import format
import unittest

class TestFormatFunctions(unittest.TestCase):

    def test_to_txt(self):
        text = format.to_txt('zorro')
        self.assertEqual(text, 'zorro.txt')

    def test_capitalize(self):
        capitalized = format.capitalize('zorro')
        self.assertEqual(capitalized, 'Zorro')

if __name__ == '__main__':
    unittest.main()
