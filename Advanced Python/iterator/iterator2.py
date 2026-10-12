
class Counter:

    def __init__(self, max_value):
        self.current = 1
        self.max_value = max_value

    # "This object itself is an iterator."
    def __iter__(self):
        return self

    # This is where the actual iteration happens.
    def __next__(self):

        if self.current <= self.max_value:
            value = self.current
            self.current += 1
            return value

        raise StopIteration




counter = Counter(3)

#------- this one --------------
print(next(counter))
print(next(counter))
print(next(counter))

#------- this 2nd type --------------
for value in counter:
    print(value)
