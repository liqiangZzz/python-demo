#   符号	     含义	             记忆法
# *args  	接收位置参数（元组）	一个星号 → 收一堆值 → 元组
# **kwargs	接收关键字参数（字典）	两个星号 → 收键值对 → 字典

t1 = ()  # 创建空元组
t1 = ('abc')
print(t1)
t1 = ('abc',)  # 创建单元素元组，注意逗号不能省略，否则就是字符串 'abc' 而不是元组
print(t1)
t1 = 'abc', 12, 13  # 使用逗号创建元组（省略括号的写法）,不推荐使用
print(t1)
t1 = ('abc', 12, 3.14, 13, [1, 2])
print(t1)

# 下标访问
print(t1[1])
# 切片（截取子元组）
print(t1[0:3])
# 切片（反转）
print(t1[::-1])

print('-' * 50)

# index() 函数：返回指定数据的索引
t = ('a', 'b', 'c', 'b', 'd', 'b')

# 查找第一个匹配项的索引
print(t.index('b'))  # 输出: 1（第一个 'b' 在索引 1）

# 指定查找范围：从索引 2 到末尾
print(t.index('b', 2))  # 输出: 3（跳过索引1，找到索引3的 'b'）

# 指定查找范围：从索引 2 到索引 5（不包含5）
print(t.index('b', 2, 5))  # 输出: 3

# 如果元素不存在，会报错
# print(t.index('z'))   # ValueError: tuple.index(x): x not in tuple

print('-' * 50)
# count() 函数：统计指定数据出现的次数
t = ('a', 'b', 'c', 'b', 'd', 'b')

print(t.count('b'))  # 输出: 3
print(t.count('a'))  # 输出: 1
print(t.count('z'))  # 输出: 0（不存在返回0，不报错）

print('-' * 50)

# len() 函数：获取元组长度
t = ('a', 'b', 'c', 'd', 'e')

print(len(t))  # 输出: 5

# 空元组
empty = ()
print(len(empty))  # 输出: 0

# 嵌套元组（只计算外层元素个数）
nested = (1, 2, (3, 4, 5), 6)
print(len(nested))  # 输出: 4（外层有4个元素）
