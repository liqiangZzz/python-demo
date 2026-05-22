s1 = 'hello'
s2 = "hello"
s3 = """hello
world"""
s4 = '''hello
world'''

s5 = 'hello\nword'
s6 = 'I\'m Tom'

s7 = '我是"中国"人'
s8 = "我是\"中国\"人"
s9 = '我是\"中国\"人'

# print(s9[0])
# print(s9[4])

# 截取字符串：切片
s = 'abcefghijk'

# print(s[2:6:1])
# print(s[2:6:2])  # 步长就是"跳跃的间隔"
# print(s[-8:-4])  # 从索引-8开始，到索引-4结束（不包含-4）
# print(s[:4])  # 起始索引省略，默认从0开始；结束索引是4（不包含4）
# print(s[3:])  # 起始索引是3，结束索引省略，默认到字符串末尾

# 字符串的倒序
# print(s[::-1])

# 字符串的函数
ss = 'hellopythonpyworld'
# print(ss.find('py'))

#   find('hi')  → 找不到 → -1
#   rfind('hi') → 找不到 → -1
#   index('hi') → 找不到 → 报错
# print(ss.find('hi'))
# print(ss.rfind('hi'))
# print(ss.index('hi'))


# 字符串大小写转换
sss = "hello_Word"
# print(sss.upper())  # upper()：将所有字母转换为大写
# print(sss.lower())  # lower()：将所有字母转换为小写
# print(sss.swapcase())  # swapcase()：大小写互换（大写变小写，小写变大写）
# print(sss.capitalize())  # capitalize()：首字母大写，其余字母小写
# print(sss.title())  # title()：每个单词的首字母大写，其余字母小写

# 字符串切割
ssss = 'I am a student'

# split() 返回值类型:列表（list),切割次数:全部切割（可指定maxsplit）
print(ssss.split())  # split() 默认按空白切割
print(ssss.split(' '))
# partition() 返回值类型:元组（tuple）,切割次数:只切割第一次出现的位置
print(ssss.partition(' '))

# 字符串替换
print(ssss.replace('student','worker'))

#字符串合并