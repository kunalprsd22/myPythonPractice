import time
import timeit

def for_test(number):
    list = []
    for i in range(1,number+1):
        list.append(i)
    return list

def while_test(number):
    list = []
    counter = 1
    while counter <= number:
        list.append(counter)
        counter += 1
    return  list


declaratio1 = '''
for_test(10)
'''

declaratio2 = '''
while_test(10)
'''

my_setup1 = '''
def for_test(number):
    list = []
    for i in range(1,number+1):
        list.append(i)
    return list
'''

my_setup2 = '''

def while_test(number):
    list = []
    counter = 1
    while counter <= number:
        list.append(counter)
        counter += 1
    return  list
'''

length1 = timeit.timeit(declaratio1, my_setup1,number=10000)
length2 = timeit.timeit(declaratio2, my_setup2,number=10000)

print(length1)
print(length2)  