# 坐公交如果有钱可以上车，如果没钱就不能上车;上车后如果有空座位就可以坐下，如果没有就要站着
while True:
    try:
        moy = int(input('请输入你现在带的钱'))
        if moy >= 2:
            print('可以上车')
            while True:
                try:
                    seat = int(input('请输入还有多少个座位'))
                    if seat > 0:
                        print(f'现在还有{seat}个座位，有座可以坐下')
                        break
                    if seat < 0:
                        print(f'现在有{seat}个座位，你可以虚空坐下')
                        break
                    else:
                        print('现在没座位你得站着')
                        break
                except ValueError:
                    print('座位不合法。请重新输入')
        else:
            print("穷逼，混")
    except ValueError:
        print("钱不合法，请重新输入")
