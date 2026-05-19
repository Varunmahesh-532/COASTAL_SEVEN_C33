#create a set
fruits = {'apple', 'banana', 'orange'}
empty_set = set()
print(fruits)
print(empty_set)

#Automatic removal of duplicates
numbers =[1, 2, 3, 4, 5, 2, 3, 4, 5]
print(numbers)
unique_numbers = set(numbers)
print(unique_numbers)

color = {'red', 'green', 'blue'}
color.add('yellow')
print(color)
color.update(['orange', 'purple'])
print(color)
color.remove('green')
print(color)
#color.remove('Pink') #This will raise an error because 'Pink' is not in the set
color.discard('Pink') #This will not raise an error even if 'Pink' is not in the set
print(color)

#Math operations on sets
python_student = {'Alice', 'Bob', 'Charlie', 'David'}
web_student = {'Charlie', 'David', 'Eve', 'Frank'}

#print common students in both courses [Intersection] '&'
print(python_student.intersection(web_student))

#print(all the students in either course [Union] '|'
print(python_student.union(web_student))

#print student who are only in python course [Difference] '-'
print(python_student.difference(web_student))

#print student who are only in web course [Difference] '-'
print(web_student.difference(python_student))

#print the student who are in single course but not in both [Symmetric Difference] '^'
print(python_student.symmetric_difference(web_student))

#Frozen set
immutable_set = frozenset(['a', 'b', 'd', 'c', 'c'])
print(immutable_set)