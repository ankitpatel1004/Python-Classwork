# for i in range(1,6):
#     print("*"*5)

# for i in range(1,6):
#     print("*"*i)

# for i in range(5,0,-1):
#     print("*"*i)

# for i in range(5):
#     print("*",end="")

# *****
# *****
# *****
# *****
# *****

# lines=5
# for j in range(lines):
#     for i in range(lines):
#         print("*",end="")
#     print()

# *
# **
# ***
# ****
# *****

# lines=5
# for j in range(lines):
#     for i in range(j+1):
#         print("*",end="")
#     print()

# *****
# ****
# ***
# **
# *

# lines=5
# for j in range(lines):
#     for i in range(lines-j):
#         print("*",end="")
#     print()

#     *
#    **
#   ***
#  ****
# *****

# lines=5
# for j in range(lines):
#     for k in range(lines-(j+1)):
#         print(" ",end="")
#     for i in range(j+1):
#         print("*",end="")
#     print()

# *****
#  ****
#   ***
#    **
#     *

# lines=5
# for j in range(lines):
#     for k in range(j):
#         print(" ",end="")
#     for i in range(lines-j):
#         print("*",end="")
#     print()

#    *
#   * *
#  * * *
# * * * *
#* * * * *

# lines=5
# for j in range(lines):
#     for k in range(lines-(j+1)):
#         print(" ",end="")
#     for i in range(j+1):
#         print("* ",end="")
#     print()

#     *
#    ***
#   *****
#  *******
# *********

# lines=5
# for j in range(lines):
#     for k in range(lines-(j+1)):
#         print(" ",end="")
#     for i in range((j*2)+1):
#         print("*",end="")
#     print()

#   *
#  * *
# * * *
#  * *
#   *

# lines=3
# for j in range(lines):
#      for k in range(lines-(j+1)):
#          print(" ",end="")
#      for i in range(j+1):
#          print("* ",end="")
#      print()
# lines=2
# for l in range(lines):
#      for m in range(l):
#          print(" ",end="")
#      for n in range(lines-l):
#          print(" *",end="")
#      print()

#     *
#    **
#   ***
#  ****
# *****

lines=5
for j in range(lines):
    print(" "*(lines-(j+1)),"*"*(j+1))
