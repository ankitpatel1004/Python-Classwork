
sum = 0
for j in range(3,15):

    number = j
    flag = 0
    for i in range (2,number):
        if number%i==0:
            flag=1
            break

    if flag==0:
        print(f"{number} is prime number")
        sum+=number
    else:
        print(f"{number} is not prime number")

print(sum)
