"""
GrandSon.__init__(name, age, sex)  # ('张三', 22, '男')
         ↓
    super().__init__(name, age, sex)
         ↓
    ┌─────────────────────────────────────────────┐
    │ Son2.__init__(self, name, sex)              │
    │ 期望：(name, sex)     实际：(name, age, sex)  │
    │ ❌ TypeError: 参数数量不匹配                  │
    └─────────────────────────────────────────────┘
                    ↓ (如果能继续)
    ┌─────────────────────────────────────────────┐
    │ Son1.__init__(self, name, age)              │
    │ 期望：(name, age)     实际：(name, sex)      │
    │ ❌ TypeError: 参数数量不匹配                  │
    └─────────────────────────────────────────────┘
                    ↓ (如果能继续)
    ┌─────────────────────────────────────────────┐
    │ Parent.__init__(self, name)                 │
    │ ✅ 正确                                      │
    └─────────────────────────────────────────────┘


    方案	         能用吗	    原因
    *args	    ❌ 不行	    位置参数会错位，顺序无法保证
    **kwargs	✅ 推荐	    关键字参数按名字匹配，不会错乱

  总结：  多继承必须用 **kwargs，不能用 *args。因为 *args 依赖位置顺序，多继承时顺序很容易乱。
"""


class Parent:
    def __init__(self, name, **kwargs):
        self.name = name
        print('parent的init函数执行了')


class Son1(Parent):
    def __init__(self, age, **kwargs):
        self.age = age
        print('Son1的init函数执行了')
        super().__init__(**kwargs)


class Son2(Parent):

    def __init__(self, sex, **kwargs):
        self.sex = sex
        print('Son2的init函数执行了')
        super().__init__(**kwargs)


class GrandSon(Son2, Son1):  # 多继承

    def __init__(self, name, age, sex, **kwargs):
        print('GrandSon的init函数执行了')
        # ✅ 关键：用关键字参数传递，不要用位置参数！
        super().__init__(name=name, age=age, sex=sex, **kwargs)


print(f'MRO序列是：{GrandSon.__mro__}')
gs = GrandSon(name='张三', age=22, sex='男')
print(f"姓名：{gs.name}，年龄：{gs.age}，性别：{gs.sex}")

"""
多继承的调用链：

GrandSon
    ↓ super().__init__(name='张三', age=22, sex='男')
    ↓
Son2: 需要 sex，从 kwargs 里取 sex='男' ✅
    ↓ super().__init__(**kwargs)  # 传递剩余参数
    ↓
Son1: 需要 age，从 kwargs 里取 age=22 ✅
    ↓
Parent: 需要 name，从 kwargs 里取 name='张三' ✅

如果用 *args：
GrandSon
    ↓ super().__init__('张三', 22, '男')
    ↓
Son2: 第一个参数是 sex，拿到 '张三' ❌ 错位！

"""
