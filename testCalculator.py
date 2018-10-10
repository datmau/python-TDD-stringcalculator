import unittest
import Calculator

class TestEmptyString(unittest.TestCase):

    '''def test_empty_string(self):
        self.assertEqual(Calculator.sum(''),0)

    def test_one_number(self):
        self.assertEqual(Calculator.sum('1'),1)
        self.assertNotEqual(Calculator.sum('1'),0)

    def test_two_numbers(self):
        self.assertEqual(Calculator.sum('1,2'),3)
        self.assertNotEqual(Calculator.sum('1,2'),4)

    def test_uknow_numbers(self):
        self.assertEqual(Calculator.sum('1,2,3'),6)
        self.assertNotEqual(Calculator.sum('1,2,5'),4)
    
    def test_multiline_entry_numbers(self):
        self.assertEqual(Calculator.sum('1\n2,3\n2,2'),10)
        self.assertNotEqual(Calculator.sum('1\n3,4\n1'),40)

    def test_different_delimiter(self):
        self.assertEqual(Calculator.sum_whit_delimiter('//;\n1;1\n2\n6;-3'),7)'''

    def test_sum_class_Calculator(self):
        calc = Calculator.StringCalculator('//;\n1;1\n2\n6;-3')
        self.assertEqual(calc.add(),7)
        self.assertNotEqual(calc.add(),10)
        


if __name__ == '__main__':
    unittest.main()
