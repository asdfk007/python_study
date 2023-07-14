# 使用while嵌套语句生成九九乘法表

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j}*{i}={j*i}', end="\t")
        j += 1
    print()
    i += 1
