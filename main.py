class Person:
    pass

    def __init__(self, name, last_name,age):
         self.name = name
         self.last_name = last_name
         self.age = age

    def full_name(self):
        return f'{self.name} {self.last_name}'



person = Person('Yukihiro', 'Matsumoto', 47)
print(person.full_name())
print(person.age)