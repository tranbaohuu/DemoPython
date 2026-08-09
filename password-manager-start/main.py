from itertools import count
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------  ------------- #


window = Tk()
window.title("Password Manager")
window.configure(padx=20, pady=20)


# Pomodoro Timer Text
canvas = Canvas(window, width=400, height=400, highlightthickness=0)
photo = PhotoImage(file="./password-manager-start/logo.png")
canvas.create_image(200, 200, image=photo)
canvas.pack()


window.mainloop()
