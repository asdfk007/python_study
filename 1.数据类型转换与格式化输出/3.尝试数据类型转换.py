# coding=utf-8

# 给定变量a和b的值
a = '你好'
b = '20'

# 输出a和b
print(a)
print(b)

# 输出变量a和b的数据类型
print('a的数据类型=' + str(type(a)) + 'b的数据类型=' + str(type(b)))

# 将b的数据类型转换为整数类型，并且将转换后的值给变量c
c = int(b)
print(c)    # 输出c
print('c的数据类型为' + str(type(c)))     # 输出c的数据类型

# 将c转换为浮点型数据，并将转换后的值给d
d = float(c)
print(d)    # 输出d
print('d的数据类型为' + str(type(d)))     # 输出d的数据类型

# 将d转换为布尔类型，并将转换后的值给e
e = bool(d)
print(e)    # 输出e
print('e的数据类型为' + str(type(e)))     # 输出e的数据类型

# 定义变量f为一个列表
f = [1, 2, 3, 4]
print(f)    # 输出变量f
print('f的数据类型为' + str(type(f)))

# 将f转换为元组，并将转换后的值给g
g = tuple(f)
print(g)    # 输出g
print('g的数据类型为' + str(type(g)))

# eval函数使用示例，这个函数的作用是识别字符串中的python表达式
expression = "1 + 2"        # 给变量expression赋值
result = eval(expression)   # 使用eval函数评估字符串中的python表达式，并且将结果给变量result
print(result)               # 输出变量result的值
print('result的值为' + str(type(result)))      # 输出变量result的值

# 将一个整数转换为一个unicode字符
x = 20
x = chr(x)
print(x)
print('x的数据类型为' + str(type(x)))

# 将一个整数转换为一个十六进制字符串
x = 20
x = hex(x)
print(x)
print('x的数据类型为' + str(type(x)))

# 将一个整数转换为一个八进制字符串
x = 20
x = oct(x)
print(x)
print('x的数据类型为' + str(type(x)))

# 将一个整数转换为一个二进制字符串
x = 20
x = bin(x)
print(x)
print('x的数据类型为' + str(type(x)))
