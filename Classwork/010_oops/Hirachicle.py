class Animal:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def display(self):
        print(self.name,self.breed)

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name, breed)

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name,breed)

d = Dog("Tommy","Labrado")
c = Cat("snow","persian")

d.display()
c.display()
