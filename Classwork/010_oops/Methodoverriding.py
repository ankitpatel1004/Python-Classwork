class A:

    def test(self):
        print("test calling of A")

class B(A):

    def test(self):
        print("class B test calling")
        super().test()

b=B()
b.test()
