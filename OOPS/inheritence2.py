class Father:
    def talk(self):
        print("Hello")

class Mother:
    def laugh(self):
        print("Ha haa")

    def talk(self):
        print("How are you?")


class Child(Father, Mother):
    pass

class GrandChild(Child):
    pass



gchild = GrandChild()
gchild.talk()
