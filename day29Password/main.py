from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generator_passw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [ random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [ random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [ random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pass():
    passw = pass_entry.get()
    web = web_entry.get()
    email = email_entry.get()
    new_data = {web: {
        "email": email,
        "password": passw
        }
    }
    if len(passw) == 0 or len(web) == 0:
        no_word = messagebox.showinfo("WARRNING!!!", "You must fill all the field")
    else:
        try:
            with open("data.json", "r") as box:
                data = json.load(box)
        except FileNotFoundError:
            with open("data.json", "w") as box:
                json.dump(new_data, box, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as box:
                json.dump(data, box, indent=4)

        finally:
            pass_entry.delete(0, 'end')
            web_entry.delete(0, 'end')
#-----------------------------------FIND PASSWORD_______________________________


def find_password():
    passw = pass_entry.get()
    web = web_entry.get()
    email = email_entry.get()
    try:
        with open("data.json", "r") as box:
            data = json.load(box)
    except FileNotFoundError:
        no_find = messagebox.showinfo("Warning", "No Data File Found")
    else:
        try:
            find = messagebox.showinfo(f"{web}", f"Email:{data[web]['email']}\nPassword:{data[web]['password']}")
        except KeyError:
            no_find = messagebox.showinfo("Warning", "No details for the website")

    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#B4B4B3")

canvas = Canvas(width=200, height=200, bg="#B4B4B3", highlightthickness=0)
key_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=key_image)
canvas.grid(column=1, row=0)


#LABELS
web_label = Label(text="Website:", bg="#B4B4B3")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg="#B4B4B3")
email_label.grid(column=0, row=2)

pass_label = Label(text="Password:", bg="#B4B4B3")
pass_label.grid(column=0, row=3)


#ENTRY
web_entry = Entry(width=20)
web_entry.grid(column=1, row=1)
web_entry.focus()


email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "agagag@hdhdh.pl")


pass_entry = Entry(width=20)
pass_entry.grid(column=1, row=3)


#BUTTON
sear_button = Button(text="Search", width=15, command=find_password)
sear_button.grid(column=2, row=1)

gen_button = Button(text="Generate Password", width=15, command=generator_passw)
gen_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save_pass)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()