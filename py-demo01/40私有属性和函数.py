class Animal:
    # 私有类属性（双下划线开头）：只能在类内部访问
    # 实际上 Python 会改名为 _Animal__name
    __name = '动物'

    def __init__(self, color):
        # 私有实例属性：只能在类内部访问
        # 实际上 Python 会改名为 _Animal__color
        self.__color = color

    # 私有方法：只能在类内部调用
    # 实际上 Python 会改名为 _Animal__run
    def __run(self):
        # ✅ 类内部可以访问私有属性和私有方法
        print(f'{self.__name}跑起来,它的颜色{self.__color}')

    # 普通函数
    def say(self):
        # 通过类名修改私有类属性（类内部可以访问）
        # self.__color = 'green'
        Animal.__name = '生物'
        print(self.__color)
        # 调用私有方法
        self.__run()

    # 公有 setter 方法：外部通过这个方法修改私有属性
    def set_color(self, new_color):
        self.__color = new_color

    # 公有 getter 方法：外部通过这个方法获取私有属性
    def get_color(self):
        return self.__color


class Dog(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.__color = None

    pass


# 创建 Dog 实例
d = Dog('red')

# 调用公有方法 say()：内部会访问私有属性和私有方法
d.say()  # 输出：red \n 生物跑起来,它的颜色red

# 通过公有 setter 修改私有属性
d.set_color("black")

# 再次调用 say() 验证颜色已修改
d.say()  # 输出：black \n 生物跑起来,它的颜色black

# ❌ 外部直接访问私有属性会报错
# d.__name      # AttributeError: 'Dog' object has no attribute '__name'
# Animal.__name # AttributeError: type object 'Animal' has no attribute '__name'

# ⚠️ 这不是修改私有属性！是创建一个新的普通实例属性
# 真正的私有属性被改名为 _Animal__color，仍然存在且未被修改
d.__color = "red"

# 调用 say() 发现颜色还是 "black"，没有变成 "red"
# 因为 say() 内部访问的是 self.__color（实际是 _Animal__color）
d.say()  # 输出：black \n 生物跑起来,它的颜色black

# 打印的是新创建的普通属性 __color，不是真正的私有属性
# 真正的私有属性需要通过 d._Animal__color 才能访问
print(d._Animal__color)  # 输出：black
print(d.__color)  # 输出：red
