def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Calculator")
print("1 for Add")
print("2 for Subtract")
print("3 for Multiply")
print("4 for Divide")

choice = input("Enter the choice : ")

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

if choice == '1':
    print("Result : ", add(num1, num2))
elif choice == '2':
    print("Result : ", subtract(num1, num2))
elif choice == '3':
    print("Result : ", multiply(num1, num2))
elif choice == '4':
    print("Result : ", divide(num1, num2))
else:
    print("Invalid choice")