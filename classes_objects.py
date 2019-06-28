class Person:
    all_objects = []
    def __init__(self, name, family):
        self.name = name
        self.family = family
        Person.all_objects.append(self)

    def full_name(self):
        return(self.name + " "+ self.family)

    @classmethod
    def all(cls):
        return(cls.all_objects)

person = Person("soroush","khosravi")

print(person.full_name())

person.name = "farnaz"

print(person.full_name())

print(person.name)
