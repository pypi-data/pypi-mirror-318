from typing import List, Optional, Dict, Tuple, Union, Any
import re
from collections import Counter

def split_lines(text: str, keep_ends: bool = False) -> List[str]:
    """
    将文本按行分割，可选是否保留行尾
    
    参数:
        text: 输入文本
        keep_ends: 是否保留行尾字符
        
    返回:
        行列表
        
    示例:
        >>> split_lines("hello\\nworld")
        ['hello', 'world']
        >>> split_lines("hello\\nworld", keep_ends=True)
        ['hello\\n', 'world']
    """
    return text.splitlines(keep_ends)

def is_empty(text: str, ignore_whitespace: bool = False) -> bool:
    """
    检查字符串是否为空
    
    参数:
        text: 输入文本
        ignore_whitespace: 是否忽略空白字符
        
    返回:
        是否为空
        
    示例:
        >>> is_empty("")
        True
        >>> is_empty("  ", ignore_whitespace=True)
        True
    """
    return not text or (ignore_whitespace and not text.strip())

def reverse(text: str) -> str:
    """
    反转字符串
    
    参数:
        text: 输入文本
        
    返回:
        反转后的文本
        
    示例:
        >>> reverse("hello")
        'olleh'
    """
    return text[::-1]

def is_palindrome(text: str, ignore_case: bool = False, ignore_spaces: bool = False) -> bool:
    """
    检查字符串是否是回文
    
    参数:
        text: 输入文本
        ignore_case: 是否忽略大小写
        ignore_spaces: 是否忽略空格
        
    返回:
        是否是回文
        
    示例:
        >>> is_palindrome("A man a plan a canal Panama", ignore_case=True, ignore_spaces=True)
        True
    """
    if ignore_spaces:
        text = ''.join(text.split())
    if ignore_case:
        text = text.lower()
    return text == text[::-1]

def count_words(text: str, ignore_case: bool = False) -> Dict[str, int]:
    """
    统计单词出现次数
    
    参数:
        text: 输入文本
        ignore_case: 是否忽略大小写
        
    返回:
        单词计数字典
        
    示例:
        >>> count_words("hello world hello")
        {'hello': 2, 'world': 1}
    """
    if ignore_case:
        text = text.lower()
    return dict(Counter(text.split()))

def truncate(text: str, length: int, suffix: str = '...') -> str:
    """
    截断文本到指定长度
    
    参数:
        text: 输入文本
        length: 目标长度
        suffix: 截断后添加的后缀
        
    返回:
        截断后的文本
        
    示例:
        >>> truncate("hello world", 8)
        'hello...'
    """
    if len(text) <= length:
        return text
    return text[:length - len(suffix)] + suffix

def wrap(text: str, width: int, break_long_words: bool = True) -> List[str]:
    """
    将文本按指定宽度换行
    
    参数:
        text: 输入文本
        width: 每行宽度
        break_long_words: 是否打断长单词
        
    返回:
        换行后的文本行列表
        
    示例:
        >>> wrap("hello world", 5)
        ['hello', 'world']
    """
    import textwrap
    return textwrap.wrap(text, width, break_long_words=break_long_words)

def remove_extra_spaces(text: str) -> str:
    """
    移除多余的空格
    
    参数:
        text: 输入文本
        
    返回:
        处理后的文本
        
    示例:
        >>> remove_extra_spaces("hello   world  ")
        'hello world'
    """
    return ' '.join(text.split())

def capitalize_words(text: str) -> str:
    """
    将每个单词首字母大写
    
    参数:
        text: 输入文本
        
    返回:
        处理后的文本
        
    示例:
        >>> capitalize_words("hello world")
        'Hello World'
    """
    return ' '.join(word.capitalize() for word in text.split())

