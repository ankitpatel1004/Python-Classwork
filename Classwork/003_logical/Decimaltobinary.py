# Decimal to binary

# Using string
num = int(input("Enter number : "))
num = 91
st = ""
while num != 0:
    rem = num%2
    st = str(rem) + st
    num //=2
print(st)
print("Decimal t0 binary is - ",st)

number = 91
st = 0
mul = 1
while number != 0:
    rem = number%2
    st = (rem*mul) + st
    number //=2
    mul*=10
print(st)
