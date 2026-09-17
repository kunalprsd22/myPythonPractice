from collections import Counter

series = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
my_name = "hello my name is kunal"
my_counter = Counter([1,1,1,1,12,2,2,33,3,3,3,3,])

#print(Counter(series))
#print(Counter(my_name.split()))
#print(Counter(my_name))

print(my_counter.most_common())


