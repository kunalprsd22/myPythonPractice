class Bird:

    # it is class level variable it will effect all the part
    wings: bool = True

    # it is attributed variable limit to there object
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def speak(self):
        print(self.color)

    def fly(self, feet):
        print(f"it can fly {feet} feet.")

    # it will not udate the attributes only
    # will update class attributes  "wings"
    @classmethod
    def lay_eggs(cls, eggs):
        print(f"it can lay {eggs} eggs.")
        cls.wings = True

    @classmethod
    def stop_flying(cls):
        cls.wings = False

    @staticmethod
    def say_hello():
       print("sfskfsjf akjdbajkdbad ak jbadjkabdjkab djkad bajk")

obj = Bird('Yellow', "eagle")

Bird.stop_flying()
Bird.lay_eggs(12)

#it will print "false" becuase class level attribute is updated using  Bird.stop_flying()
print(obj.wings)


# Swift                         Python
#------------------------------------------------
#static var                   class attribute
#static func                  @staticmethod
#(type-level method)          @classmethod
#instance var                 self.attribute
#instance func                normal method