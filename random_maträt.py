from tkinter import *
from random import randint
import random

maträter = ["korvstråganof", "kykling salad", "spageti och kötfärsås", "hamburgare", "pizza"]

efterrätter = ["kladdkaka", "Brownies", "Rulltårta", "Daller", "chokladbollar"]

root = Tk()
root.title("Random måltid")
text_Box = Label(root, text="")
text_Box.pack()

def show_main():
    maträt = random.choice(maträter)
    text_Box.config(text=maträt)

def show_desär():
    efterrätt = random.choice(efterrätter)
    text_Box.config(text=efterrätt)

show_button1 = Button(root, text="Få en random måltid", width=50, command=show_main)
show_button1.pack()
show_button2 = Button(root, text="Få en random efterrätt", width=50, command=show_desär)
show_button2.pack()
Button = Button(root, text="Avsluta", width=50, command=root.destroy)
Button.pack()


root.mainloop()