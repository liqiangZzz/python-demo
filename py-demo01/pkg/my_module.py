def my_sum(n):
    """计算 1+2+...+n 的和"""
    result = 0
    for i in range(n + 1):
        result += i
    return result

def my_sum2(n):
    return n * 2