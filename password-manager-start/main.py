from itertools import count
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------  ------------- #


window = Tk()
window.title("Password Manager")
window.configure(padx=20, pady=20, bg="white")


# Pomodoro Timer Text
canvas = Canvas(window, width=400, height=400, highlightthickness=0, bg="white")
photo = PhotoImage(file="./password-manager-start/logo.png")
canvas.create_image(200, 200, image=photo)
canvas.grid(row=0, column=1)


label_website = Label(text="Website:")
label_website.grid(row=1, column=0, pady=5)
label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0, pady=5)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0, pady=5)

text_website = Entry(width=35, highlightthickness=0, bg="white", fg="black")
text_website.grid(row=1, column=1, columnspan=2, pady=5)
text_email = Entry(width=35, highlightthickness=0, bg="white", fg="black")
text_email.grid(row=2, column=1, columnspan=2, pady=5)
text_password = Entry(width=21, highlightthickness=0, bg="white", fg="black")
text_password.grid(row=3, column=1, pady=5)

button_generate = Button(text="Generate Password", highlightthickness=0, bg="white")
button_generate.grid(row=3, column=2, pady=5)
button_add = Button(text="Add", width=36, highlightthickness=0, bg="white")
button_add.grid(row=4, column=1, columnspan=2, pady=5)


window.mainloop()
