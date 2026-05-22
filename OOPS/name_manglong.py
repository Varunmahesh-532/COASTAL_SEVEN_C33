class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
    
    def show_balance(self):
        print("Balance:", self.__balance)

b1 = BankAccount("Varun", 5000)
b1.show_balance()
b1.deposit(100)
b1.show_balance()
print(b1._BankAccount__balance)