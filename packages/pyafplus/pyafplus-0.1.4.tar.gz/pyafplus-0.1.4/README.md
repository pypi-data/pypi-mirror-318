# PyAFPlus

PyAFPlus 是一个 Python 工具集合，提供了多种实用的扩展功能。

## 功能特性

- dictplus: 字典扩展功能
- strplus: 字符串扩展功能
- listplus: 列表扩展功能
- bccmaths: 数学计算功能
- strmaths: 字符串数学计算功能
- progressplus: 高性能进度条功能

## 安装

```bash
pip install pyafplus
```

## 更新

```bash
pip install --upgrade pyafplus
```

## 各种模块的说明

### dictplus
`dictplus` 模块提供了对字典进行各种操作的扩展功能，包括：
- 合并：将两个或多个字典合并为一个。
- 过滤：根据键或值的条件过滤字典。
- 反转：交换字典的键和值。
- 扁平化：将嵌套字典转换为单层字典。
- 还原扁平化：将扁平化字典还原为嵌套字典。
- 深度获取：根据路径获取嵌套字典中的值。
- 深度设置：根据路径设置嵌套字典中的值。
- 深度删除：根据路径删除嵌套字典中的值。
等

### strplus
`strplus` 模块提供了对字符串进行各种操作的扩展功能，包括：
- 大小写转换：将字符串转换为大写或小写。
- 查找子串：查找字符串中所有子串的位置。
- 提取邮箱和URL：从字符串中提取邮箱地址和URL。
- 掩码处理：对字符串进行部分掩码处理。
等

### listplus
`listplus` 模块提供了对列表进行各种操作的扩展功能，包括：
- 分块：将列表分割成固定大小的块。
- 展平：展平嵌套列表。
- 分组：根据键函数对列表元素进行分组。
- 去重：去除列表中的重复元素。
- 滑动窗口：创建滑动窗口。
- 交错合并：交错合并多个列表。
等

### bccmaths
`bccmaths` 模块提供了各种数学常数的高精度值获取功能，包括：
- 圆周率（π）：获取指定精度的圆周率值。
- 自然对数底（e）：获取指定精度的自然对数底值。
- 光速：获取指定精度的光速值。
- 普朗克常数：获取指定精度的普朗克常数值。
等

### strmaths
`strmaths` 模块提供了字符串形式的数学运算功能，包括：
- 加法：对两个字符串形式的数字进行加法运算。
- 乘法：对两个字符串形式的数字进行乘法运算。
- 除法：对两个字符串形式的数字进行除法运算，支持分数和小数模式。

### progressplus
`progressplus` 模块提供了两种进度条实现：
- `ProgressBar`：标准进度条，提供丰富的自定义选项
- `FastProgressBar`：高速进度条，提供基本功能但运行速度更快

#### 标准进度条示例
```python
from progressplus import ProgressBar
import time

# 基本用法
total = 100
bar = ProgressBar(total)
for i in range(total):
    # 做一些工作
    time.sleep(0.1)
    bar.update()

# 自定义选项
bar = ProgressBar(
    total=50,
    prefix='Progress:',
    suffix='Complete',
    decimals=2,
    length=40,
    fill='#',
    empty='-',
    show_time=True,
    show_count=True
)
for i in range(50):
    time.sleep(0.1)
    bar.update()

# 自定义格式化
def custom_format(percent, data):
    return f"Custom: |{data['bar']}| {percent:.1f}% [{data['time']:.1f}s]"

bar = ProgressBar(
    total=100,
    custom_format=True,
    custom_formatter=custom_format
)
for i in range(100):
    time.sleep(0.1)
    bar.update()
```

#### 高速进度条示例
```python
from progressplus import FastProgressBar

# 适用于需要频繁更新的场景
total = 1000000
bar = FastProgressBar(total)
for i in range(total):
    # 高速操作
    bar.update()
```

