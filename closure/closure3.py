

def increment():
    x = 0
    def inner ():
        x = x + 1
        return x
    return inner


value = increment()
print(value())
print(value())
print(value())