# class student:

#     def __init__(self,name,email,age):
#         self.name = name
#         self.email = email
#         self.age = age

#     def display(self):
#         print(self.name,self.email,self.age)

# s = student("ankit","ankitpatel8085@gmail.com",32)
# s.display()

# s = student("yash","yash@gmail.com",25)
# s.display()

# class product:
#     def __init__(self,pro_name,pro_price,pro_quantity):
#         self.pro_name = pro_name
#         self.pro_price = pro_price
#         self.pro_quantity = pro_quantity
#     def display(self):
#         print(self.pro_name,self.pro_price,self.pro_quantity)
# p = product("Soap",50,500)
# p.display()

class student:

    clg = "abc"
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age
    def display(self):
        print(self.name,self.email,self.age,self.clg)

    @classmethod
    def test(cls):
        print(cls.clg)

    @staticmethod
    def demo():
        print("staic method calling")

student.clg = "B&B"
# s1.id = 55

s = student("ankit","ankitpatel8085@gmail.com",32)
s.display()

s1 = student("yash","yash@gmail.com",25)
s1.display()

student.test()
student.demo()
