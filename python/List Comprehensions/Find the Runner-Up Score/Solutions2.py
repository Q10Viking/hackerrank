if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    winner = max(arr)
    # 有冠军不只有一个
    while max(arr) == winner:
        arr.remove(winner)
    print(max(arr))