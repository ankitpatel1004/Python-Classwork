# # w means write
# f = open("test.txt",'w')
# # f.write("Something")
# f.writelines(["Hello\n","World\n","Python"])
# f.close()

# # a means append
# f = open("test.txt",'a')
# # f.write("Something")
# f.writelines(["Hello\n","world\n","Python\n","Tops\n","Surat"])
# f.close()

# # r means read
# f = open("test.txt",'r')
# data = f.read()
# # data = f.readlines()
# print(data)
# f.close()

# f = open("test.txt",'r')
# while True:
#     data = f.readline()
#     if 'e' in data:
#         print(data)
#     if not data:
#         break

# f = open("test.txt",'r')
# while True:
#     data = f.readline()
#     if data.startswith("P"):
#         print(data)
#     if not data:
#         break

# with open("home.txt",'w') as f:
#     print("write something")

# with open("home.txt",'r') as f:
#     print(f.tell())
#     f.seek(7)
#     data = f.read()
#     print(f.tell())
#     print(data)

# # a+ means append after starts first
# with open("abc.txt",'a+') as f:
#     f.write("Write something")
#     f.seek(0)
#     data = f.read()
#     print(data)

# # rb means read binary
# with open("abc.jpg",'rb') as f:
#     data = f.read()
#     print(data)
    
# dictionary print karva json import karvu
import json

# d = {"name":"ankit","email":"ankitpatel8085@gmail.com"}
# with open ("data.json",'w') as f:
#     json.dump(d,f)

with open("data.json",'r') as f:
    data = json.load(f)
    print(data)
