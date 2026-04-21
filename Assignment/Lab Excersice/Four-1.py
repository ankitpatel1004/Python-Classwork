num1 = float(input("Enter the number1 : "))
num2 = float(input("Enter the number2 : "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both number are same")
