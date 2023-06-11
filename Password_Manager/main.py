from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for value in range(randint(8, 10))]
    sym_list = [choice(symbols) for value in range(randint(2, 4))]
    num_list = [choice(numbers) for value in range(randint(2, 4))]

    password_list = letters_list + sym_list + num_list

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        saved_email = data[website]['email']
        saved_password = data[website]['password']
    except FileNotFoundError:
        messagebox.showinfo(title= website, message='No Data Text Found')  
    except KeyError:
        messagebox.showinfo(title= website, message='No Details for the website exists')  
    else:
        messagebox.showinfo(title= website, message=f'Email: {saved_email} \nPassword: {saved_password}')        


def save_password():
    website_name = website_entry.get()
    email_name = email_entry.get()
    password = password_entry.get()

    new_data = {website_name: {
        'email' : email_name,
        'password': password
    },
    }

    if len(website_name) == 0 or len(email_name) == 0:
        messagebox.showinfo(title='Oops', message="Please do not leave any fields blank!")
    else:
        try:      
            file = open("data.json", 'r')
            data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent= 4)
        else:
            file = open('data.json', 'w')
            data.update(new_data)
            json.dump(data, file, indent=4)
            file.close()
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady=50)

canvas = Canvas(width= 200, height=200)
lock_img = PhotoImage(file= 'logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Buttons
gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky= "w")

search_button = Button(text="Search", width= 14, command=search_password)
search_button.grid(column=2, row=1)

#Entries
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1, sticky= "w")
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2, sticky= "w")
email_entry.insert(0, "ephhraimakai-nettey@yale.edu")

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3, sticky= "w")




window.mainloop()