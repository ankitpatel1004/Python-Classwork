class Father:
    def work(self):
        print("Father - Earning")
class Mother:
    def role(self):
        print("Mother - Cooking")
class Child(Father,Mother):
    pass
c = Child()
c.work()
c.role()
