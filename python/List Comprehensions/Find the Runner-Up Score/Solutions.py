if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    winner,runner_up = -200,-200
    for score in arr:
        if score > winner:
            winner,runner_up = score,winner
        elif ( score>runner_up and score<winner):
            runner_up = score
    print(runner_up)
       
# 5
# 2 3 6 6 5
# 5
