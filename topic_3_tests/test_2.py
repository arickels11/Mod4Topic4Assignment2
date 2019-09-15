import unittest
from topic_3_main import main_calc

# Test set 1:, price from $10.00 to $29.99
# price: between 10 and 30, 5 cash, 10%
# price: between 10 and 30, 5 cash, 15%
# price: between 10 and 30, 5 cash, 20%
# price: between 10 and 30, 10 cash, 10%
# price: between 10 and 30, 10 cash, 15%
# price: between 10 and 30, 10 cash, 20%


class MyTestCase(unittest.TestCase):  # tax rate 6%, shipping rate $7.95
    def test_10to30_1(self):
        self.assertEqual(12.72, main_calc.calculate_order(10.00, 5, 10))

    def test_10to30_2(self):
        self.assertEqual(16.96, main_calc.calculate_order(15.00, 5, 15))

    def test_10to30_3(self):
        self.assertEqual(18.97, main_calc.calculate_order(17.99, 5, 20))

    def test_10to30_4(self):
        self.assertEqual(17.49, main_calc.calculate_order(20.00, 10, 10))

    def test_10to30_5(self):
        self.assertEqual(20.11, main_calc.calculate_order(23.50, 10, 15))

    def test_10to30_6(self):
        self.assertEqual(24.90, main_calc.calculate_order(29.99, 10, 20))


if __name__ == '__main__':
    unittest.main()
