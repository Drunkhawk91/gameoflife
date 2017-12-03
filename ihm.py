# -*- coding: utf-8 -*-
from Tkinter import *
from PIL import ImageTk, Image
import os


fenetre = Tk()
img = ImageTk.PhotoImage(Image.open("image.png"))
panel = Label(fenetre, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
