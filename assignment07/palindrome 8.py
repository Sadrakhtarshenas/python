a = input('enter sentence :')

a = list(a)
b = list(a)
b.reverse()

print(a)
print(b)

if a == b :
    print('yes palindrome')
else :
    print('no palindrome')