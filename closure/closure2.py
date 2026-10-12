

def create_adder(x):

    def add(y):
        return x + y

    return add

add10 = create_adder(10)
print(add10(5))