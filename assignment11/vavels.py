calame = input("Enter your calame: ")
horoof_bozorg = ['o','u','i','e','a']
for i in calame:
    for j in range(5):
        if i == horoof_bozorg[j]:
            calame_nahaee = calame.replace(i, "!")
print(calame_nahaee)