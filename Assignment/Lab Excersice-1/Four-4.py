age = int(input("Enter your age : "))
weight = float(input("Enter your weight : "))
if age>=18:
    if age<60:
        if weight>=50:
            print("You are eligible to donate blood")
        else:
            print("Your weight is lower than 50, you do not donate blood")
    else:
        print("You are senior citizen, you do not donate blood")
else:
    print("You are not eligible to donate blood")