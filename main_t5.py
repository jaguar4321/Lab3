
class ReNameAbleClass():

    def __init__(self):
        pass

    def change_nameClass(cls,name):
         if not name.isalnum() or not name[0].isupper():
            raise ValueError("ERROR")
         else:
            cls.__name__ = name

    def __str__(self):
        return f"Class name: {self.__class__.__name__}"


class Myclass(ReNameAbleClass):
    def __init__(self):
        pass


obj = Myclass()
Myclass.change_nameClass(Myclass,'UsefulClass')
print(obj)