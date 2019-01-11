def second_lowest_grade(nsl):
    '''
    print the name(s) of any student(s) having the second lowest grade.
    If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
    '''
    scores = list(sorted(set([score for name,score in nsl])))
    second_lowest_score = scores[1]
    # 能够对嵌入的list第一个元素排序
    result = '\n'.join([name for name,score in sorted(nsl) if score == second_lowest_score])
    print(result)


if __name__ == '__main__':
    names_scores_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names_scores_list.append([name,score])
    second_lowest_grade(names_scores_list)

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Berry
# Harry
