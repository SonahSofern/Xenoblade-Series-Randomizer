from tkinter import *

def ResizeWindow(top:Toplevel, innerFrame:Frame, padx = 37, pady = 20, maxHeight = 700):
    innerFrame.update_idletasks()  # Ensure the geometry is up to date
    w = innerFrame.winfo_width() + padx
    h = min(innerFrame.winfo_height() + pady, maxHeight)
    top.geometry(f"{w}x{h}")
    top.update()
 
    
