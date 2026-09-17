
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper


@logger
def add(a, b):
    return a + b

print(add(10, 20))


# *args -> it is arguments


