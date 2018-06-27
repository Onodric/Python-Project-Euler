import unittest
from challenges import Problem_001

class Problem_001_Spec(unittest.TestCase):
    """The test cases for 001

    See Above

    Methods:

    """

    def setup(self, *args, **kwargs):
        self.problem = Problem_001.Problem_001()

    def test_happy_path(self):
        self.setup()
        self.assertEqual(self.problem.sum_of_multiples(10, 3, 5), 23)

    def test_null_path(self):
        self.setup()
        self.assertEqual(self.problem.sum_of_multiples(None, 3, 5), 0)
        self.assertEqual(self.problem.sum_of_multiples(30, None, 5), 0)
        self.assertEqual(self.problem.sum_of_multiples(30, 3, None), 0)

    def test_zero_path(self):
        self.setup()
        self.assertEqual(self.problem.sum_of_multiples(20, 0, 2), 0)
        self.assertEqual(self.problem.sum_of_multiples(20, 2, 0), 0)
        self.assertEqual(self.problem.sum_of_multiples(0, 10, 2), 0)

if __name__ == "__main__":
    unittest.main()