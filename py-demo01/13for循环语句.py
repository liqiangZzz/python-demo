# 1、 计算1 ~ 100的所有奇数 和

sum = 0  # 定义一个结果

# 语法是：range([开始点]，结束点，[间隔])  口诀：包头不包尾

# 第一种写法
# for n in range(1, 100, 2):
#     sum += n

# 第二种写法
# for n in range(100):
#     if n % 2 != 0:
#         sum += n

# 第三种写法
# n = 0
# while True:
#     n += 1
#     if n > 100: # 超出了循环的范围, 则退出
#         break
#     if n % 2 != 0:
#         sum += n

# 第四种：
# for i in range(100):
#     if i % 2 == 0:    # 意味着当前的n为偶数，不做计算，退出当次循环。继续下一个数字
#         continue
#     sum += i


# 实现99乘法表
# for
for i in range(1, 10):
    for j in range(1, i + 1):
        # 把该行的所有算式输出
        print(f'{j}*{i}={j * i}', end='\t')
    print()



# while
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j}*{i}={j * i}', end='\t')
        j += 1
    i += 1
    print()
