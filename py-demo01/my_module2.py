# my_module2.py
def my_sum(n):
    """计算 n 的阶乘"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == '__main__':
    print(my_sum(1))