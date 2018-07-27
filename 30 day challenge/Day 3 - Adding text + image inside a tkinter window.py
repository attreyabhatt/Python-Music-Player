from tkinter import *

root = Tk()
root.geometry('300x300')
root.title("Melody")
root.iconbitmap(r'melody.ico')

text = Label(root, text='Lets make some noise!')
text.pack()

photo = PhotoImage(file='play.png')
labelphoto = Label(root, image = photo)
labelphoto.pack()

root.mainloop()
