import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generate():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_letters = [random.choice(letters) for _ in range(nr_letters)]
    random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    random_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = random_letters + random_symbols + random_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_input.get()
    email = email_input.get()
    password = pass_input.get()

    new_data = {
        web: {
            "email": email,
            "password": password,
        }
    }
    # messagebox.showinfo(title="Title", message="message")

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Read old data
                data = json.load(data_file)  # Read, read mode and print in the console
                # print(data["Amazon"]["email"])
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)  # Write, write mode
        else:
            # Update  old data with new data
            data.update(new_data)  # Update new data, write mode

            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)  # Write, write mode
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)
        web_input.focus()
# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    # pass
    website = web_input.get()

    try:
        with open("data.json", mode="r") as data_file:
            # Read old data
            data = json.load(data_file)  # Read, read mode and print in the console
            # print(data["Amazon"])
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title=f"Error", message=f"No Data File Found")
    else:
        if website in data:
            email = data[f"{website}"]["email"]
            password = data[f"{website}"]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Entry
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
web_input = Entry(width=31)
web_input.grid(column=1, row=1)
web_input.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_input = Entry(width=50)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "adam@gmail.com")  # prewrite

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)
pass_input = Entry(width=31)
pass_input.grid(column=1, row=3)

# Button
pass_button = Button(text="Generate Password", width=15, command=password_generate)
pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)
window.mainloop()
