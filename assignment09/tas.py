import random
tas1 = random.randint(1 , 6)
tas2 = random.randint(1 , 6)
print("tas1:",tas1,"tas2:",tas2)
while False:
    if tas1 or tas2 == 6:
        tas1 = random.randint(1 , 6)
        tas2 = random.randint(1 , 6)
        print(tas1,tas2)
        break