# 计算一个人的BMI

h = float(input('请输入你的身高(单位：米)\t'))
w = float(input('请输入你的体重(单位：千克)\t'))


# 开始计算
bmi = w / h ** 2  # 最终得到一个float
print(f'你的身高是：{h}米，', end='')
print(f'你的体重是：{w}千克，', end='')
print('你的BMI体质指数是：%.2f' % bmi)