import os
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog

from pygame import mixer

root = Tk()

# Create the menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create the submenu

subMenu = Menu(menubar, tearoff=0)


def browse_file():
    global filename
    filename = filedialog.askopenfilename()


menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)


def about_us():
    tkinter.messagebox.showinfo('About Melody', 'This is a music player build using Python Tkinter by @attreyabhatt')


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)

mixer.init()  # initializing the mixer

root.title("Melody")
root.iconbitmap(r'melody.ico')

text = Label(root, text='Lets make some noise!')
text.pack(pady=10)


def play_music():
    try:
        paused  # Checks whether the 'paused' variable is initialized or not.

    except NameError:  # If not initialized then executes the code under except condition
        try:
            mixer.music.load('journey.wav')
            mixer.music.play()
            statusbar['text'] = "Playing music" + ' - ' + os.path.basename('journey.wav')
        except:
            tkinter.messagebox.showerror('File not found', 'Melody could not find the file. Please check again.')

    else:  # If initialized the it goes to the else condition
        mixer.music.unpause()
        statusbar['text'] = "Music Resumed"


def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Music Stopped"


def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = "Music Paused"


def rewind_music():
    play_music()
    statusbar['text'] = "Music Rewinded"


def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)
    # set_volume of mixer takes value only from 0 to 1. Example - 0, 0.1,0.55,0.54.0.99,1


middleframe = Frame(root)
middleframe.pack(pady=30,padx=30)

playPhoto = PhotoImage(file='play.png')
playBtn = Button(middleframe, image=playPhoto, command=play_music)
playBtn.grid(row=0, column=0, padx=10)

stopPhoto = PhotoImage(file='stop.png')
stopBtn = Button(middleframe, image=stopPhoto, command=stop_music)
stopBtn.grid(row=0, column=1, padx=10)

pausePhoto = PhotoImage(file='pause.png')
pauseBtn = Button(middleframe, image=pausePhoto, command=pause_music)
pauseBtn.grid(row=0, column=2, padx=10)


bottomframe = Frame(root)
bottomframe.pack()

rewindPhoto = PhotoImage(file='rewind.png')
rewindBtn = Button(bottomframe, image=rewindPhoto, command=rewind_music)
rewindBtn.grid(row=0,column=0)

scale = Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.grid(row=0,column=1,pady=15,padx=30)

statusbar = Label(root, text="Welcome to Melody", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
