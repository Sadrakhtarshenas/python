def number(num):
    num = str(num)
    nu1 = num
    nu2 = num+num
    nu3 = num+num+num
    return int(nu1) + int(nu2) + int(nu3)
number_user = int(input("enter youre number: "))
print(number(number_user))