## 使用示例
提供了各个模块的使用示例，帮助用户快速上手。
### dictplus
```python
from dictplus import DictPlus
# 示例字典
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

# 合并字典
merged = merge(d1, d2)
print(merged)  # 输出: {'a': 1, 'b': 3, 'c': 4}

# 深度合并字典
deep_merged = deep_merge({'a': {'b': 1}}, {'a': {'c': 2}})
print(deep_merged)  # 输出: {'a': {'b': 1, 'c': 2}}

# 按键过滤字典
filtered_by_keys = filter_by_keys({'a': 1, 'b': 2, 'c': 3}, ['a', 'c'])
print(filtered_by_keys)  # 输出: {'a': 1, 'c': 3}

# 按值过滤字典
filtered_by_values = filter_by_values({'a': 1, 'b': 2, 'c': 3}, lambda x: x > 1)
print(filtered_by_values)  # 输出: {'b': 2, 'c': 3}

# 反转字典
inverted = invert({'a': 1, 'b': 2})
print(inverted)  # 输出: {1: 'a', 2: 'b'}

# 扁平化字典
flattened = flatten({'a': {'b': 1, 'c': {'d': 2}}})
print(flattened)  # 输出: {'a.b': 1, 'a.c.d': 2}

# 还原扁平化字典
unflattened = unflatten({'a.b': 1, 'a.c.d': 2})
print(unflattened)  # 输出: {'a': {'b': 1, 'c': {'d': 2}}}

# 根据路径获取嵌套字典中的值
value = deep_get({'a': {'b': {'c': 1}}}, 'a.b.c')
print(value)  # 输出: 1

# 根据路径设置嵌套字典中的值
deep_set({'a': {'b': {}}}, 'a.b.c', 1)
print(deep_set({'a': {'b': {}}}, 'a.b.c', 1))  # 输出: {'a': {'b': {'c': 1}}}

# 根据路径删除嵌套字典中的值
d = {'a': {'b': {'c': 1}}}
deep_delete(d, 'a.b.c')
print(d)  # 输出: {'a': {'b': {}}}

# 查找值对应的键路径
path = find_key_path({'a': {'b': {'c': 1}}}, 1)
print(path)  # 输出: 'a.b.c'

# 比较两个字典的差异
diff_result = diff({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
print(diff_result)  # 输出: ({'a': 1}, {'c': 4}, {'b': (2, 3)})

# 递归比较两个嵌套字典的差异
deep_diff_result = deep_diff({'a': {'b': 1}}, {'a': {'b': 2, 'c': 3}})
print(deep_diff_result)  # 输出: ({}, {'a': {'c': 3}}, {'a': {'b': (1, 2)}})

# 转换字典的所有键
transformed_keys = transform_keys({'a': 1, 'b': 2}, str.upper)
print(transformed_keys)  # 输出: {'A': 1, 'B': 2}

# 转换字典的所有值
transformed_values = transform_values({'a': 1, 'b': 2}, lambda x: x * 2)
print(transformed_values)  # 输出: {'a': 2, 'b': 4}

# 递归转换嵌套字典的所有值
deep_transformed_values = deep_transform_values({'a': 1, 'b': {'c': 2}}, lambda x: x * 2)
print(deep_transformed_values)  # 输出: {'a': 2, 'b': {'c': 4}}

# 从字典中选择指定的键值对
picked = pick({'a': 1, 'b': 2, 'c': 3}, 'a', 'c')
print(picked)  # 输出: {'a': 1, 'c': 3}

# 从字典中排除指定的键值对
omitted = omit({'a': 1, 'b': 2, 'c': 3}, 'b')
print(omitted)  # 输出: {'a': 1, 'c': 3}

# 检查嵌套字典中是否存在指定路径
has_path_result = has_path({'a': {'b': {'c': 1}}}, 'a.b.c')
print(has_path_result)  # 输出: True

```
### strplus
```python
from strplus import StrPlus

# 字符串工具示例

# 分行
lines = split_lines("hello\nworld\ntest")
print(lines)  # 输出: ['hello', 'world', 'test']

# 检查空字符串
is_empty_result = is_empty("")
print(is_empty_result)  # 输出: True

# 反转字符串
reversed_text = reverse("hello")
print(reversed_text)  # 输出: 'olleh'

# 检查回文
is_palindrome_result = is_palindrome("A man a plan a canal Panama", ignore_case=True, ignore_spaces=True)
print(is_palindrome_result)  # 输出: True

# 统计单词出现次数
word_count = count_words("hello world hello", ignore_case=True)
print(word_count)  # 输出: {'hello': 2, 'world': 1}

# 截断文本
truncated_text = truncate("hello world", 8)
print(truncated_text)  # 输出: 'hello...'

# 文本换行
wrapped_text = wrap("hello world", 5)
print(wrapped_text)  # 输出: ['hello', 'world']

# 移除多余的空格
cleaned_text = remove_extra_spaces("hello   world  ")
print(cleaned_text)  # 输出: 'hello world'

# 每个单词首字母大写
capitalized_text = capitalize_words("hello world")
print(capitalized_text)  # 输出: 'Hello World'

# 查找所有子串的位置
positions = find_all("hello hello", "hello")
print(positions)  # 输出: [0, 6]

# 提取邮箱地址
emails = extract_emails("Contact us at: support@example.com or sales@example.com")
print(emails)  # 输出: ['support@example.com', 'sales@example.com']

# 提取URL
urls = extract_urls("Visit https://example.com or http://test.com")
print(urls)  # 输出: ['https://example.com', 'http://test.com']

# 提取数字
numbers = extract_numbers("The price is 12.99 and quantity is 5")
print(numbers)  # 输出: [12.99, 5.0]

# 检查是否是有效数字
is_number_result = is_number("12.34")
print(is_number_result)  # 输出: True

# 计算编辑距离
distance = levenshtein_distance("hello", "hallo")
print(distance)  # 输出: 1

# 计算字符串相似度
similarity_score = similarity("hello", "hallo")
print(similarity_score)  # 输出: 0.8

# 对字符串进行掩码处理
masked_text = mask("1234567890", 4, -4)
print(masked_text)  # 输出: '1234**7890'

# 验证邮箱地址是否有效
is_valid_email_result = is_valid_email("user@example.com")
print(is_valid_email_result)  # 输出: True

# 验证电话号码是否有效
is_valid_phone_result = is_valid_phone("13812345678")
print(is_valid_phone_result)  # 输出: True

# 格式化数字
formatted_number = format_number(1234567.89, precision=2)
print(formatted_number)  # 输出: '1,234,567.89'

# 将文本转换为URL友好的格式
slugified_text = slugify("Hello World!")
print(slugified_text)  # 输出: 'hello-world'

# 提取两个标记之间的所有文本
extracted_texts = extract_between("(1) and (2) and (3)", "(", ")")
print(extracted_texts)  # 输出: ['1', '2', '3']

# 对文本进行自动换行
wrapped_text = word_wrap("A very long text", width=5)
print(wrapped_text)  # 输出: 'A\nvery\nlong\ntext'

```

