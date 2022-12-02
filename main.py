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

logo_image = PhotoImage(file="images/icon.png")
logo = Label(image=logo_image)
logo.place(x=179, y=120)

# BOTTOM BOX

frame_image = PhotoImage(file="images/bottom.png")
frame_myimage = Label(image=frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# LABELS

label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg="black", bg="white")
label1.place(x=100, y=380)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="black", bg="white")
label2.place(x=225, y=380)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="black", bg="white")
label3.place(x=375, y=380)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="black", bg="white")
label4.place(x=570, y=380)

t = Label(font=("arial", 70, "bold"), fg="blue")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="yellow")
w.place(x=110, y=430)

h = Label(text="...", font=("arial", 20, "bold"), bg="yellow")
h.place(x=245, y=430)

d = Label(text="...", font=("arial", 20, "bold"), bg="yellow")
d.place(x=390, y=430)

p = Label(text="...", font=("arial", 20, "bold"), bg="yellow")
p.place(x=570, y=430)

root.mainloop()
