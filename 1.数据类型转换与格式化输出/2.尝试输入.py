password = input('请输入你的密码')     # 输入密码，括号内的是提示词
print(f'您输入的密码是{password}')     # 反馈结果
print(type(password))               # 输出数据类型
password = int(password)            # 将password转化为整型
print(type(password))               # 输出数据的类型
