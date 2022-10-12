import random

from replit import clear

from hangman_art import game_over_art, good_work, stages, welcome
from hangman_words import word_list


def arr(n=3):
    return list(range(n))


print(welcome)

chosen_word = random.choice(word_list)
print(chosen_word)

plots = list(map(lambda n: "_", arr(len(chosen_word))))

wrong_guesses = []

lives = 6
game_over = False

while not game_over:
    print(" ".join(plots))
    print("\n")
    guess_letter = input("Guess a letter: ")

    clear()

    if guess_letter in wrong_guesses:
        print(f"You've already guessed '{guess_letter}'")

    for index in range(0, len(chosen_word)):
        letter = chosen_word[index]
        if letter == guess_letter:
            plots[index] = letter

    # check if user got all the letters
    if "_" not in plots:
        result = good_work
        game_over = True

    if guess_letter not in chosen_word and guess_letter not in wrong_guesses:
        wrong_guesses.append(guess_letter)
        lives -= 1

        if lives == 0:
            result = game_over_art
            game_over = True

    print("Wrong Guesses:")
    print(", ".join(wrong_guesses))

    print(stages[lives])

print("\n")
print(result)
