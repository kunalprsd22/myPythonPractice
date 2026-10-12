

def numbers():
    yield 1
    yield 2
    yield 3


def all_numbers():
    for number in numbers():
        yield number

def all_numbers1():
    yield from numbers()


for number in all_numbers():
    print(number)