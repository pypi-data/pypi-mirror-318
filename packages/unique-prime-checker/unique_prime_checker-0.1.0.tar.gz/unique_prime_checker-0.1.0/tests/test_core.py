import unittest
from prime_checker.core import is_prime

class TestPrimeChecker(unittest.TestCase):
    def test_prime_number(self):
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(13))

    def test_non_prime_number(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(10))

    def test_edge_cases(self):
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(0))
        self.assertTrue(is_prime(2))  # Smallest prime

if __name__ == "__main__":
    unittest.main()
