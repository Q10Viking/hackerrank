for i in range(int(input())):
    try:
        a,b = list(map(int, input().split()))
        print(a//b)
    except ZeroDivisionError as e:
        print('Error Code:',e)
    except ValueError as e:
        print('Error Code:',e)

'''
3
1 0
2 $
3 1
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
'''