class Person:
    def __init__(self,name, family):
        self.name = name
        self.family = family

    def full_name(self):
        print("The full name is {} {}".format(self.name, self.family))

class Student(Person):
    def __init__(self,name, family, grade):
        super().__init__(name, family)
        self.grade = grade

    def show_grade(self):
        print("The grade of the student is {}".format(self.grade))

me = Person("soroush", "khosravi")

me.full_name()

farnaz = Student("Farnaz","Ostovari", 20)

farnaz.full_name()

farnaz.show_grade()
