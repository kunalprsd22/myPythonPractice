

# Closure can maintain state

def counter():
    count = 0
    def increment():
        nonlocal count #because Python would treat count as a local variable inside increment().
        count += 1
        return count

    return increment


my_counter = counter()
print(my_counter())
print(my_counter())
print(my_counter())