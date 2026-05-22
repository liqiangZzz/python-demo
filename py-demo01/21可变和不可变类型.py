# 可变类型
s1 = 'helloworld!'

print(id(s1))
s1 = 'abcefghijk'

print(id(s1))
print('-' * 60)

num = 123
print(id(num))
num = 456
print(id(num))

print('-' * 60)

# 元祖不可变类型
t1 = ('A', 'a', 'b', 'c')
# print(type(t1))
# t1[0] = '123'  # TypeError: 'tuple' object does not support item assignment
# print(type(t1))


# 不可变类型
# list集合
print('-' * 60)
lst = [100, 200, 400]
print(id(lst))
lst.append(500)
lst.pop(1)
print(id(lst))

# set 集合
print('-' * 60)

set1 = {'a', 'b', 'c', 3}
print(id(set1))
set1.add('a')
set1.add(10)
print(type(set1))
print(id(set1))

# 字典
print('-' * 60)
dict1 = {'name': 'lisi', 'age': 12}
print(id(dict1))
dict1['city'] = 'china'
print(id(dict1))
