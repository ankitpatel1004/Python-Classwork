class test:
    id = 20
    _name = "ankit"
    __email = "ankitpatel8085@gmail.com"
    def display(self):
        print(self.id)
t = test()
print(t.id)
# print(dir(t))
print(t._name)
print(t._test__email)
