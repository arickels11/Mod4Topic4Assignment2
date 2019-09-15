import unittest
from topic_3_main import main_calc

# Test set 3:, price greater than or equal to $50.00
# price: 50+, 5 cash, 10%
# price: 50+, 5 cash, 15%
# price: 50+, 5 cash, 20%
# price: 50+, 10 cash, 10%
# price: 50+, 10 cash, 15%
# price: 50+, 10 cash, 20%


class MyTestCase(unittest.TestCase):  # tax rate 6%, shipping is free
    def test_50_and_up_1(self):
        self.assertEqual(35.80, main_calc.calculate_order(50.00, 5, 10))

    def test_50_and_up_2(self):
        self.assertEqual(38.98, main_calc.calculate_order(55.00, 5, 15))

    def test_50_and_up_3(self):
        self.assertEqual(42.47, main_calc.calculate_order(59.99, 5, 20))

    def test_50_and_up_4(self):
        self.assertEqual(41.52, main_calc.calculate_order(100.00, 10, 10))

    def test_50_and_up_5(self):
        self.assertEqual(43.03, main_calc.calculate_order(110.50, 10, 15))

    def test_50_and_up_6(self):
        self.assertEqual(45.86, main_calc.calculate_order(199.99, 10, 20))


if __name__ == '__main__':
    unittest.main()
