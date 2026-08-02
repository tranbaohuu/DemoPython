from itertools import count
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
def reset_timer():
    canvas.itemconfig(timer_text, text="00:00")
    # cancel the timer global variable to stop the countdown
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ----------Ï--------------------- #
def start_timer():
    count_down(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    # format the count to display in minutes and seconds with 02d format
    # itemconfig is used to change the text of the timer_text item in the canvas
    canvas.itemconfig(timer_text, text=f"{count // 60:02d}:{count % 60:02d}")
    if count > 0:
        # declare global variable timer to be used in reset_timer function
        global timer
        timer = window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=50, bg=YELLOW)

# title
label_timer = tkinter.Label(
    window, text="Timer", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN
)
label_timer.grid(row=0, column=1)


# Pomodoro Timer Text
canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=photo)
timer_text = canvas.create_text(
    103, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white"
)
canvas.grid(row=1, column=1)

# Buttons
start_button = Button(window, text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(window, text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Add tick mark
label_check_mark = Label(
    window, text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold")
)
label_check_mark.grid(row=3, column=1)

window.mainloop()
