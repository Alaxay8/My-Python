
list = ["world","hello","soccer","computer","music","amazing", "game"]


def game():
    import random
    word = random.choice(list)
    health = len(word)
    hidden = "*" * len(word)
    character = ""
    answer = ""
    print(hidden)
    while True:

        enter = str(input("Enter"))
        if enter == str(word):
            answer = character + enter
            print(answer)
            print("WOW")
            break
        elif enter != str(word) and str(word).__contains__(enter):
            answer = answer + enter
            print(answer)
        else:
            health = health - 1
            print("Wrong, You have",health, "try")
            if health == 0:
                print("Game Over")
    while True:
        restart = input("Do you want Restart? [yes/no]")
        if restart == "yes":
            game()
        elif restart == "no":
            print("Thank You")
            break
game()


