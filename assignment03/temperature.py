# سانتی گراد به کلوین
# سانتی گراد به فارنهایت
# کلوین به سانتی گراد
# کلوین به فارنهایت
# فارنهایت به سانتی گراد
# فارنهایت به کلوین

# if (operotor == '1') or ( operotor == '-'):
#     a = float(input('enter first number: '))
#     b= float(input('enter second number: '))
#     answer = a- b
#     print('your answer is', answer)
# operotor = input('enter operator:')


print("1.  Celsius to Kelvin" )
print("2.  Celsius to Fahrenheit")
print("3.  Kelvin to Celsius")
print("4.  Kelvin to Fahrenheit")
print("5.  Fahrenheit to Celsius")
print("6.  Fahrenheit to Kelvin")


temperature = input(" What do you want me to do for you? ")



if (temperature =="1") or (temperature == "Celsius to Kelvin"):
    c = float(input("Enter your number: "))
    k = c + 273.15
    print('your snswer is' ,k)

if (temperature == "2") or (temperature == "Celsius to Fahrenheit"):
    c = float(input("Enter your number: "))
    f = c * 1.8 + 32
    print("your answer is" ,f)

if (temperature =="3") or (temperature == "Kelvin to Celsius"):
    c = float(input("Enter your number: "))
    can = c - 273.15
    print("your answer is",can)

if (temperature == "4") or (temperature == "Kelvin to Fahrenheit"):
    c = float(input("Enter your number: "))
    fa = 1.8 * c + 32
    print("your answer is",fa)