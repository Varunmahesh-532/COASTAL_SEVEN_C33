class ATMSimulator:

    def __init__(self, pin: str, initial_balance: int):
        self.__correct_pin = pin
        self.__balance = initial_balance

    def verify_pin(self, input_pin: str) -> bool:
        return self.__correct_pin == input_pin
    
    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount: int) -> list[bool, str]:
        if amount <= 0:
            return False, "Invalid amount"
        if amount % 100 != 0:
            return False, "Amount must be in multiples of 100"
        if amount > self.__balance:
            return False, "Insufficient funds"
        
        self.__balance -= amount
        return True, f"Withdrawal successful Rs {amount}. New balance: {self.__balance}"
    
    
def main():
    atm = ATMSimulator(pin = "1234", initial_balance = 10000)
    pin_input = input("Enter PIN: ")
    if atm.verify_pin(pin_input):
        print(f"Access Granted. Available Funds: Rs. {atm.get_balance()}")
        try:
            amount = int(input("Enter amount to withdraw: "))
            success, message = atm.withdraw(amount)
            if success:
                print(f"\n[SUCCESS] {message}")
            else:
                print(f"\n[FAIL] {message}")
        except ValueError:
            print("\n[ERROR] Invalid input. Please enter a numeric value.")
    else:
        print("Invalid PIN. ACCESS DENIED.")

if __name__ == "__main__":
    main()

