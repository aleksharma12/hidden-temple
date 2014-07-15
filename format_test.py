import format
import unittest

class TestFormatFunctions(unittest.TestCase):

    def test_to_txt(self):
        text = format.to_txt('zorro')
        self.assertEqual(text, 'zorro.txt')

if __name__ == '__main__':
    unittest.main()
