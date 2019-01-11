n,m= map(int,input().split())

symbol_1 = '-'
symbol_2 = 'WELCOME'
symbol_3 = '.|.'


# 上半
for j in range(1,n,2):
    print((symbol_3*j).center(m,symbol_1))

# 中间welcome

print(symbol_2.center(m,symbol_1))

# 下半
for j in range(n-2,0,-2):
    print((symbol_3*j).center(m,symbol_1))

'''
9 27
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
'''