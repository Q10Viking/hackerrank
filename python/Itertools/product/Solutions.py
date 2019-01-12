from itertools import product
A = map(int,input().split())
B = map(int,input().split())
C = list(product(A,B))
print(*C)

'''
1 2
3 4
(1, 3) (1, 4) (2, 3) (2, 4)
'''