# 2.  Write python program that accepts a sentence and calculate the number of words, digits, uppercase letters and lowercase letters.

import re

sentence = input("Enter a String\n")
smallLetters = 0
capitalLetters = 0
numbers = 0
word = len(re.findall(r'\w+', sentence))

for i in sentence:
    if (re.search("[a-z]",i)):
        smallLetters += 1 

    elif (re.search("[A-Z]",i)):
        capitalLetters += 1

    elif (re.search("[0-9]",i)):
        numbers += 1

print(f'In the string lower latters are {smallLetters} , capital letters are {capitalLetters} ,numbers are {numbers} and total word are {word} ')
