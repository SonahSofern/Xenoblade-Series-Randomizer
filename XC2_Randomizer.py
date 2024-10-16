import tkinter as tk
from tkinter import PhotoImage
import os
import sys
from tkinter import filedialog
from tkinter import ttk
import random
import subprocess
import JSONParser
import json

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

def FileInsertHelper(insertIndex,  lowNum, highNum, mainString = str, pathTo = str):
    listOfFiles = []
    for i in range(lowNum, highNum):
        listOfFiles.append(pathTo + mainString[:insertIndex] + f"{i:02}" + mainString[insertIndex:]) # fstring allows us to format with 2 digits like xc2 wants
    #print(listOfFiles)
    return listOfFiles

def FindBadValuesList(filePath, keyWordList, keywordBadValueList, returnedKeyWordValue): # used for me to find a list of values from a file with certain characteristsics that i want to remove
    bad_values_found = []
    
    with open(filePath, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        
        for row in data['rows']:
            for key, value in row.items():
                if key in keyWordList and value in keywordBadValueList:
                    bad_values_found.append(row[returnedKeyWordValue]) 
    
    print(bad_values_found)


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

    if len(randomize_parameters) <= 4:
        randomize_parameters.append("")
        randomize_parameters.append([])

    print(len(ForcedBadValuesList))
    if len(ForcedBadValuesList) > 0:
        randomize_parameters[3] = [i for i in randomize_parameters[3] if i not in ForcedBadValuesList]
    OptionsRunList.append(lambda: JSONParser.RandomizeBetweenRange("Randomizing " + optionName, randomize_parameters[0], randomize_parameters[1], randomize_parameters[2], optionSlider.get(), randomize_parameters[3]))

GenOption("Pouch Item Shops", TabGeneral, "Randomizes what Pouch Items appear in Pouch Item Shops", [["common/MNU_ShopNormal.json"], StartsWithHelper("DefItem", 1, 10), inclRange(40001,40428), inclRange(40001,40428)], [40106, 40107, 40280, 40282, 40284, 40285, 40300, 40387] + inclRange(40350, 40363) + inclRange(40389, 40402))
GenOption("Accessory Shops", TabGeneral, "Randomizes what Accessories appear in Accessory Shops", [["common/MNU_ShopNormal.json"], StartsWithHelper("DefItem", 1, 10),inclRange(1,687),  inclRange(1,687) + inclRange(448,455)])
GenOption("Weapon Chip Shops", TabGeneral, "Randomizes what Weapon Chips appear in Chip Shops", [["common/MNU_ShopNormal.json"], StartsWithHelper("DefItem", 1, 10), inclRange(10001, 10060), inclRange(10001, 10060)])

GenOption("Driver Art Debuffs", TabDrivers, "Randomizes a Driver's Art debuff effect", [["common/BTL_Arts_Dr.json"], ["ArtsDeBuff"], inclRange(0,35), inclRange(0,35)],[], ["Doom", 21] )
GenOption("Driver Art Distances", TabDrivers, "Randomizes how far away you can cast an art", [["common/BTL_Arts_Dr.json"], ["Distance"], inclRange(0, 20), inclRange(1,20)])
GenOption("Driver Skill Trees", TabDrivers, "Randomizes all driver's skill trees", [["common/BTL_Skill_Dr_Table01.json", "common/BTL_Skill_Dr_Table02.json", "common/BTL_Skill_Dr_Table03.json", "common/BTL_Skill_Dr_Table04.json", "common/BTL_Skill_Dr_Table05.json", "common/BTL_Skill_Dr_Table06.json"], ["SkillID"], inclRange(1,270), inclRange(1,270)])

GenOption("Blade Special Reactions", TabBlades, "Randomizes each hit of a blade special to have a random effect such as break, knockback etc.", [["common/BTL_Arts_Bl.json"], StartsWithHelper("ReAct", 1, 16), inclRange(0,14), inclRange(0,14)])
GenOption("Blade Special Damage Types", TabBlades, "Randomizes whether a blade's special deals Physical Damage or Ether Damage", [["common/BTL_Arts_Bl.json"], ["ArtsType"], [1, 2], [1,2]])
GenOption("Blade Special Button Challenges", TabBlades, "Randomizes what button a special uses for its button challenge", [["common/MNU_BtnChallenge2.json"], StartsWithHelper("BtnType", 1, 3), inclRange(1,5), inclRange(1,5)])

GenOption("Enemy Drops", TabEnemies, "Randomizes enemy drop tables", [["common/BTL_EnDropItem.json"], StartsWithHelper("ItemID", 1, 8), inclRange(15001, 15406) + inclRange(1, 687) + inclRange(10001, 10060), inclRange(15001, 15406) + inclRange(1, 687) + inclRange(10001, 10060)])
GenOption("Enemy Size", TabEnemies, "Randomizes the size of enemies", [["common/CHR_EnArrange.json"], ["Scale"], inclRange(0, 1000), inclRange(1, 200) + inclRange(975,1000) + [9999]])
GenOption("Enemies", TabEnemies, "Randomizes what enemies appear in the world", [FileInsertHelper(2, 1,90,"maa_FLD_EnemyPop.json", "common_gmk/"), ["ene1ID", "ened2ID", "ene3ID", "ene4ID"], inclRange(1,1888), inclRange(1,1888)], [1, 3, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21,1118,1172, 1178,1179,1134,1135,1136,1154,1194,1195,1196,1197,1199,1200,332, 0, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 0, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 140, 0, 141, 142, 143, 144, 145, 146, 147, 149, 150, 151, 152, 153, 154, 155, 156, 0, 157, 158, 159, 160, 161, 0, 163, 164, 166, 165, 348, 167, 168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 220, 221, 222, 286, 348, 126, 286, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 196, 197, 198, 199, 205, 207, 208, 209, 1052, 1053, 1052, 1055, 1056, 1057, 1058, 1062, 1068, 1070, 1072, 1073, 1077, 1078, 1083, 1084, 1086, 1087, 1089, 1090, 1091, 1092, 1093, 1094, 1096, 1099, 1100, 1109, 1110, 1111, 1113, 1114, 1117, 1119, 1120, 1122, 1124, 1126, 1127, 1133, 1137, 1138, 1144, 1156, 1158, 1164, 1166, 1168, 1175, 1176, 1177, 1181, 1183, 1185, 1187, 1189, 1191, 1198, 1205, 1208, 1209, 1216, 1221, 1223, 1225, 1227, 1228, 1229, 1234, 1236, 1238, 1240, 1242, 1255, 1263, 1265, 1267, 1270, 1272, 1274, 1276, 1278, 1280, 1282, 1283, 1284, 1285, 1286, 1287, 1293, 1295, 1297, 1299, 1301, 1310, 1312, 1330, 1331, 1336, 1338, 1340, 1341, 1342, 1343, 1345, 1346, 1348, 1350, 1351, 1352, 1353, 1355, 1361, 1362, 1370, 1371, 386, 195, 354, 387, 388, 356, 189, 190, 370, 371, 372, 373, 459, 461, 463, 498, 560, 562, 564, 566, 568, 574, 579, 581, 644, 647, 649, 651, 659, 662, 683, 685, 687, 689, 718, 782, 785, 865, 867, 869, 895, 898, 1020, 1022, 1026, 1037, 1038, 1043, 346, 272, 272, 273, 273, 274, 275, 276, 277, 278, 279, 279, 280, 281, 193, 162, 325, 162, 264, 228, 229, 230, 231, 232, 233, 282, 283, 284, 1375, 1377, 210, 212, 213, 214, 215, 217, 218, 219, 272, 279, 281, 392, 1383, 1385, 1387, 1394, 1396, 1399, 1401, 0, 0, 1413, 1437, 1438, 1439, 0, 0, 0, 0, 0, 0, 0, 1486, 1487, 1488, 1491, 1496, 1499, 1502, 1505, 1506, 1507, 1521, 0, 0, 0, 0, 0, 0, 0, 1584, 1589, 1624, 1639, 1640, 1642, 0, 0, 1660, 0])
GenOption("Enemy Move Speed", TabEnemies, "Randomizes how fast enemies move in the overworld", [["common/CHR_EnParam.json"], ["WalkSpeed", "RunSpeed"], inclRange(0,100), inclRange(0,100) + inclRange(250,255)])

GenOption("Music", TabMisc, "Randomizes what music plays where", [["common/RSC_BgmCondition.json"], ["BgmIDA", "BgmIDB", "BgmIDC", "BgmIDD"], inclRange(1,180), inclRange(1,180)])

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
    FindBadValuesList("./_internal/JsonOutputs/common/CHR_EnArrange.json", ["Lv"], [0,1], "ParamID")
    # FindBadValuesList("./_internal/JsonOutputs/common_gmk/ma05a_FLD_EnemyPop.json", ["ene1ID"], inclRange(0,100000), "ene1ID")
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