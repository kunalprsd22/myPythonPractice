from functools import wraps

def logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Calling function")
        return function(*args, **kwargs)

    return wrapper


@logger
def multiply(a, b):
    """Multiply two numbers."""
    return a * b


print(multiply(5, 4))
print(multiply.__name__)
print(multiply.__doc__)