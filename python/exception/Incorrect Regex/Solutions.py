import re

for i in range(int(input())):
    try:
        regex = input()
        re.compile(regex)
    except:
        print("False")
        continue
    print("True")

'''
2
.*\+
.*+
True
False
'''