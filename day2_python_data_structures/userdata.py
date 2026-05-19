import json

# 1. Parsing JSON (Converting a raw JSON String into a Python Dictionary)
json_string = '{"name": "John", "age": 30, "has_license": false}'

# json.loads() means "Load String"
python_dict = json.loads(json_string)

print(type(python_dict))  # Output: <class 'dict'>
print(python_dict["name"]) # Output: John


# 2. Serializing JSON (Converting a Python Dictionary into a valid JSON string)
user_data = {
    "name": "Jane",
    "admin": True,
    "scores": [95, 88]
}

# json.dumps() means "Dump String"
clean_json_output = json.dumps(python_dict, indent=2) #indent parameter is used to format the JSON string with indentation for better readability 
print(clean_json_output)