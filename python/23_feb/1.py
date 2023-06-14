# 1.Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
# Note: There will be one solution for each input and do not use the same element twice.
#     • Input: numbers= [10,20,10,40,50,60,70], 
#     • target=50
#     • Output: 3, 4
class Sumn:
    def checking_indexinfg(list):
        for i in range(len(list)-1):
            if((list[i]+list[i+1]) == 50):
                print(i+1,i+2)
list = [10,20,10,40,50,60,70,10,40]
Sumn.checking_indexinfg(list)