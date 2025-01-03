import unittest
import sys
import os
import random

# 添加父目录到系统路径以导入listplus
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from listplus import *

class TestListPlus(unittest.TestCase):
    def setUp(self):
        # 设置固定的随机种子以保证测试的可重复性
        random.seed(42)
        
    def test_chunk(self):
        # 测试正常分块
        self.assertEqual(chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        # 测试块大小等于列表长度
        self.assertEqual(chunk([1, 2, 3], 3), [[1, 2, 3]])
        # 测试块大小大于列表长度
        self.assertEqual(chunk([1, 2], 3), [[1, 2]])
        # 测试空列表
        self.assertEqual(chunk([], 2), [])
        
    def test_flatten(self):
        # 测试基本展平
        self.assertEqual(flatten([[1, 2], [3, 4]]), [1, 2, 3, 4])
        # 测试深层嵌套
        self.assertEqual(flatten([[1, [2, 3]], [4, [5, 6]]]), [1, 2, 3, 4, 5, 6])
        # 测试指定深度
        self.assertEqual(flatten([[1, [2, 3]], [4, [5, 6]]], depth=1), [1, [2, 3], 4, [5, 6]])
        # 测试空列表
        self.assertEqual(flatten([]), [])
        
    def test_group_by(self):
        # 测试基本分组
        data = [1, 2, 3, 4, 5]
        self.assertEqual(group_by(data, lambda x: x % 2), {0: [2, 4], 1: [1, 3, 5]})
        # 测试字符串分组
        words = ['apple', 'banana', 'cherry', 'date']
        self.assertEqual(group_by(words, len), {5: ['apple'], 6: ['banana', 'cherry'], 4: ['date']})
        # 测试空列表
        self.assertEqual(group_by([], lambda x: x), {})
        
    def test_unique(self):
        # 测试基本去重
        self.assertEqual(unique([1, 2, 2, 3, 1]), [1, 2, 3])
        # 测试使用键函数
        data = [(1, 'a'), (2, 'a'), (1, 'b')]
        self.assertEqual(unique(data, lambda x: x[0]), [(1, 'a'), (2, 'a')])
        # 测试空列表
        self.assertEqual(unique([]), [])
        
    def test_partition(self):
        # 测试基本分区
        even, odd = partition([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
        self.assertEqual(even, [2, 4])
        self.assertEqual(odd, [1, 3, 5])
        # 测试空列表
        self.assertEqual(partition([], lambda x: True), ([], []))
        # 测试全部满足条件
        self.assertEqual(partition([2, 4, 6], lambda x: x % 2 == 0), ([2, 4, 6], []))
        
    def test_window(self):
        # 测试基本滑动窗口
        self.assertEqual(window([1, 2, 3, 4], 2), [[1, 2], [2, 3], [3, 4]])
        # 测试步长
        self.assertEqual(window([1, 2, 3, 4], 2, 2), [[1, 2], [3, 4]])
        # 测试窗口大小等于列表长度
        self.assertEqual(window([1, 2, 3], 3), [[1, 2, 3]])
        # 测试空列表
        self.assertEqual(window([], 2), [])
        
    def test_interleave(self):
        # 测试基本交错
        self.assertEqual(interleave([1, 4], [2, 5], [3, 6]), [1, 2, 3, 4, 5, 6])
        # 测试不等长列表
        self.assertEqual(interleave([1, 4], [2], [3, 6]), [1, 2, 3, 4, 6])
        # 测试单个列表
        self.assertEqual(interleave([1, 2, 3]), [1, 2, 3])
        # 测试空列表
        self.assertEqual(interleave([], [], []), [])
        
    def test_rotate(self):
        # 测试正向旋转
        self.assertEqual(rotate([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
        # 测试负向旋转
        self.assertEqual(rotate([1, 2, 3, 4, 5], -1), [2, 3, 4, 5, 1])
        # 测试旋转次数大于列表长度
        self.assertEqual(rotate([1, 2, 3], 5), [2, 3, 1])
        # 测试空列表
        self.assertEqual(rotate([], 2), [])
        
    def test_shuffle(self):
        # 测试基本打乱
        original = [1, 2, 3, 4, 5]
        shuffled = shuffle(original.copy(), seed=42)
        self.assertNotEqual(original, shuffled)
        self.assertEqual(sorted(original), sorted(shuffled))
        # 测试空列表
        self.assertEqual(shuffle([]), [])
        
    def test_count_by(self):
        # 测试基本计数
        data = [1, 2, 2, 3, 1, 3, 3]
        self.assertEqual(count_by(data, lambda x: x), {1: 2, 2: 2, 3: 3})
        # 测试字符串长度计数
        words = ['a', 'bb', 'ccc', 'bb']
        self.assertEqual(count_by(words, len), {1: 1, 2: 2, 3: 1})
        # 测试空列表
        self.assertEqual(count_by([], lambda x: x), {})
        
    def test_find_index(self):
        # 测试基本查找
        self.assertEqual(find_index([1, 2, 3, 4], lambda x: x > 2), 2)
        # 测试从指定位置开始查找
        self.assertEqual(find_index([1, 2, 3, 4], lambda x: x > 2, start=3), 3)
        # 测试未找到
        self.assertEqual(find_index([1, 2, 3], lambda x: x > 5), -1)
        # 测试空列表
        self.assertEqual(find_index([], lambda x: True), -1)
        
    def test_take_while(self):
        # 测试基本获取
        self.assertEqual(take_while([1, 2, 3, 4, 1, 2], lambda x: x < 3), [1, 2])
        # 测试全部满足条件
        self.assertEqual(take_while([1, 2, 3], lambda x: x < 4), [1, 2, 3])
        # 测试全部不满足条件
        self.assertEqual(take_while([1, 2, 3], lambda x: x < 1), [])
        # 测试空列表
        self.assertEqual(take_while([], lambda x: True), [])
        
    def test_drop_while(self):
        # 测试基本删除
        self.assertEqual(drop_while([1, 2, 3, 4, 1, 2], lambda x: x < 3), [3, 4, 1, 2])
        # 测试全部满足条件
        self.assertEqual(drop_while([1, 2, 3], lambda x: x < 4), [])
        # 测试全部不满足条件
        self.assertEqual(drop_while([1, 2, 3], lambda x: x < 1), [1, 2, 3])
        # 测试空列表
        self.assertEqual(drop_while([], lambda x: True), [])
        
    def test_zip_with_index(self):
        # 测试基本索引添加
        self.assertEqual(zip_with_index(['a', 'b', 'c']), [(0, 'a'), (1, 'b'), (2, 'c')])
        # 测试指定起始索引
        self.assertEqual(zip_with_index(['a', 'b'], start=1), [(1, 'a'), (2, 'b')])
        # 测试空列表
        self.assertEqual(zip_with_index([]), [])
        
    def test_cartesian_product(self):
        # 测试基本笛卡尔积
        self.assertEqual(cartesian_product([1, 2], ['a', 'b']), 
                        [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')])
        # 测试单个列表
        self.assertEqual(cartesian_product([1, 2]), [(1,), (2,)])
        # 测试空列表
        self.assertEqual(cartesian_product([]), [])
        
    def test_permutations(self):
        # 测试基本排列
        self.assertEqual(permutations([1, 2, 3], 2), 
                        [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        # 测试完整排列
        self.assertEqual(permutations([1, 2]), [(1, 2), (2, 1)])
        # 测试空列表
        self.assertEqual(permutations([]), [])
        
    def test_combinations(self):
        # 测试基本组合
        self.assertEqual(combinations([1, 2, 3], 2), [(1, 2), (1, 3), (2, 3)])
        # 测试选择全部元素
        self.assertEqual(combinations([1, 2], 2), [(1, 2)])
        # 测试空列表
        self.assertEqual(combinations([], 0), [()])
        
    def test_reduce_by_key(self):
        # 测试基本归约
        data = [(1, 2), (2, 3), (1, 4)]
        self.assertEqual(reduce_by_key(data, lambda x, y: x + y), {1: 6, 2: 3})
        # 测试字符串连接
        data = [('a', 'hello'), ('b', 'world'), ('a', '!')]
        self.assertEqual(reduce_by_key(data, lambda x, y: x + y), {'a': 'hello!', 'b': 'world'})
        # 测试空列表
        self.assertEqual(reduce_by_key([], lambda x, y: x + y), {})
        
    def test_sort_by(self):
        # 测试基本排序
        data = [(1, 'a'), (3, 'b'), (2, 'c')]
        self.assertEqual(sort_by(data, lambda x: x[0]), [(1, 'a'), (2, 'c'), (3, 'b')])
        # 测试降序排序
        self.assertEqual(sort_by(data, lambda x: x[0], reverse=True), [(3, 'b'), (2, 'c'), (1, 'a')])
        # 测试空列表
        self.assertEqual(sort_by([], lambda x: x), [])
        
    def test_group_consecutive(self):
        # 测试基本分组
        self.assertEqual(group_consecutive([1, 1, 2, 3, 3, 3, 4]), [[1, 1], [2], [3, 3, 3], [4]])
        # 测试全部相同
        self.assertEqual(group_consecutive([1, 1, 1]), [[1, 1, 1]])
        # 测试全部不同
        self.assertEqual(group_consecutive([1, 2, 3]), [[1], [2], [3]])
        # 测试空列表
        self.assertEqual(group_consecutive([]), [])
        
    def test_split_by(self):
        # 测试基本拆分
        self.assertEqual(split_by([1, 2, 0, 3, 4, 0, 5], 0), [[1, 2], [3, 4], [5]])
        # 测试连续分隔符
        self.assertEqual(split_by([1, 0, 0, 2], 0), [[1], [], [2]])
        # 测试首尾分隔符
        self.assertEqual(split_by([0, 1, 2, 0], 0), [[], [1, 2], []])
        # 测试空列表
        self.assertEqual(split_by([], 0), [])
        
    def test_find_all_indices(self):
        # 测试基本查找
        self.assertEqual(find_all_indices([1, 2, 1, 3, 1], lambda x: x == 1), [0, 2, 4])
        # 测试条件函数
        self.assertEqual(find_all_indices([1, 2, 3, 4, 5], lambda x: x % 2 == 0), [1, 3])
        # 测试未找到
        self.assertEqual(find_all_indices([1, 2, 3], lambda x: x > 5), [])
        # 测试空列表
        self.assertEqual(find_all_indices([], lambda x: True), [])
        
    def test_replace(self):
        # 测试基本替换
        self.assertEqual(replace([1, 2, 1, 3, 1], 1, 0), [0, 2, 0, 3, 0])
        # 测试不存在的值
        self.assertEqual(replace([1, 2, 3], 4, 0), [1, 2, 3])
        # 测试空列表
        self.assertEqual(replace([], 1, 0), [])
        
    def test_replace_by(self):
        # 测试基本替换
        self.assertEqual(replace_by([1, 2, 3, 4, 5], lambda x: x % 2 == 0, 0), [1, 0, 3, 0, 5])
        # 测试全部替换
        self.assertEqual(replace_by([1, 2, 3], lambda x: True, 0), [0, 0, 0])
        # 测试空列表
        self.assertEqual(replace_by([], lambda x: True, 0), [])
        
    def test_remove_by(self):
        # 测试基本移除
        self.assertEqual(remove_by([1, 2, 3, 4, 5], lambda x: x % 2 == 0), [1, 3, 5])
        # 测试全部移除
        self.assertEqual(remove_by([1, 2, 3], lambda x: True), [])
        # 测试全部保留
        self.assertEqual(remove_by([1, 2, 3], lambda x: False), [1, 2, 3])
        # 测试空列表
        self.assertEqual(remove_by([], lambda x: True), [])
        
    def test_insert_at(self):
        # 测试基本插入
        self.assertEqual(insert_at([1, 2, 3], 1, 4), [1, 4, 2, 3])
        # 测试负索引
        self.assertEqual(insert_at([1, 2, 3], -1, 4), [1, 2, 4, 3])
        # 测试末尾插入
        self.assertEqual(insert_at([1, 2, 3], 3, 4), [1, 2, 3, 4])
        # 测试空列表
        self.assertEqual(insert_at([], 0, 1), [1])
        
    def test_move(self):
        # 测试基本移动
        self.assertEqual(move([1, 2, 3, 4], 1, 3), [1, 3, 4, 2])
        # 测试向前移动
        self.assertEqual(move([1, 2, 3, 4], 3, 1), [1, 4, 2, 3])
        # 测试相同位置
        self.assertEqual(move([1, 2, 3], 1, 1), [1, 2, 3])
        # 测试空列表
        with self.assertRaises(IndexError):
            move([], 0, 0)
            
    def test_sliding_window_sum(self):
        # 测试基本求和
        self.assertEqual(sliding_window_sum([1, 2, 3, 4, 5], 3), [6, 9, 12])
        # 测试窗口大小等于列表长度
        self.assertEqual(sliding_window_sum([1, 2, 3], 3), [6])
        # 测试窗口大小大于列表长度
        self.assertEqual(sliding_window_sum([1, 2], 3), [])
        # 测试空列表
        self.assertEqual(sliding_window_sum([], 2), [])
        
    def test_running_total(self):
        # 测试基本累计
        self.assertEqual(running_total([1, 2, 3, 4, 5]), [1, 3, 6, 10, 15])
        # 测试负数
        self.assertEqual(running_total([1, -2, 3, -4]), [1, -1, 2, -2])
        # 测试单个元素
        self.assertEqual(running_total([5]), [5])
        # 测试空列表
        self.assertEqual(running_total([]), [])
        
    def test_frequencies(self):
        # 测试基本频率
        result = frequencies([1, 2, 2, 3, 1, 3, 3])
        self.assertAlmostEqual(result[1], 0.286, places=3)
        self.assertAlmostEqual(result[2], 0.286, places=3)
        self.assertAlmostEqual(result[3], 0.429, places=3)
        # 测试单个元素
        self.assertEqual(frequencies([1, 1, 1]), {1: 1.0})
        # 测试空列表
        self.assertEqual(frequencies([]), {})
        
    def test_split_at_indices(self):
        # 测试基本拆分
        self.assertEqual(split_at_indices([1, 2, 3, 4, 5], [2, 4]), 
                        [[1, 2], [3, 4], [5]])
        # 测试重复索引
        self.assertEqual(split_at_indices([1, 2, 3], [1, 1, 2]), 
                        [[1], [2], [3]])
        # 测试空索引列表
        self.assertEqual(split_at_indices([1, 2, 3], []), [[1, 2, 3]])
        # 测试空列表
        self.assertEqual(split_at_indices([], [1, 2]), [])
        
    def test_is_sorted(self):
        # 测试基本排序检查
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))
        # 测试降序检查
        self.assertTrue(is_sorted([5, 4, 3, 2, 1], reverse=True))
        # 测试键函数
        data = [(1, 'a'), (2, 'b'), (3, 'c')]
        self.assertTrue(is_sorted(data, key_func=lambda x: x[0]))
        # 测试空列表
        self.assertTrue(is_sorted([]))
        # 测试单个元素
        self.assertTrue(is_sorted([1]))
        
    def test_first(self):
        # 测试基本获取
        self.assertEqual(first([1, 2, 3]), 1)
        # 测试空列表
        self.assertEqual(first([], default=0), 0)
        # 测试默认值为None
        self.assertIsNone(first([]))
        
    def test_last(self):
        # 测试基本获取
        self.assertEqual(last([1, 2, 3]), 3)
        # 测试空列表
        self.assertEqual(last([], default=0), 0)
        # 测试默认值为None
        self.assertIsNone(last([]))
        
    def test_compact(self):
        # 测试基本压缩
        self.assertEqual(compact([1, None, 2, '', 3, [], False, 4]), [1, 2, 3, 4])
        # 测试全部假值
        self.assertEqual(compact([None, '', [], {}, False, 0]), [])
        # 测试空列表
        self.assertEqual(compact([]), [])
        
    def test_difference(self):
        # 测试基本差集
        self.assertEqual(difference([1, 2, 3, 4], [2, 4]), [1, 3])
        # 测试无交集
        self.assertEqual(difference([1, 2, 3], [4, 5, 6]), [1, 2, 3])
        # 测试完全相同
        self.assertEqual(difference([1, 2, 3], [1, 2, 3]), [])
        # 测试空列表
        self.assertEqual(difference([], [1, 2]), [])
        self.assertEqual(difference([1, 2], []), [1, 2])
        
    def test_intersection(self):
        # 测试基本交集
        self.assertEqual(intersection([1, 2, 3, 4], [2, 4, 6]), [2, 4])
        # 测试无交集
        self.assertEqual(intersection([1, 2, 3], [4, 5, 6]), [])
        # 测试完全相同
        self.assertEqual(intersection([1, 2, 3], [1, 2, 3]), [1, 2, 3])
        # 测试空列表
        self.assertEqual(intersection([], [1, 2]), [])
        self.assertEqual(intersection([1, 2], []), [])
        
    def test_union(self):
        # 测试基本并集
        self.assertEqual(union([1, 2, 3], [2, 3, 4], [3, 4, 5]), [1, 2, 3, 4, 5])
        # 测试无重复
        self.assertEqual(union([1, 2], [3, 4], [5, 6]), [1, 2, 3, 4, 5, 6])
        # 测试完全重复
        self.assertEqual(union([1, 2], [1, 2], [1, 2]), [1, 2])
        # 测试空列表
        self.assertEqual(union([], [], []), [])
        self.assertEqual(union([1, 2], [], [3, 4]), [1, 2, 3, 4])
        
    def test_min_by(self):
        # 测试基本最小值
        data = [(1, 'a'), (2, 'b'), (0, 'c')]
        self.assertEqual(min_by(data, lambda x: x[0]), (0, 'c'))
        # 测试字符串长度
        words = ['apple', 'banana', 'cat']
        self.assertEqual(min_by(words, len), 'cat')
        # 测试空列表
        self.assertEqual(min_by([], lambda x: x, default=0), 0)
        
    def test_max_by(self):
        # 测试基本最大值
        data = [(1, 'a'), (2, 'b'), (0, 'c')]
        self.assertEqual(max_by(data, lambda x: x[0]), (2, 'b'))
        # 测试字符串长度
        words = ['apple', 'banana', 'cat']
        self.assertEqual(max_by(words, len), 'banana')
        # 测试空列表
        self.assertEqual(max_by([], lambda x: x, default=0), 0)
        
    def test_average(self):
        # 测试基本平均值
        self.assertEqual(average([1, 2, 3, 4, 5]), 3.0)
        # 测试负数
        self.assertEqual(average([1, -1, 2, -2]), 0.0)
        # 测试单个元素
        self.assertEqual(average([5]), 5.0)
        # 测试空列表
        self.assertEqual(average([], default=0), 0)
        
    def test_median(self):
        # 测试奇数个元素
        self.assertEqual(median([1, 2, 3, 4, 5]), 3.0)
        # 测试偶数个元素
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        # 测试单个元素
        self.assertEqual(median([5]), 5.0)
        # 测试空列表
        self.assertEqual(median([], default=0), 0)
        
    def test_mode(self):
        # 测试基本众数
        self.assertEqual(mode([1, 2, 2, 3, 3, 3, 4]), 3)
        # 测试单个元素
        self.assertEqual(mode([5]), 5)
        # 测试空列表
        self.assertEqual(mode([], default=0), 0)
        
    def test_all_equal(self):
        # 测试全部相等
        self.assertTrue(all_equal([1, 1, 1]))
        # 测试部分相等
        self.assertFalse(all_equal([1, 2, 1]))
        # 测试单个元素
        self.assertTrue(all_equal([5]))
        # 测试空列表
        self.assertTrue(all_equal([]))
        
    def test_is_palindrome(self):
        # 测试基本回文
        self.assertTrue(is_palindrome([1, 2, 3, 2, 1]))
        # 测试非回文
        self.assertFalse(is_palindrome([1, 2, 3]))
        # 测试单个元素
        self.assertTrue(is_palindrome([5]))
        # 测试空列表
        self.assertTrue(is_palindrome([]))
        
    def test_swap(self):
        # 测试基本交换
        self.assertEqual(swap([1, 2, 3, 4], 1, 2), [1, 3, 2, 4])
        # 测试相同位置
        self.assertEqual(swap([1, 2, 3], 1, 1), [1, 2, 3])
        # 测试边界位置
        self.assertEqual(swap([1, 2, 3], 0, 2), [3, 2, 1])
        
    def test_sample(self):
        # 测试单个采样
        result = sample([1, 2, 3, 4, 5], k=1, seed=42)
        self.assertIn(result, [1, 2, 3, 4, 5])
        
        # 测试多个采样
        result = sample([1, 2, 3, 4, 5], k=3, seed=42)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(x in [1, 2, 3, 4, 5] for x in result))
        self.assertEqual(len(set(result)), 3)  # 确保没有重复
        
        # 测试k等于列表长度
        result = sample([1, 2, 3], k=3, seed=42)
        self.assertEqual(sorted(result), [1, 2, 3])
        
        # 测试空列表
        with self.assertRaises(IndexError):
            sample([], k=1)
            
    def test_split_at(self):
        # 测试基本分割
        self.assertEqual(split_at([1, 2, 3, 4, 5], 2), ([1, 2], [3, 4, 5]))
        # 测试边界分割
        self.assertEqual(split_at([1, 2, 3], 0), ([], [1, 2, 3]))
        self.assertEqual(split_at([1, 2, 3], 3), ([1, 2, 3], []))
        # 测试空列表
        self.assertEqual(split_at([], 0), ([], []))
        
    def test_trim(self):
        # 测试基本修剪
        self.assertEqual(trim([0, 0, 1, 2, 3, 0, 0], lambda x: x == 0), [1, 2, 3])
        # 测试全部修剪
        self.assertEqual(trim([0, 0, 0], lambda x: x == 0), [])
        # 测试无需修剪
        self.assertEqual(trim([1, 2, 3], lambda x: x == 0), [1, 2, 3])
        # 测试空列表
        self.assertEqual(trim([], lambda x: True), [])

if __name__ == '__main__':
    unittest.main() 