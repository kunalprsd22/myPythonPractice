
def decorator_one(function):
    def wrapper(*args, **kwargs):
        print("Decorator One - Before")

        result = function(*args, **kwargs)

        print("Decorator One - After")
        return result

    return wrapper

def decorator_two(function):
    def wrapper(*args, **kwargs):
        print("Decorator Two - Before")

        result = function(*args, **kwargs)

        print("Decorator Two - After")
        return result

    return wrapper



@decorator_one
@decorator_two
def hello():
    print("Hello")

hello()