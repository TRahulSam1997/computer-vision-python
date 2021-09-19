import json

items = json.loads('{"name":"John", "age":30, "car":null}')

for item in items:
    print(item('name'))