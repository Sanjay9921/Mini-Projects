import tkinter
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    # print(f"Your password is: {password}")

    entry_pswd.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    pswd = entry_pswd.get()

    # Validation
    if len(website) == 0 or len(pswd) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure that the fields are not empty!")
    else:
        # messagebox.showinfo(title="Title", message=f"These are the details entered: \n Email: {email} \nPassword: {pswd} \n. Is it OK to save?")
        is_ok = messagebox.askokcancel(title="Title",
                                       message=f"These are the details entered: \n Email: {email} \nPassword: {pswd} \n. Is it OK to save?")

        if is_ok:
            # with
            # opens and closes file automatically
            with open("data.txt", "a") as data_file:  # append mode
                data_file.write(f"{website} | {email} | {pswd}")
                entry_website.delete(0, END)
                entry_pswd.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Canvas Widget
canvas = Canvas(height=200, width=200)
img_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img_logo)
canvas.grid(row=0, column=1)

#Label Widgets
lbl_website = Label(text="Website:")
lbl_email = Label(text="Email/Username:")
lbl_pswd = Label(text="Password:")

lbl_website.grid(row=1, column=0)
lbl_email.grid(row=2, column=0)
lbl_pswd.grid(row=3, column=0)

#Entry Widgets
entry_website = Entry(width=35)
entry_email = Entry(width=35)
entry_pswd = Entry(width=21)

entry_website.focus()
entry_email.insert(0, "ryan.gosling@literallyme.com")

entry_website.grid(row=1, column=1, columnspan=2)
entry_email.grid(row=2, column=1, columnspan=2)
entry_pswd.grid(row=3, column=1)

#Button Widget
btn_generate_pswd = Button(text="Generate Password", command=generate_password)
btn_add = Button(text="Add", width=36, command=save)

btn_generate_pswd.grid(row=3, column=2)
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
