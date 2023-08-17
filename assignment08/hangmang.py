import random
ostan_ha= ['khorasan','tehran','semnan','sistan','esfahan','yazd','mazandran','golestan']
answer = random.choice(ostan_ha)
health = 6

bordgame = []
for i in range(len(answer)):
    bordgame.append('_')
while True:
    print(' '.join(bordgame))
    print(health * '❤')

    if health == 0:
        print("game over")
        break
    letter = input("enter a letter: ")
    if letter in answer:
        idx = answer.index(letter)
        bordgame[idx] = letter
        continue
    else:
        health -= 1
        print(health)