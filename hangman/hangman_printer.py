
def try_guesses(word, guess_list):
    current_guess = ''
    for letter in word:
        if letter not in guess_list:
            current_guess += '_'
        else:
            current_guess += letter
    if current_guess == word:
        return True
    else:
        print(current_guess)
    return False
