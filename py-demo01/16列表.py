lst = []
lst = [12, 'ab', 12, 3.14, [1, 2]]

# 修改操作
lst[1] = 'abc'

# 查找操作
print(lst.index(12))  # 从左到右第一个 12 的索引 → 0
print(lst.count(12))  # 12 出现的次数 → 2
print(len(lst))  # 列表长度 → 5

# 添加数据的操作
print(lst)
lst.append('hello')  # 末尾追加 'hello'
lst.extend('world')  # 将 'w','o','r','l','d' 逐个追加到末尾
lst.insert(0, 'hello')  # 在索引 0 位置插入 'hello'

print(lst)

# 删除数据操作
lst.pop()  # pop() 不指定参数时，会删除并返回最后一个元素。
print(lst.pop(0))  # 输出: hello（删除索引0的元素，并返回它）
del lst[2]  # 删除索引 2 的元素
lst.remove(12)  # 从左到右第一次出现的 12
print(lst)

# 对列表逆序逆序
lst2 = [4, 9, 98, 32, 2, 12]

# print(lst2[::-1])
lst2.reverse()  # 反转列表顺序
print(lst2)  # 反转列表顺序

lst2.sort(reverse=True)  # 排序
print(lst2)

for i in lst2:
    print(i)
