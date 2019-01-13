from datetime import datetime

fmt = "%a %d %b %Y %H:%M:%S %z"
for _ in range(int(input())):
    t1 = datetime.strptime(input(),fmt)
    t2 = datetime.strptime(input(),fmt)
    # t1-t2 return timedelta类型
    print("{:.0f}".format(abs((t1-t2).total_seconds())))

'''
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

25200
88200
'''