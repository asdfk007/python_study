def testA():
    print('这是testA开始')
    print('这是testA执行的代码')
    print('这是testA结束')


def testB():
    print('这是testB开始')
    testA()
    print('这是testB结束')


testB()


# 计算任意三个数字的和并返回和


def sum3(x, y, z):
    return x + y + z


a = sum3(1, 2, 3)
print(a)