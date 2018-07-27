from tkinter import *

from pygame import mixer

root = Tk()

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


playPhoto = PhotoImage(file='play.png')
playBtn = Button(root, image=playPhoto, command=play_music)
playBtn.pack()

stopPhoto = PhotoImage(file='stop.png')
stopBtn = Button(root, image=stopPhoto, command=stop_music)
stopBtn.pack()

root.mainloop()
