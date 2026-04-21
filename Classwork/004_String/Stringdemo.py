# st = "Sun rises in East"
# print(st)

# name = "ankit"
# a = "ankit"
# print(name is a)

# #check length of string
# print(len(st))

# #string convert into lowercase
# st = "Sun rises in East ß"
# print(st.lower())
# #string convert into lowercase aggressively, also convert other languange symbol into lowercase
# st = "Sun rises in East ß"
# print(st.casefold())

# #string convert into uppercase
# print(st.upper())
# #string first word first letter convert into uppercase
# print(st.capitalize())
# #string every words first letter convert into uppercase
# print(st.title())

# #remove all space from starting and ending
# st = "     Sun rises in East     "
# print(st.strip())

# #replace s with Z
# print(st.replace("s","Z"))
# #replace s with Z one time with starting
# print(st.replace("s","Z",1))

# #position of find character
# print(st.find("e"))
# #check value true or false with string starts
# print(st.startswith("S"))
# #check value true or false with string ends
# print(st.endswith("t"))

# #split value after given data in () seprated by coma and also in ' ' and in list
# print(st.split(" "))
# print(st.split("s"))

# #value added after string start and before end
# k = "A"
# print(k.join("XYZ"))

# #check value true or false is alphabat or not
# print("abc1".isalpha())
# #check value true or false is digit or not
# print("123".isdigit())
# #check value true or false is alphanum or not 
# print("abc1$".isalnum())

# #zfill means added zero before string given by data remaning string
# print("abc".zfill(7))
# #center means space or given data added before and after string equally by center
# print("abc".center(11,'#'))


st = "abcdefghijklmn"
print(st)
#skip 2 characters starting from string
print(st[2:])
#print only given data characters from starting string
print(st[:5])
#print string between 2 to 5
print(st[2:5])
#print string reverse -5 to -1
print(st[-5:-1])
#print string 1 to 9 jump by 23
print(st[1:9:3])
#print return string
print(st[::-1])


