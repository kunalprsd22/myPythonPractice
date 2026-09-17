from functools import reduce

# lamda args: expresssion

# lamda declaration
add = lambda a,b: a+b
print(add(1,2))

######################################################################

# squares = list(map(function,iteration))
nums = [1,2,3,4,5]
sqareNumber = list(map(lambda x: x*2,nums))
addNumber = list(map(lambda x: x+2,nums))
print(addNumber)

######################################################################

# even = list(filter(lamda x: x%2 == 0, nums))

evenNumber = list(filter(lambda x: x % 2 == 0, nums))
print(evenNumber)

multiply = reduce(lambda x,y: x*y, nums)
print(multiply)