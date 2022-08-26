from tkinter import *
import random

root=Tk()
root.title("Dictionary")
root.geometry("600x400")

dictionary = {'colour':['red1','lawngreen','magenta2','purple1','springgreen2','chocolate1','yellow','cyan']}

def idk():
    random_no = random.randint(0,7)
    root.configure(bg=dictionary['colour'][random_no])
    
btn = Button(root, text="click me", command=idk)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
