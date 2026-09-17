from collections import defaultdict

my_dict = defaultdict(lambda :"No")

my_dict['A'] = "Yes"

print(my_dict['B'])
