import unittest
import sys
import os

# 添加父目录到系统路径以导入strmaths
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from strmaths import mul, div

class TestStrMaths(unittest.TestCase):
    def test_multiplication(self):
        # 测试整数乘法
        self.assertEqual(float(mul(2, 3)), 6.0)
        self.assertEqual(float(mul(0, 5)), 0.0)
        
        # 测试小数乘法
        self.assertAlmostEqual(float(mul(1.5, 2.0)), 3.0)
        self.assertAlmostEqual(float(mul(0.1, 0.1)), 0.01)
        
    def test_division_fraction(self):
        # 测试分数模式除法
        self.assertEqual(div(6, 2, mode='fraction'), '3/1')
        self.assertEqual(div(1, 2, mode='fraction'), '1/2')
        
        # 测试小数除法（分数模式）
        result = div(1.5, 0.5, mode='fraction')
        numerator, denominator = map(int, result.split('/'))
        self.assertEqual(numerator/denominator, 3.0)
        
    def test_division_decimal(self):
        # 测试小数模式除法
        quotient, remainder = div(6, 2, mode='decimal')
        self.assertEqual(float(quotient), 3.0)
        self.assertEqual(remainder, 0.0)
        
        quotient, remainder = div(5, 2, mode='decimal')
        self.assertEqual(float(quotient), 2.5)
        self.assertEqual(remainder, 0.0)
        
    def test_zero_division(self):
        # 测试除以零的情况
        with self.assertRaises(ValueError):
            div(1, 0)
            
if __name__ == '__main__':
    unittest.main() 