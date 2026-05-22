import  traceback
class PasswordToShortError(Exception):
    """
     自定义的异常，密码太短了
     """

    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    # 打印异常对象，就会打印str函数的返回值
    def __str__(self):
        return f'你输入的密码长度是{self.length}, 密码不能少于{self.min_len}个字符串'


def input_password():
    pwd = input('请输入你的密码:')
    # 规定密码的长度不能少于6个字符
    if len(pwd) < 6:
        raise PasswordToShortError(pwd, min_len=6)


if __name__ == '__main__':

    try:
        input_password()
    except Exception as e:
        print(e)
        print("="*50)
        print(traceback.format_exc())