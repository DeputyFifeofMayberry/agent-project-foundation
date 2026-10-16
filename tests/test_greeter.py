import unittest
from greeter import greet


class GreetUnitTests(unittest.TestCase):
    def test_basic_greeting(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_custom_punctuation(self):
        self.assertEqual(greet("Ada", "?"), "Hello, Ada?")

    def test_empty_name_raises(self):
        with self.assertRaises(ValueError):
            greet("   ")

    def test_name_is_trimmed(self):
        self.assertEqual(greet("  Bo "), "Hello, Bo!")


if __name__ == "__main__":
    unittest.main()
