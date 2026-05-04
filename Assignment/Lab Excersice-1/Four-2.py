num = int(input("Enter the number : "))
if num > 1:
    for i in range(2,num):
        if num%2 == 0:
            print(f"{num} is prime number")
            break
        else:
            print(f"{num} is not prime number")
            break
else:
    print("Invalid number")
