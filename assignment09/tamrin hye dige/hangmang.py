import random
import pyfiglet

Animals_1 = ["cat", "dog", "cow", "pig", "fly", "eik", "fox", "bat", "ant", "bee"]
Animals_2 = ["deer", "crab", "duck", "fish", "goat", "wolf", "tang", "lion", "hare", "frog"]
Animals_3 = ["dhole", "bison", "fossa", "lemur", "xerus", "prawn", "moose", "liger", "zorse", "sloth"]
Colors_1 = ["red", "blue", "black", "white", "green", "orange", "gold", "gray", "coral", "purple"]
Colors_2 = ["teal", "cyan", "pink", "bice", "puce", "jade", "aero", "fawn", "finn", "erin"]
Colors_3 = ["azure", "ebony", "beige", "yellow", "coquelicot", "magenta", "fallow", "champagne", "hibiscus", "ginger"]
Musical_instruments_1 = ["harp", "flute", "guitar", "drums", "tuba", "organ", "sitar", "piano", "ukelele", "violin"]
Musical_instruments_2 = ["banjo", "bugle", "bagpipes", "accordion", "bassoon", "keyboard", "maracas", "triangle", "cymbals", "clarinet"]
Musical_instruments_3 = ["didgeridoo", "mandolin", "harpsichord", "saxophone", "xylophone", "trombone", "harmonica", "mridangam", "	euphonium", "harmonium"]
Sports_1 = ["soccer", "tennis", "golf", "boxing", "skiing", "pool", "rugby", "karate", "archery", "judo"]
Sports_2 = ["basketball", "baseball", "volleyball", "cricket", "bowling", "fencing", "rowing", "handball", "sailing", "hiking"]
Sports_3 = ["badminton", "snowboarding", "skateboarding", "taekwondo", "gymnastics", "paddleboarding", "equestrian", "snowmobiling", "bobsledding", "orienteering"]
Clothes_1 = ["skirt", "cap", "hat", "vest", "scarf", "dress", "boots", "tie", "socks", "ring"]
Clothes_2 = ["bathrobe", "jumper", "overalls", "mittens", "diaper", "singlet", "cardigan", "sweater", "swimsuit", "blazer"]
Clothes_3 = ["sunglasses", "pullover", "waistcoat", "earrings", "trenchcoat", "earmuffs", "umbrella", "mortarboard", "longsleevetop", "businessshoes"]
while True:
    result= pyfiglet.figlet_format("Welcome to Hangman game!")  
    print(result) 
    while True:
        choose_category = int(input("1_Animals.2_Colors.3_Musical_instruments.4_Sports.5_Clothes.enter number of the category you have chosen: "))
        if choose_category == 1:
            Animals_level = int(input("1_easy.2_medium.3_difficult.enter number of the Animals category level:(deafult = 1)."))
            if Animals_level == 2:
                word = random.choice(Animals_2)
            elif Animals_level == 3:
                word = random.choice(Animals_3)
            else:
                word = random.choice(Animals_1)
            break
        elif choose_category == 2:
            Colors_level = int(input("1_easy.2_medium.3_difficult.enter number of the Colors category level:(deafult = 1)."))
            if Colors_level == 2:
                word = random.choice(Colors_2)
            elif Colors_level == 3:
                word = random.choice(Colors_3)
            else:
                word = random.choice(Colors_1)
            break

        elif choose_category == 3:
            Musical_instruments_level = int(input("1_easy.2_medium.3_difficult.enter number of the Musical_instruments category level:(deafult = 1)."))
            if Musical_instruments_level == 2:
                word = random.choice(Musical_instruments_2)
            elif Musical_instruments_level == 3:
                word = random.choice(Musical_instruments_3)
            else:
                word = random.choice(Musical_instruments_1)
            break

        elif choose_category == 4:
            Sports_level = int(input("1_easy.2_medium.3_difficult.enter number of the Sports category level:(deafult = 1)."))
            if Sports_level == 2:
                word = random.choice(Sports_2)
            elif Sports_level == 3:
                word = random.choice(Sports_3)
            else:
                word = random.choice(Sports_1)
            break

        elif choose_category == 5:
            Clothes_level = int(input("1_easy.2_medium.3_difficult.enter number of the Clothes category level:(deafult = 1)."))
            if Clothes_level == 2:
                word = random.choice(Clothes_2)
            elif Clothes_level == 3:
                word = random.choice(Clothes_3)
            else:
                word = random.choice(Clothes_1)
            break
        else:
            print("your number of the category is not in range(1, 5)(deafult = Animals , level = easy)")
            try_again = input("do you want to chosen agian?(y, n)")
            if try_again != "y":
                word = random.choice(Animals_1)
                break
    hearts = (len(word) * 1.5) // 1
    show_word = []
    number_of_true_char = 0
    for i in range(len(word)):
        show_word.append("_")
    while True:
    
        print("".join(show_word))
        print("❤" * int(hearts))
        if hearts == 0:
            print("Game over")
            break
        if not("_" in show_word):
            print("Hip Hip Hoorey!")
            break
        user_char = input("enter your character : ").lower()
        idx = 0
        if user_char in word:
            for j in word:
                if user_char == j:
                    show_word[word.index(j, idx)] = user_char
                idx += 1  
        else:
            print("your character is not exist")
            hearts -= 1
    try_again = input("do you want to try agian?(y, n)")
    if try_again != "y":
        break