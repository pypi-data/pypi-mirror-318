import unittest
import sys
import os

# 添加父目录到系统路径以导入dictplus模块
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dictplus import *

class TestDictPlus(unittest.TestCase):
    def test_merge(self):
        """测试字典合并功能"""
        d1 = {'a': 1}
        d2 = {'b': 2}
        d3 = {'c': 3}
        self.assertEqual(merge(d1, d2, d3), {'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(merge(d1), {'a': 1})
        self.assertEqual(merge(), {})

    def test_deep_merge(self):
        """测试深度合并功能"""
        d1 = {'a': {'b': 1}}
        d2 = {'a': {'c': 2}}
        d3 = {'a': {'d': 3}}
        self.assertEqual(deep_merge(d1, d2, d3), {'a': {'b': 1, 'c': 2, 'd': 3}})
        # 测试值覆盖
        self.assertEqual(deep_merge({'a': {'b': 1}}, {'a': {'b': 2}}), {'a': {'b': 2}})
        # 测试非字典值
        self.assertEqual(deep_merge({'a': 1}, {'a': {'b': 2}}), {'a': {'b': 2}})

    def test_filter_by_keys(self):
        """测试按键过滤功能"""
        d = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(filter_by_keys(d, ['a', 'c']), {'a': 1, 'c': 3})
        self.assertEqual(filter_by_keys(d, []), {})
        self.assertEqual(filter_by_keys(d, ['d']), {})

    def test_filter_by_values(self):
        """测试按值过滤功能"""
        d = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(filter_by_values(d, lambda x: x > 1), {'b': 2, 'c': 3})
        self.assertEqual(filter_by_values(d, lambda x: x < 0), {})
        self.assertEqual(filter_by_values(d, lambda x: isinstance(x, int)), d)

    def test_invert(self):
        """测试键值对反转功能"""
        d = {'a': 1, 'b': 2}
        self.assertEqual(invert(d), {1: 'a', 2: 'b'})
        self.assertEqual(invert({}), {})
        # 注意：如果有重复的值，后面的键会覆盖前面的
        self.assertEqual(invert({'a': 1, 'b': 1}), {1: 'b'})

    def test_group_by(self):
        """测试分组功能"""
        items = [1, 2, 3, 4, 5]
        self.assertEqual(group_by(items, lambda x: x % 2), {0: [2, 4], 1: [1, 3, 5]})
        self.assertEqual(group_by([], lambda x: x), {})
        # 测试字符串分组
        words = ['apple', 'banana', 'cherry']
        self.assertEqual(group_by(words, len), {5: ['apple'], 6: ['banana', 'cherry']})

    def test_flatten(self):
        """测试字典扁平化功能"""
        d = {'a': {'b': 1, 'c': {'d': 2}}}
        self.assertEqual(flatten(d), {'a.b': 1, 'a.c.d': 2})
        self.assertEqual(flatten({'a': 1}), {'a': 1})
        self.assertEqual(flatten({}), {})
        # 测试自定义分隔符
        self.assertEqual(flatten(d, separator='/'), {'a/b': 1, 'a/c/d': 2})

    def test_unflatten(self):
        """测试字典展开功能"""
        d = {'a.b': 1, 'a.c.d': 2}
        self.assertEqual(unflatten(d), {'a': {'b': 1, 'c': {'d': 2}}})
        self.assertEqual(unflatten({'a': 1}), {'a': 1})
        self.assertEqual(unflatten({}), {})
        # 测试自定义分隔符
        self.assertEqual(unflatten({'a/b': 1}, separator='/'), {'a': {'b': 1}})

    def test_deep_get(self):
        """测试深度获取值功能"""
        d = {'a': {'b': {'c': 1}}}
        self.assertEqual(deep_get(d, 'a.b.c'), 1)
        self.assertEqual(deep_get(d, 'a.b'), {'c': 1})
        self.assertIsNone(deep_get(d, 'x.y.z'))
        self.assertEqual(deep_get(d, 'x.y.z', default=0), 0)

    def test_deep_set(self):
        """测试深度设置值功能"""
        d = {'a': {'b': {}}}
        self.assertEqual(deep_set(d, 'a.b.c', 1), {'a': {'b': {'c': 1}}})
        self.assertEqual(deep_set({}, 'a.b.c', 1), {'a': {'b': {'c': 1}}})
        # 测试覆盖非字典值
        d = {'a': 1}
        self.assertEqual(deep_set(d, 'a.b', 2), {'a': {'b': 2}})

    def test_deep_delete(self):
        """测试深度删除值功能"""
        d = {'a': {'b': {'c': 1}}}
        self.assertTrue(deep_delete(d, 'a.b.c'))
        self.assertEqual(d, {'a': {'b': {}}})
        self.assertFalse(deep_delete(d, 'x.y.z'))
        self.assertTrue(deep_delete(d, 'a'))
        self.assertEqual(d, {})

    def test_find_key_path(self):
        """测试查找键路径功能"""
        d = {'a': {'b': {'c': 1}}}
        self.assertEqual(find_key_path(d, 1), 'a.b.c')
        self.assertIsNone(find_key_path(d, 2))
        self.assertEqual(find_key_path({'a': 1}, 1), 'a')

    def test_diff(self):
        """测试字典差异比较功能"""
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        only_in_d1, only_in_d2, different = diff(d1, d2)
        self.assertEqual(only_in_d1, {'a': 1})
        self.assertEqual(only_in_d2, {'c': 4})
        self.assertEqual(different, {'b': (2, 3)})

    def test_deep_diff(self):
        """测试深度差异比较功能"""
        d1 = {'a': {'b': 1}}
        d2 = {'a': {'b': 2, 'c': 3}}
        only_in_d1, only_in_d2, different = deep_diff(d1, d2)
        self.assertEqual(only_in_d1, {})
        self.assertEqual(only_in_d2, {'a.c': 3})
        self.assertEqual(different, {'a.b': (1, 2)})

    def test_transform_keys(self):
        """测试键转换功能"""
        d = {'a': 1, 'b': 2}
        self.assertEqual(transform_keys(d, str.upper), {'A': 1, 'B': 2})
        self.assertEqual(transform_keys(d, lambda x: x + '_new'), {'a_new': 1, 'b_new': 2})
        self.assertEqual(transform_keys({}, str.upper), {})

    def test_transform_values(self):
        """测试值转换功能"""
        d = {'a': 1, 'b': 2}
        self.assertEqual(transform_values(d, lambda x: x * 2), {'a': 2, 'b': 4})
        self.assertEqual(transform_values(d, str), {'a': '1', 'b': '2'})
        self.assertEqual(transform_values({}, lambda x: x * 2), {})

    def test_deep_transform_values(self):
        """测试深度值转换功能"""
        d = {'a': 1, 'b': {'c': 2}}
        self.assertEqual(deep_transform_values(d, lambda x: x * 2), {'a': 2, 'b': {'c': 4}})
        self.assertEqual(deep_transform_values(d, str), {'a': '1', 'b': {'c': '2'}})
        self.assertEqual(deep_transform_values({}, lambda x: x * 2), {})

    def test_pick(self):
        """测试选择键值对功能"""
        d = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(pick(d, 'a', 'c'), {'a': 1, 'c': 3})
        self.assertEqual(pick(d, 'a', 'd'), {'a': 1})
        self.assertEqual(pick(d), {})

    def test_omit(self):
        """测试排除键值对功能"""
        d = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(omit(d, 'b'), {'a': 1, 'c': 3})
        self.assertEqual(omit(d, 'd'), d)
        self.assertEqual(omit(d, 'a', 'b', 'c'), {})

    def test_has_path(self):
        """测试路径存在检查功能"""
        d = {'a': {'b': {'c': 1}}}
        self.assertTrue(has_path(d, 'a.b.c'))
        self.assertTrue(has_path(d, 'a.b'))
        self.assertFalse(has_path(d, 'x.y.z'))
        self.assertFalse(has_path(d, 'a.b.c.d'))

if __name__ == '__main__':
    unittest.main() 