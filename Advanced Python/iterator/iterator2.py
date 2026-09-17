

class Counter:

    def __init__(self, max_value):
        self.current = 1
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.max_value:
            value = self.current
            self.current += 1
            return value

        raise StopIteration



counter = Counter(3)

print(next(counter))
print(next(counter))
print(next(counter))