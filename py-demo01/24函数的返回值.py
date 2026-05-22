def test1():
    print('hello, 执行函数test1')
    return 1
    print('11111')


print(test1())


def test2(x, y):
    x2 = x ** 2
    y2 = y ** 2
    return x2, y2


# 返回一个元组
result = test2(1, 2)

# (1, 4) 被解包赋值给 r1 和 r2
r1, r2 = test2(1, 2)
print(r1, r2)
print(result, type(result))
