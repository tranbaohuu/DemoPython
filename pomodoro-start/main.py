from tkinter import Tk, Canvas, PhotoImage

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
window.configure(padx=100, pady=50)

canvas = Canvas(window, width=200, height=224)
photo =  PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=photo)
canvas.create_text(103,130,text="00:00", font=(FONT_NAME,35,"bold"), fill="white")
canvas.pack()

window.mainloop()