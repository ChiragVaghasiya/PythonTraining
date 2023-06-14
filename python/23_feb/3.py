# 4. Write a program which implement the 'Insertion Sort.' It allows to add/remove number at any
# position and after add/remove operation all the numbers should be displayed in as sorted.
import re
class Insertion_Sort():

    def insertionSort(arr):

        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j] :
                    arr[j + 1] = arr[j]
                    j -= 1
            arr[j + 1] = key

inputList = input("Enter Your list")
string = re.split(r',| |-',inputList)
arrr = list(map(lambda x : int(x) , string))
arr = arrr
Insertion_Sort.insertionSort(arr)
print("Your Sorted Array : ",arr)

while(True):
    check = input("You need add or Remve Element (y\\n)")
    if (check == 'y'):
        addDeletCheck = input("DELET FOR press (d) or EDIT for press (e)")
        if (addDeletCheck == 'd'):
            delet = int(input("which elemet You want to want: "))
            arr.remove(delet)
            print(arr)
        elif(addDeletCheck == 'e'):
            add = int(input("Enter YOur Number WHich YOU want to Add : "))
            arr.append(add)
            Insertion_Sort.insertionSort(arr)
            print(arr)
        else:
            print("please input valid Input")
            continue
    elif (check == 'n'):
        break
    else:
        print("please Input valid character")
        continue
