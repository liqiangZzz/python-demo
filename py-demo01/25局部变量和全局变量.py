a = 10


def test1():
    b = 100  # 局部变量
    print(a)
    return b ** (1 / 2), a ** 2

print(test1())


def test2():
    # print(a)  #Python 的语法规则规定：只要函数内出现了 global a 声明，那么在 global a 之前就不能出现任何对 a 的操作，哪怕是只读的 print(a) 也不行。
    # print(globals()['a'])  # 强制读取全局 a（不推荐，太啰嗦）
    global a
    a = 20  # 在函数内部， 使用global声明a为全局变量。
    print(a)
    a = 30  # 再次修改
    print(a)  # 30


print(test2())
print(a)