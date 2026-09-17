class Person:

    def __init__(self, name):
        self.name = name

    #automatic call while print object
    def __str__(self) -> str:
        return f"person {self.name}"

    # automatic call when len(person1) called
    def __len__(self):
        return len(self.name)

person1 = Person("Kunakl  111")
print(person1)
print(len(person1))

########################################################################

class Numbers:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Numbers(self.number + other.number)

    def __eq__(self, other):
        return self.number == other.number

num1 = Numbers(2)
num2 = Numbers(2)
results = num1 + num2
print(results.number)
print(num1 == num2)

########################################################################
