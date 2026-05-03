# function without parameter
# def message():
#     print("Hello world")
# message()

# funaction with single parameter
# def square(a):
#     print(f"Square of {a} is {a*a}")
# square(5)

# function with parameters
# def add(a,b):
#     print(f"Addition of {a} and {b} is {a+b}")
# add(50,70)

# function with return type
# def cube(a):
#     q=a*a*a
#     return q
# print(cube(3))

# default argument
# def person(name="ankit",email="ankitpatel8085@gmail.com",age=35):
#     print(name,email,age)
# person()
# person("Ankit","ankit@gmail.com",age=32)

# arbitrary arguments
# def add(*a):
#     sum=0
#     for i in a:
#         sum+=i
#     print(sum)
# add(10,20,30,40,50,60)

# def person(**k):
#     print(k)
# person(name="ankit",email="ankitpatel8085@gmail.com",age=35)

# lambda function
add = lambda a,b:a+b
sq = lambda a : a*a
print(add(20,30))
print(sq(20))
