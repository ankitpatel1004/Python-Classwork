# Octal to decimal

number = 233
p = 0
sum = 0
while number != 0:
    rem = number%10
    sum+=(rem*pow(8,p))
    number //= 10
    p+= 1
print(sum)
