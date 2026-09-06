import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
window = tk.Tk()


my_image = tk.PhotoImage(file="flash-card-project-start/images/card_front.png")

window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, width=800, height=526)

canvas = tk.Canvas(
    window,
    width=800,
    height=526,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
)
canvas.create_image(400, 263, image=my_image)
canvas.grid(row=0, column=1, columnspan=3)

label1 = tk.Label(
    window,
    text="Flash Card",
    bg=BACKGROUND_COLOR,
    font=("Ariel", 40, "italic"),
    foreground="black",
).grid(row=1, column=1)


label2 = tk.Label(
    window,
    text="Flash Card",
    bg=BACKGROUND_COLOR,
    font=("Ariel", 60, "bold"),
    foreground="black",
).grid(row=2, column=1)

window.mainloop()
