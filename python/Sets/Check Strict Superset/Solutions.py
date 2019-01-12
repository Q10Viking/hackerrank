A = set(input().split())
N = list()
for i in range(int(input())):
    N.append(set(input().split()))
print(all([A.issuperset(item) for item in N]))

'''
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
False
'''