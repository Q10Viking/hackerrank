num = int(input())
array = input().split()
A = set()
B = set()
for i in array:
    if i not in A:
        A.add(i)
    else:
        B.add(i)
print(''.join(A-B))