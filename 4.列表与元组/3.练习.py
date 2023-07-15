# 将列表中的重复值去掉，思路：新建一个空列表，判断是否有值在空列表中，如果有不追加，如果没有追加
list1 = [1, 1, 2, 3, 4, 4]
empty = []
for i in list1:
    if i not in empty:
        empty.append(i)
print(empty)

# 将两个列表合并
list2 = [1, 2, 3, 4, 5]
list3 = ['a', 'b', 'c', 'd', 'e']
list2.extend(list3)
print(list2)
