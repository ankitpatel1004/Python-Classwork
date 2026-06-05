class student:
    id = 10
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