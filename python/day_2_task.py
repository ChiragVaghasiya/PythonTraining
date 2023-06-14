# 1. Write a program that asks users to enter their percentage mark for a module of study.  The program prints the module grade as either A, B, C, D, E or F depending on the percentage mark entered.
# Like You can take 4 subject as static. User add marks of subject in any format like 75 or seventy five, count percentage on that basis and applied followed condition.
#     • A mark of 80% and above is awarded an A.
#     • A mark in the range of 70% through to 79% is awarded a B.
#     • A mark in the range of 60% through to 69% is awarded a C.
#     • A mark in the range of 50% through to 59% is awarded a D.
#     • A mark in the range of 40% through to 49% is awarded a E.
#     • Marks less than 40% are awarded an F.
# And output look like  Grade :A, Total=370, Percentage=92.5

# subMark1 = input("enter the first subject mark")
# subMark2 = input("enter the second subject mark")
# subMark3 = input("enter the third subject mark")
# subMark4 = input("enter the forth subject mark")
# check = True
# grade = ""


# def text_to_int(a):
#     data = {'zero' : 0, 'one' : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9, "ten" : 10, "eleven" : 11, "twelve" : 12, "thirteen" : 13, "fourteen" : 14, "feefteen" : 15, "sixteen" : 16, "seventeen" : 17, "eighteen" : 18, "ninteen" : 19, "twenty" : 20, "thirty" : 30,"fourty" : 40, "fifty" : 50, "sixty" : 60, "seventy" : 70, "eighty" : 80, "ninty":90, "hundred" : 100, "thousand" : 1000, "million" : 1000000, "billion" : 1000000000, "trillion" : 1000000000000}
#     amount = a
#     arr = []
#     counter = 0
#     newString = amount.split()
#     for i in range (len(newString)):
#         for key in data:
#             if key == newString[i]:
#                 arr.append(data[key])
#     if arr[len(arr)-1] == "hundred" or "thousand" or "million" or "billion" or "trillion":
#         if len(arr) == 1: 
#             counter += arr[0]
#             # print(counter)
#         elif len(arr) == 2:
#             counter += arr[0]+arr[1]
#             # print(counter)  
#         elif len(arr) == 3:
#             counter += arr[0]*arr[1]  +arr[2]
#             # print(counter)  
#         elif len(arr) == 4:
#             counter += arr[0]*arr[1] + arr[2]*arr[3]
#             # print(counter)  
#         elif len(arr) == 5:
#             counter += arr[0]*arr[1] + arr[2]*arr[3]+ arr[4]
#             # print(counter)  
#         elif len(arr) == 6:
#             counter += arr[0]*arr[1] + arr[2]*arr[3] + arr[4]*arr[5]
#             # print(counter)  
#         elif len(arr) == 7:
#             counter += arr[0]*arr[1] + arr[2]*arr[3] + arr[4]*arr[5] + arr[6]
#             # print(counter)  
#         elif len(arr) == 8:
#             counter += arr[0]*arr[1] + arr[2]*arr[3] + arr[4]*arr[5] + arr[6]*arr[7]
#             # print(counter)    
#     else :
#         if len(arr) == 1: 
#             counter += arr[0]
#             # print(counter)  
#         elif len(arr) == 2:
#             counter += arr[0]+arr[1]
#             # print(counter)  
#         elif len(arr) == 3:
#             counter += arr[0]*arr[1]+arr[2]
#             # print(counter)  
#         elif len(arr) == 4:
#             counter += arr[0]*arr[1]+arr[2]+arr[3]
#             # print(counter)  
#         elif len(arr) == 5:
#             counter += arr[0]*arr[1]+arr[2]*arr[3]+arr[4]
#             # print(counter)  
#         elif len(arr) == 6:
#             counter += arr[0]*arr[1]+arr[2]*arr[3]+arr[4]+arr[5]
#             # print(counter)  
#         elif len(arr) == 7:
#             counter += arr[0]*arr[1]+arr[2]*arr[3]+arr[4]*arr[5]+arr[6]
#             # print(counter)  
#         elif len(arr) == 8:
#             counter += arr[0]*arr[1]+arr[2]*arr[3]+arr[4]*arr[5]+arr[6]+arr[7]
#             # print(counter)
#     return counter

# def persentCount():
#    persentage = (subMark1+subMark2+subMark3+subMark4)/4
#    return persentage

# def totalMark():
#    total = subMark1+subMark2+subMark3+subMark4
#    return total

# if (subMark1.isdigit()==True):
#    subMark1=int(subMark1)
#    subMark2=int(subMark2)
#    subMark3=int(subMark3)
#    subMark4=int(subMark4)

