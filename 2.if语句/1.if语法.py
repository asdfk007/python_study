'''
if 条件:
    条件成立执行代码1
    条件成立执行代码2
'''
if True:
    print('条件成立执行的代码1')
    print('条件成立执行的代码2')

# 下方代码没有在if的缩进内
print('3')

# 模拟网吧上网

while True:
    try:
        age = int(input('请输入你的年龄'))
        if age >= 18:
            print('可以上网')
        else:
            print('不可以上网')
    except ValueError as ex:
        print(ex)
        print("输入有问题请重新输入")