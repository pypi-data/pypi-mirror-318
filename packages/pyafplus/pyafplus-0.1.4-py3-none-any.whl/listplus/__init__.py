from typing import TypeVar, List, Callable, Any, Dict, Set, Tuple, Optional, Union
from collections import defaultdict
import random
import itertools
import functools
from decimal import Decimal, ROUND_HALF_UP

T = TypeVar('T')
S = TypeVar('S')

def chunk(lst: List[T], size: int) -> List[List[T]]:
    """
    将列表分割成固定大小的块
    
    参数:
        lst: 输入列表
        size: 每个块的大小
        
    返回:
        分割后的列表的列表
        
    示例:
        >>> chunk([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
    """
    return [lst[i:i + size] for i in range(0, len(lst), size)]

def flatten(lst: List[Any], depth: int = -1) -> List[Any]:
    """
    展平嵌套列表
    
    参数:
        lst: 输入的嵌套列表
        depth: 展平的深度，-1表示完全展平
        
    返回:
        展平后的列表
        
    示例:
        >>> flatten([[1, [2, 3]], [4, 5]])
        [1, 2, 3, 4, 5]
    """
    result = []
    for item in lst:
        if isinstance(item, list) and depth != 0:
            result.extend(flatten(item, depth - 1))
        else:
            result.append(item)
    return result

def group_by(lst: List[T], key_func: Callable[[T], S]) -> Dict[S, List[T]]:
    """
    根据键函数对列表元素进行分组
    
    参数:
        lst: 输入列表
        key_func: 用于生成分组键的函数
        
    返回:
        分组后的字典
        
    示例:
        >>> group_by([1, 2, 3, 4, 5], lambda x: x % 2)
        {0: [2, 4], 1: [1, 3, 5]}
    """
    groups = defaultdict(list)
    for item in lst:
        groups[key_func(item)].append(item)
    return dict(groups)

def unique(lst: List[T], key_func: Optional[Callable[[T], Any]] = None) -> List[T]:
    """
    去除列表中的重复元素，保持原有顺序
    
    参数:
        lst: 输入列表
        key_func: 可选的键函数，用于确定元素唯一性
        
    返回:
        去重后的列表
        
    示例:
        >>> unique([1, 2, 2, 3, 1])
        [1, 2, 3]
    """
    seen = set()
    result = []
    for item in lst:
        key = key_func(item) if key_func else item
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result

def partition(lst: List[T], predicate: Callable[[T], bool]) -> Tuple[List[T], List[T]]:
    """
    根据谓词函数将列表分成两部分
    
    参数:
        lst: 输入列表
        predicate: 谓词函数，返回True/False
        
    返回:
        满足条件和不满足条件的两个列表组成的元组
        
    示例:
        >>> partition([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
        ([2, 4], [1, 3, 5])
    """
    true_list, false_list = [], []
    for item in lst:
        (true_list if predicate(item) else false_list).append(item)
    return true_list, false_list

def window(lst: List[T], size: int, step: int = 1) -> List[List[T]]:
    """
    创建滑动窗口
    
    参数:
        lst: 输入列表
        size: 窗口大小
        step: 滑动步长
        
    返回:
        窗口列表
        
    示例:
        >>> window([1, 2, 3, 4, 5], 3, 1)
        [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    """
    return [lst[i:i + size] for i in range(0, len(lst) - size + 1, step)]

def interleave(*lists: List[T]) -> List[T]:
    """
    交错合并多个列表
    
    参数:
        *lists: 要合并的列表
        
    返回:
        交错合并后的列表
        
    示例:
        >>> interleave([1, 4], [2, 5], [3, 6])
        [1, 2, 3, 4, 5, 6]
    """
    result = []
    max_len = max(len(lst) for lst in lists) if lists else 0
    for i in range(max_len):
        for lst in lists:
            if i < len(lst):
                result.append(lst[i])
    return result

def rotate(lst: List[T], k: int) -> List[T]:
    """
    旋转列表
    
    参数:
        lst: 输入列表
        k: 旋转位数（正数右移，负数左移）
        
    返回:
        旋转后的列表
        
    示例:
        >>> rotate([1, 2, 3, 4, 5], 2)
        [4, 5, 1, 2, 3]
    """
    if not lst:
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

