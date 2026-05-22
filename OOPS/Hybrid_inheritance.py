class User:

    def login(self):
        print("user Logged in...")

class Customer(User):

    def buy_product(self):
        print("Buy Products")

class Seller(User):

    def sell_product(self):
        print("Selling Products")

class Admin(Customer, Seller):

    def manage(self):
        print("Managing System...")

a1 = Admin()


a1.buy_product()
a1.sell_product()
a1.manage()
a1.login()

