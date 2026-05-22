# 第一种:导入整个模块，通过"模块名.函数名"调用
# 模块名.函数（对象）
import math

print(math.log2(8))
print(math.log(8, 2))

# 第二种 : 导入所有内容，直接使用函数名（不推荐，容易命名冲突）
from math import *

print(log2(8))
print(log10(100))

# 第三种： 精确导入指定函数，直接使用函数名
from math import log2, log10

print(log2(8))
print(log10(100))

# 第四种：导入整个模块并起别名
import math as m

print(m.log2(8))
print(m.log10(100))

# 第五种:导入指定函数并起别名
from math import log2 as l2, log10 as l10

print(l2(8))
print(l10(100))
