import unittest
from helpers import factorize


class Problem_001_Spec(unittest.TestCase):
    """The test cases for helpers.factorize

    Methods:
        setup(self, *args, **kwargs):
        test_get_all_prime_factors_of_happy_path(self):
        test_get_all_prime_factors_of_null_path(self):
        test_get_all_prime_factors_of_zero_path(self):
        test_get_all_factor_pairs_of_happy_path(self):
        test_get_all_factor_pairs_of_null_path(self):
        test_get_all_factor_pairs_of_zero_path(self):
    """

    def setup(self, *args, **kwargs):
        self.problem = factorize.Factorize()

    def test_get_all_prime_factors_of_happy_path(self):
        self.setup()
        self.assertTrue(False)

    def test_get_all_prime_factors_of_null_path(self):
        self.setup()
        self.assertTrue(False)

    def test_get_all_prime_factors_of_zero_path(self):
        self.setup()
        self.assertTrue(False)

    def test_get_all_factor_pairs_of_happy_path(self):
        self.setup()
        self.assertTrue(False)

    def test_get_all_factor_pairs_of_null_path(self):
        self.setup()
        self.assertTrue(False)

    def test_get_all_factor_pairs_of_zero_path(self):
        self.setup()
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
