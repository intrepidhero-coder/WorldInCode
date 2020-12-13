import random

YN = ["yes", "no"]
NSEW = ["north", "south", "east", "west"]
dunes_count = 0

def get_input(message, prompt, valid_input):
    print(message)
    command = input(prompt).lower()
    while not command in valid_input:
        print("Sorry I don't understand that.")
        print("Valid commands are: " + ", ".join(valid_input))
        command = input(prompt).lower()
    return command


def start():
    name = input("What is your name? ")
    print("Hello " + name)
    command = get_input("You are standing on a empty stretch of road, running east and west. To the north are rugged looking mountains. To south, are sandy hills.",
        "Which way do you want to go? ", NSEW)
    if command == "north":
        mountains()
    elif command == "south":
        dunes()
    elif command == "east":
        road()
    elif command == "west":
        road()


def mountains():
    print("You get lost and die of thirst. Sorry.")
    end()


def dunes():
    global dunes_count
    if dunes_count > 0:
        tired = "You are getting " + ("very"*dunes_count) + " tired."
    else:
        tired = ""
    dunes_count += 1
    command = get_input("You are lost in the the rolling, sandy dunes. They seem to go on forever. " + tired,
        "Which way do you want to go? ", NSEW)
    if command in ["north", "east", "west"]:
        dunes()
    elif command == "south":
        if dunes_count > 1:
            sea()
        else:
            dunes()

def sea():
    print("You have come at last to the sea and can go no farther.")
    end()

def road():
    r = random.randint(1, 10)
    if r == 3:
        print("VVVVRRROOOOOOOOOOOOOOM!!!\n\nYou are hit by a bus. Why were you walking on the road anyway?")
        end()
    else:
        start()

def end():
    print("The game is over.")

