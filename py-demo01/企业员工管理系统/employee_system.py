from employee import Employee
import os


class EmployeeManagerSystem:

    def __init__(self):
        # 存放员工数据的文件
        self.employee_data_file = 'employee.data'

        # 上次保存前的员工备份文件，而且只备份一个
        self.employee_data_file_backup = 'employee.data.backup'

        # 文件中加载之后的员工列表
        self.employees = []

        self.save_flag = True  # 已经保存员工数据

    def main(self):
        """员工管理系统的入口"""
        # 1、加载和读取员工数据文件
        self.load_employee()
        while True:
            # 2、显示系统欢迎界面
            self.show_hello()
            # 3、由用户输入指定的功能数字
            menu_number = int(input('请输入你需要的功能编号:'))
            if menu_number == 7:
                break
            elif menu_number == 1:
                self.add_employee()
            elif menu_number == 2:
                self.del_employee()
            elif menu_number == 3:
                self.update_employee()
            elif menu_number == 4:
                self.search_employee()
            elif menu_number == 5:
                self.search_all_employee()
            elif menu_number == 6:
                self.save_employee()

    def go_out(self):
        """
        退出程序的需求： 如果，员工进行了添加，修改，删除。那么必须要保存到文件中
        1、如果没有保存，则在退出之前要自动保存
        2、怎么样：确定没有保存呢？
        :return:
        """
        if not self.save_flag:  # 员工数据没有保存
            self.save_employee()
        print('谢谢！程序退出！')

    def save_employee(self):
        """
        保存的需求和步骤：
        1、先把原来的数据文件备份（如果已经存在备份文件，则把备份文件删除）
        2、创建新文件
        3、写入数据
        4、关闭文件流
        :return:
        """
        if os.path.exists(self.employee_data_file_backup):
            os.remove(self.employee_data_file_backup)  # 删除备份文件

        # 1、备份
        os.rename(self.employee_data_file, self.employee_data_file_backup)

        # 2 、打开文件流
        with open(self.employee_data_file, 'w', encoding='utf-8') as f:
            # 3、写入数据
            new_list = []
            for employee in self.employees:
                new_list.append(employee.__dict__)

            print(new_list)
            print(str(new_list))
            f.write(str(new_list))

    def search_all_employee(self):
        """展示所有的员工信息"""
        print('姓名\t年龄\t性别\t手机号码\t是否离职')
        for emp in self.employees:
            print(emp)

    def search_employee(self):
        """根据姓名，查找员工信息"""
        # 1、输入员工姓名
        search_name = input('请输入要查询的员工姓名:')
        for emp in self.employees:
            if emp.name == search_name:
                print(f'当前查询到的员工信息\t{emp}')
                break
        else:
            print(f'没有找到名字叫{search_name}的员工')

    def update_employee(self):
        """
        修改员工：首先需要输入被修改的员工姓名，然后再依次修改该员工的属性
        :return:
        """
        # 1、输入员工姓名
        update_name = input('请输入要修改的员工姓名:')

        # 2、遍历员工列表，判断是否存在，存在则修改
        for emp in self.employees:
            if emp.name == update_name:
                # 3、修改员工其他属性
                new_name = input('请输入新的姓名(不修改直接回车):').strip()
                emp.name = new_name if new_name else emp.name

                new_sex = input('请输入新的性别(不修改直接回车):').strip()
                emp.sex = new_name if new_sex else emp.sex

                new_age = input('请输入新的年龄(不修改直接回车):').strip()
                emp.age = int(new_age) if new_age else emp.age

                new_number = input('请输入新的手机号码(不修改直接回车):').strip()
                emp.mobile = new_number if new_number else emp.mobile

                new_leave = input('请输入是否离职信息,1表示离职，0表示在职(不修改直接回车):').strip()
                if new_leave:
                    emp.is_leave = True if int(new_leave) == 1 else False

                self.save_flag = False
                print(f'员工的信息已经修改完成：{emp}')
                break
        else:  # 循环正常结束
            print(f'没有找到名字叫{update_name}的员工')

    def del_employee(self):
        """删除员工信息"""
        # 1、 由用户输入你需要删除员工信息
        del_name = input('请输入要删除员工的姓名:')

        for emp in self.employees:
            if emp.name == del_name:
                self.employees.remove(emp)
                self.save_flag = False  # 你完成了一次修改，必须要保存数据
                print(f'名字叫：{del_name}的员工已经删除')
            break
        else:
            print(f'没有找到名字叫{del_name}的员工')

    def add_employee(self):
        """添加员工信息"""
        # 1、 由用户输入你需要添加员工信息
        name = input('请输入员工的姓名:')
        sex = input('请输入员工的性别:')
        age = int(input('请输入员工的年龄:'))
        mobile = input('请输入员工的手机号码:')
        is_leave = int(input('请输入员工是否离职，1表示离职，0表示在职:'))

        new_leave = True if is_leave else False

        emp = Employee(name, age, sex, mobile, new_leave)
        self.employees.append(emp)
        self.save_flag = False  # 你完成了一次修改，必须要保存数据
        print(f'添加 {emp} 员工信息成功')

    @staticmethod
    def show_hello():
        """显示系统的欢迎界面"""
        print('欢迎进入企业员工管理系统')
        print('-' * 60)
        print('1:添加员工')
        print('2:删除员工')
        print('3:修改员工')
        print('4:查找员工')
        print('5:展示所有员工')
        print('6:保存员工数据')
        print('7:退出系统')
        print('-' * 60)

    def load_employee(self):
        """
       读取员工数据文件， 把所有的员工信息都放到一个列表中
       :return:
       """
        f = None
        try:
            f = open(self.employee_data_file, 'r', encoding='utf-8')
        except Exception as err:
            # 如果报错，很有可能第一次启动程序。这个文件还不存在。需要创建一下
            f = open(self.employee_data_file, 'w', encoding='utf-8')
        else:  # 没有报错，意味着文件存在
            # 读取文件中的数据
            data = f.read()
            if data:
                lst = eval(data)  # 把文件的内容（字符串）,当成Python表达式解析。
                for dict1 in lst:
                    self.employees.append(
                        Employee(dict1['name'], dict1['age'], dict1['sex'], dict1['mobile'], dict1['is_leave'], ))
        finally:
            if f:
                f.close()


if __name__ == '__main__':
    emp = EmployeeManagerSystem()
    emp.main()
