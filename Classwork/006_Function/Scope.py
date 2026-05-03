# Scope means local and global variable, created inside a function and globally

a = 10
def test():
    global a
    a = 20 
    print(a)
print(a)
test()
print(a)
