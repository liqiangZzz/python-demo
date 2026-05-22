# 使用匿名函数计算两个数字的和
fn = lambda x, y: x + y
print(fn(10, 20))

nums = lambda num, *args: num + sum(args)
print(nums(10, 20, 30, 40))

# 需要给某个复杂的列表排序
lst = [
    {'name': '张三', 'age': 34},
    {'name': '李四', 'age': 16},
    {'name': '王五', 'age': 41}
]

lst.sort(key=lambda x: x['age'])  # key=lambda x: x['age'] 就相当于把整个集合拿过来，自己取 age 的值排序
print(lst)
