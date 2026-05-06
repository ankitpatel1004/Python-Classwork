def even():
    count = 0
    num = 2
    while count < 10:
        yield num
        num += 2
        count += 1
number = even()
for i in number:
    print(i)