### listplus


```python
from listplus import ListPlus

# 示例代码

# 创建一个ListPlus对象
lp = ListPlus([1, 2, 3, 4, 5])

# 将列表分割成固定大小的块
chunks = lp.chunk(2)
print(chunks)  # 输出: [[1, 2], [3, 4], [5]]

# 展平嵌套列表
flattened = lp.flatten()
print(flattened)  # 输出: [1, 2, 3, 4, 5]

# 根据键函数对列表元素进行分组
grouped = lp.group_by(lambda x: x % 2)
print(grouped)  # 输出: {1: [1, 3, 5], 0: [2, 4]}

# 去除列表中的重复元素
unique_list = lp.unique()
print(unique_list)  # 输出: [1, 2, 3, 4, 5]

# 根据谓词函数将列表分成两部分
partitioned = lp.partition(lambda x: x % 2 == 0)
print(partitioned)  # 输出: ([2, 4], [1, 3, 5])

# 创建滑动窗口
windows = lp.window(3)
print(windows)  # 输出: [[1, 2, 3], [2, 3, 4], [3, 4, 5]]

# 交错合并多个列表
interleaved = lp.interleave([6, 7, 8])
print(interleaved)  # 输出: [1, 6, 2, 7, 3, 8, 4, 5]

# 旋转列表
rotated = lp.rotate(2)
print(rotated)  # 输出: [4, 5, 1, 2, 3]

# 随机打乱列表
shuffled = lp.shuffle(seed=42)
print(shuffled)  # 输出: [1, 5, 2, 4, 3]

# 统计列表元素出现次数
counted = lp.count_by(lambda x: x)
print(counted)  # 输出: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}

# 查找满足条件的第一个元素的索引
index = lp.find_index(lambda x: x > 3)
print(index)  # 输出: 3

# 获取列表中满足条件的前缀元素
prefix = lp.take_while(lambda x: x < 4)
print(prefix)  # 输出: [1, 2, 3]

# 删除列表中满足条件的前缀元素
trimmed = lp.drop_while(lambda x: x < 4)
print(trimmed)  # 输出: [4, 5]

# 为列表元素添加索引
indexed = lp.zip_with_index()
print(indexed)  # 输出: [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

# 计算多个列表的笛卡尔积
cartesian = lp.cartesian_product([6, 7])
print(cartesian)  # 输出: [(1, 6), (1, 7), (2, 6), (2, 7), (3, 6), (3, 7), (4, 6), (4, 7), (5, 6), (5, 7)]

# 计算列表元素的排列
perms = lp.permutations(2)
print(perms)  # 输出: [(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)]

# 计算列表元素的组合
combs = lp.combinations(2)
print(combs)  # 输出: [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]

# 按键归约列表元素
reduced = lp.reduce_by_key(lambda x, y: x + y)


```

