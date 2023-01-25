from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

#search box
# search_img= PhotoImage(file="sicon.png")
# myImage = Label(image = search_img)
# myImage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=20, y=20)
textfield.focus()

search_icon = PhotoImage(file="searcgi.png")
myImageIcon=Button(image=search_icon, borderwidth=0, cursor="hand2")
myImageIcon.place(x=400, y=34)
root.mainloop()