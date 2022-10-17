import math
x = int(input("Input first value"))

root_error = True

while root_error == True:
    root_error = False
    try:
        root = math.sqrt(x)
    except ValueError:
        print("error please try again")
        x = int(input("Input first Value"))
        root_error = True

print(root)