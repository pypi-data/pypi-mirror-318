import unittest
from your_package import your_function

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(your_function(), 'Hello, World!')

if __name__ == '__main__':
    unittest.main()