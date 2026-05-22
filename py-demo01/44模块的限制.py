from my_module3 import *

print(my_sum(2))
print(my_multiply(3, 4))

# print(my_subtract(10, 5))  #  NameError: name 'my_subtract' is not defined
# print(_private_func())     #  NameError   不管有 __all__ 或者没有 _private_func 这个都不能执行
