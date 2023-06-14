# 1.Write a function that takes a filename as an argument and returns the number of lines in the file. If the file does not exist, the function should raise a FileNotFoundError with the message "The file [filename] does not exist."

def fileFound(x):
    try:
        with open(x) as f:
            return print(len(f.readlines()))
    except:
        raise FileNotFoundError(f"The file {x} does not Found")

inputFileName = input("Enter Your File Name\n")
fileFound(inputFileName)