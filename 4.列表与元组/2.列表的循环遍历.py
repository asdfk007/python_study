# 列表的循环遍历
name_list = ['Tom', 'Lily', 'Rose']
for i in name_list:
    print(i)

print('==============')

# 使用while循环达到同样效果
i = 0
while i <= len(name_list) - 1:
    print(name_list[i])
    i += 1
