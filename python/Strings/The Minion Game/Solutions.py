def minion_game(string):
    scores = {'Kevin':0,'Stuart':0}
    for i in range(len(string)):
        if string[i] in "AEIOU":
            # Kevin gets score
            scores['Kevin'] += len(string)-i
        else:
            # Stuart gets score
            scores['Stuart'] += len(string)-i

    if scores['Kevin'] < scores['Stuart']:
        print("Stuart"+" "+ str(scores['Stuart']))
    elif scores['Kevin'] > scores['Stuart']:
        print("Kevin"+" "+ str(scores['Kevin']))
    else:
        print("Drawn")
        

if __name__ == "__main__":
    s = input()
    minion_game(s)


'''
BANANA
Stuart 12
'''