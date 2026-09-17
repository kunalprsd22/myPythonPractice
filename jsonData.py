import json

data = {
    "number": 2,
    "balance": 0
}

# convert to string
json_data = json.dumps(data)
print(json_data)

##################################################

data2 =  '{ "number": 2, "balance": 0}'
json_data2 = json.loads(data2)
print(json_data2)
