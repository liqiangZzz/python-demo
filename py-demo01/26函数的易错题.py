def test(item, lst=[1, 2]):
    print(f"lst 的内存地址: {id(lst)}")
    # 把 item 添加到列表中
    if item not in lst:
        lst.append(item)
    return lst



print(f'第一次调用test函数的结果是：{test(10)}')
print(f'第二次调用test函数的结果是：{test(20)}')  #  1, 2, 20 ,正确的是：1， 2，10，20
print(f'第三次调用test函数的结果是：{test(30, lst=[60, 70])}')  # 正确的是：60，70，30
print(f'第四次调用test函数的结果是：{test(40)}')  # 正确的是：  [1, 2, 10, 20, 40]

