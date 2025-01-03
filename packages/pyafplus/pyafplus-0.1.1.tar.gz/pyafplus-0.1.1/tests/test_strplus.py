import unittest
import sys
import os

# 添加父目录到系统路径以导入strplus模块
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strplus import *

class TestStrPlus(unittest.TestCase):
    def test_split_lines(self):
        """测试文本分行功能"""
        text = "hello\nworld\ntest"
        self.assertEqual(split_lines(text), ['hello', 'world', 'test'])
        self.assertEqual(split_lines(text, keep_ends=True), ['hello\n', 'world\n', 'test'])
        self.assertEqual(split_lines(""), [])

    def test_is_empty(self):
        """测试空字符串检查功能"""
        self.assertTrue(is_empty(""))
        self.assertFalse(is_empty(" "))
        self.assertTrue(is_empty(" ", ignore_whitespace=True))
        self.assertFalse(is_empty("hello"))

    def test_reverse(self):
        """测试字符串反转功能"""
        self.assertEqual(reverse("hello"), "olleh")
        self.assertEqual(reverse(""), "")
        self.assertEqual(reverse("a"), "a")
        self.assertEqual(reverse("12345"), "54321")

    def test_is_palindrome(self):
        """测试回文检查功能"""
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama", ignore_case=True, ignore_spaces=True))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("Race car", ignore_case=True, ignore_spaces=True))

    def test_count_words(self):
        """测试单词计数功能"""
        text = "hello world hello HELLO World"
        self.assertEqual(count_words(text), {'hello': 2, 'HELLO': 1, 'world': 1, 'World': 1})
        self.assertEqual(count_words(text, ignore_case=True), {'hello': 3, 'world': 2})

    def test_truncate(self):
        """测试文本截断功能"""
        self.assertEqual(truncate("hello world", 8), "hello...")
        self.assertEqual(truncate("hello", 10), "hello")
        self.assertEqual(truncate("hello world", 5, ".."), "hel..")

    def test_wrap(self):
        """测试文本换行功能"""
        text = "hello world test"
        self.assertEqual(wrap(text, 5), ['hello', 'world', 'test'])
        self.assertEqual(wrap("helloworld", 5, break_long_words=False), ['helloworld'])

    def test_remove_extra_spaces(self):
        """测试移除多余空格功能"""
        self.assertEqual(remove_extra_spaces("  hello   world  "), "hello world")
        self.assertEqual(remove_extra_spaces("hello"), "hello")
        self.assertEqual(remove_extra_spaces("   "), "")

    def test_capitalize_words(self):
        """测试单词首字母大写功能"""
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("HELLO WORLD"), "Hello World")
        self.assertEqual(capitalize_words(""), "")

    def test_find_all(self):
        """测试查找所有子串位置功能"""
        self.assertEqual(find_all("hello hello world hello", "hello"), [0, 6, 18])
        self.assertEqual(find_all("HELLO hello", "hello", ignore_case=True), [0, 6])
        self.assertEqual(find_all("hello", "world"), [])

    def test_extract_emails(self):
        """测试提取邮箱地址功能"""
        text = "Contact us at test@example.com or support@test.com"
        self.assertEqual(extract_emails(text), ['test@example.com', 'support@test.com'])
        self.assertEqual(extract_emails("No email here"), [])

    def test_extract_urls(self):
        """测试提取URL功能"""
        text = "Visit https://example.com or http://test.com"
        self.assertEqual(extract_urls(text), ['https://example.com', 'http://test.com'])
        self.assertEqual(extract_urls("No URL here"), [])

    def test_extract_numbers(self):
        """测试提取数字功能"""
        text = "The price is 12.99 and quantity is -5"
        self.assertEqual(extract_numbers(text), [12.99, -5.0])
        self.assertEqual(extract_numbers("No numbers"), [])

    def test_is_number(self):
        """测试数字检查功能"""
        self.assertTrue(is_number("123"))
        self.assertTrue(is_number("-12.34"))
        self.assertTrue(is_number("1.23e-4"))
        self.assertFalse(is_number("abc"))
        self.assertFalse(is_number("12.34.56"))

    def test_levenshtein_distance(self):
        """测试编辑距离计算功能"""
        self.assertEqual(levenshtein_distance("hello", "hallo"), 1)
        self.assertEqual(levenshtein_distance("", "hello"), 5)
        self.assertEqual(levenshtein_distance("hello", "hello"), 0)

    def test_similarity(self):
        """测试字符串相似度计算功能"""
        self.assertEqual(similarity("hello", "hello"), 1.0)
        self.assertEqual(similarity("", ""), 1.0)
        self.assertEqual(similarity("hello", ""), 0.0)
        self.assertAlmostEqual(similarity("hello", "hallo"), 0.8)

    def test_mask(self):
        """测试字符串掩码功能"""
        # 测试基本功能
        self.assertEqual(mask("1234567890", 4, -4), "1234**7890")
        # 测试不同长度的掩码
        self.assertEqual(mask("password", 2, -2), "pa***rd")
        # 测试自定义掩码字符
        self.assertEqual(mask("short", 2, -2, '#'), "sh#rt")
        # 测试边界情况
        self.assertEqual(mask("a", 1, -1), "a")
        self.assertEqual(mask("ab", 1, -1), "a*b")
        # 测试超出范围的索引
        self.assertEqual(mask("test", 10, -1), "test")
        self.assertEqual(mask("test", 0, 10), "****")

    def test_is_valid_email(self):
        """测试邮箱地址验证功能"""
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertTrue(is_valid_email("user.name+tag@example.co.uk"))
        self.assertFalse(is_valid_email("invalid.email"))
        self.assertFalse(is_valid_email("@example.com"))

    def test_is_valid_phone(self):
        """测试电话号码验证功能"""
        self.assertTrue(is_valid_phone("13812345678"))  # 中国手机号
        self.assertTrue(is_valid_phone("1234567890", country="US"))  # 美国电话
        self.assertFalse(is_valid_phone("1234"))  # 太短
        self.assertFalse(is_valid_phone("abcdefghij"))  # 非数字

    def test_format_number(self):
        """测试数字格式化功能"""
        self.assertEqual(format_number(1234567.89, precision=2), "1,234,567.89")
        self.assertEqual(format_number(-1234.5, precision=1), "-1,234.5")
        self.assertEqual(format_number(1234, thousands_sep='.', decimal_sep=','), "1.234")

    def test_slugify(self):
        """测试URL友好文本转换功能"""
        self.assertEqual(slugify("Hello World!"), "hello-world")
        self.assertEqual(slugify("This & That"), "this-that")
        self.assertEqual(slugify("Hello_World", separator="_"), "hello_world")

    def test_extract_between(self):
        """测试提取标记之间文本功能"""
        text = "(1) and (2) and (3)"
        self.assertEqual(extract_between(text, "(", ")"), ["1", "2", "3"])
        self.assertEqual(extract_between(text, "(", ")", include_bounds=True), ["(1)", "(2)", "(3)"])
        self.assertEqual(extract_between("no markers", "(", ")"), [])

    def test_word_wrap(self):
        """测试文本自动换行功能"""
        text = "A very long text that needs to be wrapped"
        self.assertEqual(word_wrap(text, width=10), "A very\nlong text\nthat needs\nto be\nwrapped")
        self.assertEqual(word_wrap(text, width=10, indent="  "), "  A very\nlong text\nthat needs\nto be\nwrapped")

if __name__ == '__main__':
    unittest.main() 