from tdd_fizzbuzz import Answer
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(1, Answer(1))
        self.assertEqual(2, Answer(2))
        self.assertEqual("fizz", Answer(3))
        self.assertEqual(4, Answer(4))
        self.assertEqual("buzz", Answer(5))