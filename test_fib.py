import unittest
from fib import fib


class TestFibonacci(unittest.TestCase):
    def test_fib(self):
        casos = [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
        ]

        for n, expected in casos:
            with self.subTest(n=n):
                self.assertEqual(fib(n), expected)


if __name__ == "__main__":
    unittest.main()
