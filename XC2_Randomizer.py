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


rowIncrement = 0
def GenOption(name, parentTab, desc, amountOfCheckBoxes = [], BadValuesList = [], ToggleableIndicesIntList=[]):
    global rowIncrement
    parentTab.bind("<FocusIn>", lambda e: parentTab.state(["!focus"])) # removes highlights of inner tabs
    optionPanel = tk.Frame(parentTab, padx=10, pady=10)
    optionPanel.grid(row=rowIncrement, column= 0, sticky="sw")

    if (rowIncrement %2 == 0):
        desColor = "#ffffff"
    else:
        desColor ="#D5D5D5"
    
    optionPanel.config(background=desColor)
    option = tk.Label(optionPanel, text=name, background=desColor, width=30, anchor="w")
    option.grid(row=rowIncrement, column=0, sticky="sw")
    optionSlider = tk.Scale(optionPanel, from_=0, to=100, orient=tk.HORIZONTAL, sliderlength=10, background=desColor, highlightthickness=0)
    optionSlider.grid(row=rowIncrement, column=1, sticky='n')
    optionDesc = tk.Label(optionPanel, text=desc, background=desColor, width=900, anchor='w')
    optionDesc.grid(row=rowIncrement, column=2, sticky="sw")
    for i in range(len(amountOfCheckBoxes)):
        var = tk.IntVar()
        var.set(0)
        box = tk.Checkbutton(optionPanel, background=desColor, text=amountOfCheckBoxes[i], variable=var, command=lambda i=i: OptionCarveouts(BadValuesList, ToggleableIndicesIntList, var.get()))
        box.grid(row=rowIncrement+i+1, column=0, sticky="sw")
    rowIncrement += 1
    return optionSlider



icon = PhotoImage(file="./_internal/Images/XC2Icon.png")
root.iconphoto(True, icon)

CommonBdatInput = ""
JsonOutput = "./_internal/JsonOutputs"
cmnBdatOutput = "RandomizedBDATOutput"

def inclRange(start, end):
     return list(range(start, end+1))

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

def OptionCarveouts( badValuesList = list, badIndexValue = int, stateOfButton = int):
    if stateOfButton == 1:
        badValuesList.append(badIndexValue)
    else:
        badValuesList.remove(badIndexValue)
    print(badValuesList)
    

DriverArtDebuffsBadValues = []

BladeSpecialReactionSlider = GenOption("Blade Special Reactions", TabBlades, "Randomizes each hit of a blade special to have a random effect such as break, knockback etc.")
BladeSpecialDamageTypeSlider = GenOption("Blade Special Damage Types", TabBlades, "Randomizes whether a blade's special deals Physical Damage or Ether Damage")
BladeSpecialButtonChallengeSlider = GenOption("Blade Special Button Challenges", TabBlades, "Randomizes what button a special uses for its button challenge")
PouchItemShopSlider = GenOption("Randomize Pouch Item Shops", TabGeneral, "Randomizes what Pouch Items appear in Pouch Item Shops")
AccessoryShopSlider = GenOption("Randomize Accessory Shops", TabGeneral, "Randomizes what Accessories appear in Accessory Shops")
ChipShopSlider = GenOption("Randomize Weapon Chip Shops", TabGeneral, "Randomizes what Weapon Chips appear in Chip Shops")
DriverArtEffectSlider = GenOption("Randomize Driver Art Debuffs", TabDrivers, "Randomizes a Driver's Art debuff effect", ["Doom"], DriverArtDebuffsBadValues)

def Main():
    random.seed(randoSeedEntry.get())
    print("seed: " + randoSeedEntry.get())
    subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe extract {bdatFilePathEntry.get()} -o {JsonOutput} -f json --pretty")

    JSONParser.RandomizeBetweenRange("Randomizing Blade Reactions", "BTL_Arts_Bl.json", "ReAct", 0, 14, BladeSpecialReactionSlider.get(), inclRange(0,14))
    JSONParser.RandomizeBetweenRange("Randomizing Blade Special Damage Type", "BTL_Arts_Bl.json", "ArtsType", 1, 2, BladeSpecialDamageTypeSlider.get(), [1,2])
    JSONParser.RandomizeBetweenRange("Randomizing Blade Special Button Challenges", "MNU_BtnChallenge2.json", "BtnType", 1, 5, BladeSpecialButtonChallengeSlider.get(), inclRange(1,5))
    JSONParser.RandomizeBetweenRange("Randomizing Pouch Items Shops", "MNU_ShopNormal.json", "DefItem", 40001, 40428, PouchItemShopSlider.get(), inclRange(40001,40428), [40106, 40107, 40280, 40282, 40284, 40285, 40300, 40387] + inclRange(40350, 40363) + inclRange(40389, 40402))
    JSONParser.RandomizeBetweenRange("Randomizing Accessory Shops", "MNU_ShopNormal.json", "DefItem",1,687, AccessoryShopSlider.get(),  inclRange(1,687), inclRange(448,455))
    JSONParser.RandomizeBetweenRange("Randomizing Chip Shops", "MNU_ShopNormal.json", "DefItem", 10001, 10060, ChipShopSlider.get(), inclRange(10001, 10060))
    JSONParser.RandomizeBetweenRange("Randomizing Driver Art Debuffs", "BTL_Arts_Dr.json", "ArtsDeBuff", 1, 35, DriverArtEffectSlider.get(), inclRange(0,35), DriverArtDebuffsBadValues)

    subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe pack {JsonOutput} -o {outDirEntry.get()} -f json")

def GenRandomSeed():
    print("Gen Random Seed")

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