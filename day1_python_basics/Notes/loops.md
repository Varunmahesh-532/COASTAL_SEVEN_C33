Iteration Concept
Iteration is the process of executing a set of instructions repeatedly until a specific condition is met. Repetition is essential to keep a computer doing useful work, allowing software to process large datasets or perform recurring tasks without manual instruction for every step.

Real-World Software Examples

Data Processing: Iterating through a CSV file to calculate total revenue from thousands of rows.
Game Logic: A while loop that keeps a game window open until the user clicks "Exit".
Automation: Sending an automated email to a list of subscribers by looping through a database of user IDs.

The for Loop (Definite Iteration)

A for loop is used to iterate over a sequence (such as a list, tuple, string, or range). It executes a set number of times based on the length of that sequence.

Syntax:
for item in sequence:
    # Code block to execute

Example:

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

The while Loop (Indefinite Iteration)

A while loop repeatedly executes a block of code as long as a given condition remains True. You must ensure that the condition eventually becomes False, otherwise, you will create an infinite loop that crashes your program.

Syntax:
while condition:
    # Code block to execute

Example:

count = 1
while count <= 5:
    print(f"Count is {count}")
    count += 1

Loop Control Statements : Sometimes you need to alter the normal flow of a loop based on an external factor or a specific condition inside the loop. Python provides three keywords for this.

break:

Terminates the loop prematurely and jumps to the code directly following the loop.

for num in range(1, 10):
    if num == 5:
        break  # Stops the loop completely when num hits 5
    print(num)

continue:

Skips the rest of the code inside the current iteration and jumps straight to the next evaluation cycle of the loop.

for num in range(1, 6):
    if num == 3:
        continue  # Skips printing 3, goes straight to 4
    print(num)

pass

A null statement used as a placeholder when a statement is syntactically required, but you do not want to execute any code yet.

for num in range(1, 5):
    if num == 3:
        pass  # Does nothing, loop continues normally
    print(num)


The else Clause in Loops
A unique feature of Python is that both for and while loops can have an optional else block.
The else block executes only if the loop finishes normally (i.e., it ran through the entire sequence or the condition became false).
If the loop is terminated early by a break statement, the else block is skipped.

Example:

for num in range(1, 4):
    print(num)
else:
    print("Loop finished successfully without encountering a break!")