def shuffle(lst: List[T], seed: Optional[int] = None) -> List[T]:
    """
    随机打乱列表
    
    参数:
        lst: 输入列表
        seed: 随机种子
        
    返回:
        打乱后的列表副本
        
    示例:
        >>> shuffle([1, 2, 3, 4, 5], seed=42)
        [2, 5, 1, 4, 3]
    """
    result = lst.copy()
    if seed is not None:
        random.seed(seed)
    random.shuffle(result)
    return result

def count_by(lst: List[T], key_func: Callable[[T], S]) -> Dict[S, int]:
    """
    统计列表元素出现次数
    
    参数:
        lst: 输入列表
        key_func: 用于生成统计键的函数
        
    返回:
        统计结果字典
        
    示例:
        >>> count_by([1, 2, 2, 3, 1], lambda x: x)
        {1: 2, 2: 2, 3: 1}
    """
    counter = defaultdict(int)
    for item in lst:
        counter[key_func(item)] += 1
    return dict(counter)

def find_index(lst: List[T], predicate: Callable[[T], bool], start: int = 0) -> int:
    """
    查找满足条件的第一个元素的索引
    
    参数:
        lst: 输入列表
        predicate: 判断条件的函数
        start: 开始查找的位置
        
    返回:
        找到的索引，未找到返回-1
        
    示例:
        >>> find_index([1, 2, 3, 4], lambda x: x > 2)
        2
    """
    for i in range(start, len(lst)):
        if predicate(lst[i]):
            return i
    return -1

def take_while(lst: List[T], predicate: Callable[[T], bool]) -> List[T]:
    """
    获取列表中满足条件的前缀元素
    
    参数:
        lst: 输入列表
        predicate: 判断条件的函数
        
    返回:
        满足条件的前缀列表
        
    示例:
        >>> take_while([1, 2, 3, 4, 1, 2], lambda x: x < 3)
        [1, 2]
    """
    for i, item in enumerate(lst):
        if not predicate(item):
            return lst[:i]
    return lst

def drop_while(lst: List[T], predicate: Callable[[T], bool]) -> List[T]:
    """
    删除列表中满足条件的前缀元素
    
    参数:
        lst: 输入列表
        predicate: 判断条件的函数
        
    返回:
        删除前缀后的列表
        
    示例:
        >>> drop_while([1, 2, 3, 4, 1, 2], lambda x: x < 3)
        [3, 4, 1, 2]
    """
    for i, item in enumerate(lst):
        if not predicate(item):
            return lst[i:]
    return []

def zip_with_index(lst: List[T], start: int = 0) -> List[Tuple[int, T]]:
    """
    为列表元素添加索引
    
    参数:
        lst: 输入列表
        start: 起始索引
        
    返回:
        索引和元素的元组列表
        
    示例:
        >>> zip_with_index(['a', 'b', 'c'])
        [(0, 'a'), (1, 'b'), (2, 'c')]
    """
    return list(enumerate(lst, start))

def cartesian_product(*lists: List[T]) -> List[Tuple[T, ...]]:
    """
    计算多个列表的笛卡尔积
    
    参数:
        *lists: 输入的多个列表
        
    返回:
        笛卡尔积结果列表
        
    示例:
        >>> cartesian_product([1, 2], ['a', 'b'])
        [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
    """
    return list(itertools.product(*lists))

def permutations(lst: List[T], r: Optional[int] = None) -> List[Tuple[T, ...]]:
    """
    计算列表元素的排列
    
    参数:
        lst: 输入列表
        r: 排列的元素个数
        
    返回:
        排列结果列表
        
    示例:
        >>> permutations([1, 2, 3], 2)
        [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
    """
    if not lst:
        return []
    if r is None:
        r = len(lst)
    return list(itertools.permutations(lst, r))

