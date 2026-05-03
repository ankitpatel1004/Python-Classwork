# person = {
#     "name":"ankit",
#     "email":"ankitpatel8085@gmail.com",
#     "age":35,
#     #"name":"yash", #if same 2 keys then last one updated
#     123 : "abc",
#     True : "jklm",
#     (10,20,30) : "fghj",
#     #[10,20,30] : "hhjj", #cannot use 'list' as a dict key
#     #{10,20,30} : "ccdd" #cannot use 'set' as a dict key
# }
# print(person)
# print(type(person))
# print(len(person))

# #second method dict
# d = dict(name='ankit',email='ankitpatel8085@gmail.com')
# print(d)

cn = {
    "India":"IN",
    "USA":"US",
    "Canada":"CN",
    "Australia":"AUS"
}
# print(cn)
# print(cn.get("India"))
# #get means nothing then give none
# print(cn.get("India1"))
# print(cn['India'])
# #nothing then error
# #print(cn['India1'])
# #above statement comment then also print
# print("Hello")

# #print only keys
# print(cn.keys())
# #print only values
# print(cn.values())
# #print both keys and values
# print(cn.items())
# #print dictionary
# print(cn)

# for i in cn:
#     print(i)

# for i in cn.items():
#     print(i)

# for i,j in cn.items():
#     print(i,j)

#update given data
# cn['India']='abc'
#also update out of dictionary
# cn.update({"abc":"xyz","India":"K"})
# print(cn) 

#remove specify data
# cn.pop("India")
# remove from last
# cn.popitem()
# #clear dictionary
# cn.clear()
# #delete dictionary and then given error
# del cn
# print(cn)

#copy dictionary and not change in original
# k=cn.copy()
#both are equal
# k=cn
# k.update({"A":"X"})
# print(k)
# print(cn)

# nested dictionary
# student={
#     "name":"ankit",
#     "email":"ankitpatel8085@gmail.com",
#     "marks":{
#         "python":70,
#         "java":60,
#         "php":50
#     }
# }
# print(student)

# for i,j in student['marks'].items():
#     print(i,j)

# x=('key1','key2','key3')
# y=0
# thisdict=dict.fromkeys(x,y)
# print(thisdict)

# x=("k1","k2","k3")
# y=(10,20,20,30,40)
# d=zip(x,y)
# print(list(d))
# print(tuple(d))

k={"a":1,"b":2}
# k.setdefault("b",3)
k['b']=5
print(k)
