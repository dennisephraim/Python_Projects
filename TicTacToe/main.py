from tkinter import *

window = Tk()
window.title("TicTacToe")
window.config(padx=50, pady=50)
# window.geometry('400x400')


def play():
    play = int(move.get()) -1
    current_box = all_boxes[play]
    current_box.config(text="X", font=('Arial', 50, 'bold'))
    move.delete(0, END)


# Labels
box1 = Label(text='1') 
box1.grid(row=0, column=0)

box2 = Label(text='',) 
box2.grid(row=0, column=1)

box3 = Label(text='',) 
box3.grid(row=0, column=2)

box4 = Label(text='',) 
box4.grid(row=1, column=0)

box5 = Label(text='',) 
box5.grid(row=1, column=1)

box6 = Label(text='',) 
box6.grid(row=1, column=2)

box7 = Label(text='') 
box7.grid(row=2, column=0)

box8 = Label(text='',) 
box8.grid(row=2, column=1)

box9 = Label(text='',) 
box9.grid(row=2, column=2)

all_boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]
print(all_boxes)
# Button
player = Button(text='Play', command=play)
player.grid(row=3, column=1)

# Entries
move = Entry(width=5)
move.grid(row=3, column=2)
move.focus()




window.mainloop()