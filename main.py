import trek
import wander


while True:
    print("Games")
    print("-----")
    print("0. Quit")
    print("1. Trek")
    print("2. Wander")


    choice = input("What do you want to play?")
    if choice == "0":
        break
    elif choice == "1":
        trek.start()
    elif choice == "2":
        wander.start()
    

