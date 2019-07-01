class Student():
    def __init__(self, name, school):
        self.name = name
        self.school = school

    @classmethod
    def friend(cls ,name , origin):
        return cls(name , origin.school)



class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name , school)
        self.salary = salary
    @classmethod
    def friend(cls,name, origin, salary):
        return cls(name, origin.school,salary )

anna= Student("anna", "MIT")

john = anna.friend("john", anna)

soroush = WorkingStudent("soroush","MIT", 200)

farnaz = soroush.friend("farnaz",soroush, 300)
