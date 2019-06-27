class Person:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def full_name(self):
        return(self.name + " "+ self.family)

person = Person("soroush","khosravi")

print(person.full_name())

print(person.name)

print(person.family)