### bccmaths
```python
from bccmaths import *

# bccmaths 示例代码

# 获取指定精度的常数值
pi_10_digits = get_constant_precision(PI, 10)
print(pi_10_digits)  # 输出: 3.1415926535

e_5_digits = get_constant_precision(E, 5)
print(e_5_digits)  # 输出: 2.71828

# 处理科学计数法
speed_of_light = get_constant_precision(SPEED_OF_LIGHT, 10)
print(speed_of_light)  # 输出: 299792458

planck_constant = get_constant_precision(PLANCK, 10)
print(planck_constant)  # 输出: 0.0000000007

# 获取默认精度的常数值
phi_default = get_constant_precision(PHI)
print(phi_default)  # 输出: 1.61803398874989484820458683436563811772030917980576

# 获取天文常数
light_year = get_constant_precision(LIGHT_YEAR, 5)
print(light_year)  # 输出: 9461000000000000

# 获取物理常数
electron_mass = get_constant_precision(ELECTRON_MASS, 15)
print(electron_mass)  # 输出: 0.000000000000000

# 获取对数常数
ln2 = get_constant_precision(LN2, 10)
print(ln2)  # 输出: 0.6931471805

# 获取三角函数常数
pi_2 = get_constant_precision(PI_2, 10)
print(pi_2)  # 输出: 1.5707963267

# 获取其他重要常数
euler_gamma = get_constant_precision(EULER_GAMMA, 10)
print(euler_gamma)  # 输出: 0.5772156649


```

### strmaths
```python
from strmaths import *
from strmaths import mul, div

# strmaths 示例代码

# 乘法示例
result_mul = mul(123.456, 789.012)
print(result_mul)  # 输出: 97407.518432

# 分数模式除法示例
result_div_fraction = div(123.456, 789.012, mode='fraction')
print(result_div_fraction)  # 输出: 10288/65625

# 小数模式除法示例
result_div_decimal, remainder = div(123.456, 789.012, mode='decimal')
print(result_div_decimal)  # 输出: 0.156456
print(remainder)  # 输出: 0.0

```

### progressplus
```python
from progressplus import *

# progressplus 示例代码

# 基本用法
total = 100
bar = ProgressBar(total)
for i in range(total):
    # 做一些工作
    time.sleep(0.1)
    bar.update()

# 自定义选项
bar = ProgressBar(
    total=50,
    prefix='Progress:',
    suffix='Complete',
    decimals=2,
    length=40,
    fill='#',
    empty='-',
    show_time=True,
    show_count=True
)
for i in range(50):
    time.sleep(0.1)
    bar.update()

# 自定义格式化
def custom_format(percent, data):
    return f"Custom: |{data['bar']}| {percent:.1f}% [{data['time']:.1f}s]"

bar = ProgressBar(
    total=100,
    custom_format=True,
    custom_formatter=custom_format
)
for i in range(100):
    time.sleep(0.1)
    bar.update()

```

## 许可证

本项目采用 MIT 许可证。 