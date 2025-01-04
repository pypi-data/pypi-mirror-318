from typing import Dict, Any, List, Tuple, Callable, Optional, TypeVar, Set, Union
from collections import defaultdict
from copy import deepcopy

K = TypeVar('K')
V = TypeVar('V')

def merge(*dicts: Dict) -> Dict:
    """
    合并多个字典
    
    参数:
        *dicts: 要合并的字典列表
        
    返回:
        合并后的新字典
        
    示例:
        >>> merge({'a': 1}, {'b': 2}, {'c': 3})
        {'a': 1, 'b': 2, 'c': 3}
    """
    result = {}
    for d in dicts:
        result.update(d)
    return result

def deep_merge(*dicts: Dict) -> Dict:
    """
    深度合并多个字典，递归合并嵌套的字典
    
    参数:
        *dicts: 要合并的字典列表
        
    返回:
        深度合并后的新字典
        
    示例:
        >>> deep_merge({'a': {'b': 1}}, {'a': {'c': 2}})
        {'a': {'b': 1, 'c': 2}}
    """
    result = {}
    for d in dicts:
        for k, v in d.items():
            if k in result and isinstance(result[k], dict) and isinstance(v, dict):
                result[k] = deep_merge(result[k], v)
            else:
                result[k] = deepcopy(v)
    return result

def filter_by_keys(d: Dict, keys: List) -> Dict:
    """
    根据键列表过滤字典
    
    参数:
        d: 输入字典
        keys: 要保留的键列表
        
    返回:
        过滤后的新字典
        
    示例:
        >>> filter_by_keys({'a': 1, 'b': 2, 'c': 3}, ['a', 'b'])
        {'a': 1, 'b': 2}
    """
    return {k: v for k, v in d.items() if k in keys}

def filter_by_values(d: Dict, predicate: Callable[[Any], bool]) -> Dict:
    """
    根据值的条件过滤字典
    
    参数:
        d: 输入字典
        predicate: 过滤条件函数
        
    返回:
        过滤后的新字典
        
    示例:
        >>> filter_by_values({'a': 1, 'b': 2, 'c': 3}, lambda x: x > 1)
        {'b': 2, 'c': 3}
    """
    return {k: v for k, v in d.items() if predicate(v)}

def invert(d: Dict) -> Dict:
    """
    反转字典的键值对
    
    参数:
        d: 输入字典
        
    返回:
        反转后的新字典
        
    示例:
        >>> invert({'a': 1, 'b': 2})
        {1: 'a', 2: 'b'}
    """
    return {v: k for k, v in d.items()}

def group_by(items: List[Any], key: Callable[[Any], Any]) -> Dict:
    """
    根据指定的键函数对列表项进行分组
    
    参数:
        items: 输入列表
        key: 分组键函数
        
    返回:
        分组后的字典
        
    示例:
        >>> group_by([1, 2, 3, 4, 5], lambda x: x % 2)
        {0: [2, 4], 1: [1, 3, 5]}
    """
    result = defaultdict(list)
    for item in items:
        result[key(item)].append(item)
    return dict(result)

def flatten(d: Dict, separator: str = '.', prefix: str = '') -> Dict:
    """
    将嵌套字典扁平化为单层字典
    
    参数:
        d: 输入字典
        separator: 键的分隔符
        prefix: 键的前缀
        
    返回:
        扁平化后的字典
        
    示例:
        >>> flatten({'a': {'b': 1, 'c': {'d': 2}}})
        {'a.b': 1, 'a.c.d': 2}
    """
    result = {}
    for k, v in d.items():
        new_key = f"{prefix}{separator}{k}" if prefix else k
        if isinstance(v, dict):
            result.update(flatten(v, separator, new_key))
        else:
            result[new_key] = v
    return result

