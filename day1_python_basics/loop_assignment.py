def calculate_factorial(n):
    if n < 0:
        return "Undefined (Negitive number)"
    fact = 1
    current = n
    while current > 1:
        fact *= current
        current -= 1
    return fact

def analyse_number():
    try:
        start = int(input("Enter the starting number:"))
        end = int(input("Enter the ending number:"))
        if start > end:
            print("[ERROR] Starting number must be less than or equal to ending number.")
            return
        factorial_result = calculate_factorial(start)
        print(f"\n [FACTORIAL] {start} ! = {factorial_result}")
        print(f"\n[EVEN NUMBERS] Even numbers between {start} and {end} (skipping multiples of 5):")
        for num in range(start,end + 1):
            if num % 5 == 0:
                continue
            if num % 2 == 0:
                print(num, end = " ")
            print()
    except ValueError:
        print("\n[ERROR] Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    analyse_number()

