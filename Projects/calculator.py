# first we should type name Mathematical operations for calculator.
import math

print('1 +')
print('2 -')
print('3 *')
print('4 /')


Question = input('What operation do you want me to do for you? ')

if ( Question == '1') or ( Question == '+'):
    num1 = float(input('Enter your first number: '))
    num2 = float(input('Enter your second number: '))
# M and O is mean Mathematical operations in Variable.
    MO = num1 + num2
    print(MO)

elif ( Question == '2') or ( Question == '-'):
    num1 = float(input('Enter your first number: '))
    num2 = float(input('Enter your second number: '))
    MO = num1 - num2
    print(MO)

elif ( Question == '3') or ( Question == '*'):
    num1 = float(input('Enter your first number: '))
    num2 = float(input('Enter your second number: '))
    MO = num1 * num2 
    print(MO)

elif ( Question == '4') or ( Question == '/'):
    num1 = float(input('Enter yor first number: '))
    num2 = float(input('Enter your second number: '))
    MO = num1 / num2 
    print(MO)