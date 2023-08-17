na = list(input('enter your sentence: '))
new_da = input('enter your string: ')
c = 0
for i in range(len(na)):
    if new_da == na[0]:
        c += 1
    na.pop(0)
print(c)