def combinations(lst: List[T], r: int) -> List[Tuple[T, ...]]:
    """
    计算列表元素的组合
    
    参数:
        lst: 输入列表
        r: 组合的元素个数
        
    返回:
        组合结果列表
        
    示例:
        >>> combinations([1, 2, 3], 2)
        [(1, 2), (1, 3), (2, 3)]
    """
    return list(itertools.combinations(lst, r))

def reduce_by_key(lst: List[Tuple[S, T]], func: Callable[[T, T], T]) -> Dict[S, T]:
    """
    按键归约列表元素
    
    参数:
        lst: 键值对列表
        func: 归约函数
        
    返回:
        归约结果字典
        
    示例:
        >>> reduce_by_key([(1, 2), (2, 3), (1, 4)], lambda x, y: x + y)
        {1: 6, 2: 3}
    """
    groups = group_by(lst, lambda x: x[0])
    return {k: functools.reduce(func, [v[1] for v in group]) for k, group in groups.items()}

def sort_by(lst: List[T], key_func: Callable[[T], Any], reverse: bool = False) -> List[T]:
    """
    根据键函数对列表进行排序
    
    参数:
        lst: 输入列表
        key_func: 用于生成排序键的函数
        reverse: 是否降序排序
        
    返回:
        排序后的新列表
        
    示例:
        >>> sort_by([(1, 'a'), (2, 'b'), (0, 'c')], lambda x: x[0])
        [(0, 'c'), (1, 'a'), (2, 'b')]
    """
    return sorted(lst, key=key_func, reverse=reverse)

def group_consecutive(lst: List[T]) -> List[List[T]]:
    """
    将连续的相同元素分组
    
    参数:
        lst: 输入列表
        
    返回:
        分组后的列表
        
    示例:
        >>> group_consecutive([1, 1, 2, 3, 3, 3, 4])
        [[1, 1], [2], [3, 3, 3], [4]]
    """
    if not lst:
        return []
    result = []
    current_group = [lst[0]]
    for item in lst[1:]:
        if item == current_group[0]:
            current_group.append(item)
        else:
            result.append(current_group)
            current_group = [item]
    result.append(current_group)
    return result

def split_by(lst: List[T], separator: T) -> List[List[T]]:
    """
    根据分隔符拆分列表
    
    参数:
        lst: 输入列表
        separator: 分隔符元素
        
    返回:
        拆分后的列表的列表
        
    示例:
        >>> split_by([1, 2, 0, 3, 4, 0, 5], 0)
        [[1, 2], [3, 4], [5]]
    """
    if not lst:
        return []
    result = []
    current = []
    for item in lst:
        if item == separator:
            result.append(current)
            current = []
        else:
            current.append(item)
    result.append(current)
    return result

def find_all_indices(lst: List[T], predicate: Callable[[T], bool]) -> List[int]:
    """
    查找所有满足条件的元素的索引
    
    参数:
        lst: 输入列表
        predicate: 判断条件的函数
        
    返回:
        满足条件的元素的索引列表
        
    示例:
        >>> find_all_indices([1, 2, 1, 3, 1], lambda x: x == 1)
        [0, 2, 4]
    """
    return [i for i, item in enumerate(lst) if predicate(item)]

def replace(lst: List[T], old_value: T, new_value: T) -> List[T]:
    """
    替换列表中的所有指定值
    
    参数:
        lst: 输入列表
        old_value: 要替换的值
        new_value: 新值
        
    返回:
        替换后的新列表
        
    示例:
        >>> replace([1, 2, 1, 3, 1], 1, 0)
        [0, 2, 0, 3, 0]
    """
    return [new_value if item == old_value else item for item in lst]

def replace_by(lst: List[T], predicate: Callable[[T], bool], new_value: T) -> List[T]:
    """
    根据条件替换列表中的元素
    
    参数:
        lst: 输入列表
        predicate: 判断条件的函数
        new_value: 新值
        
    返回:
        替换后的新列表
        
    示例:
        >>> replace_by([1, 2, 3, 4, 5], lambda x: x % 2 == 0, 0)
        [1, 0, 3, 0, 5]
    """
    return [new_value if predicate(item) else item for item in lst]

