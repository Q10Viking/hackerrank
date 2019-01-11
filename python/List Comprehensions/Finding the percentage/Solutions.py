if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        # 处理输入
        name, *line = input().split()
        # 字符转数字
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    score = student_marks[query_name]
    print("{:.2f}".format(sum(score)/len(score)))

# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh
# 26.50
