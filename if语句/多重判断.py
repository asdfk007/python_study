# 年龄<18,童工，不合法；18=<年龄<=60，合法工龄；年龄>60，退休
while True:
    try:
        age = int(input("请输入你的年龄"))
        if age < 18:
            print('不满18，童工，不合法')
        elif age >= 18 and age < 60:
            print('合法工龄')
        else:
            print(f'您的年龄是{age}，您已到退休年龄')
    except Exception:
        print('您输入的年龄不正确请重新输入')
