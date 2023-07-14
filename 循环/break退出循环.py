# 吃苹果，吃到第三个苹果吃饱了，不吃了

i = 0
while i < 5:
    if i == 3:
        print('吃饱了，不吃了')
        break
    print(f'吃到第{i+1}个')
    i += 1
    