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

print(person.name)

print(person.family)

print(Person.all())

person_2 = Person("farnaz","ostovari")

print(Person.all())
