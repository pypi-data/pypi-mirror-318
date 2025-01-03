import unittest
from python_example_sdk import add

class TestExample(unittest.TestCase):
    def test_sample(self):
        self.assertTrue(True)

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()