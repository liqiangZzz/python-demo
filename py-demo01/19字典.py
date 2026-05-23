# 创建字典
dict1 = {}  # 空字典
dict2 = {'name': '老李', 'age': 100}
dict3 = dict([('name', 'lisi'), ('city', 'shanghai')])
dict4 = dict(name='lisi', age=100, city='shanghai')

# 新增和修改
dict2['address'] = '泗泾镇'
dict2['age'] = 50

# 删除
# dict2.clear()
# print(dict2.pop('address'))
# del dict2['name']


# 查询
# if 'address' in dict2:
#     print(dict2['address'])

# 创建一个新字典，参数作为字典的键，值默认为 None。
new_dict = dict.fromkeys(['name', 'age'])
new_dict['name'] = '王五'
# print(new_dict)

# 第一个参数：必须是一个可迭代对象（iterable），它的每个元素都会成为字典的键
# 第二个参数：所有键对应的值（默认为 None）
new_dict = dict.fromkeys('name',
                         '20')  # 等价于： dict.fromkeys(['n', 'a', 'm', 'e'], '20'),结果：{'n': '20', 'a': '20', 'm': '20', 'e': '20'}
# print(new_dict)

# 返回对应的值: 区别：
# print(dict2['address'])  # 键不存在时，抛出 KeyError 异常
# print(dict2.get('address'))  # 键不存在时，返回 None（不报错）


# 字典遍历
# 遍历键值对
for k, v in dict2.items():
    print(f'key={k}, value={v}')

# 遍历所有键
for k in dict2.keys():
    print(f'{k}')

# 遍历所有值
for v in dict2.values():
    print(f'{v}')
