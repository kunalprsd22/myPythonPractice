class Animal:
    def __init__(self, age , color):
        self.age = age
        self.color = color

    def born(self):
        print(f"I am borne")

    def talk(self):
        print("I am talking")


class Bird(Animal):

    def __init__(self, age , color, altitude):
        super().__init__(age , color)
        self.altitude = altitude

    def talk(self):
        print("I am not talking")



twettie = Bird(12, "Yellow", 12)
twettie.talk()