class Vehicle:
    def range(self):
        print("Vehicals range")

class Car(Vehicle):
    def test(self):
        print("Swift Creta Seltos")

c = Car()
c.range()
c.test()
