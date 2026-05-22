# 需求：计算一个正整数n的阶乘

def test(n: int) -> int:
    """
    计算一个数字n的阶乘
    :param n:
    :return:
    """
    if n == 1:
        return 1  # 递归函数退出的出口
    return n * test(n - 1)


print(test(6))
