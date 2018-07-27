import tkinter.messagebox
from tkinter import *

from pygame import mixer

root = Tk()

# Create the menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create the submenu

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open")
subMenu.add_command(label="Exit", command=root.destroy)


def about_us():
    tkinter.messagebox.showinfo('About Melody', 'This is a music player build using Python Tkinter by @attreyabhatt')


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)

mixer.init()  # initializing the mixer

root.geometry('300x300')
root.title("Melody")
root.iconbitmap(r'melody.ico')

text = Label(root, text='Lets make some noise!')
text.pack()


def play_music():
    mixer.music.load("journey.wav")
    mixer.music.play()


def stop_music():
    mixer.music.stop()


def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)
    # set_volume of mixer takes value only from 0 to 1. Example - 0, 0.1,0.55,0.54.0.99,1


playPhoto = PhotoImage(file='play.png')
playBtn = Button(root, image=playPhoto, command=play_music)
playBtn.pack()

stopPhoto = PhotoImage(file='stop.png')
stopBtn = Button(root, image=stopPhoto, command=stop_music)
stopBtn.pack()

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70)
mixer.music.set_volume(70)
scale.pack()

root.mainloop()
