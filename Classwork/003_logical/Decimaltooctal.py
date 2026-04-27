# Decimal to octal

# using string
num = 155
s = ""
while num != 0:
    rem=num%8
    s=str(rem)+s
    num //=8
print(s)

number = 155
st = 0
mul = 1
while number != 0:
    rem = number%8
    st = (rem*mul) + st
    number //=8
    mul*=10
print(st)
