def swap_case(s):
    result = ""
    for index in range(len(s)):
        if s[index].islower():
            result += s[index].upper()
        elif s[index].isupper() :
            result += s[index].lower()
        else:
            result += s[index]
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# HackerRank.com presents "Pythonist 2".
# hACKERrANK.COM PRESENTS "pYTHONIST 2".
