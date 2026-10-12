

def numbers():
    yield from [1, 2, 3, 4, 5]

def numbers1():
    return [1,2,3,4,5]

for number in numbers():
    print(number)