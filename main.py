from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for x in range(nr_letters)]
    symbols_list = [random.choice(symbols) for x in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for x in range(nr_numbers)]
    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            'email' : email,
            'password' : password
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title= "Fail", message="You can't leave any of the entries empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent= 4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                data = json.dump(new_data, data_file)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
def find_password():
    introduced_website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message= "There is no data in the file")
    else:
        if introduced_website in data.keys():
            email = data[introduced_website]['email']
            password = data[introduced_website]['password']
            messagebox.showinfo(title= "Your password", message= f"Website : {introduced_website}\n Email : {email}\n Password : {password}\n")
        else:
            messagebox.showinfo(title="Error", message= f"There is no data for {introduced_website}")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(height= 200, width= 200)
logo_img = PhotoImage(file="/Users/jasin/PasswordManager/pythonProject/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row= 0, column= 1)

#Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=30)
website_entry.grid(column= 1, row=1, columnspan= 2)
email_entry = Entry(width=35)
email_entry.grid(column= 1, row=2, columnspan= 2)
password_entry = Entry(width=21, show= "*")
password_entry.grid(column=1, row=3)

#Buttons
password_button = Button(text="Generate Password", width= 14, command=generate_password)
password_button.grid(column= 2, row= 3)
add_button = Button(text= "Add", width= 36, command=save)
add_button.grid(column = 1, row= 4, columnspan = 2)
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()