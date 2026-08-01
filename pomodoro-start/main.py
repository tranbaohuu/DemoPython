import tkinter
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ----------Ï--------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=50, bg=YELLOW)

# title
tkinter.Label(window, text="Timer", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN).grid(row=0, column=1)

# Pomodoro Timer Text
canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=photo)
canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

# Buttons
Button(window, text="Start", highlightthickness=0).grid(row=2, column=0)
Button(window, text="Reset", highlightthickness=0).grid(row=2, column=2)
# canvas.pack()

window.mainloop()
