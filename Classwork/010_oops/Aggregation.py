class Salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
    def annual_salary(self):
        return (self.pay*12)+self.bonus

class Employee:
    def __init__(self,name,age,s):
        self.name = name
        self.age = age 
        self.salary = s
    def total_salary(self):
        return self.salary.annual_salary()

s = Salary(10000,5000)
e = Employee("Ankit",35,s)
print(e.total_salary())
