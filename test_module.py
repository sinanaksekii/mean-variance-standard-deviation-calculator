import unittest
from mean_var_std import calculate

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = calculate([2,6,2,8,4,0,1,5,7])
        expected = {
          'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.7777777777777777],
          'variance': [[9.555555555555555, 0.6666666666666666, 13.333333333333334], [4.222222222222222, 10.666666666666666, 6.222222222222222], 6.888888888888889],
          'standard deviation': [[3.091206165165235, 0.816496580927726, 3.6514837167011076], [2.0548046676563256, 3.265986323710904, 2.494438257849294], 2.6246692913372702],
          'max': [[8, 6, 7], [6, 8, 7], 8],
          'min': [[1, 4, 0], [2, 0, 1], 0],
          'sum': [[11, 15, 9], [10, 12, 13], 34]
        }
        for key in expected:
            self.assertAlmostEqual(actual[key][2], expected[key][2], places=1)
            for a, e in zip(actual[key][0], expected[key][0]):
                self.assertAlmostEqual(a, e, places=1)
            for a, e in zip(actual[key][1], expected[key][1]):
                self.assertAlmostEqual(a, e, places=1)
