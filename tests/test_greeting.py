import unittest

from greeting import greet


class TestGreet(unittest.TestCase):
    def test_greet_returns_hello_plus_name(self):
        self.assertEqual(greet('World'), 'Hello, World')

    def test_greet_returns_hello_plus_empty_name(self):
        self.assertEqual(greet(''), 'Hello, ')


if __name__ == '__main__':
    unittest.main()
