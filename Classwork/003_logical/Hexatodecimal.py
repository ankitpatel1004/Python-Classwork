# number = '9B'
# for i in number:
#     print(i)

number = '15A'

l = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

p = 0
sum = 0
for i in number[::-1]:
    sum=(l.index(i)*pow(16,p))
    p+=1
print(sum)
