print("1.  Celsius to Kelvin" )
print("2.  Celsius to Fahrenheit")
print("3.  Kelvin to Celsius")
print("4.  Kelvin to Fahrenheit")
print("5.  Fahrenheit to Celsius")
print("6.  Fahrenheit to Kelvin")
print("7. exit()")
temperature = input(" What do you want me to do for you? ")

# while (u != '7') or (u != 'exit'):

while (temperature != 7) or (temperature != "exit") or (temperature != "()"):
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




if (temperature == "5") or (temperature == "Fahrenheit to Celsius"):
    c = float(input("Enter your number: "))
    san = (c - 32) / 1.8
    print("your answer is",san)




if (temperature == "6") or (temperature == "Fahrenheit to Kelvin"):
    
    c = float(input("Enter your number: "))
    kel = c + 273.15
    print("your answer is",kel)
else:
    print("byy")
