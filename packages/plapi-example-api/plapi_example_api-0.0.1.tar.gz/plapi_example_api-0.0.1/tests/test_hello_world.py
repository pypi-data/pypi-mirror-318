import unittest
from plapi_example import hello
from io import StringIO
import sys

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        hello()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()