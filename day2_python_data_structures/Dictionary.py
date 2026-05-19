#creating the dictonary
user_profile = {
    "username" : 'coderam',
    "email" : "ram@gmail.com",
    "age" : 25,
    "is_active" : True
}

empty_dict = {}

print(user_profile)

#Accessing values in a dictionary
print(user_profile["username"])
print(user_profile["email"])    
print(user_profile["age"])

#Modify the existing values
user_profile["age"] = 26
print(user_profile)

#adding the brand new key_value pair
user_profile["country"] ="India"
print(user_profile)

#Safe accesing of values using get() method
#print(user_profile["college"]) #This will raises error because the key "college" does not exist in the dictionary
print(user_profile.get("college")) #This will return None because the key "college" does not exist in the dictionary
print(user_profile.get('college', "Not Found")) #This will return "Not Found" because the key "college" does not exist in the dictionary

#Iteration Methods
for key in user_profile:
    print(key)

for details in user_profile.values():
    print(details)

for key, value in user_profile.items():
    print(f"{key}: {value}")


#merge the two dicts
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2 #In case of duplicate keys, the value from the second dictionary will be used
print(merged)

print(user_profile.keys())
print(user_profile.values())
print(user_profile.items())


profile = {"name": "Bob", "age": 30}
profile.update({"age": 32, "city": "New york"})
print(profile)

#pop method
age = profile.pop("age")
print(f"Popped age: {age}")

print(profile)

ph_num = profile.pop("phone", 0)
print(f"Popped phone number: {ph_num}")

profile.clear()
print(profile)