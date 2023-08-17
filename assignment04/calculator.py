#start
import math

print('1 -')
print('2 +')
print('3 *')
print('4 ÷')
print('5 cotan(Degree)')
print('6 tanjan(Degree)')
print('7 cosinos(Degree)')
print('8 sinos(Degree)')
print('9 x²')
print('10 √')
print('11 |…|')
print('12 x**y')
print('13 Round the number')
print('14 log x ')
operotor = input('enter operator:')


if (operotor == '1') or ( operotor == '-'):
    a = float(input('enter first number: '))
    b= float(input('enter second number: '))
    answer = a- b
    print('your answer is', answer)


elif (operotor == '2') or (operotor == '+'):
        a = float(input('enter first number: '))
        b= float(input('enter second number: '))
        answer = a + b
        print('your answer is', answer)


elif (operotor == '3')or (operotor == '*'):
    a =float(input('enter first number: '))
    b = float(input('enter second number: '))
    answer = a * b
    print('your answer is', answer)

elif (operotor == '4') or ( operotor == '/'):
    a= float(input('enter first number: '))
    b= float(input('enter second number:'))
    answer = a/b 
    if b!=0:
        print('your number is uncorect')
    else:
        print('your number is uncorect')

    print('your answer is', answer)


elif (operotor == '5') or (operotor == 'cotan'):
    a = float(input('enter your first number:'))
    a2 = (math.cot(a))
    answer = a2 * (math.pi) / 180
    print('your answer is',answer)


elif (operotor == '6') or (operotor == 'cosinos'):
    a = float(input('enter your first number: '))
    a2 = (math.cos(a))
    answer = a2 * (math.pi) / 180
    print('your answer is',answer)


elif (operotor == '7') or (operotor == 'tan'):
    a = float(input('enter your first number: '))
    a2 = (math.tan(a))
    answer = a2 * (math.pi) / 180
    print('your answer is',answer)

elif (operotor == '8') or (operotor == 'sinos'):
    a = float(input('enter your first number: '))
    a2 = (math.sin(a))
    a3 = 1 / a2
    answer = a3 * (math.pi) / 180
    print('your answer is',answer)

elif(operotor == '10') or (operotor == 'x²'):
    a= float(input('a:'))
    answer = a * a
    print(' your answer is', answer)


elif (operotor == '9') or (operotor == '√'):
    a = float(input('a:'))
    answer = math.sqrt(a)
    print('your answer is',answer)


elif (operotor == '11') or (operotor == '|…|'):
    a= float(input('enter your first number: '))
    if a >= 0:
        print('your answer is',a)
    elif a < 0 :
        a2 = -a
        print('your answer is',a2)

elif (operotor == '11') or (operotor == 'x**y'):
    a= float(input('enter your first number: '))
    b= float(input('enter your second number: '))
    answer =(math.pow(a,b))
    print('your answer is', answer)


elif (operotor == '12') or (operotor == 'Round the number'):
    a= float(input('enter your first number: '))
    b= a % 10
    if b >= 5:
        print('your answer is',math.ceil(a))
    else:
        print('your answer is',math.floor(a))

elif (operotor == '13') or (operotor == 'log x'):
    j = int(input('enter your first number: '))
    k = int(input('is base of the logarithm: '))
    answer = (math.log(j,k))
    print('your answer is',answer)
else:
    print('this operator false')
#end