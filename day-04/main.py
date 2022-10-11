import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

weapon_art_choices = [rock, paper, scissors]
weapon_word_choices = ["rock", "paper", "scissors"]

p1 = int(input("What do you choose?\n0 for Rock\n1 for Paper\n2 for Scissors\nAns: "))
p2 = random.randint(0, 2)

p1_word_weapon = weapon_word_choices[p1]
p2_word_weapon = weapon_word_choices[p2]

winning_picks = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

print(weapon_art_choices[p1])

print(f"Computer chose:\n {weapon_art_choices[p2]}")

if p1_word_weapon == p2_word_weapon:
    print("====== DRAW ====== ")
elif winning_picks[p1_word_weapon] == p2_word_weapon:
    print("====== You won! ======")
else:
    print("====== You lost! ======")
