# 5.Write a Program has two basic functions :
#       
#     2. To Print Possible Series of Sum Of Consecutive Numbers.
#     For Example : Enter the Number : 15
#     The Next 5 Perfect Squares are :
#     16 25 36 49 64
#     The Consecutive Series Of Sum 15 :
#     1+2+3+4+5
#     4+5+6

from math import ceil, sqrt

def squars(x):
    list = []
    b = ceil(sqrt(x))
    for i in range(b,b+5):
        list.append(i*i)
    return print(list)

def summ(x):
    count = 0
    lst = []
    for i in range(1,x):
        for j in range(i,x):
            count  = count + j
            lst.append(j)

            if (count == x):
                print(f"The Consecutive Series Of Sum {x} :" , lst )
                lst = []
                count = 0
                break
            
            elif(count > x):
                count = 0
                lst = []
                break
            # print(lst)

userInput = int(input("Enter The Number"))
# squars(userInput)
summ(userInput)