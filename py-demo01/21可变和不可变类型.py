# 不可变类型示例 - 字符串
s1 = 'helloworld!'
print(id(s1))
s1 = 'abcefghijk'
print(id(s1))
print('-' * 60)

# 不可变类型示例 - 数字
num = 123
print(id(num))
num = 456
print(id(num))
print('-' * 60)

# 不可变类型示例 - 元组（被注释的演示）
t1 = ('A', 'a', 'b', 'c')
# t1[0] = '123'  # 取消注释会报错：元组不支持元素赋值
# print(type(t1))

# 可变类型示例 - 列表
print('-' * 60)
lst = [100, 200, 400]
print(id(lst))
lst.append(500)
lst.pop(1)
print(id(lst))

# 可变类型示例 - 集合
print('-' * 60)
set1 = {'a', 'b', 'c', 3}
print(id(set1))
set1.add('a')      # 重复添加，集合无变化
set1.add(10)
print(type(set1))
print(id(set1))

# 可变类型示例 - 字典
print('-' * 60)
dict1 = {'name': 'lisi', 'age': 12}
print(id(dict1))
dict1['city'] = 'china'
print(id(dict1))