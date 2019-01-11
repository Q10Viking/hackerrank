def print_rangoli(size):
    # your code goes here
    a = 97
    b = a+size-1
    cp = (size+(size-1))*2-1

    # 上半部分
    for i in range(size):
        tmp = [chr(j) for j in range(b,b-i-1,-1)]
        tmp.extend([chr(k) for k in range(b-i+1,b+1,1) ])
        print('-'.join(tmp).center(cp,'-'))

    # 下半部分
    for i in range(size -2,-1,-1):
        tmp = [chr(j) for j in range(b,b-i-1,-1)]
        tmp.extend([chr(k) for k in range(b-i+1,b+1,1) ])
        print('-'.join(tmp).center(cp,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


'''
10
------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
'''