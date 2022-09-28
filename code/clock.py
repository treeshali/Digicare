from time import strftime
from tkinter import Label, Tk

#======= Configuring window =========
root = Tk()
root.title("")
root.geometry("1900x1000")


clock_label = Label(root,bg="black",fg="white")
clock_label.place(x = 0, y = 5)

def update_label():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_label)

update_label()



root.mainloop()