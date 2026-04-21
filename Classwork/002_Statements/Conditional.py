# # if else or if elif else

# age=12
# if age>=18:
#     print("Eligible for voting")
# else:
#     print("Not eligilble for voting")

# a=100
# b=200
# c=300
# if a>b:
#     if a>c:
#         print("a is grater")
#     else:
#         print("c is grater")
# else:
#     if b>c:
#         print("b is grater")
#     else:
#         print("c is grater")

# if a>b and a>c:
#     print("a is grater")
# elif b>a and b>c:
#     print("b is grater")
# elif c>a and c>b:
#     print("c is grater")

# # match

a = int(input("Enter your choice : "))
match a:
    case 1:print("Gujarati")
    case 2:print("Hindi")
    case 3:print("English")
    case _:print("Invalid choice")