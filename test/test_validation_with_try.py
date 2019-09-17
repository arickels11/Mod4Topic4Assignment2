from input_validation import validation_with_try
import unittest


class MyTestCase(unittest.TestCase):
    def test_average_exception(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(-90, 60, 89)


if __name__ == '__main__':
    unittest.main()
