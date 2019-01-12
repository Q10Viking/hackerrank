n = int(input())
N = set(map(int,input().split()))

m = int(input())
M = set(map(int,input().split()))

l = sorted(list(N^M))
print('\n'.join(map(str,l)))