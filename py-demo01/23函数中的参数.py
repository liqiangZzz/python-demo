# 形参

def test1(x, y):
    return x + y


# 必要传参,按照参数顺序传递参数
print(test1(1, 2))

# 关键字传参,函数调用，通过“键=值”形式加以指定
print(test1(y=10, x=20))


# 默认值参数

def test2(x, y, init_num=5):
    init_num += x + y
    return init_num


# init_num 不传使用默认值，传输使用给定的值
print(test2(1, 2, 100))


# 不定长传参
def test3(*args, init_num=5):
    print(type(args))
    return sum(args) + init_num


print(test3())
print(test3(2, 4, 6, 8, init_num=100))


# 不定长关键字参数
def test4(**kwargs):
    print(f"kwargs 的类型: {type(kwargs)}")
    print(f"kwargs 的内容: {kwargs}")


test4(name='张三', age=25, city='北京')

print('*' * 50)


def test5(x, y, init_num=5, *args, **kwargs):
    """
    演示各种参数类型的函数

    参数:
        x, y: 普通位置参数
        init_num: 默认参数（默认值为5）
        *args: 不定长位置参数（元组）
        **kwargs: 不定长关键字参数（字典）
    """
    print("=" * 50)
    print(f"普通参数 x = {x}")
    print(f"普通参数 y = {y}")
    print(f"默认参数 init_num = {init_num}")
    print(f"不定长位置参数 *args = {args}")
    print(f"不定长关键字参数 **kwargs = {kwargs}")

    # 计算演示
    result = x + y + init_num
    print(f"\n基础计算 x + y + init_num = {result}")

    # 如果有 *args，求和
    if args:  # 判断不定长位置参数 *args 是否传入了额外的值。
        args_sum = sum(args)
        print(f"*args 的和 = {args_sum}")
        result += args_sum

    # 如果有 **kwargs，打印出来
    if kwargs:  # 判断是否有额外的关键字参数
        print("**kwargs 的内容:")
        for key, value in kwargs.items():
            print(f"  {key} = {value}")

    print("=" * 50)
    return result


print("\n测试: 传必需参数 + 默认传参 + *args + **kwargs")
test5(1, 2, 200, 100, 200, 300, name='张三', age=25, city='北京')
