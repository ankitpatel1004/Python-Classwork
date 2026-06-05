try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Invalid operator")
        exit()
    print("Result =", result)

except ValueError:
    print("Error: Please enter valid numeric values")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

except Exception as e:
    print("An unexpected error occurred", e)
    