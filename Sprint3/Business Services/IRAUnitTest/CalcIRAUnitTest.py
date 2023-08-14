import unittest
from io import StringIO
from contextlib import redirect_stdout
from CalcMonthlyPayoutIRA import calc


class TestCalc(unittest.TestCase):
    def test_calc_1(self):
        result = calc("UserInputIRA.txt")
        self.assertEqual(result, "3333.33")

    def test_calc_2(self):
        result = calc("UserInputIRA2.txt")
        self.assertEqual(result, "2083.33")

    def test_calc_3(self):
        result = calc("UserInputIRA3.txt")
        self.assertEqual(result, "946.97")


if __name__ == '__main__':
    unittest.main()
