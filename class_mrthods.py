class Student:
    def __init__(self, name, family):
        self.name = name
        self.family = family
    @classmethod
    def class_method(cls):
        print(cls)
        print("I am a class method")
    @staticmethod
    def static_method():
        print(" I am a static method needing no argument.")

student_1 = Student("soroush","khosravi")

student_1.class_method()

Student.class_method()

student_1.static_method()

Student.static_method()
