# 1
# 12
# 123
# 1234
# 12345

lines=5
# for j in range(lines):
#     for i in range(j+1):
#         print(i+1,end="")
#     print()

# 1
# 23
# 456
# 78910

# lines=4
# n=1
# for j in range(lines):
#     for i in range(j+1):
#         print(n,end="")
#         n+=1
#     print()

# 1
# 23
# 456
# 78910
# 1112131415

# lines=5
# n=1
# for j in range(lines):
#     for i in range(j+1):
#         print(n,end="")
#         n+=1
#     print()

# 5
# 45
# 345
# 2345
# 12345

# lines=5
# for j in range(lines,0,-1):
#     for i in range(lines-j+1):
#         print(j+i,end="")
#     print()

# 0
# 10
# 010
# 1010
# 01010

lines=5

for j in range(lines):
    for i in range(j+1):
        print((i+j)%2,end="")
    print()
    