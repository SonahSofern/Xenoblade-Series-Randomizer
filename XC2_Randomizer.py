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





icon = PhotoImage(file="./_internal/Images/XC2Icon.png")
root.iconphoto(True, icon)

CommonBdatInput = ""
JsonOutput = "./_internal/JsonOutputs"
cmnBdatOutput = "RandomizedBDATOutput"

def inclRange(start, end):
     return list(range(start, end+1))

def StartsWithHelper(startingWord, lowNum, highNum):
    listofWords = []
    for i in range(lowNum, highNum + 1):
        listofWords.append(startingWord + str(i))
    return listofWords

def DirectoryChoice(FileDescription, EntryField):
    Directory = filedialog.askdirectory(title=FileDescription)
    EntryField.delete(0, tk.END)
    EntryField.insert(0, Directory)

def OptionCarveouts( ValidValuesList = list, ToggleableIndexValue = int, stateOfButton = int):
    if stateOfButton == 1:
        if ToggleableIndexValue not in ValidValuesList:
            ValidValuesList.append(ToggleableIndexValue)
    elif stateOfButton == 0:
        if ToggleableIndexValue in ValidValuesList:
            ValidValuesList.remove(ToggleableIndexValue)
    #print(ValidValuesList)
    
OptionsRunList = []

