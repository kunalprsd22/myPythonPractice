

# A decorator is a function that modifies or extends another function without changing its original code.

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@my_decorator
def hello():
    print("Hello")

# it is equivalent to
hello = my_decorator(hello)


hello()