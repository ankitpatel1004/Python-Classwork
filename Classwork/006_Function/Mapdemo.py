# map fuction use for list in all element operations

# a=[1,2,3,4,5,6,7]
# k=[]
# def square(a):
#     return a*a
# for i in a:
#     j = square(i)
#     k.append(j)
# print(k)

a = [1,2,3,4,5,6,7]
def square(a):
        return a*a
k = map(square,a)
print(list(k))

a = [1,2,3,4,5,6,7]
k = map(lambda i:i*i,a)
print(list(k))

sub = ["java","pathon","php","node","android"]
k = map(lambda a:len(a),sub)
print(list(k))
