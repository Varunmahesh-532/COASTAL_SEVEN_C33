class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show_details(self):
        print("Name :", self.name)
        print("Salary :", self.salary)

class Developer(Employee):

    def coding(self):
        print(self.name, "is best coder")
    
s1 = Developer("Varun", 5000)
s1.show_details()
s1.coding()