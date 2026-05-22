def my_abs(num):
    """
    该函数，可以返回一个数字的绝对值。
    :param num:  传入的数字，必须是个数字，而且必传。
    :return: 回一个数字的绝对值。
    """

    if num < 0:
        return -num
    else:
        return num


# 在python3.5 之后，可以对函数参数和返回值进行类型声明
def new_abs(num: int) -> int:
    """
    该函数，可以返回一个数字的绝对值。
    :param num:  传入的数字，必须是个数字，而且必传。
    :return: 回一个数字的绝对值。
    """
    if num < 0:
        return -num
    else:
        return num


print(my_abs(-2))
print(new_abs(-2))
