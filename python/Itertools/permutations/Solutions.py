from itertools import permutations
info = input().split()

l = list(permutations(info[0],int(info[1])))
l.sort()

print(*[''.join(i) for i in l],sep="\n")

# for item in l:
#     print(''.join(item))

'''
HACK 2
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''