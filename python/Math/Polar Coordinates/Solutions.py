# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import polar

a = complex(input())
b = polar(a)

print('\n'.join(map(str,b)))

'''
1+2j
2.23606797749979
1.1071487177940904
'''