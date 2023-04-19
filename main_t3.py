class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getinfo(self):
        print(f'{self.name}s age is {self.age}')


person = Person('John',34)
person.getinfo()