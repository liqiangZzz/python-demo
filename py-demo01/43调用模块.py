# 第1步：导入整个模块（安全）
import my_module
print(my_module.my_sum(10))  # 1+2+...+10 = 55  ← 正确

# 第2步：从 my_module 导入所有（此时 my_sum = 求和函数）
from my_module import *

# 第3步：从 my_module2 导入所有（my_sum 被覆盖为阶乘函数）
from my_module2 import *  # ⚠️ 后导入的覆盖了前面的！

# 第4步：调用 my_sum
print(my_sum(5))  # 输出的是 my_module2 的阶乘（120），不是 my_module 的和（15）

