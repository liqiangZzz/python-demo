# 创建（打开）文件流
f = open('test.txt', mode='r', encoding='utf-8')

# 读操作
# print(f.read())
#
# print(f.readline())
# print(f.readline())

# print(f.readlines())

f.close()


# 写操作
#
# wf =open('test2.txt', mode='w', encoding='utf-8')
#
# #往文件中写入三个hello
# for i in range(3):
#     wf.write('hello\n')
# wf.close()


# 指针的移动操作
# 需求：在第一个hello的后面添加一个：world
wf = open('test2.txt', mode='r+', encoding='utf-8')
# 把指针移动到第一个hello 的后面
wf.seek(5,0)
# # 把第一个Hello后面的内容先读取出来。
after = wf.read() # 读完之后，指针又到了文件的末尾

# # 把指针移动到第一个hello的后面
wf.seek(5, 0)
wf.write("world"+after)
wf.close()


# with语句来操作文件流
with open('test3.txt', mode='w', encoding='utf-8') as f:
    for i in range(5):
        f.write('hello world\n')