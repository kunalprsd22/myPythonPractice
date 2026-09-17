def my_function():
    list = []
    for x in range(1,5):
        list.append(x * 10)
    return  list

def gnerator_function():
    for x in range(1,5):
        yield x * 10

print(my_function())
print(gnerator_function())

g = gnerator_function()


print(next(g))
print(next(g))
print(next(g))
print(next(g))




