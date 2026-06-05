try :
    a = 10
    b = a/2
    print(b)
except Exception as e:
    print(e)
else :
    print("Try block run")
finally :
    print("Finally always excutable")
