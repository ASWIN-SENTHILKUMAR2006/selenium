from math_operations import multiply
class TestMathOperations(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)