rowIncrement = 0
def GenOption(optionName, parentTab, desc, randomize_parameters=[], ForcedBadValuesList = [],  OptionNameANDIndexValue = []):
    global rowIncrement
    global OptionsRunList
    parentTab.bind("<FocusIn>", lambda e: parentTab.state(["!focus"])) # removes highlights of inner tabs
    optionPanel = tk.Frame(parentTab, padx=10, pady=10)
    optionPanel.grid(row=rowIncrement, column= 0, sticky="sw")

    if (rowIncrement %2 == 0):
        desColor = "#ffffff"
    else:
        desColor ="#D5D5D5"
    
    optionPanel.config(background=desColor)
    option = tk.Label(optionPanel, text=optionName, background=desColor, width=30, anchor="w")
    option.grid(row=rowIncrement, column=0, sticky="sw")
    optionSlider = tk.Scale(optionPanel, from_=0, to=100, orient=tk.HORIZONTAL, sliderlength=10, background=desColor, highlightthickness=0)
    optionSlider.grid(row=rowIncrement, column=1, sticky='n')
    optionDesc = tk.Label(optionPanel, text=desc, background=desColor, width=900, anchor='w')
    optionDesc.grid(row=rowIncrement, column=2, sticky="sw")
    for i in range((len(OptionNameANDIndexValue))//2):
        var = tk.IntVar()
        OptionCarveouts(randomize_parameters[3], OptionNameANDIndexValue[i+1], var.get()) # run it initially
        box = tk.Checkbutton(optionPanel, background=desColor, text=OptionNameANDIndexValue[2*i], variable=var, command=lambda i=i: OptionCarveouts(randomize_parameters[3], OptionNameANDIndexValue[i+1], var.get()))
        box.grid(row=rowIncrement+i+1, column=0, sticky="sw")
    rowIncrement += 1
    OptionsRunList.append(lambda: JSONParser.RandomizeBetweenRange("Randomizing " + optionName, randomize_parameters[0], randomize_parameters[1], randomize_parameters[2], optionSlider.get(),randomize_parameters[3] if ForcedBadValuesList not in randomize_parameters[3] else randomize_parameters[3].remove(ForcedBadValuesList)))


GenOption("Pouch Item Shops", TabGeneral, "Randomizes what Pouch Items appear in Pouch Item Shops", [["MNU_ShopNormal.json"], StartsWithHelper("DefItem", 1, 10), inclRange(40001,40428), inclRange(40001,40428)], [40106, 40107, 40280, 40282, 40284, 40285, 40300, 40387] + inclRange(40350, 40363) + inclRange(40389, 40402))
GenOption("Accessory Shops", TabGeneral, "Randomizes what Accessories appear in Accessory Shops", [["MNU_ShopNormal.json"], StartsWithHelper("DefItem", 1, 10),inclRange(1,687),  inclRange(1,687) + inclRange(448,455)])
GenOption("Weapon Chip Shops", TabGeneral, "Randomizes what Weapon Chips appear in Chip Shops", [["MNU_ShopNormal.json"], StartsWithHelper("DefItem", 1, 10), inclRange(10001, 10060), inclRange(10001, 10060)])

GenOption("Driver Art Debuffs", TabDrivers, "Randomizes a Driver's Art debuff effect", [["BTL_Arts_Dr.json"], ["ArtsDeBuff"], inclRange(0,35), inclRange(0,35)],[], ["Doom", 21] )
GenOption("Driver Art Distances", TabDrivers, "Randomizes how far away you can cast an art", [["BTL_Arts_Dr.json"], ["Distance"], inclRange(0, 20), inclRange(1,20)])
GenOption("Driver Skill Trees", TabDrivers, "Randomizes all driver's skill trees", [["BTL_Skill_Dr_Table01.json", "BTL_Skill_Dr_Table02.json", "BTL_Skill_Dr_Table03.json", "BTL_Skill_Dr_Table04.json", "BTL_Skill_Dr_Table05.json", "BTL_Skill_Dr_Table06.json"], ["SkillID"], inclRange(1,270), inclRange(1,270)])

GenOption("Blade Special Reactions", TabBlades, "Randomizes each hit of a blade special to have a random effect such as break, knockback etc.", [["BTL_Arts_Bl.json"], StartsWithHelper("ReAct", 1, 16), inclRange(0,14), inclRange(0,14)])
GenOption("Blade Special Damage Types", TabBlades, "Randomizes whether a blade's special deals Physical Damage or Ether Damage", [["BTL_Arts_Bl.json"], ["ArtsType"], [1, 2], [1,2]])
GenOption("Blade Special Button Challenges", TabBlades, "Randomizes what button a special uses for its button challenge", [["MNU_BtnChallenge2.json"], StartsWithHelper("BtnType", 1, 3), inclRange(1,5), inclRange(1,5)])

GenOption("Enemy Drops", TabEnemies, "Randomizes enemy drop tables", [["BTL_EnDropItem.json"], StartsWithHelper("ItemID", 1, 8), inclRange(15001, 15406) + inclRange(1, 687) + inclRange(10001, 10060), inclRange(15001, 15406) + inclRange(1, 687) + inclRange(10001, 10060)])
GenOption("Enemy Size", TabEnemies, "Randomizes the size of enemies", [["CHR_EnArrange.json"], ["Scale"], inclRange(0, 1000), inclRange(1, 200) + inclRange(975,1000) + [9999]])
GenOption("Enemies", TabEnemies, "Randomizes what enemies appear in the world", [["CHR_EnArrange.json"], ["ParamID"], inclRange(1,1888), inclRange(1,1888)]) # change text name and stats?
GenOption("Enemy Move Speed", TabEnemies, "Randomizes how fast enemies move in the overworld", [["CHR_EnParam.json"], ["WalkSpeed", "RunSpeed"], inclRange(0,100), inclRange(0,100) + inclRange(250,255)])

GenOption("Music", TabMisc, "Randomizes what music plays where", [["RSC_BgmCondition.json"], ["BgmIDA", "BgmIDB", "BgmIDC", "BgmIDD"], inclRange(1,180), inclRange(1,180)])

def Main():
    global OptionsRunList
    random.seed(randoSeedEntry.get())
    print("seed: " + randoSeedEntry.get())
    subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe extract {bdatFilePathEntry.get()}/common.bdat -o {JsonOutput} -f json --pretty")
    subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe extract {bdatFilePathEntry.get()}/common_gmk.bdat -o {JsonOutput} -f json --pretty")
    subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe extract {bdatFilePathEntry.get()}/gb/common_ms.bdat -o {JsonOutput} -f json --pretty")

    for Option in OptionsRunList:
        Option()

    subprocess.run(f"./_internal/Toolset/bdat-toolset-win64.exe pack {JsonOutput} -o {outDirEntry.get()} -f json")

def GenRandomSeed():
    print(inclRange(15001, 15406) + inclRange(1, 687) + inclRange(10001, 10060))
    print("Gen Random Seed")

bdatcommonFrame = tk.Frame(root, background='#632424')
bdatcommonFrame.pack(anchor="w", padx=10)

bdatButton = tk.Button(bdatcommonFrame, text="Choose Input Folder (bdat)", command= lambda: DirectoryChoice("Choose your bdat folder", bdatFilePathEntry))
bdatButton.pack(side="left", padx=2, pady=2)

bdatFilePathEntry = tk.Entry(bdatcommonFrame, width=500)
bdatFilePathEntry.insert(0, "C:/Users/benja/Desktop/XC2_Randomizer/bdat")
bdatFilePathEntry.pack(side="left", padx=2)


OutputDirectoryFrame = tk.Frame(root, background='#632424')
OutputDirectoryFrame.pack(anchor="w", padx=10)

outputDirButton = tk.Button(OutputDirectoryFrame, text='Choose Output Folder', command= lambda: DirectoryChoice("Choose an output folder", outDirEntry))
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