a = [1,3,5,98,7,8,4,2]
b = filter(lambda i : i%2 != 0, a)
print(list(b))
 
a = [1,3,5,98,7,8,4,2]
b = map(lambda i : i*i, a)
print(list(b))

from functools import reduce

a = [1,3,5,98,7,8,4,2]
b = reduce(lambda c,d : c+d, a)
print(b)

