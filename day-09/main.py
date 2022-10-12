# run this code in in replit.com
from replit import clear  # because of this

art = """
  /$$$$$$                                       /$$            /$$$$$$                     /$$    /$$                  
 /$$__  $$                                     | $$           /$$__  $$                   | $$   |__/                  
| $$  \__/ /$$$$$$  /$$$$$$$ /$$$$$$  /$$$$$$ /$$$$$$        | $$  \ $$/$$   /$$ /$$$$$$$/$$$$$$  /$$ /$$$$$$ /$$$$$$$ 
|  $$$$$$ /$$__  $$/$$_____//$$__  $$/$$__  $|_  $$_/        | $$$$$$$| $$  | $$/$$_____|_  $$_/ | $$/$$__  $| $$__  $$
 \____  $| $$$$$$$| $$     | $$  \__| $$$$$$$$ | $$          | $$__  $| $$  | $| $$       | $$   | $| $$  \ $| $$  \ $$
 /$$  \ $| $$_____| $$     | $$     | $$_____/ | $$ /$$      | $$  | $| $$  | $| $$       | $$ /$| $| $$  | $| $$  | $$
|  $$$$$$|  $$$$$$|  $$$$$$| $$     |  $$$$$$$ |  $$$$/      | $$  | $|  $$$$$$|  $$$$$$$ |  $$$$| $|  $$$$$$| $$  | $$
 \______/ \_______/\_______|__/      \_______/  \___/        |__/  |__/\______/ \_______/  \___/ |__/\______/|__/  |__/
"""

print(art)

print("\n--------- W E L C O M E ---------\n")

bids = []


def add_bidder(name, bid):
    bids.append({"name": name, "bid_value": bid})


name = input("What is your name? ")
bid_value = float(input("How much would you like to bid? $"))
add_bidder(name, bid_value)

while True:
    print("\n")
    other_bidders_present = input(
        "Are there any other bidders? Type 'yes' or 'no': "
    ).lower()

    if other_bidders_present == "no":
        break

    clear()

    name = input("What is your name? ")
    bid_value = float(input("How much would you like to bid? $"))
    add_bidder(name, bid_value)

# check who won
print("\n")

highest_bidder = bids[0]

for index in range(1, len(bids)):
    bidder = bids[index]
    bid_value = bidder["bid_value"]

    if bid_value > highest_bidder["bid_value"]:
        highest_bidder = bidder

print("------------------------------------")
print(
    f"The highest bidder is: {highest_bidder['name']} with a bid of ${highest_bidder['bid_value']}"
)
print("------------------------------------")
