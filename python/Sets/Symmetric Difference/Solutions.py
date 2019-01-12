n = int(input())
N = set(map(int,input().split()))

m = int(input())
M = set(map(int,input().split()))

l = sorted(N.difference(M).union(M.difference(N)))
for item in l:
    print(item)

'''
4
2 4 5 9
4
2 4 11 12
5
9
11
12
'''