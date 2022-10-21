from tkinter import *
from tkinter import messagebox
from typing import final
from pw_generator import generate_password
import pyperclip
import json


# ------------------------ PASSWORD GENERATOR ------------------------ #
def generate_random_password():
    random_password = generate_password()
    pyperclip.copy(random_password)
    password_input.insert(0, random_password)


# ------------------------ SAVE PASSWORD ------------------------ #
def save_data():
    website = website_input.get().title()
    email = email_input.get()
    password = password_input.get()
    # new_data = f"{website} | {email} | {password}\n"
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0:
        have_empty_fields = messagebox.askokcancel(
            title="Error", message="Please don't leave any empty fields."
        )
    else:

        # is_ok = messagebox.askokcancel(
        #     title=website,
        #     message=f"These are the details entered: \nEmail: {email} \nPassword: {password}\nClick 'ok' to confirm.",
        # )

        # if is_ok:
        #     with open("data.txt", mode="a") as saved_data:
        #         saved_data.write(new_data)
        #
        #         website_input.delete(0, END)
        #         password_input.delete(0, END)

        try:
            # if file already exist
            with open("data.json", mode="r") as saved_data:
                # read old data
                old_data = json.load(saved_data)

        except FileNotFoundError:
            # saved new changes to data.json
            with open("data.json", mode="w") as saved_data:
                json.dump(new_data, saved_data, indent=4)

        else:
            # add new data to old data (append)
            old_data.update(new_data)

            # saved new changes to data.json
            with open("data.json", mode="w") as saved_data:
                json.dump(old_data, saved_data, indent=4)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ------------------------ UI SETUP ------------------------ #

# ------------------------ SEARCH ------------------------ #
def search_data():
    website_to_search = website_input.get().title()

    if website_to_search.strip() != "":
        try:
            with open("data.json", mode="r") as saved_data:
                data = json.load(saved_data)

        except FileNotFoundError:
            messagebox.showerror(
                title="Error", message=f"No data associated with'{website_to_search}'."
            )
        else:
            if website_to_search in data:
                fetched_data = data[website_to_search]
                email = fetched_data["email"]
                password = fetched_data["password"]

                messagebox.showinfo(
                    title=website_to_search,
                    message=f"Email: {email}\nPassword: {password}",
                )
            else:
                messagebox.showerror(
                    title="Error",
                    message=f"No data associated with'{website_to_search}'.",
                )


FONT = (
    "Arial",
    13,
)

window = Tk()
window.title("Pomodoro")
window.config(
    padx=40,
    pady=40,
)

canvas = Canvas(
    width=200,
    height=200,
)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# website ------
website_label = Label(text="Website: ", font=FONT, pady=15)
website_label.grid(row=1, column=0)

website_input = Entry(font=FONT, width=19)
website_input.grid(row=1, column=1)

# search -----
search_btn = Button(text="Search", font=("Arial", 11), command=search_data)
search_btn.grid(row=1, column=2)

# email / username ------
email_label = Label(text="Email/Username: ", font=FONT)
email_label.grid(row=2, column=0)

email_input = Entry(font=FONT, width=35)
email_input.insert(0, "test@user.com")
email_input.grid(row=2, column=1, columnspan=2)

# password ------
password_label = Label(text="Password: ", font=FONT, pady=15)
password_label.grid(row=3, column=0)

password_input = Entry(
    font=FONT,
    width=19,
)
password_input.grid(row=3, column=1)

# generate password button ------
generate_password_btn = Button(
    text="Generate Password", font=("Arial", 11), command=generate_random_password
)
generate_password_btn.grid(row=3, column=2)

# add pw button ------
add_btn = Button(text="Add", width=35, font=FONT, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()
