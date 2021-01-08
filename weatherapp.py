import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url = "https://weather.com/fr-DZ/temps/aujour/l/AGXX0001:1:AG?Goto=Redirected"

master = Tk()
master.title("Weather App")
master.config(bg="white")

img = Image.open("./index.png")
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

LocationLabel = Label(master, font=("Calibri bold", 20), bg="white")
LocationLabel.grid(row=0, sticky="N", padx=100)
master.mainloop()
