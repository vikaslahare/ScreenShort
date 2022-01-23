from cgitb import grey, text
from importlib.resources import path
from msilib.schema import Icon
from tkinter import font
from tkinter.ttk import Button
from unicodedata import name
import pyautogui
import tkinter as tk
from tkinter import *
import webbrowser



root = tk.Tk()


# create application title
root.title('ScreenShort')

greeting= tk.Label(root, text="Made by vikas lahare", font=100, bg="darkgrey")
greeting.pack()


# create Social Links labels
def callback(url):
    webbrowser.open_new(url)

link1 = Label(root, text="Follow me on GitHub", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("https://github.com/vikaslahare"))

link2 = Label(root, text="Follow me on Instagram", fg="blue", cursor="hand2")
link2.pack()
link2.bind("<Button-1>", lambda e: callback("https://instagram.com/__vikas__05"))

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

# create here screen short method
def myscreenshort():
    sc = pyautogui.screenshot()
    sc.save(r'ScreenShort.png')

# create a button for take screenshort
myButton = tk.Button(text='Take ScreeShort', command=myscreenshort, bg='darkgrey', fg='black', font=15)
canvas1.create_window(150, 150, window=myButton)

#create a close(Exit) button
def close():
    root.destroy()

exit_button = Button(root, text='Exit', command=close, width=10, height=2, bg='grey', font=15)
exit_button.pack(padx=200, pady=20)

tk.mainloop()