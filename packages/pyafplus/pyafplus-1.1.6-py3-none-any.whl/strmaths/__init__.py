from . import basicSM

def mul(a, b):
    a_str = str(a)
    b_str = str(b)
    
    # 计算小数点后的最大位数
    a_dec_len = len(a_str.split('.')[1]) if '.' in a_str else 0
    b_dec_len = len(b_str.split('.')[1]) if '.' in b_str else 0
    total_dec_len = a_dec_len + b_dec_len
    
    # 将小数转换为整数进行计算
    a_int = int(a_str.replace('.', ''))
    b_int = int(b_str.replace('.', ''))
    
    # 计算乘积
    product = 0
    for _ in range(abs(a_int)):
        product = basicSM.add(product, abs(b_int))
    
    # 处理符号
    if (a < 0) != (b < 0):
        product = -product
    
    # 将结果转换回小数
    product_str = str(product)
    if total_dec_len > 0:
        # 确保结果有足够的位数
        while len(product_str) <= total_dec_len:
            product_str = '0' + product_str
        product_str = product_str[:-total_dec_len] + '.' + product_str[-total_dec_len:]
    
    return product_str

def div(a, b, mode='fraction'):
    if b == 0:
        raise ValueError("除数不能为零")
    
    # 将输入转换为字符串以处理小数
    a_str = str(a)
    b_str = str(b)
    
    # 计算小数点后的最大位数
    a_dec_len = len(a_str.split('.')[1]) if '.' in a_str else 0
    b_dec_len = len(b_str.split('.')[1]) if '.' in b_str else 0
    
    # 将小数转换为整数进行计算
    a_int = int(a_str.replace('.', ''))
    b_int = int(b_str.replace('.', ''))
    
    # 调整数字使其对齐小数点
    if a_dec_len > b_dec_len:
        b_int *= 10 ** (a_dec_len - b_dec_len)
    elif b_dec_len > a_dec_len:
        a_int *= 10 ** (b_dec_len - a_dec_len)
    
    if mode == 'fraction':
        # 计算分数形式的商
        numerator = a_int
        denominator = b_int
        
        # 简化分数
        def gcd(x, y):
            x, y = abs(x), abs(y)
            while y != 0:
                (x, y) = (y, x % y)
            return x
        
        common_divisor = gcd(numerator, denominator)
        numerator //= common_divisor
        denominator //= common_divisor
        
        # 处理负数
        if (a < 0) != (b < 0):
            numerator = -numerator
        
        return f"{numerator}/{denominator}"
    
    elif mode == 'decimal':
        # 为了提高精度，在除法前将被除数扩大
        precision = 10
        a_int *= 10 ** precision
        
        # 计算商和余数
        quotient = a_int // b_int
        remainder = a_int % b_int
        
        # 将商转换为字符串并添加小数点
        quotient_str = str(quotient)
        while len(quotient_str) <= precision:
            quotient_str = '0' + quotient_str
        quotient_str = quotient_str[:-precision] + '.' + quotient_str[-precision:]
        
        # 处理余数
        remainder = remainder / b_int / (10 ** precision)
        
        return quotient_str, remainder

if __name__ == "__main__":
    print(mul(123.456, 789.012))
    print(div(123.456, 789.012, mode='fraction'))
    print(div(123.456, 789.012, mode='decimal'))
