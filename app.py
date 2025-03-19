from tkinter import *
from random import randint

root = Tk()
root.title("Rulla tärning")
text_Box = Label(root, text="")
text_Box.pack()

def show():
    roll = randint(1, 6)
    text_Box.config(text=roll)

show_button = Button(root, text="Rulla en T6", width=50, command=show)
show_button.pack()
Button = Button(root, text="Avsluta", width=50, command=root.destroy)
Button.pack()

root.mainloop()