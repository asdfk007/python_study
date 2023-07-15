# 列表可以用来存储多个数据
# 列表和字符串，整型一样是一种数据类型
# 使用列表存储多个人的姓名

name_list = ['Tom', 'Lily', 'Rose']

print(name_list[0])
print(name_list[1])
print(name_list[2])

# 查找：index函数
print(name_list.index('Lily'))

# 如果找不到就报错
try:
    print(name_list.index('Lucy'))
except Exception as ex:
    print(ex)

# 统计函数count
print(name_list.count('Rose'))

# len函数获取长度
print(len(name_list))

# 判断函数
print('Tom' in name_list)       # 判断存在返回True
print('小明' in name_list)        # 判断不存在返回False
print('小明' not in name_list)    # 判断不存在返回True

# append函数追加数据
name_list.append('蔡徐坤')
print(name_list)

# extend拆开来追加函数
name_list.extend('李云迪')
print(name_list)

# insert函数插入数据
name_list.insert(4, '马牛逼')
print(name_list)

# del函数删除整个列表
del name_list
try:
    print(name_list)
except Exception as ex:
    print(ex)

# pop函数删除数据
name_list = ['Tom', 'Lily', 'Rose']
name_list.pop(1)
print(name_list)

# remove函数删除找到的第一个数据
name_list = ['Tom', 'Lily', 'Rose', 'Tom']
name_list.remove('Tom')
print(name_list)

