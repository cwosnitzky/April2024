import os
import sys
from time import sleep
import random

import pyfiglet

TITLE = "Ikki's Run!"
GREETING = "Hello, traveler\nWhat is your name?"
TEXT_DELAY = 0.2

ate_pizza = False
pressed_button = False
has_flashlight = False

rooms = ['entrance', 'pizza_room', 'left_room']


def main():
    # clears the terminal
    os.system('cls')

    # displays the title
    title_art = pyfiglet.figlet_format(TITLE, font='chunky')
    sys.stdout.write(title_art)

    # gets globals
    global ate_pizza
    global pressed_button
    global has_flashlight

    # begins the game
    current_room = 'start'
    display_text(GREETING)
    player_name = input()
    display_text('Welcome, ' + player_name + ', to Castle Ikkinstein. There is a great monster inside. I hope you are ready.')
    print()
    sleep(1)
    if player_name.lower() == 'quit':
        quit()

    # game loop
    while True:
        if current_room == 'end' or current_room == 'game_over':
            play_again = input('Would you like to play again? (y/n): ')
            if play_again.lower() == 'y':
                current_room = 'start'
                ate_pizza = False
                pressed_button = False
                has_flashlight = False
            elif play_again.lower() == 'n':
                sys.exit()
            else:
                continue
        elif current_room == 'pizza_room':
            current_room = pizza_room()
        elif current_room == 'left_room':
            current_room = left_room()
        elif current_room == 'entrance':
            current_room == cake_room()

        if reward == 'pizza':
            ate_pizza = True
        elif reward == 'button':
            pressed_button = True
        elif reward == 'flashlight':
            has_flashlight = True
        if story[current_room]['actions'][action]['next'] != 'stay':
            current_room = story[current_room]['actions'][action]['next']


def pizza_room():
    actions = {
        ''
    }
    if not ate_pizza:
        text = 'This room is bright and cheerful, with a great window and blue curtains.\nThere is pizza on the table.'
    else:
        text = 'This room is bright and cheerful, with a great window and blue curtains.\nThere is an empty plate on the table.'

    display_text(text)
    action = get_action(story[current_room])
    display_text(story[current_room]['actions'][action]['text'])
    reward = story[current_room]['actions'][action]['reward']


def cake_room():
    pass


def left_room():
    pass


def get_action(room: dict):
    prompt = 'What would you like to do?'
    options = ''
    for action_name, action in room['actions'].items():
        options += "\n" + action_name.upper() + " : " + action['description']

    while True:
        print()
        display_text(prompt)
        sleep(1)
        choice = input(options + '\n\n')
        if choice.lower() in room['actions'].keys():
            return choice
        elif choice.lower() == 'quit':
            quit()
        else:
            print('Nope.')


def display_text(text):
    for char in text:
        if char != '\n':
            sleep_time = random.uniform(0.05, 0.15)
        else:
            sleep_time = .5
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(sleep_time)
    print()


if __name__ == '__main__':
    main()