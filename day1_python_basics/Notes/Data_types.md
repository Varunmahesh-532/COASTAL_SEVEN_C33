Integer (int)

Python integers have arbitrary precision, meaning they can grow infinitely large until your computer runs out of RAM.
Minimum size is 28 bytes due to Python object overhead.
The raw value inside grows dynamically in chunks of 4 or 8 bytes depending on how massive the number is.
Example: x = 42

Character (char / str)

Python does not have a native char type. A single character is just a string of length 1.
1 Byte for standard English/ASCII text ('a', '1').
2 Bytes for extended scripts (Cyrillic, Arabic).
4 Bytes for complex characters and Emojis ('🚀').
Example: char = 'A' (Python treats this as a 1-character string)

Float (float)

Handles numbers with decimal points.
Python floats are implemented as C doubles, using exactly 8 bytes of raw memory for the number itself (total 24 bytes with Python object overhead).
Provides up to 15–17 digits of decimal precision.
Example: pi = 3.14159

Double

Python does not have a separate double type.
Because Python's standard float is already 64-bit (8 bytes), a Python float IS a C double.
Example: x = 0.0000000000042 (Still just a standard float in Python)

Boolean (bool)

Represents True or False. It is actually a subclass of int (where True == 1 and False == 0).
28 bytes total overhead, but represents a single truth value.
Example: is_active = True

List (list)

Ordered, mutable (changeable), allows duplicate elements.
An array of 8-byte memory pointers pointing to the actual items.
Python overallocates extra 8-byte spaces so that appending items is incredibly fast.
xample: my_list = [1, "apple", 3.4]


Tuple (tuple)

Ordered, immutable (cannot be changed after creation). Faster than lists.
An array of 8-byte memory pointers.
Unlike a list, it allocates exactly the number of slots needed (no overallocation), making it highly memory-efficient.
Example: my_tuple = (10, 20, 30)

Set (set)

Unordered, mutable, contains only unique items. Great for math operations like unions and intersections.
Uses a Hash Table structure.
Has high memory overhead (starts at 216 bytes) because it pre-allocates empty buckets to prevent data collisions.
Example: my_set = {1, 2, 3, 3} (The duplicate 3 is automatically removed)

Dictionary (dict)
Stores data in Key:Value pairs. Highly optimized for lightning-fast lookups.
Split into two parts:
An Index Array (uses 1, 2, or 4 bytes per slot depending on how large the dictionary is).
An Entries Array where each row takes exactly 24 bytes (an 8-byte hash, an 8-byte pointer to the Key, and an 8-byte pointer to the Value).
Example: my_dict = {"name": "Alice", "age": 25}

