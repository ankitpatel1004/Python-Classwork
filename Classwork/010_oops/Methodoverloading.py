from multipledispatch import dispatch

class calc:

    @dispatch(int,int)
    def add(self,a,b):
        print(f"addition of {a} and {b} is {a+b}")
    
    @dispatch(int,int,int)
    def add(self,a,b,c):
        print(f"addition of {a} {b} and {c} is {a+b+c}")

    # def add(self,*a):
    #     sum = 0
    #     for i in a:
    #         sum+=i
    #     print(sum)

c=calc()
c.add(10,20)
c.add(10,20,30)

