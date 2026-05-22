class Person:
    species = '人类'  # 物种

    def __init__(self, name, age):
        # 对象属性，成员属性， 实例属性
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}  {self.species}'


p1 = Person('Java', 1)
print(p1.name)

# 访问属性（类属性， 对象属性）
print(p1.species)  # 实例属性（对象属性） 人类 ← 对象没有自己的 species，去类里找
print(Person.species)  # 人类 ← 直接访问类属性

# 修改属性
p1.name = '张三'
print(p1.name)

# 修改类属性只有一种方法
Person.species = '人种'
print(Person.species)
print(p1.species)  # 人种 ← 对象还是去类里找

p1.species = '人科'  # 这不是修改类属性，而是给 p1 创建了一个实例属性！
print(p1)  # 张三 1  人科 ← 打印自己的实例属性
print(Person.species)  # 人种 ← 类属性没变
