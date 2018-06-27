import unittest
from challenges import Problem_002


class Test_Problem_001(unittest.TestCase):
    """The test cases for 002

    See Above

    Methods:

    """

    def setup(self, *args, **kwargs):
        self.problem = Problem_002.Problem_002()

    def test_happy_path(self):
        self.setup()
        self.assertEqual(self.problem.fibbonacci_sum_of_multiples(100, 5), 60)

    def test_null_path(self):
        self.setup()
        self.assertEqual(self.problem.fibbonacci_sum_of_multiples(None, 3), 0)
        self.assertEqual(
            self.problem.fibbonacci_sum_of_multiples(100, None), 0)

    def test_zero_path(self):
        self.setup()
        self.assertEqual(self.problem.fibbonacci_sum_of_multiples(100, 0), 0)
        self.assertEqual(self.problem.fibbonacci_sum_of_multiples(0, 2), 0)


if __name__ == "__main__":
    unittest.main()
