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


def GenOption(name, parentTab, desc, row):
    option = tk.Label(parentTab, text=name)
    option.grid(row=row, column=0, sticky="sw")
    optionSlider = tk.Scale(parentTab, from_=0, to=100, orient=tk.HORIZONTAL, sliderlength=10)
    optionSlider.grid(row=row, column=1)
    optionDesc = tk.Label(parentTab, text=desc)
    optionDesc.grid(row=row, column=2, sticky="sw")
    return optionSlider



icon = PhotoImage(file="./_internal/Images/XC2Icon.png")
root.iconphoto(True, icon)

CommonBdatInput = ""
JsonOutput = "./_internal/JsonOutputs"
cmnBdatOutput = "RandomizedBDATOutput"

def BDATDirectory():
    global CommonBdatInput
    CommonBdatInput = filedialog.askopenfilename(filetypes=[("BDAT file", "*.bdat")])
    bdatFilePathEntry.delete(0, tk.END)
    bdatFilePathEntry.insert(0, CommonBdatInput)

def OutputDirectory():
    global cmnBdatOutput
    cmnBdatOutput = filedialog.askdirectory(title="Select an output folder")
    outDirEntry.delete(0, tk.END)
    outDirEntry.insert(0, cmnBdatOutput)


BladeSpecialReactionSlider = GenOption("Blade Special Reactions", TabBlades, "Randomizes each hit of a blade special to have a random effect such as break, knockback etc.", 0)
# BladeSpecialLevelSlider = GenOption("Blade Special Levels", TabBlades, "Randomizes blades special levels 1-3", 1)
BladeSpecialDamageTypeSlider = GenOption("Blade Special Damage Types", TabBlades, "Randomizes whether a blade's special deals Physical Damage or Ether Damage", 2)
BladeSpecialButtonChallengeSlider = GenOption("Blade Special Button Challenges", TabBlades, "Randomizes what button a special uses for its button challenge", 3)
PouchItemShopSlider = GenOption("Randomize Pouch Item Shops", TabGeneral, "Randomizes what items appear in pouch item shops", 4)

def Main():
    random.seed(randoSeedEntry.get())
    print("seed: " + randoSeedEntry.get())
    subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe extract {bdatFilePathEntry.get()} -o {JsonOutput} -f json --pretty")

    JSONParser.RandomizeBetweenRange("Randomizing Blade Reactions", "BTL_Arts_Bl.json", "ReAct", 0, 14, BladeSpecialReactionSlider.get(), list(range(0,15)))
    JSONParser.RandomizeBetweenRange("Randomizing Blade Special Damage Type", "BTL_Arts_Bl.json", "ArtsType", 1, 2, BladeSpecialDamageTypeSlider.get(), [1,2])
    JSONParser.RandomizeBetweenRange("Randomizing Blade Special Button Challenges", "MNU_BtnChallenge2.json", "BtnType", 1, 5, BladeSpecialButtonChallengeSlider.get(), list(range(1,6)))
    JSONParser.RandomizeBetweenRange("Randomizing Pouch Items Shops", "MNU_ShopNormal.json", "DefItem", 40001, 40428, PouchItemShopSlider.get(), list(range(40001,40429)), [40106, 40107, 40280, 40282, 40284, 40285, 40300, 40387] + list(range(40350, 40364)) + list(range(40389, 40403)))



    subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe pack {JsonOutput} -o {outDirEntry.get()} -f json")

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
bdatFilePathEntry.insert(0, "C:/Users/benja/Desktop/XC2_Randomizer/OriginalBDAT/common.bdat")
bdatFilePathEntry.pack(side="left", padx=2)


OutputDirectoryFrame = tk.Frame(root, background='#632424')
OutputDirectoryFrame.pack(anchor="w", padx=10)

outputDirButton = tk.Button(OutputDirectoryFrame, text='Choose Output Directory', command=OutputDirectory)
outputDirButton.pack(side="left", padx=2, pady=2)

outDirEntry = tk.Entry(OutputDirectoryFrame, width=500)
outDirEntry.insert(0,"C:/Users/benja/AppData/Roaming/yuzu/load/0100E95004039001/0100E95004039001/romfs/bdat")
outDirEntry.pack(side="left", padx=2)


SeedFrame = tk.Frame(root, background='#632424')
SeedFrame.pack(anchor="w", padx=10)

seedDesc = tk.Button(SeedFrame, text="Seed", command=GenRandomSeed)
seedDesc.pack(side='left', padx=2, pady=2)

randoSeedEntry = tk.Entry(SeedFrame)
randoSeedEntry.pack(side='left', padx=2)



RandomizeButton = tk.Button(text='Randomize', command=Main)



RandomizeButton.pack(pady=10)

root.mainloop()