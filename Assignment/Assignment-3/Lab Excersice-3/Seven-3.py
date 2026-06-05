class Vehicle:
    def range(self):
        print("Vehicals range")
class Car(Vehicle):
    def test(self):
        print("Swift Creta Seltos")
class Bike(Vehicle):
    def demo(self):
        print("Passion Unicorn Shine")
c = Car()
b = Bike()
c.range()
c.test()
b.demo()
