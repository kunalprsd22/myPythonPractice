import time

def timer(function):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.2f} seconds")
        return result
    return wrapper


@timer
def calculate(a, b):
    time.sleep(2)
    return a + b




calculate(12,20)