
#1 Method capitalize
'''
Upper case the first letter in this sentence:
'''
txt = "hello Q10Viking,hello World"
x = txt.capitalize()
print(x)

# Output: Hello q10viking,hello world

#-----------------------------------------------------

#2 Method casefold
'''
Make the string lower case:
'''
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

# Output: hello, and welcome to my world!

#-----------------------------------------------------

#3 Method center
'''
Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
'''
txt = "banana"
x = txt.center(20)
print(x)


#-----------------------------------------------------

#4 Method count
'''
Return the number of times the value "apple" appears in the string:
'''
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

# Output: 2


#-----------------------------------------------------
#5 Method encode
'''
UTF-8 encode the string:
'''
txt = "My name is 黄壮壮"
x = txt.encode()
print(x)


# Output: b'My name is \xe9\xbb\x84\xe5\xa3\xae\xe5\xa3\xae'


#-----------------------------------------------------
#6 Method: endswith
'''
Check if the string ends with a punctuation sign (.):
'''
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

# Output: True


#-----------------------------------------------------
#7 Method: expandtabs
'''
Set the tab size to 2 whitespaces:
'''
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
# Output: H e l l o




#-----------------------------------------------------
#8 Method: find
'''
Where in the text is the word "welcome"?:
'''
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
# Output: 7 




#-----------------------------------------------------
#9 Method: format
'''
Formats specified values in a string
'''

txt = "hello,my name is {}"
print(txt.format('黄壮壮'))


# Output: hello,my name is 黄壮壮




#-----------------------------------------------------
#10 Method: index 
'''
Where in the text is the word "welcome"?:
'''
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)
# Output: 7 




#-----------------------------------------------------
#11 Method: isalnum
'''
Check if all the characters in the text are alphanumeric:
'''

txt = "Company12"

x = txt.isalnum()

print(x)
# Output: True




#-----------------------------------------------------
#12 Method: isalpha
'''
Check if all the characters in the text are letters:
'''

txt = "CompanyX1"

x = txt.isalpha()

print(x)
# Output: False




#-----------------------------------------------------
#13 Method: isdecimal
'''
Check if all the characters in the unicode object are decimals:
'''

txt = "\u0033" #unicode for 3

x = txt.isdecimal()

print(x)

# Output: True




#-----------------------------------------------------
#14 Method: isdigit
'''
Check if all the characters in the text are digits:

'''

txt = "50800"

x = txt.isdigit()

print(x)
# Output: True




#-----------------------------------------------------
#15 Method: isidentifier
'''
Check if the string is a valid identifier:
'''

txt = "Demo"

x = txt.isidentifier()

print(x)

# Output: True




#-----------------------------------------------------
#16 Method: islower
'''
Check if all the characters in the text are in lower case:
'''

txt = "hello world!"

x = txt.islower()

print(x)

# Output: True



#-----------------------------------------------------
#17 Method: isnumeric
'''
Check if all the characters in the text are numeric:
'''
txt = "565543"

x = txt.isnumeric()

print(x)
# Output: True




#-----------------------------------------------------
#18 Method: isprintable
'''
Check if all the characters in the text are printable:
'''

txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)

# Output: True



#-----------------------------------------------------
#19 Method: isspace
'''
Check if all the characters in the text are whitespaces:
'''

txt = "   "

x = txt.isspace()

print(x)

# Output: True




#-----------------------------------------------------
#20 Method: istitle
'''
Check if each word start with an upper case letter:
'''

txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)


# Output: True




#-----------------------------------------------------
#21 Method: isupper
'''
Check if all the characters in the text are in upper case:
'''

txt = "THIS IS NOW!"

x = txt.isupper()

print(x)


# Output: True




#-----------------------------------------------------
#22 Method: join
'''
Join all items in a tuple into a string, using a hash tag as separator:
'''

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)


# Output: John#Peter#Vicky




#-----------------------------------------------------
#23 Method: ljust
'''
Return a 20 characters long, left justified version of the word "banana":
'''

txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")

# Output: banana               is my favorite fruit.




#-----------------------------------------------------
#24 Method: lower
'''
Lower case the string:

'''

txt = "Hello my FRIENDS"

x = txt.lower()

print(x)


# Output: hello my friends



#-----------------------------------------------------
#25 Method: lstrip
'''
Remove spaces to the left of the string:
'''

txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")

# Output: of all fruits banana      is my favorite




#-----------------------------------------------------
#26 Method: partition
'''
Search for the word "bananas", and return a tuple with three elements:

1 - everything before the "match"
2 - the "match"
3 - everything after the "match"

'''

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)


# Output: ('I could eat ', 'bananas', ' all day')



#-----------------------------------------------------
#27 Method: split
'''
Split a string into a list where each word is a list item:
'''

txt = "welcome to the jungle"

x = txt.split()

print(x)
# Output: ['welcome', 'to', 'the', 'jungle']



#-----------------------------------------------------
#28 Method: upper
'''
Upper case the string:
'''

txt = "Hello my friends"

x = txt.upper()

print(x)


# Output: HELLO MY FRIENDS



#-----------------------------------------------------
#29 Method: 
'''
Make the first letter in each word upper case:
'''

txt = "Welcome to my world"

x = txt.title()

print(x)

# Output: Welcome To My World



#-----------------------------------------------------
#30 Method: startswith
'''
Check if the string starts with "Hello":
'''

txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)

# Output: True

