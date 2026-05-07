# reducer single value return 

# l = [10,20,30,40,50,60,70]
# def sum(a,b):
#     return a+b
# k=0
# for i in l:
#     k = sum(i,k)
# print(k)

from functools import reduce

# l = [10,20,30,40,50,60,70]
# def sum(a,b):
#     #print(a,b)
#     return a+b
# r = reduce(sum,l)
# print(r)

l = [10,20,30,40,50,60,70]
r = reduce(lambda a,b:a+b,l)
print(r)

l = [10,20,30,40,50,60,70]
r = reduce(lambda a,b : a if a>b else b , l)
print(r)
