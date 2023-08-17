n = int(input('enter your number:  '))
print('...')
print()
for k in range(n,0,-1):
        for a in range(1,k+1):
            print(a,end='')
        print()
for i in range(1,n + 1):
    for j in range(1,i+1):
        print(j,end='')
    print()
print('...')