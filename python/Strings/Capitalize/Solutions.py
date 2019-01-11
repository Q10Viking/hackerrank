#!/bin/python3
def solve(s):
    result = ""
    need_capicatilize = True
    for c in s:
        if c == ' ':
            need_capicatilize = True
            result += c 
        elif need_capicatilize:
            need_capicatilize = False
            result += c.capitalize()
        else:
            result += c 
    return result


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)

'''
hello   world  lol
Hello   World  Lol
'''