def remove_by(lst: List[T], predicate: Callable[[T], bool]) -> List[T]:
    """
    移除所有满足条件的元素
    
    参数:
        lst: 输入列表
        predicate: 判断条件的函数
        
    返回:
        移除元素后的新列表
        
    示例:
        >>> remove_by([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
        [1, 3, 5]
    """
    return [item for item in lst if not predicate(item)]

def insert_at(lst: List[T], index: int, item: T) -> List[T]:
    """
    在指定位置插入元素
    
    参数:
        lst: 输入列表
        index: 插入位置（支持负数索引）
        item: 要插入的元素
        
    返回:
        插入元素后的新列表
        
    示例:
        >>> insert_at([1, 2, 3], 1, 4)
        [1, 4, 2, 3]
    """
    result = lst.copy()
    if index < 0:
        index = max(0, len(result) + index)
    result.insert(index, item)
    return result

def move(lst: List[T], from_index: int, to_index: int) -> List[T]:
    """
    移动列表中的元素
    
    参数:
        lst: 输入列表
        from_index: 原位置
        to_index: 目标位置
        
    返回:
        移动元素后的新列表
        
    示例:
        >>> move([1, 2, 3, 4], 1, 3)
        [1, 3, 4, 2]
    """
    result = lst.copy()
    item = result.pop(from_index)
    result.insert(to_index, item)
    return result

def sliding_window_sum(lst: List[Union[int, float]], window_size: int) -> List[Union[int, float]]:
    """
    计算滑动窗口的和
    
    参数:
        lst: 输入数值列表
        window_size: 窗口大小
        
    返回:
        窗口和的列表
        
    示例:
        >>> sliding_window_sum([1, 2, 3, 4, 5], 3)
        [6, 9, 12]
    """
    if len(lst) < window_size:
        return []
    result = []
    current_sum = sum(lst[:window_size])
    result.append(current_sum)
    for i in range(len(lst) - window_size):
        current_sum = current_sum - lst[i] + lst[i + window_size]
        result.append(current_sum)
    return result

