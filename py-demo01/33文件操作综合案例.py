import os


# 给于一个源目录： /Users/Python/project/project-learn/pythod_code
# 需求： 把该目录（目录下面可能还有子目录）中所有.py文件拷贝到另外一个指定的目录中


def copy_dir(source_dir, target_dir):
    """
    拷贝source_dir目录中所有的.py文件，到另外一个目录 target_dir 中
    :param source_dir:  原始目录
    :param target_dir:  目标目录
    :return:   返回一共拷贝的文件数量
    """
    count = 0
    for f in os.listdir(source_dir):
        # 把文件名和目录拼凑成一个完整的绝对路径 （原始目录+循环出来的（文件/目录））
        f_path = os.path.join(source_dir, f)
        if os.path.isfile(f_path) and f.endswith('.py'):  # 表示f是一个普通文件，并且也是py文件
            # 要拷贝该文件

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)  # 目标目录不存在，则创建

            # 拼凑一个拷贝之后的目标文件绝对路线 （目标目录+循环出来的文件）
            sink_path = os.path.join(target_dir, f)
            # 将源文件拷贝文件内容到sink_path（目标文件）中
            num = copy_file(f_path, sink_path)
            count += num
         # 是一个目录
        elif os.path.isdir(f_path):
            # 采用递归函数的写法
            # 跳过特殊目录（可选）
            if f.startswith('.'):  # 跳过隐藏目录
                continue
            # 为了保持同样的目录结构， 目标目录要跟着变化 （目标目录+循环出来的目录）
            new_target_path = os.path.join(target_dir, f)
            # 源文件地址不变，目标位置变动
            copy_dir(f_path, new_target_path)
    return count


def copy_file(source_file, sink_file):
    """
    拷贝单个文件， 把source_file文件内容，拷贝到sink_file中
    :param source_file: 原始文件的绝对路径
    :param sink_file: 目标文件的绝对路线
    :return: 拷贝成功之后返回1
    """
    # 第一种：考虑到文件都是小文件：可以一次性读取全部文件内容，并一次性写入新文件
    # with open(source_file, 'r', encoding='utf8') as source_f:
    #     content = source_f.read()
    #     with open(sink_file, 'w', encoding='utf8') as sink_f:
    #         sink_f.write(content)

    # 第二种: 考虑到文件都比较大，每次从源文件中读取一部分内容，并且写入到新文件（循环多次）
    source_f = open(source_file, mode='r', encoding='utf8')
    sink_f = open(sink_file, mode='w', encoding='utf8')
    while True:
        content = source_f.read(1024 * 10) # 每次读取10KB
        if content == '' or content is None:  # 没有读取到数据
            break  # 意味着文件读完
        sink_f.write(content)
    source_f.close()
    sink_f.close()
    return 1


print(copy_dir(
    r'/Users/Python/project/project-learn/pythod_code/py-demo01',
    r'/Users/Python/project/project-learn/pythod_code/py-demo03'
))

