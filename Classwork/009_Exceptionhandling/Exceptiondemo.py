# try ma koi error hoy to except function vall thay ane error batave athva else print thay and finally always print thay

print("program started")
try :
    a = 10
    b = a/0
    # b = a/2
    print(b)
# except ZeroDivisionError as e:
except Exception as e:
    print(e)
else :
    print("Something")
finally :
    print("always executable")
print("program ended")
