# class Demo:

#     name = "ankit"
#     def __str__(self):
#         return self.name

# d = Demo()
# print(d)

# class Calc:

#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def __eq__(self,value):
#         return self.a==value.a and self.b==value.b

# c = Calc(100,200)
# c1 = Calc(100,2000)
# print(c==c1)

class Sample:

    def __init__(self,a):
        self.a = a

    def __len__(self):
        return len(self.a)

    def __setitem__(self,key,value):
        self.a[key] = value

    def __getitem__(self,key):
        return self.a[key]

s = Sample([10,20,30,40,50])
print(len(s))
s[0] = 100
print(s.a)
print(s[0])
