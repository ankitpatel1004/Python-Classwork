try: 
    a = [10,20,30,40,50]
    a = 30/0
except ZeroDivisionError as e:
    print(e)

try:
    open ("first.txt",'r')
except FileNotFoundError as f:
    print(f)
try:
    a = "30a"
    b = int(a)
except ValueError as g:
    print(g)
