import unittest
from topic_3_main import main_calc

# Test set 3:, price from $30.00 to $49.99
# price: between 30 and 50, 5 cash, 10%
# price: between 30 and 50, 5 cash, 15%
# price: between 30 and 50, 5 cash, 20%
# price: between 30 and 50, 10 cash, 10%
# price: between 30 and 50, 10 cash, 15%
# price: between 30 and 50, 10 cash, 20%


class MyTestCase(unittest.TestCase):  # tax rate 6%, shipping rate $11.95
    def test_30to50_1(self):
        self.assertEqual(35.80, main_calc.calculate_order(30.00, 5, 10))

    def test_30to50_2(self):
        self.assertEqual(38.98, main_calc.calculate_order(35.00, 5, 15))

    def test_30to50_3(self):
        self.assertEqual(42.47, main_calc.calculate_order(40.99, 5, 20))

    def test_30to50_4(self):
        self.assertEqual(41.52, main_calc.calculate_order(41.00, 10, 10))

    def test_30to50_5(self):
        self.assertEqual(43.03, main_calc.calculate_order(44.50, 10, 15))

    def test_30to50_6(self):
        self.assertEqual(45.86, main_calc.calculate_order(49.99, 10, 20))


if __name__ == '__main__':
    unittest.main()
