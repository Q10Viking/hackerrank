from itertools import combinations
S,k = (input().split())
for i in range(1,int(k)+1):
    l=list(combinations(sorted(S),i))
    # l.sort()
    print(*[''.join(j) for j in l],sep="\n")


'''
HACK 2
A
C
H
K
AC
AK
CK
HA
HC
HK
'''