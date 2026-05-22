# 第一种
name = '张三'
age = 22
city = 'shanghai'

print('我的名字是%s' % name)
print('我的名字是%s,年龄：%s' % (name, age))
print('我的名字是%s,年龄：%d,我所在的城市是%s' % (name, age, city))

#特殊格式
money= 7890
print('我的金额是: %5d' % money)
print('我的金额是: %d' % money)


# 精确到小数点后一位: 四舍五入
num = 1.71
print("%.1f" % num)

# 精确到小数点后2位：四舍五入,： 正确的66.13
num02 = 66.125
print("%.2f" % num02)


# 精确的四舍五入
from decimal import Decimal

Decimal(num02)
print(Decimal(str(num02)).quantize(Decimal('0.00'), rounding='ROUND_HALF_UP'))




# 第二种格式化
print(f'我的名字是{name},年龄：{age},我所在的城市是{city}')