import unittest
from bissexto import bissexto


class TestBissexto(unittest.TestCase):
    def test_bissexto_false(self):
        self.assertEqual(False, bissexto(2001))

    def test_bissexto_true(self):
        self.assertEqual(True, bissexto(1996))

    def test_bissexto_div_100(self):
        self.assertEqual(False, bissexto(1900))

    def test_bissexto_div_400(self):
        self.assertEqual(True, bissexto(2000))


if __name__ == "__main__":
    unittest.main()
