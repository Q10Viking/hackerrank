from itertools import combinations_with_replacement
S,k = input().split()

l = combinations_with_replacement(sorted(S),int(k))
print(*[''.join(i) for i in l],sep='\n')

'''
HACK 2
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
'''