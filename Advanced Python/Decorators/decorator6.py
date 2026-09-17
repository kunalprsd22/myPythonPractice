
# Decorator with a parameter

def repeat(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                function(*args, **kwargs)
        return wrapper

    return decorator


@repeat(3)
def hello():
    print("Hello")


hello()