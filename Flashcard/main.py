import pandas
import random
from tkinter import *
from PIL import Image, ImageTk
BACKGROUND_COLOR = "#B1DDC6"
new_word = ''

timer = None
try:
    data = pandas.read_csv('data/words_to_learn.csv')    
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
finally:
    data_list = data.to_dict(orient='records')

# ---------------------------- CREATING NEW FLASHCARDS ------------------------------- #


def next_card_known():
    global data, data_list  
    check = data.index[data['French'] == new_word['French']].tolist()

    data = data.drop(int(check[0]))
    data.to_csv('data/words_to_learn.csv', index=False)
    data_list.remove(new_word)
    next_card()
    
    
def next_card():
    global new_word, timer, data_list
    window.after_cancel(timer)
    canvas.itemconfig(title_text, text='French', fill='#000000')
    canvas.itemconfig(display, image= card_front)
    new_word = random.choice(data_list)
    canvas.itemconfig(word, text= new_word['French'], fill='#000000')

    timer = window.after(3000, flash)
    
def flash():
    canvas.itemconfig(display, image= card_back)
    canvas.itemconfig(word, text= new_word['English'], fill= '#FAFAEB')
    canvas.itemconfig(title_text, text= "English", fill= '#FAFAEB')
    
    
   

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
timer = window.after(3000, flash)

canvas = Canvas(width= 700, height=450, bg=BACKGROUND_COLOR, highlightthickness=0)
r_s = Image.open('images\card_back.png')
resize = r_s.resize((700, 450))
l_s = Image.open('images\card_front.png')
l_resize = l_s.resize((700, 450))

card_back = ImageTk.PhotoImage(resize)
card_front = ImageTk.PhotoImage(l_resize)

display = canvas.create_image(350, 225, image=card_front)

word = canvas.create_text(350, 225, text='word', font=("Arial", 60, 'bold'))
title_text = canvas.create_text(350, 110, text='', font=("Arial", 40, 'italic'))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cbutton_img = PhotoImage(file= 'images\correct.png')
correct_button = Button(image=cbutton_img, highlightthickness=0, command=next_card_known)
correct_button.grid(column=1, row=1)

xbutton_img = PhotoImage(file= 'images\wrong.png')
wrong_button = Button(image=xbutton_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()


window.mainloop()
