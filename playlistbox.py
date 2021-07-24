from tkinter import*
from typing import List
import pygame
root = Tk()

root.title('spring.com MP3 player')
root.iconbitmap('D:/coding/project/face_detector/images/starbucks.png')
root.geometry("500x300")

# Initialize pygame Mixer

pygame.mixer.init()

# create playlist Box
song_box = Listbox(root, bg="yellow", fg="green", width=60)
song_box.pack(pady=20)


root.mainloop()
