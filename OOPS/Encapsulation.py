class ATM:

    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
        print(amount, "Deposited")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(amount, "withdraw")
        else:
            print("insuffent Balance")
    
    def check_balance(self):
        print("Available Balance:", self.__balance)

a1 = ATM(10000)
a1.check_balance()
a1.deposit(1000)
a1.check_balance()
a1.withdraw(500)
a1.check_balance()