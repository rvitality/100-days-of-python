from tkinter import *

window = Tk()
window.title("Hello World!")
window.config(padx=20, pady=20)


def convert_miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    miles_to_km.config(text=km)


miles_input = Entry()

miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

miles_to_km = Label(text="")
miles_to_km.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

calculate = Button(text="Calculate", command=convert_miles_to_km)
calculate.grid(row=2, column=1)


window.mainloop()
