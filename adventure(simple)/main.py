from time import sleep

import pyfiglet


TITLE = "Monster Mansion!"
GREETING = "Hello, traveler\nWhat is your name?"
ROOMS = ['living room', 'kitchen', 'dining room', 'library', 'bathroom', 'bedroom']

ITEMS = {"laser": False, "batteries": False, "book": False}


def main():
    # displays the title
    title_art = pyfiglet.figlet_format(TITLE, font='chunky')
    print(title_art)
    sleep(3)
    print("Welcome to the Monster Mansion.")
    sleep(2)

    while True:
        room = choose_room().lower()
        print()

        if room == "living room":
            living_room()
        elif room == "kitchen":
            kitchen()
        elif room == "dining room":
            dining_room()
        elif room == "library":
            library()
        elif room == "bathroom":
            bathroom()
        elif room == "bedroom":
            bedroom()
        else:
            print("Sorry, I don't understand.")
        sleep(2)


def choose_room():
    print("\nWhich room would you like to go to?: \n")
    sleep(1)
    for room in ROOMS:
        print(room.capitalize())
    print()
    choice = input("Choose: ")
    return choice


def living_room():
    print("The living room is dark and there is a picture of a fat baby on the wall.")
    print("There is a giant black bear sleeping on the floor.")
    print()
    while True:
        choice = input("Do you want to pet the bear?(yes/no): ")
        if choice == "yes":
            print("\nYou pet the bear. It is friendly. It gives you a laser.")
            ITEMS["laser"] = True
            return
        elif choice == "no":
            return
        else:
            print("Sorry, I don't understand.")


def kitchen():
    print("The kitchen is clean and perfectly shiny.")
    print("There is a cute kitten sleeping on the floor.\n")
    while True:
        choice = input("Do you want pet the kitten?(yes/no): ")
        if choice == "yes":
            print("\nIt wasn't really a kitten! It was a bomb! It exploded!")
            sleep(1)
            print("\nGAME OVER")
            sleep(1)
            quit()
        elif choice == "no":
            return
        else:
            print("Sorry, I don't understand.")


def dining_room():
    print("The dining room has a pretty wood table with flowers in the center.")
    print("There is a piece of chocolate cake on the table.\n")
    while True:
        choice = input("Do you want eat the cake?(yes/no): ")
        if choice == "yes":
            print("\nYou eat the cake. It was poisoned!")
            sleep(1)
            print("\nGAME OVER")
            sleep(1)
            quit()
        elif choice == "no":
            return
        else:
            print("Sorry, I don't understand.")


def library():
    print("The library is very scary. All the books just say HOMEWORK on them.\n")
    while True:
        choice = input("Do you want to do your homework?(yes/no): ")
        if choice == "yes":
            print("\nYou open a heavy book to do your homework. It's really hard, so you put it in your bag to study later. "
                  "\nAlso, your mom is happy you studied.")
            ITEMS["batteries"] = True
            return
        elif choice == "no":
            return
        else:
            print("Sorry, I don't understand.")


def bathroom():
    print("The bathroom has white tiles on the floor. The toilet looks very clean.\n")
    while True:
        choice = input("Do you need to use the toilet?(yes/no): ")
        if choice == "yes":
            print("\nYou use the toilet. You feel much better now!")
            sleep(1)
            print("While washing your hands, you see some batteries in the cabinet. You take them.")
            ITEMS["book"] = True
            return
        elif choice == "no":
            return
        else:
            print("Sorry, I don't understand.")


def bedroom():
    print("You stand outside the door of the bedroom. You can hear the monster inside.\n")

    while True:
        choice = input("Are you ready to go in?(yes/no): ")
        if choice == "yes":
            break
        elif choice == "no":
            return
        else:
            print("Sorry, I don't understand.")

    print("\nThe monster stands by the window, painting a picture of three little pigs.\n")
    sleep(2)
    print("He turns towards you. It's the big bad wolf!")
    sleep(2)
    print("He tries to blow you away.")
    sleep(4)
    if ITEMS["book"]:
        print("He cannot blow you away because the big book make you heavy!\n")
        sleep(2)
    else:
        print("You are very light and he blows you way. You fly all the way to North Korea!")
        sleep(2)
        print("\nGAME OVER")
        sleep(2)
        quit()

    if ITEMS["laser"]:
        print("You pull out the laser and turn it on.")
        sleep(3)
        if ITEMS["batteries"]:
            print("It doesn't work! But you put the new batteries in.")
            sleep(2)
            print("You point it at the floor. The wolf tries to chase it!")
            sleep(2)
            print("You point it at the wall. The wolf chases it again!")
            sleep(2)
            print("\nThe wolf is having so much fun! You are best friends now!")
            sleep(2)
            print("\nYOU WIN!")
            sleep(3)
            quit()
        else:
            print("It doesn't work! The wolf is angry! He eats you!")
            sleep(1)
            print("\nGAME OVER")
            sleep(1)
            quit()

    if ITEMS["batteries"] and not ITEMS["laser"]:
        print("You throw the batteries at the wolf. They hit him in the head!")
        print("He throws them back at you! They hit you in the head!")
        print("The wolf thinks it is very funny. Then, he eats you.")
        sleep(1)
        print("\nGAME OVER")
        sleep(1)
        quit()


if __name__ == '__main__':
    main()
