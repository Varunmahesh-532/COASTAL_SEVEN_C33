class Student:
    
    def __init__(self, name):
        self.name = name
    
s1 = Student("VARUN")
print(s1.name)

s1.name = "RAHUL"

print(s1.name)