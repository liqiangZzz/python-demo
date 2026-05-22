
# 定义 __all__ 限制 from my_module3 import * 能导入的内容
__all__ = ['my_sum', 'my_multiply']  # 只允许导入这两个函数

def my_sum(n):
    """求和"""
    return n * (n + 1) // 2

def my_multiply(a, b):
    """乘法"""
    return a * b

def my_subtract(a, b):
    """减法 - 不会被导入"""
    return a - b

# 以下划线开头的私有函数，通常也不被导入
def _private_func():
    return "我是私有的"