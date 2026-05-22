
class Parent:

    def __init__(self, name):
        self.name = name
        print('parent的init函数被执行了')

    def say_hello(self):
        print(f'{self.name}: hello')
        print('parent的say_hello函数被执行了')


class Son(Parent):

    def __init__(self, name, age):
        # self.name = name
        super().__init__(name)
        self.age = age
        print('son的init函数被执行了')

    def say_hello(self):
        print(f'{self.name}: hello world!')
        print('Son的say_hello函数被执行了')

s1 = Son('张三', 32)
s1.say_hello()