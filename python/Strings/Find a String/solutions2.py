
string,sub_string = (input() for _ in range(2))
print(sum(
    [1 for index in range(len(string)-len(sub_string)+1)
     if string[index:index+len(sub_string)] == sub_string ]
         ))
