class calc:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self,other):
        return self.a+other.a,self.b+other.b

    def __mul__(self,other):
        return self.a*other.a,self.b*other.b 

    # def __add__(self,other):
    #     return self.a+self.b,other.a+other.b

    # def __mul__(self,other):
    #     return self.a*self.b,other.a*other.b 

c=calc(10,20)
c1=calc(30,40)
k=c+c1
k1=c*c1
print(k)
print(k1)
