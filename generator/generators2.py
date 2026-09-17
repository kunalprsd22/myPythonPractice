def my_generator():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x


g = my_generator()
print(next(g))
print(next(g))
print(next(g))