import random

COMMANDS = ("fire", "warp", "quit")

WORLD = ("Earth", "Mars", "Luna")

def start():
    print("Hostile aliens have invaded the solar system. You must stop them!")
    while True:
        c = ""
        while not c in COMMANDS:
            print("Commands are ", COMMANDS)
            c = input("What will you do: ")
            c = c.lower()
        if c == "fire":
            fire()
        elif c == "warp":
            warp()
        elif c == "quit":
            return


def warp():
    l = ""
    while not l in WORLD:
        l = input("Where do you want to warp? ")
        l = l.capitalize()
    print("Zwooop!")
    print("You have arrived at " + l)


def fire():
    r = str(random.randint(1, 10))
    print("You have destroyed " + r + " hostile aliens.")




    