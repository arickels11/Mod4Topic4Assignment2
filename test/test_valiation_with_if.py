from input_validation import validation_with_if
import unittest


class MyTestCase(unittest.TestCase):

    def test_input_validation_with_if(self):
        self.assertEqual(-1, validation_with_if.average(90, -90, 95))


if __name__ == '__main__':
    unittest.main()
