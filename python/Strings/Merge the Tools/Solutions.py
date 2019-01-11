def merge_the_tools(string, k):
    # your code goes here
    t = [string[i:i+k] for i in range(0,len(string),k)]
    u = ['' for _ in range(len(string)//k)]
    for index in range(len(t)):
        for c in t[index]:
            if c in u[index]:
                continue
            else:
                u[index] += c
    for item in u:
        print(item)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

'''
AABCAAADA
3
AB
CA
AD
'''