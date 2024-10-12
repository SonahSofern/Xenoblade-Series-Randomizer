import tkinter as tk
from tkinter import PhotoImage
import os
import sys
from tkinter import filedialog
from tkinter import ttk

root = tk.Tk()

root.title("Xenoblade Chronicles 2 Randomizer 0.1.0")
root.configure(background='#632424')
root.geometry('800x800')

MainWindow = ttk.Notebook(root) 

MainWindow.bind("<FocusIn>", lambda e: MainWindow.state(["!focus"])) # removes highlights of tabs
  
TabGeneral = ttk.Frame(MainWindow) 
TabDrivers = ttk.Frame(MainWindow) 
TabBlades = ttk.Frame(MainWindow) 
TabEnemies = ttk.Frame(MainWindow) 
TabMisc = ttk.Frame(MainWindow) 
  
MainWindow.add(TabGeneral, text ='General') 
MainWindow.add(TabDrivers, text ='Drivers') 
MainWindow.add(TabBlades, text ='Blades') 
MainWindow.add(TabEnemies, text ='Enemies') 
MainWindow.add(TabMisc, text ='Misc') 

MainWindow.pack(expand = 1, fill ="both", padx=10, pady= 10) 


# icon = PhotoImage(file = os.path.join(sys._MEIPASS, 'Images\XC2Icon.png'))
# root.iconphoto(True, icon)


def UploadBDAT(event=None):
    filepath = filedialog.askopenfilename(filetypes=[("BDAT file", "*.bdat")])
    # here is the logic to use rust command on filepath if(filepath)

def Randomize():
    print("Test")

# msBdatButton = tk.Button(root, text='Browse', command=UploadBDAT)
bdatFilePathEntry = tk.Entry(root,textvariable = "", font=('calibre',22,'normal'))
# msBdatFilePathEntry = tk.Entry(root,textvariable = "", font=('calibre',10,'normal'))


bdatcommonFrame = tk.Frame(root, background='#581f1f')
bdatcommonFrame.pack(anchor="w", padx=10)
bdatButton = tk.Button(bdatcommonFrame, text='Choose your "common.bdat"', command=UploadBDAT)
bdatFilePathEntry = tk.Entry(bdatcommonFrame, width=255)
bdatButton.pack(side="left", padx=2, pady=2)
bdatFilePathEntry.pack(side="left", padx=2)
RandomizeButton = tk.Button(text='Randomize', command=Randomize)

# msBdatButton.pack(anchor="w", padx=10)
# msBdatFilePathEntry.pack(anchor="w",  padx=10, pady=5)

RandomizeButton.pack(pady=10)

root.mainloop()