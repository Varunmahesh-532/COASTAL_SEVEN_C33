# Difference Between Instance, Class, Static Method

class Demo:

    company = "Google"

    def instance_method(self):
        print("Instance Method")

    @classmethod
    def class_method(cls):
        print(cls.company)
    
    @staticmethod
    def staticmethod():
        print("Static Method")


d = Demo()

d.instance_method()
d.class_method()
d.staticmethod()
