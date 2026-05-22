# 描述一台车
class Car():

    # super().__new__(cls) 的作用是：创建并返回一个空的实例对象，然后这个空对象会传给 __init__ 进行初始化。
    def __new__(cls, brand, color, price):
        print('创建Car的对象')
        return super().__new__(cls)

    # self：代表当前对象（实例）本身
    def __init__(self, brand, color, price):
        print('开始初始化car对象')
        # brand、color、price 都是 对象属性，成员属性， 实例属性
        self.brand = brand
        self.color = color
        self.price = price

    # 定义__str__ 魔法方法,如果没有定义 __str__ 打印的是内存地址（如 <__main__.Car object at 0x...>）
    def __str__(self):
        # str魔法函数， 当使用 print(对象)、str(对象) 或 f-string 格式化时自动调用
        return f'汽车的品牌是：{self.brand},颜色：{self.color},价格：{self.price}'

    def __del__(self):
        print('开始删除对象')


c = Car('BYD', '白色', '20')

print(c)
# del c   #del c 之后，c 这个名字就没了，后面所有用 c 的代码都会报错。所以如果后面还需要用 c，就不要提前 del
print(c.brand)
print(c.__dict__)
print(vars(c))
