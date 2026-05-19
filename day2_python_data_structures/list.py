#adding items to list
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)

fruits.insert(1, 'grape')
print(fruits)   

new_fruits = ['kiwi', 'mango']
fruits.extend(new_fruits)
print(fruits)

#Removing the element
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers)
numbers.pop(1)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.clear())

#Utility & information about list
letters = ['a', 'b', 'c', 'd', 'e']
print(letters.index('c'))
print(letters.count('a'))

number = [2, 5, 3, 1, 5, 4]
print(sorted(number))
print(sorted(number, reverse=False))
print(sorted(number, reverse=True))
print(number.reverse())

#Shallow copy vs Deep copy
"""Shallow copy creates a new list but does not create copies of the nested objects. 
Instead, it references the same nested objects as the original list. 
Therefore, changes to the nested objects in the shallow copy will affect the original list."""

original_list = [[1,2,3], [4,5,6]]
shallow_copy = original_list.copy()
shallow_copy[1][0] = 500
print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)

"""Deep Copy creates a new list and also creates copies of the nested objects. 
Therefore, changes to the nested objects in the deep copy will not affect the original list."""

import copy
original_list = [[1,2,3], [4,5,6]]
deep_copy = copy.deepcopy(original_list)
deep_copy[1][0] = 500
print("Original List:", original_list)
print("Deep Copy:", deep_copy)


arr = [1,2,3,4,5]
print(len(arr))

arr = 'varun'
print(arr[:3])
print(arr[3:5])
print(arr[:5])
print(arr[::-1])

if arr[::-1] == arr:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")