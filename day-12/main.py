import random

# run on replit.com
from replit import clear

print(
    """
   ____     _   _ U _____ u ____    ____          _____    _   _  U _____ u      _   _       _   _   __  __     ____  U _____ u   ____     
U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u      |_ " _|  |'| |'| \| ___"|/     | \ |"|   U |"|u| |U|' \/ '|uU | __")u\| ___"|/U |  _"\ u  
\| |  _ / \| |\| | |  _|" <\___ \/<\___ \/         | |   /| |_| |\ |  _|"      <|  \| |>   \| |\| |\| |\/| |/ \|  _ \/ |  _|"   \| |_) |/  
 | |_| |   | |_| | | |___  u___) | u___) |        /| |\  U|  _  |u | |___      U| |\  |u    | |_| | | |  | |   | |_) | | |___    |  _ <    
  \____|  <<\___/  |_____| |____/>>|____/>>      u |_|U   |_| |_|  |_____|      |_| \_|    <<\___/  |_|  |_|   |____/  |_____|   |_| \_\   
  _)(|_  (__) )(   <<   >>  )(  (__))(  (__)     _// \\_  //   \\  <<   >>      ||   \\,-.(__) )(  <<,-,,-.   _|| \\_  <<   >>   //   \\_  
 (__)__)     (__) (__) (__)(__)    (__)         (__) (__)(_") ("_)(__) (__)     (_")  (_/     (__)  (./  \.) (__) (__)(__) (__) (__)  (__)
"""
)


def check_input(guess_num, random_num):
    if guess_num > random_num:
        return "Too high"

    if guess_num < random_num:
        return "Too low"

    return "correct"


def start_game(difficulty, random_num):
    """"""
    lives = 5 if difficulty == "hard" else 10
    print(f"\nYou have {lives} attempts remaining to guess the number.\n")
    guess_correctly = False

    while lives > 0:
        lives -= 1

        guess_num = int(input("Make a guess: "))

        result = check_input(guess_num, random_num)

        print("" if result == "correct" else result)

        if result == "correct":
            guess_correctly = True
            break

        print(f"\nYou have {lives} attempts remaining to guess the number.\n")

    if guess_correctly:
        clear()
        print(f"\nAttempts: {lives}")
        print(f"-------- Nice! The number I'm thinking was {random_num}.--------\n")
    else:
        clear()
        print(f"\n-------- Game Over! .--------\n")
        print(f"Random number: {random_num}")
        print(f"-------------------------------\n")


# ! MAIN =====================================================================


print("\n------------- Welcome to the Number Guessing Game! -------------\n")
print("Guess the number between 1 to 100.")


def main():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    random_num = random.randint(1, 101)
    print("random_num: ", random_num)

    start_game(difficulty, random_num)

    while True:
        play_again = input("Play again? Type 'y' or 'n': ")

        if play_again == "y":
            main()
        else:
            print("\n------------- Happy coding! -------------\n")
            break


main()
