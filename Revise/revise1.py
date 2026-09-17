from shutil import ignore_patterns

my_data = "Kunal prasad"
#print(f"my data is {my_data}")
my_list = list(my_data)
my_list.sort(key=str.lower)
print(my_list)
