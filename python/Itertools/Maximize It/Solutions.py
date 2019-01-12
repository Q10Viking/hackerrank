from itertools import product
K,M = map(int,input().split())

s = -1
N = []
for i in range(K):
    N.append(list(map(int,input().split()))[1:])
# 遍历所有的组合
for l in product(*N):
    s = max(sum(map(lambda x: x**2,l))%M,s)
print(s)

'''
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
30
'''