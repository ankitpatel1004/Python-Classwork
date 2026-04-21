# l = [10,20,30,40,50,"abc",True,72.33]
# l = list((10,20,30,40,50))
# print(l)
# print(type(l))
# print(l[0])
# print(len(l))

# #access list item
# l = [10,20,30,40,50,60]
# print(l[2])
# print(l[1:5])
# print(l[-1])
# print(l[-4:-1])
# print(l[::-1])

# change list
# l = [10,20,30,40,50,60]
# l[0] = 100
# print(l)
# l.insert(3,300)
# print(l)
# l.append(300)
# print(l)
# # in list remove 2 and 3 value and insert new any value by given
# l[2:4] = [45,48,55,63,69,78]
# print(l)
# # in list starting 0 t0 4 value remove and insert new any value by given
# l[:5] = [45,48,55,63,69,78]
# print(l)

# a = [10,20,30]
# b = [40,50,60]
# # b value extend in a
# a.extend(b)
# print(a)

# remove
# l = [10,20,30,40,50,60]
# l.remove(20)
# print(l)
# remove from last value
# l.pop()
# print(l)
# remove from last given data value
# l.pop(3)
# print(l)

# clear list
# l.clear()
# print(l)
# delete the list and then given error l is not defined
# del l
# print(l)

# for i in l:
#     print(i)

# for i in range(len(l)):
#     print(l[i])

# i=0
# while i<len(l):
#     print(l[i])
#     i+=1

# s = ["python","java","php","android","react"]
# l = []
# for i in s:
#     if "a" in i:
#         l.append(i)
# print(l)
# l = [i for i in s if "a" in i]
# print(l)

# k = [i for i in s if i.startswith('p')]
# print(k)

s = ["python","java","php","android","react"]
# # list sorting in asending order
# s.sort()
# print(s)
# # list sorting in desending order
# s.sort(reverse=True)
# print(s)
# list only in reverse order (not desending order)
# s.reverse()
# print(s)

# k = sorted(s)
# print(k)

k = s
# k = s.copy()
# print(k)
# k = list(s)
# print(k)
k = s[:]
print(k)

k.append(5000)
print(k)
print(s)


