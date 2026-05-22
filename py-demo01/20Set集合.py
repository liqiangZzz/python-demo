# set1 = set()
set1 = {'a', 'a', 1, 2, 3, 4, 5}
print(set1)
print(type(set1))

# 添加 无序不可重复
set1.add(10)
set1.add('hello')
set1.add('world')
set1.add(5)
print(set1)

# 删除

# 删除元素 - remove() 删除指定元素
set1.remove(5)
# print(f"remove(5)后: {set1}")
# 删除元素 - pop() 随机删除并返回一个元素
removed = set1.pop()
# print(f"随机删除的元素: {removed}")
# print(f"pop()后: {set1}")

# 删除元素 - discard() 删除不存在的元素不会报错
set1.discard(20)  # 元素不存在，什么都不发生
# print(f"discard(20)后: {set1}")

# 清空所有元素
set1.clear()
# print(f"clear()后: {set1}")


set2 = {'hello', (100, 200)}
for e in set2:
    print(e)
