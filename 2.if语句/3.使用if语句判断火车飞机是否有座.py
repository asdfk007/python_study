# 判断火车是否有座

while True:
    try:
        seat = int(input('请输入还有多少个座位'))
        if bool(seat) == True:
            print('有座')
        else:
            print('无座')
    except Exception:
        print('输入错误请重新输入')