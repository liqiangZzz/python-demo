# 对任意两个数字，整理之后再求和
def sum_num(x, y):
    return abs(x) + abs(y)


print(sum_num(10, 20))


# 高阶函数的实现

def sum_num2(x, y, f):
    """
      :param x: 第一个数字
      :param y: 第二个数字
      :param f: 对数字进行整理的函数
      :return: f(x) + f(y)
      """
    return f(x) + f(y)


# 通过绝对值整理之后再求和
print(sum_num2(2, -6, abs))

# 通过平方整理之后再求和
print(sum_num2(2, -6, lambda n: n ** 2))
# 平方根 ⭐
print(sum_num2(2, -6, lambda n: n ** (1 / 2)))
# 通过立方跟整理之后再求和
print(sum_num2(3, 7, lambda n: n ** (1 / 3)))

print('='*50)

# 支持不同的运算方式（不只是求和）
def combine(x, y, func, combine_func=lambda a, b: a + b):
    """
    :param x: 第一个数字
    :param y: 第二个数字
    :param func: 对每个数字应用的函数
    :param combine_func: 合并两个结果的方式（默认求和）
    :return: combine_func(func(x), func(y))
    """
    return combine_func(func(x), func(y))

# 求和：绝对值相加
print(combine(2, -6, abs))                    # 8

# 求积：平方后相乘
print(combine(2, 3, lambda n: n ** 2, lambda a, b: a * b))  # 4 * 9 = 36

# 求最大值：开平方后取较大值
print(combine(2, 3, lambda n: n ** 0.5, max))  # max(1.414, 1.732) = 1.732
