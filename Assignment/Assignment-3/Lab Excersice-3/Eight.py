from multipledispatch import dispatch

class Calc:
    @dispatch(int,int)
    def add(self,a,b):
        print(f"Addition of {a} and {b} is {a+b}")
    
    @dispatch(int,int,int)
    def add(self,a,b,c):
        print(f"Addition of {a}, {b} and {c} is {a+b+c}")

c=Calc()
c.add(50,30)
c.add(50,30,20)
