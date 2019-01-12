from itertools import combinations
N = int(input())
s = input().split()
K = int(input())
total,den = 0,0

for item in combinations(s,K):
    total += 1
    den += 'a' in item

print('{:.3f}'.format(den/total))

'''
4
a a c d
2
0.833
'''
