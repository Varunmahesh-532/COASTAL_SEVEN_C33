class Person:
    
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name is :",self.name)

class Student(Person):

    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def show_roll(self):
        print("Roll NO:", self.roll_no)

class CollegeStudent(Student):
    def __init__(self, name, roll_no, branch):
        super().__init__(name, roll_no)
        self.branch = branch
    
    def show_branch(self):
        print("Branch:", self.branch)

s1 = CollegeStudent("Varun", 101, "CSE")
s1.show_name()
s1.show_roll()
s1.show_branch()