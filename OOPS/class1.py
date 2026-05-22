class Student:
    school = "ABC School"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Name",self.name)
        print("Marks",self.marks)

s1 = Student(55, "Varun")
s1.display()
print(s1.school)





