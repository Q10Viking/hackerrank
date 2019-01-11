if __name__ == '__main__':
    N = int(input())
    result_list=[]
    for _ in range(N):
        cmd=input().split(' ')
        keyword = cmd[0]
        if keyword == 'insert':
            result_list.insert(int(cmd[1]),int(cmd[2]))
        elif keyword == 'print':
            print(result_list)
        elif keyword == 'remove':
            result_list.remove(int(cmd[1]))
        elif keyword == 'append':
            result_list.append(int(cmd[1]))
        elif keyword == 'sort':
            result_list.sort()
        elif keyword == 'pop':
            result_list.pop()
        elif keyword == 'reverse':
            result_list.reverse()

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]    
        
