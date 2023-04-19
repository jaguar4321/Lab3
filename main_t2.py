class mylist:

    def __init__(self):
        self.arr = []
        self.count = 0

    def add(self, item):
        self.arr.append(item)
        self.count += 1
        return self

    def __str__(self):
        return str(self.arr)

list = mylist()
list.add('hello').add(1)
print(list)