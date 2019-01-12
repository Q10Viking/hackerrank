# Enter your code here. Read input from STDIN. Print output to STDOUT
line_1 = input()
array = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

# 错误的情况： array中的值有可能都不在A和B
# print(sum([1 if i in A else -1 for i in array]))
print(sum([(i in A)-(i in B) for i in array]))

'''
3 2
1 5 3
3 1
5 7
1
'''