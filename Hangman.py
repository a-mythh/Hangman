import random as ran
name = input("\n\nWhat is your name? ")
name = name.capitalize()
ans="Y"
while(ans == "Y"):
    print("\n")
    for s in range(50):
        print(" ", end="")
    print(chr(9829)+" Hey, " + name + " let's play HANGMAN "+chr(9829))
    print("")
    for s in range(57):
        print(" ", end="")
    print("Start guessing...")
    for j in range(100000):
        print("", end="")
    print()
    rand_no = ran.randint(0, 19)
    words = ["ELEPHANT", "COLOUR", "ANIMAL", "IGLOO", "CUPBOARD", "MOBILE", "SWEATER", "BEAUTIFUL", "SPOON", "COOKIES",
             "COCKROACH",
             "INTERNET", "LOCATION", "ALPHABET", "AEROPLANE", "CAPITAL", "MOUNTAIN", "GENERATE", "ELEVEN", "NEWSPAPER"]
    word = words[rand_no]
    z = ""
    inp = ""
    c = 7
    e = 0
    x = 0
    h = 0
    def Draw(c):
        for i in range(52):
            print(" ", end="")
        print(" ", end="")
        for i in range(24):
            print("_", end="")
        print()
        for i in range(9):
            for s in range(52):
                print(" ", end="")
            print("|", end="")
            for j in range(24):
                if (i == 0 and j == 15):
                    continue
                if (c == 1):
                    if ((i in range(5, 9)) and j == 3):
                        print("|", end="")
                        continue
                if (c >= 2):
                    if ((i in range(1, 9)) and j == 3):
                        print("|", end="")
                        continue
                    if (c >= 3):
                        if (i == 0 and j in range(4, 8)):
                            print("_", end="")
                            continue
                    if (c >= 4):
                        if (i == 0 and j in range(4, 12)):
                            print("_", end="")
                            continue
                    if (c >= 5):
                        if ((i == 1 and j == 6) or (i == 2 and j == 5) or (i == 3 and j == 4)):
                            print("/", end="")
                            continue
                    if (c >= 6):
                        if (i == 1 and j == 12):
                            print("|", end="")
                            continue
                    if (c >= 7):
                        if ((i == 1 or i == 2) and j == 12):
                            print("|", end="")
                            continue
                if (i == 1 or i == 2):
                    print(" ", end="")
                elif (i == 3 and j == 12):
                    print("O", end="")
                elif (i == 4 and j == 11):
                    print("/", end="")
                elif (i == 4 and j == 12):
                    print("|", end="")
                elif (i == 4 and j == 13):
                    print("\\", end="")
                elif (i == 5 and j == 12):
                    print("|", end="")
                elif (i == 6 and j == 11):
                    print("/", end="")
                elif (i == 6 and j == 13):
                    print("\\", end="")
                else:
                    print(" ", end="")
            if (i == 0):
                print(" ", end="")
            print("|")
        for s in range(52):
            print(" ", end="")
        print("|", end="")
        for i in range(24):
            print("_", end="")
        print("|")


    # word code
    while c >= 1:
        cd = 0
        x = x + 1
        n = 0
        Draw(e)
        print("\n")
        for s in range(54):
            print(" ", end="")
        print("Word: ", end="")
        for i in word:
            if i in z:
                print(i + " ", end="")
            else:
                print("_ ", end="")
                cd = cd + 1
        print("\n")
        for s in range(52):
            print(" ", end="")
        print("Attempts Remaining: ", c)
        if (x > 1):
            for s in range(52):
                print(" ", end="")
            print("Previous Guesses: ", inp)
        if cd == 0:
            print()
            for s in range(59):
                print(" ", end="")
            print("YOU WON!!! "+chr(9787))
            for s in range(50):
                print(" ", end="")
            ans = input("Do you want to play again (Y/N)?      ")
            ans = ans.upper()
            for i in range(139):
                print("=", end="")
            print()
            break
        print()
        while (inp in z) or (h >= 1):
            h = 0
            if (n >= 1):
                print("'", inp, "' has been guessed earlier")
            inp = input("Guess an Alphabet: ")
            if (inp.isalpha() == False):
                print(inp + " is not an Alphabet")
                h = 1
                continue
            if(len(inp) != 1):
                print("Invalid Input!")
                h = 1
                continue
            inp = inp.upper()
            if (inp in z):
                n = n + 1
        z = z + inp
        for i in range(139):
            print("=", end="")
        print()
        if inp not in word:
            c = c - 1
            e = e + 1

            for s in range(63):
                print(" ", end="")
            print("WRONG! "+chr(10062))
            if (c != 0):
                for s in range(54):
                    print(" ", end="")
                if(c == 1):
                    print("You have", c, "more guess")
                else:
                    print("You have", c, "more guesses")
            else:
                for s in range(48):
                    print(" ", end="")
                print("You have no more guesses remaining")
            for i in range(139):
                print("=", end="")
            print()
            if c == 0:
                Draw(e)
                print()
                for s in range(59):
                    print(" ", end="")
                print("YOU LOST!!! "+chr(10020))
                for s in range(56):
                    print(" ", end="")
                print("Word is", word)
                for s in range(50):
                    print(" ", end="")
                ans=input("Do you want to play again (Y/N)?  ")
                ans=ans.upper()
                for i in range(139):
                    print("=", end="")
                print()