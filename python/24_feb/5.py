# 5.Write a function that takes a string as an argument and returns the number of vowels in the string. If the string is empty, the function should raise a ValueError with the message "The string is empty."

def matches(x):
    count = 0
    for i in x:
        for j in vovels:
            if(i == j):
                count += 1
    return count

vovels = ['a','e','i','o','u']
string = input("Enter a string arguments\n")

if (string == ""):
    raise ValueError ("The String is Empty")

a = string.lower()
b = matches(a)
print("Total Nubers of Vovels is",b)
