import unittest
from helpers import primers


class Problem_001_Spec(unittest.TestCase):
    """The test cases for helpers.primers

    See Above

    Methods:

    """

    def setup(self, *args, **kwargs):
        self.primers = primers.Primers()

    def test_happy_path(self):
        self.setup()
        self.assertTrue(False)

    def test_null_path(self):
        self.setup()
        self.assertTrue(False)

    def test_zero_path(self):
        self.setup()
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
