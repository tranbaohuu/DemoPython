from itertools import count
import json
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # Import Python's random module so characters and lengths can be selected randomly.
    import random

    text_password.delete(0, END)

    # Define the characters that may be used in each part of the password.
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "*", "+"]

    # Create 8 to 10 random letters, choosing one character for each repetition.
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    # Create 2 to 4 random symbols.
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    # Create 2 to 4 random numbers.
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    # Combine the three character groups into one list.
    password_list = password_letters + password_symbols + password_numbers
    # Randomize the order so letters, symbols, and numbers are mixed together.
    random.shuffle(password_list)

    # Join the list characters into one password string with no spaces between them.
    password = "".join(password_list)
    # Insert the generated password into the password input field, starting at position 0.
    text_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # Get the values entered by the user in the UI fields.
    website = text_website.get()
    email = text_email.get()
    password = text_password.get()

    # Check whether the website or password field is empty.
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty."
        )
    else:
        # Show a confirmation dialog before saving the data.
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {email} "
            f"\nPassword: {password} \nIs it ok to save?",
        )
        if is_ok:
            # Open the data file in append mode so new entries are added at the end.
            # Open data.txt in append mode ("a"), which adds new data to the end
            # without deleting existing entries. The file is created if it does not exist.

            # txt file

            # with open("data.txt", "a") as data_file:
            #     # Write the website, email, and password to the file.
            #     data_file.write(f"{website} | {email} | {password}\n")
            #     # Clear the input fields after saving.
            #     text_website.delete(0, END)
            #     text_password.delete(0, END)

            # json file
            json_data = {"website": website, "email": email, "password": password}

            try:
                # we need open read mode to read the existing data from the file
                # Nếu không đọc dạng read mà dạng a (append) thì data cứ bị thêm mới thay vì update
                with open("data.json", "r") as data_file:
                    saved_passwords = json.load(data_file)
            except (FileNotFoundError, json.JSONDecodeError):
                saved_passwords = []

            for saved_password in saved_passwords:
                if saved_password["website"] == website:
                    saved_password.update(json_data)
                    break
            else:
                saved_passwords.append(json_data)

            with open("data.json", "w") as data_file:
                json.dump(saved_passwords, data_file, indent=4, separators=(",", ": "))

            # Clear the input fields after saving.
            text_website.delete(0, END)
            text_password.delete(0, END)


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
text_website.focus()
text_email = Entry(width=35, highlightthickness=0, bg="white", fg="black")
text_email.grid(row=2, column=1, columnspan=2, pady=5)
text_email.insert(0, "a@gmail.com")
text_password = Entry(width=21, highlightthickness=0, bg="white", fg="black")
text_password.grid(row=3, column=1, pady=5)

button_generate = Button(
    text="Generate Password",
    highlightthickness=0,
    bg="white",
    command=generate_password,
)
button_generate.grid(row=3, column=2, pady=5)
button_add = Button(
    text="Add", width=36, highlightthickness=0, bg="white", command=save
)
button_add.grid(row=4, column=1, columnspan=2, pady=5)


window.mainloop()
