from cgitb import text
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0

    window.after_cancel(timer)
    canvas.itemconfig(count_down_text, text="00:00")
    timer_title.config(text="Timer")
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    reps += 1

    # LONG BREAK
    if reps % 8 == 0:
        seconds = LONG_BREAK_MIN * 60
        reps = 0

        timer_title.config(text="BREAK", fg=RED)

    elif reps % 2 == 0:
        # SHORT BREAK
        seconds = SHORT_BREAK_MIN * 60

        timer_title.config(text="BREAK", fg=PINK)
    else:
        timer_title.config(text="WORK", fg="#000")
        # seconds = WORK_MIN * 60
        seconds = 3

    # takes seconds
    count_down(seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    formatted_min = f"0{count_min}" if count_min < 10 else count_min
    formatted_sec = f"0{count_sec}" if count_sec < 10 else count_sec

    if count >= 0:
        global timer
        canvas.itemconfig(count_down_text, text=f"{formatted_min}:{formatted_sec}")
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        repeat = math.floor(reps / 2)
        check_marks.config(text="✔" * repeat)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=20, bg=GREEN)


timer_title = Label(
    text="Timer",
    font=(
        FONT_NAME,
        35,
        "bold",
    ),
    bg=GREEN,
    fg=YELLOW,
    pady=15,
)
timer_title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

count_down_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold")
)
canvas.grid(row=1, column=1)


start_btn = Button(text="Start", font=(FONT_NAME, 14), command=start_timer)
start_btn.grid(row=3, column=0)

check_marks = Label(text="✔" * reps, bg=GREEN, font=(FONT_NAME, 18))
check_marks.config(pady=30)
check_marks.grid(row=3, column=1)

reset_btn = Button(text="Reset", font=(FONT_NAME, 14), command=reset_timer)
reset_btn.grid(row=3, column=2)


window.mainloop()
