from unittest import TestCase
from testing.function import multiply


class MyTestCase(TestCase):
    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_single_value(self):
        expected = 15
        self.assertEqual(multiply(expected), expected)

    def test_multiply_zero(self):
        expected = 0
        self.assertEqual(multiply(expected), expected)

    def test_multiply_inputs(self):
        inputs = (3,5)
        expected = 15
        self.assertEqual(multiply(*inputs), expected)

