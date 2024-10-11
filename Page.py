import tkinter as tk;
from tkinter import PhotoImage
import os
import sys

# create root window
root = tk.Tk()

# root window title and dimension
root.title("Xenoblade Chronicles 2 Randomizer")
# Set geometry (widthxheight)
root.geometry('1000x600')

# Function to get the correct path for resources
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # Temporary folder for bundled files
    else:
        base_path = os.path.dirname(__file__)  # Directory of the script

    return os.path.join(base_path, relative_path)

# Load the icon using the resource path function
icon_path = resource_path('Images\XC2Icon.png')
icon = PhotoImage(file=icon_path)

root.iconphoto(False, icon)

root.mainloop()