import tkinter as tk
from tkinter import PhotoImage
import os
import sys
from tkinter import filedialog
from tkinter import ttk
import random
import subprocess
import JSONParser

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



BladeSpecialReaction = tk.Label(TabBlades, text="Blade Special Reactions")
BladeSpecialReaction.grid(row=0, column=0, sticky="s")
BladeSpecialReactionSlider = tk.Scale(TabBlades, from_=0, to=100, orient=tk.HORIZONTAL, sliderlength=10)
BladeSpecialReactionSlider.grid(row=0, column=1)
BladeSpecialReactionDescription = tk.Label(TabBlades, text="Randomizes each hit of a blade special to have a random effect such as break, knockback etc.")
BladeSpecialReactionDescription.grid(row=0, column=2, sticky="s")


icon = PhotoImage(file="./_internal/Images/XC2Icon.png")
root.iconphoto(True, icon)

filepath = ""
JsonOutput = "./_internal/JsonOutputs"
cmnBdatOutput = "RandomizedBDATOutput"

def BDATDirectory():
    global filepath
    filepath = filedialog.askopenfilename(filetypes=[("BDAT file", "*.bdat")])
    bdatFilePathEntry.delete(0, tk.END)
    bdatFilePathEntry.insert(0, filepath)

def OutputDirectory():
    global cmnBdatOutput
    cmnBdatOutput = filedialog.askdirectory(title="Select an output folder")
    outDirEntry.delete(0, tk.END)
    outDirEntry.insert(0, cmnBdatOutput)


def KingRandomize():
    random.seed(randoSeedEntry.get())
    print("seed: " + randoSeedEntry.get())
    subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe extract {filepath} -o {JsonOutput} -f json --pretty")

    JSONParser.Randomize("Randomizing Blade Reactions", "./_internal/JsonOutputs/common/BTL_Arts_Bl.json", "ReAct", 0, 14, BladeSpecialReactionSlider.get(), [43,44])

    # Randomize JSONS HERE
    subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe pack {JsonOutput} -o {cmnBdatOutput} -f json")

def GenRandomSeed():
    print("Gen Random Seed")

# msBdatButton = tk.Button(root, text='Browse', command=UploadBDAT)
# msBdatFilePathEntry = tk.Entry(root,textvariable = "", font=('calibre',10,'normal'))
# msBdatButton.pack(anchor="w", padx=10)
# msBdatFilePathEntry.pack(anchor="w",  padx=10, pady=5)

bdatcommonFrame = tk.Frame(root, background='#632424')
bdatcommonFrame.pack(anchor="w", padx=10)

bdatButton = tk.Button(bdatcommonFrame, text="Choose Input (commmon.bdat)", command=BDATDirectory)
bdatButton.pack(side="left", padx=2, pady=2)

bdatFilePathEntry = tk.Entry(bdatcommonFrame, width=500)
bdatFilePathEntry.pack(side="left", padx=2)


OutputDirectoryFrame = tk.Frame(root, background='#632424')
OutputDirectoryFrame.pack(anchor="w", padx=10)

outputDirButton = tk.Button(OutputDirectoryFrame, text='Choose Output Directory', command=OutputDirectory)
outputDirButton.pack(side="left", padx=2, pady=2)

outDirEntry = tk.Entry(OutputDirectoryFrame, width=500)
outDirEntry.pack(side="left", padx=2)


SeedFrame = tk.Frame(root, background='#632424')
SeedFrame.pack(anchor="w", padx=10)

seedDesc = tk.Button(SeedFrame, text="Seed", command=GenRandomSeed)
seedDesc.pack(side='left', padx=2, pady=2)

randoSeedEntry = tk.Entry(SeedFrame)
randoSeedEntry.pack(side='left', padx=2)



RandomizeButton = tk.Button(text='Randomize', command=KingRandomize)



RandomizeButton.pack(pady=10)

root.mainloop()