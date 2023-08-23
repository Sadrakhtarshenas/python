numb = int(input('num: '))
ma = 0 
for i in range(1,numb):
    if numb % i == 0:
        ma += i

if ma == numb:
    print('This is a whole number:))')
else:
    print('This is not a whole number!!!')