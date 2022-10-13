from random import randint

# clear func. from repl.com, run this file there (see url in readme.md)
from replit import clear

from art import logo, vs
from game_data import data

print(logo)

print("\n ------------------- Welcome! ------------------- \n")


def generate_random_num():
    # randint includes both first & second param
    return randint(0, len(data) - 1)


def display_data(person):
    return f"{person['name']}, a {person['description']}, from {person['country']}."


def get_highest(num1, num2):
    return max([num1, num2])


score = 0


def start_game():
    global score
    game_over = False

    while not game_over:
        compare_a = data[generate_random_num()]
        compare_b = data[generate_random_num()]

        # print(f"\n{compare_a['follower_count']}")
        # print(f"{compare_b['follower_count']}\n")

        print("\nCompare A:")
        print(display_data(compare_a))

        print(vs)

        print("\nCompare B:")
        print(display_data(compare_b))

        print("\nWho has more followers?")
        choice = input("Type 'a' or 'b': ").lower()

        a_followers = compare_a["follower_count"]
        b_followers = compare_b["follower_count"]

        if choice == "a" and a_followers > b_followers:
            score += 1
        elif choice == "b" and b_followers > a_followers:
            score += 1
        else:
            game_over = True

        clear()

        print("=== Game Over! ===\n" if game_over else "")

        print(f"Total Score: {score}")
        print("--------------------------\n")

    print("--------------------------")
    print("---- Followers Count: ----\n")
    print(f"{compare_a['name']}: {compare_a['follower_count']} ")
    print(f"{compare_b['name']}: {compare_b['follower_count']} ")
    print("--------------------------\n")


def main():
    play_game = input("Play game? Type 'y' or 'n': ").lower()

    if play_game == "y":
        start_game()
        main()
    else:
        print("\n--------- Happy coding! ---------\n")


main()
