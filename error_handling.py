def addition():
    x = int(input("Please enter x"))
    b = int(input("Please enter y"))
    print(x+b)


try:
  addition()
except:
    print("enter correct input")
else:
   print("correct input")
finally:
    print("try again")