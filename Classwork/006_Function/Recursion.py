# Recursion means function called itself

def square(a):
    print(a*a)
    a+=1
    if a<10:
        square(a)
square(5)

def factorial():
    num = int(input("Enter the number : "))
    fact=1
    for i in range (num,0,-1):
        fact=fact*i
    print(f"Factorial is = ",fact)
factorial()

def factorial(n):
    # Base case: 0! and 1! are 1
    if n <= 1:
        return 1
    # Recursive case: n * (n-1)!
    else:
        return n * factorial(n - 1)
        
print(factorial(5)) 
