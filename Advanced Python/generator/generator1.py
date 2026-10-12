

def numbers():
    print("Start")
    yield 1

    print("Middle")
    yield 2

    print("End")
    yield 3

gen = numbers()
print(next(gen))
print(next(gen))
print(next(gen))

for number in numbers():
    print(number)
