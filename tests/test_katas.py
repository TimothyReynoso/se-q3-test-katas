import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(2, 2), 4)

    def test_multiply(self):
        self.assertEqual(katas.multiply(2, 2), 4)
        self.assertEqual(katas.multiply(2, 3), 6)

    def test_power(self):
        self.assertEqual(katas.power(2, 2), 4)
        self.assertEqual(katas.power(2, 4), 16)

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(10), 55)


if __name__ == '__main__':
    unittest.main()
