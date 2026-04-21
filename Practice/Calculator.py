# select="y"
# while select != "n":

#     a=int(input("Enter the first number : "))
#     b=int(input("Enter the second number : "))

#     choice = int(input("""For addition press 1
#     For subtraction press 2
#     For Multiplication press 3
#     For Divide press 4 : """))
#     match choice:
#         case 1:print("addition is : ", a+b)
#         case 2:print("subtracton is : ", a-b)
#         case 3:print("multiplication is ", a*b)
#         case 4:print("division is : ", a/b)

#     select = input("Do you want to contionue (y/n) : ")



choice = "y"
while choice != "n":

    a=int(input("Enter first value : "))
    b=int(input("Enter second value : "))
    c=int(input("Enter your choice = "))
    match c:
        case 1:print("Addition is", a+b)
        case 2:print("Subtraction is", a-b)
        case 3:print("Multiplication is", a*b)
        case 4:print("Division is", a/b)
        case _:print("Invalid choice")

    choice = input("Do you want to continue? y or n : ")
