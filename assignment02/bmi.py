vazn = float(input("Enter your vazn (kg): "))
ghad = float(input('Enter your ghad (cm): '))
f = ghad * ghad
a = vazn / f
if a < 18.5:
    print("you are thin!!")
elif a >= 18.5  <= 24.9:
    print("your body is normal:)")
elif a >= 25.0 <= 29.9:
    print("your body is The borderline of obesity:!")
elif a >= 30.0 <= 34.9:
    print("your body is fat:/")
elif a >= 35:
    print("your body is very fat:(!")
