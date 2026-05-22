# 计算 1 ～ 100 内所有的奇数和
# sum = 0  # 定义一个结果
# n = 1
# while 1 <= n <= 100:
#     if n % 2 != 0:
#         sum += n
#     n += 1
#
# print(f'结果是:{sum}')


# 2、输出一个 99惩罚表
# 思考99乘法表：有9行

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j}*{i}={j * i}', end='\t')
        j += 1
    i += 1
    print()
