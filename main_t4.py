class Myclass:
    pass

def change_nameClass(cls,name):
    if not name.isalnum() or not name[0].isupper():
        raise ValueError("ERROR")
    else:
        cls.__name__ = name

change_nameClass(Myclass,'UsefulClass')
print(Myclass.__name__)