# 全局变量与局部变量相对，所有函数都可以调用全局变量

a = 100


def test1():
    print(a)


def test2():
    print(a)


test1()
test2()

x = 1


def test3():
    # 关键字声明x是全局变量
    global x
    x = 10000
    print(x)


test3()
print(x)