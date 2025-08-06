import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method with various inputs."""
        # positive integers
        self.assertEqual(self.calc.add(2, 3), 5)
        # mix of negative and positive
        self.assertEqual(self.calc.add(-1, 1), 0)
        # zeros
        self.assertEqual(self.calc.add(0, 0), 0)
        # floats
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)
        # large numbers
        self.assertEqual(self.calc.add(1_000_000, 2_000_000), 3_000_000)

    def test_subtraction(self):
        """Test the subtract method with various inputs."""
        # positive result
        self.assertEqual(self.calc.subtract(10, 3), 7)
        # zero result
        self.assertEqual(self.calc.subtract(5, 5), 0)
        # negative result
        self.assertEqual(self.calc.subtract(3, 10), -7)
        # floats
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    def test_multiplication(self):
        """Test the multiply method with various inputs."""
        # positive numbers
        self.assertEqual(self.calc.multiply(4, 5), 20)
        # zero
        self.assertEqual(self.calc.multiply(0, 100), 0)
        # mix of negative and positive
        self.assertEqual(self.calc.multiply(-3, 5), -15)
        # two negatives
        self.assertEqual(self.calc.multiply(-3, -2), 6)
        # floats
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)

    def test_division_normal(self):
        """Test the divide method with valid non-zero denominators."""
        # integer division
        self.assertEqual(self.calc.divide(10, 2), 5)
        # float result
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        # mix floats
        self.assertAlmostEqual(self.calc.divide(5.5, 1.1), 5.0)

    def test_division_by_zero(self):
        """Test that dividing by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))
        # numerator zero as well
        self.assertIsNone(self.calc.divide(0, 0))

    def test_chain_operations(self):
        """
        Test a small 'workflow' of operations to ensure state
        is not carried over incorrectly (statelessness).
        """
        result1 = self.calc.add(1, 2)        # 3
        result2 = self.calc.multiply(result1, 4)  # 12
        result3 = self.calc.subtract(result2, 5)  # 7
        result4 = self.calc.divide(result3, 7)    # 1.0
        self.assertEqual((result1, result2, result3, result4), (3, 12, 7, 1.0))
        
    def test_division(self):
    # normal division
    self.assertEqual(self.calc.divide(10, 2), 5)
    # division by zero
    self.assertIsNone(self.calc.divide(10, 0))
    

if __name__ == "__main__":
    unittest.main()
