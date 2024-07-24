# tests/test_greeter.py

import unittest
from hello_world.greeter import get_greeting

class TestGreeter(unittest.TestCase):
    def test_get_greeting(self):
        self.assertEqual(get_greeting(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
