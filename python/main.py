import random
import time
import sys
from functools import reduce

# functions

# minus = lambda x,y : x - y
# a = minus(5,6)
# # print(a)
# a1 = random.randint(0,5)
# print(a1)

# var1 = "chirafg"
# var2 = 45
# print(f"hello{var1} , your roll no{var2}")

# def myFun(**kwargs):
# 	# print("First argument :", arg1)
# 	for arg in kwargs:
# 		print(arg)

# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# def func2(*args):
#     # print(f"Total is {args[0+1+2+3+4+5]} ")
#     # p1 = f"Total is {args} "
#     p1 = args   # tuples
#     print(p1)
#     print(type(p1))
#     # p2 = f"Total is {args[0]} "
#     p2 = args[0]        #list
#     print(p2)
#     print(type(p2))

# x1 = [1,2,3,4,5,6]
# x2 = func2(x1)

# p1 = time.time()
# print(p1)
# print(time.asctime(time.localtime(time.time())))

# print("hello")
# time.sleep(3)
# print("chirag")

    # print(sys.version)
    # print(sys.stdout.write('Geeks'))

    # n1 = ['2','1','7']
    # n2 = []
    # for i in range(len(n1)):
    #     n1[i] = int (n1[i])
    #     n2.append(n1[i])
    # print(n2)
    # print(type(n2))

    # using map function
# n3 = ['1','9','5']
# n4 = list(map(int,n3))
    # print(n4)
    # print(type(n4))


    # reduce function
# l1 = [1,5,6,8,9]
# total = reduce(lambda s,y:s+y,l1)
    # print(total)
    # print(type(total))

# pattern programs: -     
print("hello buddy")

# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# *****
# ****
# ***
# **
# *

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

#     *
#    **
#   ***
#  ****
# *****

# def triangle(n):
# 	k = n - 1
# 	for i in range(0, n):
# 		for j in range(0, k):
# 			print(end=" ")
# 		k = k - 1
# 		for j in range(0, i+1):
# 			print("*", end="")
# 		print()
# n = 5
# triangle(n)


# *****
#  ****
#   ***
#    **
#     *
# pending


# 1
# strr = "python devloper"
# strrr = ""
# print(strr[6:])

# for i in range(len(strr)):
#     if i > 5 :
#         strrr = strrr + strr[i]
# print(strrr)

# 2
# print(strr[::2])

# 3
# string = "Adani Group is an Indian multinational conglomerate, headquartered in Ahmedabad. It was founded by Gautam Adani in 1988 as a commodity trading business, with the flagship company ADANI Enterprises.other subsidiaries are Adani Ports, adani power, ADaNi Wilmar etc."

# lw = string.lower()
# name = "adani"
# pc = lw.count(name)
# print(f"Adani appeared {pc} times.")

# for i in range(pc):
#     st = lw.find(name)
#     end = st + len(name)
#     print (string[st:end])
#     lw = lw[end:]
#     string = string[end:]


# **************** args and kwargs ********************
# def func1(*x):
#     print(x)
#     print(type(x))
    # for i in args :
    #     y = print(i)
    #     print(type(y))

# myList = ["REKHA" , 1,2 , "surekha"] 
# mySet = ("REKHA" , 1,2 , "surekha") 
# myDict = {"teadgjh": 56,"ere":"eqet"}
# show = func1(*myList)
# if we directly send the dta via variable then its a send by a list

# ******************functions*******************
# def func1():
#     print("hello")
# print(func1)
# print(type(func1))
# a = func1
# del func1
# # a()
# print(a)
# print(type(a))

# def func1 (num):
#     if num == 0:
#         return print
#     else:
#         return int
# a = func1(5)
# print(a)

# def outerFuction():
#     def inneerFunction():
#         print("hello ")
#     inneerFunction()
# outerFuction()

# def func2(func1):
#     def func3():
#         print("YOUR INTRO")
#         func1()
#     return func3()

# @func2
# def func1():
#     print("MY SELF CHIRAG VAGHASIYA")

# def func1():
#     print("MY SELF CHIRAG VAGHASIYA")
# a = func2(func1)



# a="chirag \n Vaghasiya"
# # print(a.strip)
# print(a.partition("a"))
# print(a.split("a"))
# b =12
# print('chirag \\n vaghasiya')
# b = a.isalnum()
# print(b)

# a = 10
# b = 10
# c =a
# print(a==b)
# print(b is a)
# print(a is c)

# test = "This pc is not working properly fgdgfgf"
# print(test.find("working"))
# print(test[21:14:-1])

