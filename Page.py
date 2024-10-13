import tkinter as tk
from tkinter import PhotoImage
import os
import sys
from tkinter import filedialog
from tkinter import ttk
import random
import subprocess

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

filepath = ""

def UploadBDAT():
    global filepath
    filepath = filedialog.askopenfilename(filetypes=[("BDAT file", "*.bdat")])
    bdatFilePathEntry.delete(0, tk.END)
    bdatFilePathEntry.insert(0, filepath)

def Randomize():
    random.seed(randoSeedEntry.get())
    print("seed: " + randoSeedEntry.get())
    subprocess.run(f"./bdat-toolset-win64.exe extract {filepath} -o OutputJsons -f json --pretty")

def GenRandomSeed():
    print("Gen Random Seed")

# msBdatButton = tk.Button(root, text='Browse', command=UploadBDAT)
# msBdatFilePathEntry = tk.Entry(root,textvariable = "", font=('calibre',10,'normal'))
# msBdatButton.pack(anchor="w", padx=10)
# msBdatFilePathEntry.pack(anchor="w",  padx=10, pady=5)

bdatcommonFrame = tk.Frame(root, background='#632424')
bdatcommonFrame.pack(anchor="w", padx=10)

bdatButton = tk.Button(bdatcommonFrame, text='Browse for "common.bdat"', command=UploadBDAT)
bdatButton.pack(side="left", padx=2, pady=2)

bdatFilePathEntry = tk.Entry(bdatcommonFrame, width=500)
bdatFilePathEntry.pack(side="left", padx=2)


SeedFrame = tk.Frame(root, background='#632424')
SeedFrame.pack(anchor="w", padx=10)

seedDesc = tk.Button(SeedFrame, text="Seed", command=GenRandomSeed)
seedDesc.pack(side='left', padx=2, pady=2)

randoSeedEntry = tk.Entry(SeedFrame)
randoSeedEntry.pack(side='left', padx=2)


RandomizeButton = tk.Button(text='Randomize', command=Randomize)



RandomizeButton.pack(pady=10)

root.mainloop()