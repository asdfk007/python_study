# 局部变量指的是在函数内部的变量

def test():
    a = 100
    print(a)


print(a)        # 这里的a打印回报错，因为他是在函数test()里面定义的