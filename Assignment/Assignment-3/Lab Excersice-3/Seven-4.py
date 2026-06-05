class A:
    def display_A(self):
        print("Class A Calling")
class B(A):
    def display_B(self):
        print("Class B Calling")
class C(A):
    def display_C(self):
        print("Class C Calling")
class D(B, C):
    def display_D(self):
        print("Class D Calling")
d = D()
d.display_A()
d.display_B()
d.display_C()
d.display_D()

