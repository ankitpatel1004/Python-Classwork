import re

st = "sun in rises in east"
# match search in only begining
# k = re.match("sun",st)
# search in all
# k = re.search("is",st)
# # findall returns all matches
# k = re.findall("is",st)
# # finditer how many times match
# k = re.finditer("in",st)
# print(next(k))
# print(next(k))

# # sub is replaceble
# k = re.sub("s","T",st)
# # split is seprater
# k = re.split("is",st)
# print(k)

# k = re.search("h.l","hello python")
# k = re.search("h.l","hlo python")
# k = re.search("^Hello","Hello Python")
# k = re.search("^Hello","Java Hello Python")
# k = re.search("python$","Hello python")
# k = re.search("python$","Hello python Hello java")
# # matches zero or more, check pt, pyt, pyyt
# k = re.search("py*t","pthon")
# k = re.search("py*t","pyhon")
# # matches one or more, check yt, yyt, yyyt
# k = re.search("py+t","pyython")
# k = re.search("py+t","pthon")
# # matches zero or one, check t or yt
# k = re.search("py?t","python")
# k = re.search("py?t","pyhon")

# k = re.findall(r"\bhello\b","hello python")

# print(k)

# number = input("Enter number : ")
# k = re.match(r"^[0-9]{10}$",number)
# if k is None:
#     print("Invalid number")
# else:
#     print(number)

# st = input("Enter your name : ")
# k = re.match(r"^[A-Za-z]+$",st)
# if k is None:
#     print("Invalid data")
# else:
#     print(st)

# email = "ankitpatel8085@gmail.com"
# k = re.match("^[a-z0-9_-]+@[a-z]+\\.[a-z]{2,5}$",email)
# print(k)

# password = input("Enter your password : ")
# p = re.match("^[A-Za-z0-9!@#$%^&*()_-]{8,15}$",password)
# print(p)

password = input("Enter your strong password : ")
p = re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_-])[A-Za-z\d!@#$%^&*()_-]{10,15}$",password)
print(p)
