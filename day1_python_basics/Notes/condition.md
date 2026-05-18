In the real world, we make choices every day: "If it is raining, I will take an umbrella." In programming, we use conditions to control the flow of execution

Authentication Example: A system checks if provided_password matches stored_password. If they match, access is granted; otherwise, access is denied.
ATM Example: Before dispensing cash, the software evaluates: if requested_amount <= account_balance. If true, it processes the transaction; otherwise, it displays "Insufficient Funds".
Login System: A multi-step verification might check if user_exists followed by a nested check if account_status == "active".

Comparison and Logical Operators

Before writing conditions, you must understand the "building blocks" used to evaluate them.
Comparison (Relational) Operators
Used to compare two values, returning a Boolean (True or False):
== : Equal to (e.g., 5 == 5 is True)
!= : Not equal to
> / < : Greater than / Less than
>= / <= : Greater than or equal to / Less than or equal to

Logical Operators

Used to combine multiple conditional statements:
and: Returns True only if both statements are true (e.g., (8 > 7) and (2 < 5)).
or: Returns True if at least one statement is true.
not: Reverses the result (e.g., not(True) becomes False).

Step-by-Step Condition Syntax

The if Statement
The simplest decision-making statement. It executes a block of code only if the condition is True.

Example:

age = 18
if age >= 18:
    print("You are eligible to vote.")

The if...else Statement
Adds an alternative path for when the condition is False.

Example:

balance = 500
withdraw = 1000
if withdraw <= balance:
    print("Dispensing cash...")
else:
    print("Insufficient funds.") # Executes if condition is False

The if...elif...else Chain
Used when you have multiple specific conditions to check in sequence.

Example:

marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80: # Checked only if the first 'if' was False
    print("Grade: B")
else:
    print("Grade: C")

Nested Conditions
An if statement placed inside another if statement, used for multi-layered requirements.

Example:

has_card = True
correct_pin = True
if has_card:
    if correct_pin:
        print("Welcome to your account.")
    else:
        print("Invalid PIN.")
else:
    print("Please insert your card.")

