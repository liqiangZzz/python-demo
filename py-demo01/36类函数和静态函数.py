print('=' * 50)


class Parent:
    value = '父类的值'


    # 类方法，第一个参数是 cls（类本身），@classmethod 的 cls 参数是 调用时传入的类，不是定义时的类。
    @classmethod
    def class_method(cls):
        print(f'类名：{cls.__name__},类方法: cls.value = {cls.value}')

    # 不传任何特殊参数，可以有普通参数，没有父子关系。
    @staticmethod
    def static_method():
        # 静态方法不知道是哪个类调用的
        print('静态方法: 不知道类信息')

    @staticmethod
    def static_method2(a, b):
        # 没有特殊参数
        # a, b 是调用时传入的普通参数
        print(f'a={a}, b={b}')


class Child(Parent):
    value = '子类的值'



# 通过子类调用
child = Child()

Child.class_method()  # 类名：Child,类方法: cls.value = 子类的值
Child.static_method()  # 静态方法: 不知道类信息（和父类一样）
Child.static_method2(1, 2)
