from itertools import groupby

num = input()
l = list(map(int,list(num)))
for k,g in groupby(l):
    print("({0}, {1})".format(len(list(g)),k),end=" ")

'''
1222311
(1, 1) (3, 2) (1, 3) (2, 1)
'''