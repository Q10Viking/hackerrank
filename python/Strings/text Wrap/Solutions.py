import textwrap

def wrap(string, max_width):
    # a single paragraph in text (a string) so that every line is width characters long at most. 
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

'''
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''