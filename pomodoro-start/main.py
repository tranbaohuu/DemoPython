from itertools import count
import tkinter
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 10

reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    canvas.itemconfig(timer_text, text="00:00")
    # cancel the timer global variable to stop the countdown
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ----------Ï--------------------- #
def start_timer():
    global reps

    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    if reps % 2 == 0:
        label_timer.config(text="Work", fg=GREEN)
        count_down(work_sec)
    else:
        if reps % 8 == 7:
            label_timer.config(text="Long Break", fg=RED)
            count_down(long_break_sec)
        else:
            label_timer.config(text="Break", fg=PINK)
            count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps

    # format the count to display in minutes and seconds with 02d format
    # itemconfig is used to change the text of the timer_text item in the canvas
    canvas.itemconfig(timer_text, text=f"{count // 60:02d}:{count % 60:02d}")
    if count > 0:
        # declare global variable timer to be used in reset_timer function
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        next_phase()
        # add tick mark for each completed work session
        label_check_mark.config(text="✓" * (reps))


def next_phase():
    global reps

    reps += 1
    if reps < 8:
        start_timer()


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
