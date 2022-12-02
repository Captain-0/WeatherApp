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
my_image.place(x=0, y=20)

root.mainloop()
