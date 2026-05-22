# map 函数
print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5, 6])))

# reduce函数 -> reduce 会依次累积地应用函数，将序列缩减为单个值。
from functools import reduce

# 有初始值的情况
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6], 10))
# 过程: 10+1=11, 11+2=13, 13+3=16, 16+4=20, 20+5=25, 25+6=31
# 结果: 31

# 没有初始值的情况
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6]))
# 过程: 1+2=3, 3+3=6, 6+4=10, 10+5=15, 15+6=21
# 结果: 21


# 案例： 给你很长的字符串， 统计字符串中每个单词出现的次数
str1 = 'hello world python hello python java hello python flask world'


# str1.split()

# 第一步，把单词切开
# lst = str1.split(' ')
# print(lst)
# 第二部：每个单词只要出现了，那么就代表有一次
# print(list(map(lambda item: {item: 1}, lst)))
# [{'hello': 1}, {'world': 1}, {'python': 1}, .....]


def func(dict1, dict2):
    # 把dict1作为叠加的返回字典
    key = list(dict2.items())[0][0]  # 得到dict2中的key（单词：world）
    value = list(dict2.items())[0][1]  # 得到dict2中的value（1）
    dict1[key] = dict1.get(key, 0) + value
    return dict1


result = reduce(func, map(lambda item: {item: 1}, str1.split()))
print(result)

print('=' * 50)

# filter函数

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 偶数留下
print(list(filter(lambda x: x % 2 == 0, lst1)))
print('=' * 50)

# sorted函数
# 需要给某个复杂的列表排序
lst = [
    {'name': '张三', 'age': 34},
    {'name': '李四', 'age': 16},
    {'name': '王五', 'age': 41}
]

print(sorted(lst, key=lambda x: x['age'],reverse = False))

str_lst = ['hello', 'Java', 'Zoo', 'world']
print(sorted(str_lst, key=str.lower))


# zip 把两个序列中对应位置的元素配对成元组
str_lst = ['hello', 'Java', 'Zoo', 'world']
str_lst2 = ['hello', 'Python', 'Zoo', 'PHP']
zip_lst = zip(str_lst, str_lst2)
print(list(zip_lst))