def find_all(text: str, sub: str, ignore_case: bool = False) -> List[int]:
    """
    查找所有子串的位置
    
    参数:
        text: 输入文本
        sub: 要查找的子串
        ignore_case: 是否忽略大小写
        
    返回:
        所有匹配位置的列表
        
    示例:
        >>> find_all("hello hello", "hello")
        [0, 6]
    """
    if ignore_case:
        text = text.lower()
        sub = sub.lower()
    
    positions = []
    start = 0
    while True:
        pos = text.find(sub, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions

def extract_emails(text: str) -> List[str]:
    """
    提取文本中的所有邮箱地址
    
    参数:
        text: 输入文本
        
    返回:
        邮箱地址列表
        
    示例:
        >>> extract_emails("Contact us at: support@example.com or sales@example.com")
        ['support@example.com', 'sales@example.com']
    """
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def extract_urls(text: str) -> List[str]:
    """
    提取文本中的所有URL
    
    参数:
        text: 输入文本
        
    返回:
        URL列表
        
    示例:
        >>> extract_urls("Visit https://example.com or http://test.com")
        ['https://example.com', 'http://test.com']
    """
    pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    return re.findall(pattern, text)

def extract_numbers(text: str) -> List[float]:
    """
    提取文本中的所有数字
    
    参数:
        text: 输入文本
        
    返回:
        数字列表
        
    示例:
        >>> extract_numbers("The price is 12.99 and quantity is 5")
        [12.99, 5.0]
    """
    pattern = r'-?\d*\.?\d+'
    return [float(x) for x in re.findall(pattern, text)]

def is_number(text: str) -> bool:
    """
    检查字符串是否是有效数字
    
    参数:
        text: 输入文本
        
    返回:
        是否是数字
        
    示例:
        >>> is_number("12.34")
        True
        >>> is_number("-12.34e-5")
        True
    """
    try:
        float(text)
        return True
    except ValueError:
        return False

def levenshtein_distance(s1: str, s2: str) -> int:
    """
    计算两个字符串的编辑距离
    
    参数:
        s1: 第一个字符串
        s2: 第二个字符串
        
    返回:
        编辑距离
        
    示例:
        >>> levenshtein_distance("hello", "hallo")
        1
    """
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    
    if not s2:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def similarity(s1: str, s2: str) -> float:
    """
    计算两个字符串的相似度（0-1之间）
    
    参数:
        s1: 第一个字符串
        s2: 第二个字符串
        
    返回:
        相似度
        
    示例:
        >>> similarity("hello", "hallo")
        0.8
    """
    if not s1 and not s2:
        return 1.0
    if not s1 or not s2:
        return 0.0
    distance = levenshtein_distance(s1, s2)
    max_len = max(len(s1), len(s2))
    return 1 - (distance / max_len)

def mask(text: str, start: int = 4, end: int = -4, mask_char: str = '*') -> str:
    """
    对字符串进行掩码处理
    
    参数:
        text: 输入文本
        start: 保留开头的字符数
        end: 保留结尾的字符数（负数表示从后往前数）
        mask_char: 掩码字符
        
    返回:
        掩码后的文本
        
    示例:
        >>> mask("1234567890", 4, -4)
        '1234**7890'
        >>> mask("password", 2, -2)
        'pa***rd'
    """
    text_len = len(text)
    
    # 如果文本长度小于等于开始位置，直接返回原文本
    if text_len <= start:
        return text
        
    # 处理负数结束位置
    actual_end = text_len + end if end < 0 else end
    
    # 确保结束位置在有效范围内
    actual_end = min(text_len, actual_end)
    
    # 如果结束位置小于等于开始位置，返回原文本
    if actual_end <= start:
        return text
    
    # 返回掩码后的文本
    return text[:start] + mask_char * (actual_end - start) + text[actual_end:]

def is_valid_email(email: str) -> bool:
    """
    验证邮箱地址是否有效
    
    参数:
        email: 邮箱地址
        
    返回:
        是否有效
        
    示例:
        >>> is_valid_email("user@example.com")
        True
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_valid_phone(phone: str, country: str = 'CN') -> bool:
    """
    验证电话号码是否有效
    
    参数:
        phone: 电话号码
        country: 国家代码
        
    返回:
        是否有效
        
    示例:
        >>> is_valid_phone("13812345678")
        True
    """
    patterns = {
        'CN': r'^1[3-9]\d{9}$',  # 中国手机号
        'US': r'^\+?1?\d{10}$',  # 美国电话号码
        'UK': r'^\+?44\d{10}$',  # 英国电话号码
    }
    pattern = patterns.get(country, r'^\+?\d{10,}$')
    return bool(re.match(pattern, phone))

def format_number(number: Union[int, float], thousands_sep: str = ',', decimal_sep: str = '.', precision: Optional[int] = None) -> str:
    """
    格式化数字
    
    参数:
        number: 输入数字
        thousands_sep: 千位分隔符
        decimal_sep: 小数点分隔符
        precision: 小数位数
        
    返回:
        格式化后的文本
        
    示例:
        >>> format_number(1234567.89, precision=2)
        '1,234,567.89'
    """
    if precision is not None:
        number = round(number, precision)
    
    parts = str(abs(number)).split('.')
    integer = parts[0]
    decimal = parts[1] if len(parts) > 1 else ''
    
    result = ''
    for i, digit in enumerate(reversed(integer)):
        if i > 0 and i % 3 == 0:
            result = thousands_sep + result
        result = digit + result
    
    if decimal:
        if precision is not None:
            decimal = decimal[:precision].ljust(precision, '0')
        result += decimal_sep + decimal
    
    if number < 0:
        result = '-' + result
    
    return result

def slugify(text: str, separator: str = '-') -> str:
    """
    将文本转换为URL友好的格式
    
    参数:
        text: 输入文本
        separator: 分隔符
        
    返回:
        处理后的文本
        
    示例:
        >>> slugify("Hello World!")
        'hello-world'
    """
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', separator, text).strip(separator)
    return text

def extract_between(text: str, start: str, end: str, include_bounds: bool = False) -> List[str]:
    """
    提取两个标记之间的所有文本
    
    参数:
        text: 输入文本
        start: 开始标记
        end: 结束标记
        include_bounds: 是否包含边界标记
        
    返回:
        匹配文本列表
        
    示例:
        >>> extract_between("(1) and (2) and (3)", "(", ")")
        ['1', '2', '3']
    """
    pattern = f'{re.escape(start)}(.*?){re.escape(end)}'
    matches = re.findall(pattern, text)
    if include_bounds:
        return [f'{start}{m}{end}' for m in matches]
    return matches

def word_wrap(text: str, width: int = 80, indent: str = '', subsequent_indent: str = '') -> str:
    """
    对文本进行自动换行
    
    参数:
        text: 输入文本
        width: 每行宽度
        indent: 首行缩进
        subsequent_indent: 后续行缩进
        
    返回:
        换行后的文本
        
    示例:
        >>> word_wrap("A very long text", width=5)
        'A\\nvery\\nlong\\ntext'
    """
    import textwrap
    return textwrap.fill(text, width, initial_indent=indent, subsequent_indent=subsequent_indent) 