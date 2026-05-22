class Employee:
    """员工类"""

    # is_leave=True表示离职，否则就是在职
    def __init__(self, name, age, sex, mobile, is_leave=False):
        self.name = name
        self.age = age
        self.sex = sex
        self.mobile = mobile
        self.is_leave = is_leave

    def __str__(self):
        return f'{self.name}\t{self.age}\t{self.sex}\t{self.mobile}\t{self.is_leave}'


if __name__ == '__main__':
    e = Employee('张三', 12, '男', '123')
    print(e)
    print(e.__dict__)
    print(vars(e))
