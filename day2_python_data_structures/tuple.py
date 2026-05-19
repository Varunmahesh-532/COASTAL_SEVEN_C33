#Tuple creation
point = (10, 25)
#point[0] = 15 # This will raise an error because tuples are immutable
print(point)
empty_tuple = ()
single_element_tuple = (5, )
print(empty_tuple)
print(single_element_tuple)

#Tuple packaging and unpacking
person = "John", 20, "Engineer" #packaging
print(person)

name, age, profession = person #unpacking
print(name)
print(f"Name: {name}, Age: {age}, Profession: {profession}")

a, b, *token, d = 1, 2, 3, 4, 5, 6 #unpacking with * operator, a will be assigned 1, b will be assigned 2 and the rest of the values will be stored in the list token
print(a)
print(b)
print(token)
print(d)


number = (1, 2, 3, 4, 5, 4)
print(number.count(4))

print(number.index(4)) #returns the index of the first occurrence of 4 in the tuple

#Slicing
print(number[1:4]) #slicing from index 1 to index 3 (4 is not included)
print(number[:3]) #slicing from the beginning to index 2 (3 is not included)
print(number[3:5]) #slicing from index 3 to index 4 (5 is not included)