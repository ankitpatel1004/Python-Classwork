# class A:

#     id = 10
#     def test(self):
#         print("class A test calling")

# class B(A):

#     # id = 50
#     def sample(self):
#         print(self.id)

# b = B()
# b.sample()
# b.test()

# class A:
#     id = 20
#     def test(self):
#         print("class A test calling")
# class B(A):
#     id = 50
#     def sample(self):
#         print(self.id)
#         print(A.id)
# b = B()
# b.sample()
# b.test()

class student:
    id = 15
    name = "Ankit"
    email = "ankitpatel8085@gmail.com"
    def test(self):
        print("class student calling")
class dept(student):
    branch = "Computer"
    def sample(self):
        print(self.branch)
        print(student.id)
        print(student.name)
        print(student.email)
c = dept()
c.sample()
c.test()
