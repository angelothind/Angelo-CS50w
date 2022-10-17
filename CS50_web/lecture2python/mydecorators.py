def announce(f):
    def wrapper():
        print("bouta run func")
        f()
        print("another statement")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()

def cubic(f):
    def double():
        base = int(input("Input the mantissa here: "))
        a = f(base)
        print(a)
        b = f(a)
        print(b)
    return double

@cubic
def square(x):
    a = x*x
    return a

square()
    