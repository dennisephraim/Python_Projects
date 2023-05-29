from tkinter import *


def button_clicked():
    km = round(float(input.get()) * 1.60934, 2)
    output_label.config(text= km) 


window = Tk()
window.geometry('350x130')
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

miles_label = Label(text='Miles', font=('Times New Roman', 15, 'bold'))
miles_label.grid(row=0, column=2)

KM_label = Label(text='KM', font=('Times New Roman', 15, 'bold'))
KM_label.grid(row=1, column=2)

is_eq_to_label = Label(text='is equal to', font=('Times New Roman', 15, 'bold'))
is_eq_to_label.grid(row=1, column=0)

output_label = Label(text='0', font=('Times New Roman', 15))
output_label.grid(row=1, column=1)

input = Entry(width= 10)
input.grid(row=0, column=1)

my_button = Button(text='Calculate', command=button_clicked)
my_button.grid(row=2, column=1)









window.mainloop()