import random

from replit import clear

print(
    """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
)


# print("\nDo you want to play a game of Blackjack? ")
# continue_playing = input("Type 'y' or 'n': ")


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_total(cards=[]):
    """Calculate sum of given list"""
    return sum(cards)


def blackjack(your_cards, computers_cards):
    """Blackjack Game"""

    my_cards = your_cards
    enemy_cards = computers_cards

    your_total = calculate_total(my_cards)
    computers_total = calculate_total(enemy_cards)

    print(f"Your cards: {my_cards}, current score: {your_total}")
    print(f"Computer's first card: {enemy_cards[0]}")

    result = ""

    game_over = False

    while not game_over:
        print(game_over)
        get_another_card = input(
            "\nType 'y' to get another card, 'n' to pass: "
        ).lower()

        if get_another_card == "n":
            while computers_total < 17:
                enemy_cards.append(deal_card())
                computers_total = calculate_total(enemy_cards)

                if computers_total > 21:
                    result = "You Win! Enemy busted!"
                    game_over = True
                    print("game_over: ", game_over)
                    # break inner loop
                    break

            game_over = True

        elif get_another_card == "y":
            new_card = deal_card()

            if your_total > 10 and new_card == 11:
                new_card = 1

            my_cards.append(new_card)
            your_total = calculate_total(my_cards)

            if your_total > 21:
                result = "You Lost! Busted!"
                game_over = True
                break

            blackjack(my_cards, enemy_cards)

    print("\n--------------------------\n")
    print(f"Your score: {your_total}")
    print(f"Computer's score: {computers_total}")
    print("\n---------")
    if result != "":
        print(result)

    else:
        if your_total == computers_total:
            print("D R A W")
        elif your_total > computers_total and computers_total <= 21:
            print("You Win!")
        else:
            print("You Lost!")
    print("---------\n")

    print("--------------------------\n")
    # print(your_cards, your_total)
    # print(computers_cards, computers_total)


def start_game():
    """"""
    play_blackjack = input("Let's play? Type 'y' or 'n': ")

    your_cards = [deal_card(), deal_card()]
    computers_cards = [deal_card(), deal_card()]

    if play_blackjack == "y":
        clear()
        print("\n--------- Let's Play! ---------\n")
        blackjack(your_cards, computers_cards)
        start_game()
    else:
        print("\n--------- Happy coding! ---------\n")


start_game()
