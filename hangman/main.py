import random
from hangman_printer import try_guesses

word_list = ['dog', 'cat', 'money', 'chicken', 'kitchen', 'house', 'shoe']


def main():
    word = random.choice(word_list)
    guess_list = []
    winner = False
    wrong_guesses = 0

    try_guesses(word, guess_list)

    while wrong_guesses < 5 and not winner:
        guess = input('Please, guess a letter or a word: ')
        # checks if the guess is a word
        if len(guess) > 1:
            # checks if the word is correct
            if guess.upper() == word.upper():
                winner = True
                break
            else:
                print('Try again!')
                wrong_guesses += 1
                guess_list.append(guess)

        # checks if the guess is a letter
        elif len(guess) == 1:
            """Check of duplicate guess only if there is time.
            if guess in guesses_list:  # checks if you already guessed that
                print('You already guessed that. Try again.')"""

            # checks if the guess is in the word
            if guess in word:
                print('Great guess!')
                guess_list.append(guess)
            else:
                print('Try again!')
                wrong_guesses += 1
                guess_list.append(guess)

        winner = try_guesses(word, guess_list)

    # Ending Message (give them this one)
    if winner:
        print(f'YOU GOT IT!! The word was "{word}"!')
    else:
        print(f'YOU LOSE!! The word was "{word}"!')


if __name__ == '__main__':
    main()
