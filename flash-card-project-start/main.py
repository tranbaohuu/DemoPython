import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
window = tk.Tk()


my_image = tk.PhotoImage(file="flash-card-project-start/images/card_front.png")

window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(
    window,
    width=800,
    height=526,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
)
canvas.create_image(400, 263, image=my_image)
canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
canvas.create_text(
    400, 263, text="Subtitle", fill="black", font=("Ariel", 40, "italic")
)


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = tk.PhotoImage(file="flash-card-project-start/images/wrong.png")
check_image = tk.PhotoImage(file="flash-card-project-start/images/right.png")

unknow_button = tk.Button(
    window,
    image=cross_image,
    text="Unknown",
    bg=BACKGROUND_COLOR,
    font=("Ariel", 20, "bold"),
    foreground="black",
    highlightthickness=0,
)
unknow_button.grid(row=1, column=0)

know_button = tk.Button(
    window,
    image=check_image,
    text="Known",
    bg=BACKGROUND_COLOR,
    font=("Ariel", 20, "bold"),
    foreground="black",
    highlightthickness=0,
)
know_button.grid(row=1, column=1)


window.mainloop()
