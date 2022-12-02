from tkinter import *

from PIL import Image, ImageTk

import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("WEATHER APP")
root.geometry("900x500+300+200")
root.resizable(False, False)

# SEARCH BOX

search_image = ImageTk.PhotoImage(file="images/Untitled-2.png")
my_image = Label(image=search_image)
my_image.place(x=20, y=20)

textfield = Entry(root, justify="center", width=23, font=("poppins", 25, "bold"), bg="#6f79c5", border=0, fg="white")
textfield.place(x=60, y=50)
textfield.focus()

search_icon = PhotoImage(file="images/awdadawwdad.png")
my_image_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#6f79c5")
my_image_icon.place(x=440, y=33)

root.mainloop()
