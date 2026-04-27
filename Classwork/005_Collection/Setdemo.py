# s = {10,20,30,40,50,60,50}
# print(s)
# print(type(s))
# print(len(s))

# for i in s:
#     print(i)

# s.add(100)
# print(s)
# remove only element remove in tuple otherwise error
# s.remove(30)
# print(s)
# discard means not in tuple but also continue progarm
# s.discard(300)
# print(s)
# s.pop()
# print(s)

a={10,20,30,40,True,0}
b={30,40,50,60,1,False}

# update means unique element of combine set
# a.update(b)
# print(a)
# a|=b
# print(a)
# k=a.union(b)
# print(k)
# k=a|b
# print(k)

# intersection means common
# a.difference_update(b)
# print(a)
# a-=b
# print(a)
# k=a.difference(b)
# print(k)
# k=a-b
# print(k)

# a.symmetric_difference_update(b)
# print(a)
# a^=b
# print(a)
# k=a.symmetric_difference(b)
# print(k)
# k=a^b
# print(k)

# a = {10,20}
# b = {10,20,30}
# print(a.issubset(b))
# print(b.issuperset(a))
# print(a.isdisjoint(b))
# a = {100,200}
# b = {10,20,30}
# print(a.isdisjoint(b))

f = frozenset({10,20,30,40})
print(type(f))
