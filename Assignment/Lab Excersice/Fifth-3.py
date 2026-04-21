list1 = ['apple', 'banana', 'mango']
target = 'mango'
search = False
for fruit in list1:
    if fruit == target:
        search = True
        break
if search == True: 
    print(f"{target} is in list")
else:
    print(f"{target} is not in list")