#    persentagee = persentCount()
#    totall = totalMark()

#    if(persentagee>79):
#       grade = "A"
#    elif(persentagee>69 and persentagee<80):
#       grade = "B"
#    elif(persentagee>59 and persentagee<70):
#       grade = "C"
#    elif(persentagee>49 and persentagee<60):
#       grade = "D"
#    elif(persentagee>39 and persentagee<50):
#       grade = "E"
#    elif(persentagee<40):
#       grade = "F"


#    print(f"Grade : {grade} , TOtal : {totall} , Persentage :{persentagee} ")

# else:
#    subMark1 = text_to_int(subMark1)
#    subMark2 = text_to_int(subMark2)
#    subMark3 = text_to_int(subMark3)
#    subMark4 = text_to_int(subMark4)
#    print(subMark1)
#    print(subMark2)
#    print(subMark3)
#    print(subMark4)
#    persentagee = persentCount()
#    totall = totalMark()

#    if(persentagee>79):
#       grade = "A"
#    elif(persentagee>69 and persentagee<80):
#       grade = "B"
#    elif(persentagee>59 and persentagee<70):
#       grade = "C"
#    elif(persentagee>49 and persentagee<60):
#       grade = "D"
#    elif(persentagee>39 and persentagee<50):
#       grade = "E"
#    elif(persentagee<40):
#       grade = "F"


#    print(f"Grade : {grade} , TOtal : {totall} , Persentage :{persentagee} ")









# 2.Write a program to display only those numbers from a list that satisfy the following conditions
#     • Note:- Generate List Dynamic by User input(single input) Split by Space or comma.
#     • The number must be divisible by five
#     • If the number is greater than 150, then skip it and move to the next number
#     • If the number is greater than 500, then stop the loop

# import re
# userInput = input("Enter The List")
# lst = []
# c  = re.split(r",| ",userInput)
# print(c)

# for i in c:
#    i = int(i)
#    if (i > 500):
#       break
#    elif(i>150):
#       continue
#    elif(i%5 == 0):
#       lst.append(i)
# print(lst)






# 3.Print list in reverse order with list values.
#     • Like Data= [50,40,'Clay','Jessica',89]
#     • Output = [98,'Acissej','Yalc',04,05]

# lst = [50,40,'Clay','Jessica',89]
# ls = []
# for i in lst:
#     print(type(i) , i)
#     if (type(i) == str):
#         print(i)
#         ul = i[::-1]
#         ul = ul.lower()
#         ul = ul.capitalize()
#         print(ul)
#         ls.append(ul)
#     else:
#         i = str(i)
#         ul = i[::-1]
#         ul = int(ul)
#         ls.append(ul)
        
# ls.reverse()
# print(ls)







# 4. Checks if one set is a subset or superset of another set. If found, delete all elements from that set
#     • first_set = {50, 44, 35}
#     • second_set = {57, 83, 50, 23, 44, 78, 5,35,92}

# first_set = {50, 44, 35}
# second_set = {57, 83, 50, 23, 44, 78, 5,35,92}
# print(first_set.issubset(second_set))

# for i in first_set:
#    second_set.discard(i)
# print(second_set)





# 5. Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
#     • Sample_dict = [47, 64, 69, 37, 76, 83, 95, 97]
#     • test_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
#     • Output == [47, 69, 76, 97]

# Sample_dict = [47, 64, 69, 37, 76, 83, 95, 97]
# test_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97,'chirag':2}
# lst = []

# for i in test_dict.values():
#    for j in Sample_dict:
#       if(i == j):
#          lst.append(i)
# print(lst)






# 6. Draw the pattern
#     •            1
#     •          1   1
#     •        1   2   1
#     •      1   3   3    1
#     •    1  4    6   4   1
#     •  1  5   10   10  5   1

# temp = 1
# for i in range(1,7):
#    for space in range(1,7-i):
#       print(end = "  ")
#    for j in range(0,i):
#       if j==0 or i==0:
#          temp = 1
#       else:
#          temp = temp * (i - j)//j
#       print(temp,end="    ")
#    print()










# 7.Access the nested key increment from the following dictionary.
#     • emp_dict = {
#     •     "company": {
#     •         "employee": {
#     •             "name": "Jess",
#     •             "payable": {
#     •                 "salary": 9000,
#     •                 "increment": 12
#     •             }
#     •         }
#     •     }
#     • }

# emp_dict = {
# "company": {
# "employee": {
# "name": "Jess",
# "payable": {
# "salary": 9000,
# "increment": 12
#              }
#            }
#         }
#      }

# print(emp_dict)     
# a = emp_dict["company"]["employee"]["payable"]["increment"]
# print(a)