name = '张三'
num = 10

# 变量类型
print(type(name))
print(type(num))

num2: float = 9.88
print(type(num2))

num2 = 9.88
print(type(num2))

# Python 是动态类型语言，变量的类型由赋给它的值决定，而不是由标注决定，不报错，有警告
num3: float = 'hello'
print(type(num3))

b01 = True
b02 = False
print(type(b01))

s01 = 'abc'  #  字符串需要使用引号。
s02 = "hello"

print(type(s01))