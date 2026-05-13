# def after(func):
#     def execute():
#         func()
#         print("calling after test")
#     return execute

# def before(func):
#     def execute():
#         print("calling before test")
#         func()
#     return execute

# @before
# @after
# def test():
#     print("test calling")
# test()

# def add(func):
#     def execute(*a):
#         print("Addition")
#         sum = 0
#         for i in a:
#             sum+=i
#         print("Addition is : ",sum)
#         func(*a)
#     return execute

# def mul(func):
#     def execute(*a):
#         print("Multiplication")
#         sum = 1
#         for i in a:
#             sum*=i
#         print("Multiplication is : ",sum)
#         func(*a)
#     return execute

# @add
# @mul
# def calc(a,b):
#     pass
# calc(20,30)

def numbersonly(func):
    def execute(a):
        if str(a).isdigit():
            func(a)
        else:
            print("Invalid input")
    return execute

@numbersonly
def get(a):
    print(a)
get("30ghj")