def running_total(lst: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    计算累计和
    
    参数:
        lst: 输入数值列表
        
    返回:
        累计和列表
        
    示例:
        >>> running_total([1, 2, 3, 4, 5])
        [1, 3, 6, 10, 15]
    """
    total = 0
    result = []
    for item in lst:
        total += item
        result.append(total)
    return result

def frequencies(lst: List[T]) -> Dict[T, float]:
    """
    计算列表中元素的频率
    
    参数:
        lst: 输入列表
        
    返回:
        元素频率字典
        
    示例:
        >>> frequencies([1, 2, 2, 3, 1, 3, 3])
        {1: 0.286, 2: 0.286, 3: 0.428}
    """
    if not lst:
        return {}
    counts = count_by(lst, lambda x: x)
    total = sum(counts.values())
    return {k: float(Decimal(str(v/total)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            for k, v in counts.items()}

def split_at_indices(lst: List[T], indices: List[int]) -> List[List[T]]:
    """
    在指定索引处拆分列表
    
    参数:
        lst: 输入列表
        indices: 拆分位置的索引列表
        
    返回:
        拆分后的列表的列表
        
    示例:
        >>> split_at_indices([1, 2, 3, 4, 5], [2, 4])
        [[1, 2], [3, 4], [5]]
    """
    if not lst:
        return []
    if not indices:
        return [lst]
    result = []
    start = 0
    for index in sorted(set(indices)):
        if index > start and index <= len(lst):
            result.append(lst[start:index])
            start = index
    if start < len(lst):
        result.append(lst[start:])
    return result

def is_sorted(lst: List[T], key_func: Optional[Callable[[T], Any]] = None, reverse: bool = False) -> bool:
    """
    检查列表是否已排序
    
    参数:
        lst: 输入列表
        key_func: 可选的键函数
        reverse: 是否检查降序排序
        
    返回:
        列表是否已排序
        
    示例:
        >>> is_sorted([1, 2, 3, 4, 5])
        True
        >>> is_sorted([1, 2, 3, 4, 5], reverse=True)
        False
    """
    if len(lst) <= 1:
        return True
    if key_func is None:
        key_func = lambda x: x
    for i in range(len(lst) - 1):
        if reverse:
            if key_func(lst[i]) < key_func(lst[i + 1]):
                return False
        else:
            if key_func(lst[i]) > key_func(lst[i + 1]):
                return False
    return True 

def first(lst: List[T], default: Optional[T] = None) -> Optional[T]:
    """
    获取列表的第一个元素
    
    参数:
        lst: 输入列表
        default: 列表为空时的默认值
        
    返回:
        第一个元素或默认值
        
    示例:
        >>> first([1, 2, 3])
        1
        >>> first([], default=0)
        0
    """
    return lst[0] if lst else default

def last(lst: List[T], default: Optional[T] = None) -> Optional[T]:
    """
    获取列表的最后一个元素
    
    参数:
        lst: 输入列表
        default: 列表为空时的默认值
        
    返回:
        最后一个元素或默认值
        
    示例:
        >>> last([1, 2, 3])
        3
        >>> last([], default=0)
        0
    """
    return lst[-1] if lst else default

def compact(lst: List[Any]) -> List[Any]:
    """
    移除列表中的所有假值（False, None, 0, '', [], {}）
    
    参数:
        lst: 输入列表
        
    返回:
        移除假值后的列表
        
    示例:
        >>> compact([1, None, 2, '', 3, [], False, 4])
        [1, 2, 3, 4]
    """
    return [x for x in lst if x]

def difference(lst1: List[T], lst2: List[T]) -> List[T]:
    """
    返回在第一个列表中但不在第二个列表中的元素
    
    参数:
        lst1: 第一个列表
        lst2: 第二个列表
        
    返回:
        差集列表
        
    示例:
        >>> difference([1, 2, 3, 4], [2, 4])
        [1, 3]
    """
    set2 = set(lst2)
    return [x for x in lst1 if x not in set2]

def intersection(lst1: List[T], lst2: List[T]) -> List[T]:
    """
    返回两个列表的交集，保持第一个列表中的顺序
    
    参数:
        lst1: 第一个列表
        lst2: 第二个列表
        
    返回:
        交集列表
        
    示例:
        >>> intersection([1, 2, 3, 4], [2, 4, 6])
        [2, 4]
    """
    set2 = set(lst2)
    return [x for x in lst1 if x in set2]

def union(*lists: List[T]) -> List[T]:
    """
    返回多个列表的并集，保持元素首次出现的顺序
    
    参数:
        *lists: 输入的多个列表
        
    返回:
        并集列表
        
    示例:
        >>> union([1, 2, 3], [2, 3, 4], [3, 4, 5])
        [1, 2, 3, 4, 5]
    """
    seen = set()
    result = []
    for lst in lists:
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
    return result

def min_by(lst: List[T], key_func: Callable[[T], Any], default: Optional[T] = None) -> Optional[T]:
    """
    根据键函数返回最小的元素
    
    参数:
        lst: 输入列表
        key_func: 用于比较的键函数
        default: 列表为空时的默认值
        
    返回:
        最小元素或默认值
        
    示例:
        >>> min_by([(1, 'a'), (2, 'b'), (0, 'c')], lambda x: x[0])
        (0, 'c')
    """
    if not lst:
        return default
    return min(lst, key=key_func)

def max_by(lst: List[T], key_func: Callable[[T], Any], default: Optional[T] = None) -> Optional[T]:
    """
    根据键函数返回最大的元素
    
    参数:
        lst: 输入列表
        key_func: 用于比较的键函数
        default: 列表为空时的默认值
        
    返回:
        最大元素或默认值
        
    示例:
        >>> max_by([(1, 'a'), (2, 'b'), (0, 'c')], lambda x: x[0])
        (2, 'b')
    """
    if not lst:
        return default
    return max(lst, key=key_func)

def average(lst: List[Union[int, float]], default: Union[int, float] = 0) -> Union[int, float]:
    """
    计算数值列表的平均值
    
    参数:
        lst: 输入数值列表
        default: 列表为空时的默认值
        
    返回:
        平均值或默认值
        
    示例:
        >>> average([1, 2, 3, 4, 5])
        3.0
    """
    return sum(lst) / len(lst) if lst else default

def median(lst: List[Union[int, float]], default: Union[int, float] = 0) -> Union[int, float]:
    """
    计算数值列表的中位数
    
    参数:
        lst: 输入数值列表
        default: 列表为空时的默认值
        
    返回:
        中位数或默认值
        
    示例:
        >>> median([1, 2, 3, 4, 5])
        3.0
        >>> median([1, 2, 3, 4])
        2.5
    """
    if not lst:
        return default
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    return sorted_lst[mid] if n % 2 else (sorted_lst[mid-1] + sorted_lst[mid]) / 2

def mode(lst: List[T], default: Optional[T] = None) -> Optional[T]:
    """
    返回列表中出现次数最多的元素
    
    参数:
        lst: 输入列表
        default: 列表为空时的默认值
        
    返回:
        众数或默认值
        
    示例:
        >>> mode([1, 2, 2, 3, 3, 3, 4])
        3
    """
    if not lst:
        return default
    counts = count_by(lst, lambda x: x)
    return max(counts.items(), key=lambda x: x[1])[0]

def all_equal(lst: List[T]) -> bool:
    """
    检查列表中的所有元素是否相等
    
    参数:
        lst: 输入列表
        
    返回:
        是否所有元素都相等
        
    示例:
        >>> all_equal([1, 1, 1])
        True
        >>> all_equal([1, 2, 1])
        False
    """
    return not lst or lst.count(lst[0]) == len(lst)

def is_palindrome(lst: List[T]) -> bool:
    """
    检查列表是否是回文（正序和倒序相同）
    
    参数:
        lst: 输入列表
        
    返回:
        是否是回文列表
        
    示例:
        >>> is_palindrome([1, 2, 3, 2, 1])
        True
        >>> is_palindrome([1, 2, 3])
        False
    """
    return lst == lst[::-1]

def swap(lst: List[T], i: int, j: int) -> List[T]:
    """
    交换列表中两个位置的元素
    
    参数:
        lst: 输入列表
        i: 第一个位置
        j: 第二个位置
        
    返回:
        交换后的新列表
        
    示例:
        >>> swap([1, 2, 3, 4], 1, 2)
        [1, 3, 2, 4]
    """
    result = lst.copy()
    result[i], result[j] = result[j], result[i]
    return result

def sample(lst: List[T], k: int = 1, seed: Optional[int] = None) -> Union[T, List[T]]:
    """
    从列表中随机采样k个元素
    
    参数:
        lst: 输入列表
        k: 采样数量，默认为1
        seed: 随机种子
        
    返回:
        当k=1时返回单个元素，否则返回列表
        
    示例:
        >>> sample([1, 2, 3, 4, 5], k=3, seed=42)
        [2, 4, 1]
        >>> sample([1, 2, 3], k=1, seed=42)
        2
    """
    if seed is not None:
        random.seed(seed)
    if k == 1:
        return random.choice(lst)
    return random.sample(lst, k)

def split_at(lst: List[T], index: int) -> Tuple[List[T], List[T]]:
    """
    在指定位置将列表分成两部分
    
    参数:
        lst: 输入列表
        index: 分割位置
        
    返回:
        分割后的两个列表组成的元组
        
    示例:
        >>> split_at([1, 2, 3, 4, 5], 2)
        ([1, 2], [3, 4, 5])
    """
    return lst[:index], lst[index:]

def trim(lst: List[T], predicate: Callable[[T], bool]) -> List[T]:
    """
    移除列表首尾满足条件的元素
    
    参数:
        lst: 输入列表
        predicate: 判断条件的函数
        
    返回:
        修剪后的列表
        
    示例:
        >>> trim([0, 0, 1, 2, 3, 0, 0], lambda x: x == 0)
        [1, 2, 3]
    """
    start = 0
    end = len(lst)
    
    while start < end and predicate(lst[start]):
        start += 1
    while start < end and predicate(lst[end - 1]):
        end -= 1
        
    return lst[start:end] 