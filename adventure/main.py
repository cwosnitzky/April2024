from display import Display
from time import sleep

import pyfiglet

from story_loader import load


TITLE = "Ikki's Run!"
GREETING = "Hello, traveler\nWhat is your name?"

story = load('story.json')

# initializes the display
display = Display(slow_text=False)


def main():
    global display
    # clears the terminal
    display.clear()

    # displays the title
    title_art = pyfiglet.figlet_format(TITLE, font='chunky')
    display.title(title_art)

    # sets reward booleans
    ate_pizza = False
    window_open = False
    has_flashlight = False
    took_torch = False
    has_torch = False

    # begins the game
    current_room = 'entrance'
    display.text(GREETING)
    player_name = input()
    print()
    welcome_text = 'Welcome, ' + player_name + ', to Castle Ikkinstein. There is a great monster inside. I hope you are ready.'
    display.text(welcome_text)
    sleep(1)
    if player_name.lower() == 'quit':
        quit()

    # game loop
    while True:
        # checks for special rooms
        if current_room == 'end' or current_room == 'game_over' or current_room == 'north_korea':
            display.text(story[current_room]['text'])
            play_again = input('Would you like to play again? (y/n): ')
            if play_again.lower() == 'y':
                display.text(welcome_text)
                current_room = 'entrance'
                text = story[current_room]['text']
                ate_pizza = False
                window_open = False
                has_flashlight = False
                story['pizza_room']['actions']['eat']['skip'] = False
                story['torch_room']['actions']['take']['skip'] = False
                story['bear_room']['actions']['pet']['skip'] = False
            elif play_again.lower() == 'n':
                exit()
            else:
                continue
        elif current_room == 'pizza_room':
            if not ate_pizza:
                text = story[current_room]['text'][0]
            else:
                text = story[current_room]['text'][1]
        elif current_room == 'torch_room':
            if not took_torch:
                text = story[current_room]['text'][0]
            else:
                text = story[current_room]['text'][1]
        elif current_room == 'monster_room':
            display.text("The monster stands by the window, painting a picture of three little pigs.\n"
                         "He turns towards you. It's the big bad wolf!\n"
                         "He tries to blow you away.")
            if has_torch:
                display.text("The wind blows out the fire on the torch!")
            if ate_pizza:
                display.text("You ate the pizza, so you are heavy and don't fly away.")
            else:
                display.text("You are very light and he blows you all the way to North Korea!")
                current_room = 'north_korea'
                continue
            if has_flashlight:
                display.text("The wind could not blow out your flashlight.\n"
                             "He thinks it's fire and tries to run away!")
            else:
                display.text("He is confused. He sniffs the air.\n"
                             '"You smell like pizza," he says.\n'
                             "He eats you. You are delicious.")
                current_room = 'game_over'
                continue
            if window_open:
                display.text("He accidentally runs into the window and falls out!")
                current_room = 'end'
                continue
            else:
                display.text("He runs into the window with a crash.\n"
                             "Now, he is angry.\n"
                             "He runs at you and eats you.")
                current_room = 'game_over'
                continue
        else:
            text = story[current_room]['text']

        # display room text
        display.text(text)

        # gets player action
        action = get_action(story[current_room])

        # displays action text
        display.text(action['text'])

        # gets the reward for the action
        reward = action['reward']
        if reward == 'pizza':
            ate_pizza = True
            action['skip'] = True
        elif reward == 'window_open':
            if not window_open:
                window_open = True
            else:
                window_open = False
        elif reward == 'flashlight':
            has_flashlight = True
            action['skip'] = True
            if has_torch:
                display.text('You throw away the torch.')
                has_torch = False
        elif reward == 'torch':
            took_torch = True
            has_torch = True
            action['skip'] = True
            if has_flashlight:
                display.text('You throw away the flashlight.')
                has_flashlight = False

        # gets the next room
        if action['next'] != 'stay':
            current_room = action['next']


def get_action(room: dict):
    prompt = 'What would you like to do?'
    options = ''
    for action_name, action in room['actions'].items():
        if not action['skip']:
            options += action_name.upper() + " : " + action['description'] + '\n'

    while True:
        display.text(prompt)
        sleep(1)
        choice = input(options + '\n\n')
        if choice.lower() in room['actions'].keys():
            return room['actions'][choice]
        elif choice.lower() == 'quit':
            quit()
        else:
            print('That is not one of the options.')


if __name__ == '__main__':
    main()
