# 153 = 1*3 + 5*3 + 3*3 = 3+125+27 = 153

for i in range (150,160):
    number = i
    temp = number
    sum = 0

    while number != 0:
        rem = number%10
        sum+=(pow(rem,3))
        number = number//10

    if temp==sum:
        print(f"{temp} is armstrong number")
    else:
        pass
        print(f"{temp} is not armstrong number")
        