def unflatten(d: Dict, separator: str = '.') -> Dict:
    """
    将扁平化的字典还原为嵌套字典
    
    参数:
        d: 输入字典
        separator: 键的分隔符
        
    返回:
        嵌套的字典
        
    示例:
        >>> unflatten({'a.b': 1, 'a.c.d': 2})
        {'a': {'b': 1, 'c': {'d': 2}}}
    """
    result = {}
    for k, v in d.items():
        parts = k.split(separator)
        current = result
        for part in parts[:-1]:
            current = current.setdefault(part, {})
        current[parts[-1]] = v
    return result

def deep_get(d: Dict, path: str, default: Any = None, separator: str = '.') -> Any:
    """
    根据路径获取嵌套字典中的值
    
    参数:
        d: 输入字典
        path: 键路径
        default: 默认值
        separator: 路径分隔符
        
    返回:
        找到的值或默认值
        
    示例:
        >>> deep_get({'a': {'b': {'c': 1}}}, 'a.b.c')
        1
    """
    try:
        current = d
        for part in path.split(separator):
            current = current[part]
        return current
    except (KeyError, TypeError):
        return default

def deep_set(d: Dict, path: str, value: Any, separator: str = '.') -> Dict:
    """
    根据路径设置嵌套字典中的值
    
    参数:
        d: 输入字典
        path: 键路径
        value: 要设置的值
        separator: 路径分隔符
        
    返回:
        修改后的字典
        
    示例:
        >>> deep_set({'a': {'b': {}}}, 'a.b.c', 1)
        {'a': {'b': {'c': 1}}}
    """
    parts = path.split(separator)
    current = d
    for part in parts[:-1]:
        if part not in current or not isinstance(current[part], dict):
            current[part] = {}
        current = current[part]
    current[parts[-1]] = value
    return d

def deep_delete(d: Dict, path: str, separator: str = '.') -> bool:
    """
    根据路径删除嵌套字典中的值
    
    参数:
        d: 输入字典
        path: 键路径
        separator: 路径分隔符
        
    返回:
        是否成功删除
        
    示例:
        >>> d = {'a': {'b': {'c': 1}}}
        >>> deep_delete(d, 'a.b.c')
        True
        >>> d
        {'a': {'b': {}}}
    """
    parts = path.split(separator)
    current = d
    try:
        for part in parts[:-1]:
            current = current[part]
        del current[parts[-1]]
        return True
    except (KeyError, TypeError):
        return False

def find_key_path(d: Dict, value: Any, current_path: str = '') -> Optional[str]:
    """
    在嵌套字典中查找值对应的键路径
    
    参数:
        d: 输入字典
        value: 要查找的值
        current_path: 当前路径
        
    返回:
        找到的键路径或None
        
    示例:
        >>> find_key_path({'a': {'b': {'c': 1}}}, 1)
        'a.b.c'
    """
    for k, v in d.items():
        path = f"{current_path}.{k}" if current_path else k
        if v == value:
            return path
        elif isinstance(v, dict):
            result = find_key_path(v, value, path)
            if result:
                return result
    return None

def diff(d1: Dict, d2: Dict) -> Tuple[Dict, Dict, Dict]:
    """
    比较两个字典的差异
    
    参数:
        d1: 第一个字典
        d2: 第二个字典
        
    返回:
        (只在d1中存在的项, 只在d2中存在的项, 值不同的项)
        
    示例:
        >>> diff({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        ({'a': 1}, {'c': 4}, {'b': (2, 3)})
    """
    only_in_d1 = {k: v for k, v in d1.items() if k not in d2}
    only_in_d2 = {k: v for k, v in d2.items() if k not in d1}
    different = {k: (d1[k], d2[k]) for k in set(d1) & set(d2) if d1[k] != d2[k]}
    return only_in_d1, only_in_d2, different

