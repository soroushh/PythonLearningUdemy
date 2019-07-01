class Student():
    def __init__(self, name, school):
        self.name = name
        self.school = school

    @classmethod
    def friend(cls ,name , origin, *args, **kwargs):
        return cls(name , origin.school, *args, **kwargs)



class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name , school)
        self.salary = salary
        self.job_title = job_title

anna= Student("anna", "MIT")

john = anna.friend("john", anna)

soroush = WorkingStudent("soroush","MIT", 200, job_title = "softwareDeveloper")

farnaz = soroush.friend("farnaz",soroush, 300, job_title = "Engineer")
