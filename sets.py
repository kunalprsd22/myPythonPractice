my_set = set([1,2,3,4])
my_set1 = set((1,2,3,4,5))
my_set1 = set({1,2,3,4,5})

other_set = {1,2,3,4,5}
other_set.add(6)
my_set.remove(1)

#print(my_set1)
#print(type(other_set))
#print(len(my_set))
#print(my_set.union(other_set))
print(my_set.pop())


print(my_set)