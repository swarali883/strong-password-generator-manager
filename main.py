from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    pass_input.insert(0, password)
    # print(f"Your password is: {password}")

    pyperclip.copy(password)           #already copied to clipboard to directly paste

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        web_input.get(): {
            "email": user_input.get(),
            "password": pass_input.get(),
        }
    }
    if len(web_input.get()) == 0 or len(pass_input.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        # is_ok = messagebox.askokcancel(title=web_input.get(), message=f"These are the details entered: \nEmail: {user_input.get()} \nPassword: {pass_input.get()} \nIs it ok to save?")
        # if is_ok:
        try:
            with open ("data.json", "r") as data_file:
                # read data, mode="r"
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)      #saving the updated data, write in json, mode="w"
        else:
            data.update(new_data)  # update the data, ie add new data

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)      #saving the updated data, write in json, mode="w"
        finally:
                web_input.delete(0, END)
                pass_input.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = web_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)
web_input = Entry(width=33)
web_input.grid(column=1, row=1)
web_input.focus()

user_label = Label(text="Email/Username:")
user_label.grid(column=0,row=2)
user_input = Entry(width=52)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(0, "patilswarali83@gmail.com")

pass_label = Label(text="Password:")
pass_label.grid(column=0,row=3)
pass_input = Entry(width=33)
pass_input.grid(column=1, row=3)

generator_button = Button(text="Generate Password", command=generate_password)
generator_button.grid(column=2, row=3)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()