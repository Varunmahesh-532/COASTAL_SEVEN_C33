class BankAccount:
    
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid Amount")

b1 = BankAccount("Varun", 5000)

print(b1.get_balance())

b1.set_balance(10000)

print(b1.get_balance())

