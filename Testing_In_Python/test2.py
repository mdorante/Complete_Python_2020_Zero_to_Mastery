import unittest
import Exercise_Testing


class TestGame(unittest.TestCase):
    def test_input(self):
        number1 = 5
        guess1 = 5
        result = Exercise_Testing.run_guess(guess1, number1)
        self.assertTrue(result)

    def test_input_incorrect(self):
        result = Exercise_Testing.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_out_of_range(self):
        result = Exercise_Testing.run_guess(4, 13)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = Exercise_Testing.run_guess(7, 'sjs')
        self.assertFalse(result)


unittest.main()
