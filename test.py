import unittest
from main import Answer

class TestFizzBuzz(unittest.TestCase):
    def test_answer_basico(self):
        self.assertEqual("1", Answer(1))
        self.assertEqual("2", Answer(2))
        self.assertEqual("4", Answer(4))
    def test_answer_fizz_multiplos_3(self):
        self.assertEqual("fizz", Answer(3))
        self.assertEqual("fizz", Answer(6))
    def test_answer_buzz_multiplos_5(self):
        self.assertEqual("buzz", Answer(5))
        self.assertEqual("buzz", Answer(10))
    def test_answer_fizzbuzz_multiplos_3_e_5(self):
        self.assertEqual("fizzbuzz", Answer(15))
        self.assertEqual("fizzbuzz", Answer(30))