import tkinter as tk;
from tkinter import PhotoImage
import os
import sys


root = tk.Tk()

root.title("Xenoblade Chronicles 2 Randomizer")

root.geometry('1000x600')

icon = PhotoImage(file = os.path.join(sys._MEIPASS, 'Images\XC2Icon.png'))

root.iconphoto(False, icon)

root.mainloop()