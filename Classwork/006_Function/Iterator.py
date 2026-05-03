l = [10,20,30,40,50]
itr = iter(l)
print(next(itr))
print(next(itr))
print("Hello")
print(next(itr))

def test():
    yield"hello"
    yield"world"
itr = test()
print(next(itr))
print(next(itr))



def square(a):
    for i in range(a):
        yield i*i

itr = square(7)
print(next(itr))
print(next(itr))
print(next(itr))
