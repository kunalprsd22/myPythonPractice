from functools import wraps

def repeat(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = 0
            for _ in range(times):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def add(a, b):
    print("Adding...")
    return a + b


result = add(10, 20)

print(result)