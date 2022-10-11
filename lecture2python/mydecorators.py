def cubic(x):
    def twice(x):
        print("this is your sqaure numb",x())
        print("This is your cubic numb", x())


@cubic  
def square(x):
    return x*x

square(2)

