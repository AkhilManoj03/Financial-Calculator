import unittest
from CalcFederalTaxes import calc


class TestCalc(unittest.TestCase):
    def test_calc_2020_S_100000(self):
        result = calc("UserInputFedTax.txt")
        self.assertEqual(result, "18079.5")

    def test_calc_2021_J_50000(self):
        result = calc("UserInputFedTax2.txt")
        self.assertEqual(result, "5602.0")

    def test_calc_2021_H_75000(self):
        result = calc("UserInputFedTax3.txt")
        self.assertEqual(result, "10796.0")

    def test_calc_2020_H_125000(self):
        result = calc("UserInputFedTax4.txt")
        self.assertEqual(result, "22638.0")

    def test_calc_invalid_argument(self):
        result = calc("InvalidInput.txt")
        self.assertEqual(result, "Error: 401")


if __name__ == '__main__':
    unittest.main()
