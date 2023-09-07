from tkinter import *
root = Tk()
btn1 = Button(root, text = 'Click me!', activebackground='red')
btn1.pack()
my_label = Label(root, text = 'Hello')
my_label.pack()

def click_handler():
    entry_text = entry_field.get()
    my_label = Label(root, text = f'{entry_text}')
    my_label.pack()

btn = Button(root, text='Click Me', command = click_handler)

btn.pack()

entry_field = Entry(root)
entry_field.pack()


root.mainloop()