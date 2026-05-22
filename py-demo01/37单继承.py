class Animal:
    name = '动物'

    @staticmethod
    def say():
        print('动物的叫声')


class Dog(Animal):

    def __init__(self, pet_name):
        self.pet_name = pet_name

    def watch_door(self):
        print(f'{self.pet_name}平时在家看门')


d = Dog('小美')
Dog.say()
d.say()
print(d.name)
print(Dog.name)
d.watch_door()


# 子类的对象 是子类类型，同时也是父类类型
print(type(d))
# isinstance 判断对象，是否是某个类型
print(isinstance(d,Animal))
print(isinstance(d,Dog))

# issubclass 判断类 ，是否是是某个父类的子类
print(issubclass(Animal, Dog))
print(issubclass(Dog, Animal))
print(issubclass(Animal, Animal))
print(issubclass(Dog, object))