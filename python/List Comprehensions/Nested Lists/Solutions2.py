from decimal import Decimal
from itertools import groupby, islice
from operator import itemgetter

def second_lowest_grade(nsl):
    '''
    print the name(s) of any student(s) having the second lowest grade.
    If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
    '''
    # 排序，未指定key,会进行二次排序
    nsl.sort()
    # 将分数分类
    
    #for key,group in islice(groupby(nsl,key=lambda x: x[0]),1,2):
    # itemgetter获取对应的数据
    for key,group in islice(groupby(nsl,key=itemgetter(0)),1,2):
        for item in group:
            print(item[1])


if __name__ == '__main__':
    names_scores_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names_scores_list.append([score,name])
    second_lowest_grade(names_scores_list)