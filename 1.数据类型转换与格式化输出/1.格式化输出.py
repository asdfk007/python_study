# 指定变量
age = 12
name = '小岚'
weight = 50.0
student_id = 1

# 我的名字是小岚
print('我的名字是%s' % name)

# 我的学号是0001号
print('我的学号是%04d' % student_id)

# 我的体重是50.00千克
print('我的体重是%.2f千克' % weight)

# 我的名字是小岚，今年12岁
print('我的名字是%s，今年%d岁了' % (name, age))

# 尝试使用转义符
print('输出内容', end="\n")     # print结束符
print("hello\tworld")       # 制表符\t
print('hello\nworld')       # 换行符\n

# 尝试使用f来进行格式化输出
print(f'我的名字是{name},我今年{age}岁了')

# 尝试使用print结束符，并且尝试使用.format来进行格式化输出
print('我的名字是{},我的年龄是{}' .format(name, age), end='')

# 编写正确的语句输出mlkj i
str = 'abcdefghi jklmnop'
# str[开始位置下标:结束位置下标:步长]
print(str[-4:-10:-1])
name = '人生苦短 我用python'