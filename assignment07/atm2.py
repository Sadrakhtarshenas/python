ramz = '1386'
a = 0

while a < 3  :
    passw = int(input('enter password:'))
    a = str(passw)
    if len(a) == 4:
        if a == a:
            print('welcome')
            break
        
        elif a == a[::-1]:
            print('call the polic')
            break

        else:
            print('not welcome')
            ramz += 1
    else:
        print('try again')