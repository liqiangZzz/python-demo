"""
年龄判断：
1、可以有用户输入一个年龄
2、0~18 ：未成年
3、18~ 60：打工仔
4、60 以后：老年人
"""
age = int(input('请输入你的年龄：\t'))
# if 0 <= age < 18:
if age <= 0:
    print('请输入正确的年龄！')
elif age < 18:
    print(f'你的年龄是{age}， 未成年')
elif age < 60:
    print(f'你的年龄是{age}， 打工仔')
else:
    print(f'你的年龄是{age}， 老年人')
