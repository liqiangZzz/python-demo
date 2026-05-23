class Animal:
    # 私有类属性：实际上 Python 会改名为 _Animal__name
    __name = '动物'

    def __init__(self, color):
        # 私有实例属性：实际上 Python 会改名为 _Animal__color
        self.__color = color

    # 私有方法：实际上 Python 会改名为 _Animal__run
    def __run(self):
        # ✅ 类内部访问私有属性，会被解析为 self._Animal__name 和 self._Animal__color
        print(f'{self.__name}跑起来,它的颜色{self.__color}')

    # 普通函数
    def say(self):
        # 内部访问：Python 自动将其替换为 _Animal__name
        Animal.__name = '生物'
        # 重点：这里访问的是 self._Animal__color
        print(self.__color)
        # 调用私有方法：实际上是调用 self._Animal__run()
        self.__run()

    # 公有 setter 方法：操作的是 self._Animal__color
    def set_color(self, new_color):
        self.__color = new_color

    # 公有 getter 方法：返回的是 self._Animal__color
    def get_color(self):
        return self.__color


class Dog(Animal):
    def __init__(self, color):
        # 1. 调用父类初始化：
        #    这行执行后，实例对象里多了一个属性：_Animal__color = 'red'
        super().__init__(color)

        # 2. 子类定义自己的“私有”属性：
        #    由于在 Dog 类里，__color 会被改名为 _Dog__color
        #    这行执行后，实例对象里又多了一个属性：_Dog__color = None
        #    结论：它完全没有覆盖父类的 _Animal__color，两者并存！
        self.__color = None

    pass


# 创建 Dog 实例
# 此时 d 的内部字典 __dict__ 包含：
# {'_Animal__color': 'red', '_Dog__color': None}
d = Dog('red')

# 调用 say() 方法：
# say() 是在 Animal 类里定义的，所以它内部引用的 __color
# 永远指向 _Animal__color。
# 因此输出的是 'red'，而不是 Dog 类里的 None。
d.say()  # 输出：red \n 生物跑起来,它的颜色red

# 通过 Animal 类定义的公有 setter 修改属性：
# 它修改的是 self._Animal__color = "black"
d.set_color("black")

# 再次验证：
# say() 依然访问 _Animal__color，所以拿到了 "black"
d.say()  # 输出：black \n 生物跑起来,它的颜色black

# ⚠️ 危险操作：在类外部直接给实例赋值 __color
# 在类外部赋值时，Python 不会自动触发名称修饰（改名机制）
# 这行代码只是给 d 增加了一个普通的属性，名字就叫 "__color"
# 此时 d 的内部字典包含：
# {'_Animal__color': 'black', '_Dog__color': None, '__color': 'red'}
d.__color = "red"

# 再次验证：
# say() 还是去读 _Animal__color，所以还是 "black"
# 你刚才赋的 "red" 只是一个毫无关系的普通变量
d.say()  # 输出：black \n 生物跑起来,它的颜色black

# 打印对比：
print(f"父类的真正私有变量：{d._Animal__color}")  # 输出：black
print(f"子类的真正私有变量：{d._Dog__color}")  # 输出：None
print(f"刚才外面瞎传的普通变量：{d.__color}")  # 输出：red