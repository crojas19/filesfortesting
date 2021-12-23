import json

# read file
with open('nuevoj.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)
print(obj)
