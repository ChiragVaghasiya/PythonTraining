# 4.Write a program which implement STACK operations PUSH,POP. It allows to add/remove elements from the STACK from any position and rearrange the stack.

stack = [1,2,3]
print("Orignal Array : ", stack)
while(1):
    inputt = input("press 1 for the pop element ,press 2 for add element ,press 3 for remove element , Press 4 for push element , press 5 for exit the program\n")

    if (inputt == "1"):
        stack.pop()
        print("Now Your New stack is :\n",stack)

    elif (inputt == "2"):
        index = int(input("Enter U want to add Element in which positions :\n"))
        element = int(input("enter Your element U Want to add :\n"))
        stack.insert(index,element)
        print("Now Your New stack is :\n",stack)
        
    elif (inputt == "3"):
        stack.remove(int(input("enter Your element U Want to Remove :\n")))
        print("Now Your New stack is :\n",stack)

    elif (inputt == "4"):
        stack.append(int(input("enter Your element U Want to add an last :\n")))
        print("Now Your New stack is :\n",stack)

    elif (inputt == "5"):
        break

    else :
        print("Please Input Valid Value")
        continue
