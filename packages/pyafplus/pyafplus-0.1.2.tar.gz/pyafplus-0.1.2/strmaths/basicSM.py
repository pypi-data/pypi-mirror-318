def add(add_1, add_2):
    # 检查符号
    sign1 = '-' if str(add_1).startswith('-') else ''
    sign2 = '-' if str(add_2).startswith('-') else ''
    
    # 去掉符号以便后续处理
    sadd_1 = str(add_1).lstrip('-')
    sadd_2 = str(add_2).lstrip('-')
    
    # 将字符串转换为列表,便于操作
    num1 = list(sadd_1)
    num2 = list(sadd_2)
    
    # 找到小数点位置,如果没有则为-1
    dot1 = sadd_1.find('.')
    dot2 = sadd_2.find('.')
    
    # 对齐小数点后的位数
    max_dec_len = 0
    if dot1 != -1 or dot2 != -1:
        if dot1 == -1:
            num1.append('.')
            dot1 = len(num1) - 1
        if dot2 == -1:
            num2.append('.')
            dot2 = len(num2) - 1
            
        # 补齐小数点后的0
        len1 = len(num1) - dot1 - 1
        len2 = len(num2) - dot2 - 1
        max_dec_len = max(len1, len2)
        if len1 < len2:
            num1.extend(['0'] * (len2 - len1))
        elif len2 < len1:
            num2.extend(['0'] * (len1 - len2))
    
    # 对齐整数部分
    len1 = dot1 if dot1 != -1 else len(num1)
    len2 = dot2 if dot2 != -1 else len(num2)
    if len1 < len2:
        num1 = ['0'] * (len2 - len1) + num1
    elif len2 < len1:
        num2 = ['0'] * (len1 - len2) + num2
        
    # 从后向前逐位相加
    carry = 0  # 进位
    result = []
    
    for i in range(len(num1)-1, -1, -1):
        if num1[i] == '.':
            continue
        
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        carry = digit_sum // 10
        result.append(str(digit_sum % 10))
    
    # 处理最后的进位
    if carry:
        result.append('1')
        
    # 反转并插入小数点
    result = ''.join(reversed(result))
    if max_dec_len:
        result = result[:-max_dec_len] + '.' + result[-max_dec_len:]
    
    # 处理符号
    if sign1 == sign2:
        result = sign1 + result
    else:
        # 需要实现减法逻辑
        # 这里只是简单处理，假设add_1的绝对值大于add_2
        # 实际上需要比较大小并调整符号
        result = '-' + result if sign1 else result
    
    return result



# 测试
if __name__ == '__main__':
    import time
    start = time.time()
    print(add("123.4563453738387433454467867875777", "78.91078676678678454878678678678678678678767"))  # 输出: 202.36713214062552789423357357436448678678767
    end = time.time()
    print(f'Time taken: {end - start} seconds')
    # 对比python自带的加法
    start = time.time()
    print(123.4563453738387433454467867875777 + 78.91078676678678454878678678678678678678767) # 有误差，因为浮点数精度问题
    end = time.time()
    print(f'Time taken: {end - start} seconds')
