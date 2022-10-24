import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

words = {}
current_card = {}

try:
    data = pandas.read_csv("data/remaining_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")


def flip_card():
    english = current_card["English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english, fill="white")

    canvas.itemconfig(card_bg_img, image=card_back_img)


def next_card():
    global current_card
    global flip_card_timer

    window.after_cancel(flip_card_timer)

    current_card = random.choice(words)
    french = current_card["French"]

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french, fill="black")

    canvas.itemconfig(card_bg_img, image=card_front_img)

    # flip card after 3s
    flip_card_timer = window.after(3000, func=flip_card)


def is_known():
    words.remove(current_card)

    data = pandas.DataFrame(words)
    data.to_csv("data/remaining_words.csv", index=False)

    next_card()


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_card_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 35, "italic"))

card_word = canvas.create_text(400, 263, text="word", font=("Arial", 50, "bold"))

cross_image = PhotoImage(
    file="images/wrong.png",
)
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(
    row=1,
    column=0,
)

check_image = PhotoImage(
    file="images/right.png",
)
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# get random french word when the app starts
next_card()

window.mainloop()
