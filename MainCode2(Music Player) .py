import pygame
import tkinter
from tkinter.filedialog import askdirectory
import os
import re


def play():
    ''' For playing music '''
    pygame.mixer.music.load(playList.get(tkinter.ACTIVE))  
    var.set(playList.get(tkinter.ACTIVE))  
    pygame.mixer.music.play()  

def stop():
    ''' To stop music '''
    pygame.mixer.music.stop()

def pause():
    ''' To pause music '''
    pygame.mixer.music.pause()

def resume():
    ''' To resume music '''
    pygame.mixer.music.unpause()

def masterButton():
    ''' The button to play/stop/pause/resume music '''
    global buttonText

    if pygame.mixer.music.get_busy():  
        pause()
        buttonText.set("Play")
    else:
        if var.get() == playList.get(tkinter.ACTIVE):  
            resume()
            buttonText.set("Pause") 
        else:
            stop()
            play() 
            buttonText.set("Pause")

def lowerVolume():
    ''' Decreases volume '''
    newVolume = pygame.mixer.music.get_volume() - 0.1
    pygame.mixer.music.set_volume(newVolume)
    volume.set(str(int(newVolume*100)) + " %")

def raiseVolume():
    ''' Increases volume '''
    newVolume = pygame.mixer.music.get_volume() + 0.1
    pygame.mixer.music.set_volume(newVolume)
    volume.set(str(int(newVolume*100)) + " %")

def setDirectory():
    ''' Sets the directory according to user '''
    global songList, playList
    directory = askdirectory() 
    os.chdir(directory)  
    songList = os.listdir()  
    playList.delete(0, tkinter.END) 
    counter = True 
    pos = 0
    for item in songList:
        if re.search(".mp3$", item):
            playList.insert(pos, item)
            pos = pos + 1
            counter = False

    if counter:  
        playList.insert(pos, "No MP3 songs found")

def packEverything():
    ''' One function for packing everything '''
    canvas.pack(fill="both", expand=True)
    songTitle.pack()
    playList.pack(fill="both", expand="yes")
    playButton.pack(side=tkinter.TOP)
    changeDirectory.pack(side=tkinter.LEFT)
    increaseVolume.pack(side=tkinter.RIGHT)
    decreaseVolume.pack(side=tkinter.RIGHT)
    volumeLabel.pack(side=tkinter.BOTTOM)

musicPlayer = tkinter.Tk()  
musicPlayer.title('Deepu Music Player')  
musicPlayer.geometry('800x600')  
musicPlayer.configure(background='#808080')  

canvas = tkinter.Canvas(musicPlayer, bg="#0D0D0D", highlightthickness=0)
canvas.pack(fill="both", expand=True)

songList = os.listdir()  
playList = tkinter.Listbox(canvas, font="times 14", bg="#FFFFFF", selectmode=tkinter.SINGLE)  

pos = 0
counter = True  


if counter:  
    playList.insert(pos, "No MP3 songs found")


pygame.init()
pygame.mixer.init()

buttonText = tkinter.StringVar()
buttonText.set("Play")


playButton = tkinter.Button(canvas, height=2, width=10, textvariable=buttonText, command=masterButton, bg="#242B2E", fg="#23C4ED")
decreaseVolume = tkinter.Button(canvas, height=2, width=15, text="Decrease Volume", command=lowerVolume, bg="#242B2E", fg="#23C4ED")
increaseVolume = tkinter.Button(canvas, height=2, width=15, text="Increase Volume", command=raiseVolume, bg="#242B2E", fg="#23C4ED")
changeDirectory = tkinter.Button(canvas, height=2, width=15, text="Change Directory", command=setDirectory, bg="#242B2E", fg="#23C4ED")
pauseButton = tkinter.Button(canvas, height=2, width=15, text="Pause", command=pause, bg="#000000", fg="#FFE4C4")
var = tkinter.StringVar()
songTitle = tkinter.Label(canvas, font="times 16", textvariable=var, fg="#F4CE6A", bg="#207398")

volume = tkinter.StringVar()
volume.set(str(int(pygame.mixer.music.get_volume() * 100)) + " %")
volumeLabel = tkinter.Label(canvas, font="times 12", textvariable=volume, bg="#00FFFF")

packEverything()

musicPlayer.mainloop() 
