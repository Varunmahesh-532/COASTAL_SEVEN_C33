class student:
    def greet(self):
        print("Hello Student")
    def greets(self, name):
        print("Hello", name)
    def __init__(self, user):
        self.user = user
    def display(self):
        print(self.user)
s1 = student("Vijay")
s1.greet()
s1.greets("Varun")
s1.display()