def deep_diff(d1: Dict, d2: Dict) -> Tuple[Dict, Dict, Dict]:
    """
    递归比较两个嵌套字典的差异
    
    参数:
        d1: 第一个字典
        d2: 第二个字典
        
    返回:
        (只在d1中存在的项, 只在d2中存在的项, 值不同的项)
        
    示例:
        >>> deep_diff({'a': {'b': 1}}, {'a': {'b': 2, 'c': 3}})
        ({}, {'a': {'c': 3}}, {'a': {'b': (1, 2)}})
    """
    def _deep_diff(d1: Dict, d2: Dict, path: str = '') -> Tuple[Dict, Dict, Dict]:
        only_in_d1 = {}
        only_in_d2 = {}
        different = {}
        
        all_keys = set(d1) | set(d2)
        for k in all_keys:
            current_path = f"{path}.{k}" if path else k
            if k not in d2:
                only_in_d1[current_path] = d1[k]
            elif k not in d1:
                only_in_d2[current_path] = d2[k]
            elif isinstance(d1[k], dict) and isinstance(d2[k], dict):
                o1, o2, diff = _deep_diff(d1[k], d2[k], current_path)
                only_in_d1.update(o1)
                only_in_d2.update(o2)
                different.update(diff)
            elif d1[k] != d2[k]:
                different[current_path] = (d1[k], d2[k])
                
        return only_in_d1, only_in_d2, different
    
    return _deep_diff(d1, d2)

def transform_keys(d: Dict, transform: Callable[[Any], Any]) -> Dict:
    """
    转换字典的所有键
    
    参数:
        d: 输入字典
        transform: 转换函数
        
    返回:
        转换后的新字典
        
    示例:
        >>> transform_keys({'a': 1, 'b': 2}, str.upper)
        {'A': 1, 'B': 2}
    """
    return {transform(k): v for k, v in d.items()}

def transform_values(d: Dict, transform: Callable[[Any], Any]) -> Dict:
    """
    转换字典的所有值
    
    参数:
        d: 输入字典
        transform: 转换函数
        
    返回:
        转换后的新字典
        
    示例:
        >>> transform_values({'a': 1, 'b': 2}, lambda x: x * 2)
        {'a': 2, 'b': 4}
    """
    return {k: transform(v) for k, v in d.items()}

def deep_transform_values(d: Dict, transform: Callable[[Any], Any]) -> Dict:
    """
    递归转换嵌套字典的所有值
    
    参数:
        d: 输入字典
        transform: 转换函数
        
    返回:
        转换后的新字典
        
    示例:
        >>> deep_transform_values({'a': 1, 'b': {'c': 2}}, lambda x: x * 2)
        {'a': 2, 'b': {'c': 4}}
    """
    result = {}
    for k, v in d.items():
        if isinstance(v, dict):
            result[k] = deep_transform_values(v, transform)
        else:
            result[k] = transform(v)
    return result

def pick(d: Dict, *keys: str) -> Dict:
    """
    从字典中选择指定的键值对
    
    参数:
        d: 输入字典
        *keys: 要选择的键
        
    返回:
        选择后的新字典
        
    示例:
        >>> pick({'a': 1, 'b': 2, 'c': 3}, 'a', 'c')
        {'a': 1, 'c': 3}
    """
    return {k: d[k] for k in keys if k in d}

def omit(d: Dict, *keys: str) -> Dict:
    """
    从字典中排除指定的键值对
    
    参数:
        d: 输入字典
        *keys: 要排除的键
        
    返回:
        排除后的新字典
        
    示例:
        >>> omit({'a': 1, 'b': 2, 'c': 3}, 'b')
        {'a': 1, 'c': 3}
    """
    return {k: v for k, v in d.items() if k not in keys}

def has_path(d: Dict, path: str, separator: str = '.') -> bool:
    """
    检查嵌套字典中是否存在指定路径
    
    参数:
        d: 输入字典
        path: 键路径
        separator: 路径分隔符
        
    返回:
        路径是否存在
        
    示例:
        >>> has_path({'a': {'b': {'c': 1}}}, 'a.b.c')
        True
    """
    try:
        current = d
        for part in path.split(separator):
            current = current[part]
        return True
    except (KeyError, TypeError):
        return False 