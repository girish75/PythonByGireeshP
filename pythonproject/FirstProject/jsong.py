import json

'''
The Json module provides an easy way to encode and decode data in JSON
Convert from Python to JSON:
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
convert Python objects of the following types, into JSON strings:     dict, list
    tuple,     string,     int
    float,     True,     False
    None
'''
data = {"Name": "Girish",
        "Shares": 100,
        "Price": 540}

# convert into JSON:
json_str = json.dumps(data)
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))

# the result is a JSON string:
print(json_str)

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
# Use the indent parameter to define the numbers of indents:
print(json.dumps(x, indent=4))  # Very useful.

# Use the separators parameter to change the default separator:
print(json.dumps(x, indent=4, separators=("|| ", " = ")))
# Order the Result
# Use the sort_keys parameter to specify if the result should be sorted or not:
print("New Dict = ", json.dumps(x, indent=4, sort_keys=True))

# ==============================================================
# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.
# The result will be a Python dictionary.

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
