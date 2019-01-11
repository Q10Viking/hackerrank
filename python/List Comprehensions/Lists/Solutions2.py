if __name__ == '__main__':
    N = int(input())
    result_list=[]
    for _ in range(N):
        # *args接受多个参数
        cmd,*args = input().split(' ')
        if cmd != 'print':
            cmd += '('+','.join(args)+')'
            # eval执行字符形式的命令
            eval('result_list.'+cmd)
        else:
            print(result_list)