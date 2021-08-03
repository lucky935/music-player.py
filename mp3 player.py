from tkinter import*
import pygame

root = Tk()
root.title('spring.com MP3 Player')
root.iconbitmap('c:/gui/spotify+icon-1320191405346920333_32.ico')
root.geometry("700x500")
pygame.mixer.init()

def play():
    pygame.mixer.music.load("C:/gui/audio/Milaa Yun - Haseen Dillruba.mp3")
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()

my_button = Button(root,text = "play song",font=("Helvetica", 32),command=play)
my_button.pack(pady=10)
stop_button = Button(root, text='stop',command=stop)
stop_button.pack(pady=21)




root.mainloop()

