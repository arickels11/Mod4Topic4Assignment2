import unittest
from topic_3_main import main_calc

# Test set 1:, price under 10.00
# price: under 10, 5 cash, 10%
# price: under 10, 5 cash, 15%
# price: under 10, 5 cash, 20%
# price: under 10, 10 cash, 10%
# price: under 10, 10 cash, 15%
# price: under 10, 10 cash, 20%


class MyTestCase(unittest.TestCase):  # tax rate 6%, shipping rate $5.95
    def test_under_ten1(self):
        self.assertEqual(7.86, main_calc.calculate_order(7.00, 5, 10))

    def test_under_ten2(self):
        self.assertEqual(7.75, main_calc.calculate_order(7.00, 5, 15))

    def test_under_ten3(self):
        self.assertEqual(10.18, main_calc.calculate_order(9.99, 5, 20))

    def test_under_ten4(self):
        self.assertEqual(5.95, main_calc.calculate_order(8.00, 10, 10))

    def test_under_ten5(self):
        self.assertEqual(5.95, main_calc.calculate_order(6.70, 10, 15))

    def test_under_ten6(self):
        self.assertEqual(5.95, main_calc.calculate_order(3.50, 10, 20))


if __name__ == '__main__':
    unittest.main()
