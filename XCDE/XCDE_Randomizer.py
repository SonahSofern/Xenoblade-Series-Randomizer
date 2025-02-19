import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Allows us to use the scripts folder as a module
from tkinter import PhotoImage, ttk
from tkinter import *
import tkinter as tk
root = Tk()
import Options, os, sys
from scripts import SavedOptions, JSONParser, Helper, GUISettings, PermalinkManagement, UI_Colors
import SeedNames
from tkinter.font import Font
import tkinter as tk

Game = "XCDE"
Version = "1.0.0"
CommonBdatInput = ""
JsonOutput = "./XCDE/_internal/JsonOutputs"
MaxWidth = 1000
windowWidth = "1550"
windowHeight = "900"
OptionColorLight = UI_Colors.White
OptionColorDark = UI_Colors.Gray
SavedOptionsFileName = f"SavedOptionsv{Version}.txt"
if getattr(sys, 'frozen', False):  # If the app is running as a bundled executable
    isOnefile = True
else:
    isOnefile = False
    
SavedOptions.loadData([GUISettings.fontSizeSave, GUISettings.fontType, GUISettings.GUITheme], "GUISavedOptions.txt", Game)


GUISettings.RootsForStyling.append(root)
defaultFont = Font(family=GUISettings.defFontVar.get(), size=GUISettings.defFontSizeVar.get())

root.title(f"Xenoblade Chronicles DE Randomizer v{Version}")
root.option_add("*Font", defaultFont)
root.geometry(f'{windowWidth}x{windowHeight}')

if isOnefile:
    bdat_path = os.path.join(sys._MEIPASS, 'Toolset', 'bdat-toolset-win64.exe')
else:
    bdat_path = "./XCDE/_internal/Toolset/bdat-toolset-win64.exe"

if isOnefile: 
    icon_path = os.path.join(sys._MEIPASS, 'Images', 'XCDEIcon.png')
else:
    icon_path = "./XCDE/_internal/Images/XCDEIcon.png"
icon = PhotoImage(file=icon_path)
root.iconphoto(True, icon)


# The Notebook
MainWindow = ttk.Notebook(root, height=5)
# Frames in the notebook
TabGeneralOuter = ttk.Frame(MainWindow) 
TabCharactersOuter = ttk.Frame(MainWindow) 
TabEnemiesOuter = ttk.Frame(MainWindow) 
TabMiscOuter = ttk.Frame(MainWindow) 
TabQOLOuter = ttk.Frame(MainWindow)
TabCosmeticsOuter = ttk.Frame(MainWindow)
TabGameModeOuter = ttk.Frame(MainWindow)
TabFunnyOuter = ttk.Frame(MainWindow)

# Canvas 
TabGeneralCanvas = Canvas(TabGeneralOuter) 
TabDriversCanvas = Canvas(TabCharactersOuter) 
TabEnemiesCanvas = Canvas(TabEnemiesOuter) 
TabMiscCanvas = Canvas(TabMiscOuter)
TabQOLCanvas = Canvas(TabQOLOuter)
TabCosmeticsCanvas = Canvas(TabCosmeticsOuter)
TabGameModeCanvas = Canvas(TabGameModeOuter)
TabFunnyCanvas = Canvas(TabFunnyOuter)

# Actual Scrollable Content
TabGeneral = ttk.Frame(TabGeneralCanvas)
TabDrivers = ttk.Frame(TabDriversCanvas) 
TabEnemies = ttk.Frame(TabEnemiesCanvas) 
TabMisc = ttk.Frame(TabMiscCanvas)
TabQOL = ttk.Frame(TabQOLCanvas)
TabCosmetics = ttk.Frame(TabCosmeticsCanvas)
TabGameMode = ttk.Frame(TabGameModeCanvas)
TabFunny = ttk.Frame(TabFunnyCanvas)


GUISettings.CreateScrollBars([TabGeneralOuter, TabCharactersOuter, TabEnemiesOuter, TabMiscOuter, TabQOLOuter, TabCosmeticsOuter, TabGameModeOuter, TabFunnyOuter],[TabGeneralCanvas, TabDriversCanvas, TabEnemiesCanvas, TabMiscCanvas, TabQOLCanvas, TabCosmeticsCanvas, TabGameModeCanvas, TabFunnyCanvas],[TabGeneral, TabDrivers, TabEnemies, TabMisc, TabQOL, TabCosmetics, TabGameMode, TabFunny])

# Tabs
MainWindow.add(TabGeneralOuter, text ='General') 
MainWindow.add(TabCharactersOuter, text ='Drivers') 
MainWindow.add(TabEnemiesOuter, text ='Enemies') 
MainWindow.add(TabCosmeticsOuter, text='Cosmetics')
MainWindow.add(TabQOLOuter, text = 'Quality of Life')
MainWindow.add(TabGameModeOuter, text='Game Modes')
MainWindow.add(TabFunnyOuter, text='Funny')
MainWindow.add(TabMiscOuter, text ='Misc.') 
MainWindow.pack(expand = True, fill ="both", padx=10, pady=10) 

Tabs = {
    1: TabGeneral,
    2: TabDrivers,
    3: TabEnemies,
    4: TabMisc,
    5: TabQOL,
    6: TabFunny,
    7: TabCosmetics,
    8: TabGameMode
}

Options.OptionList.sort(key= lambda x: x.name) # Sorts alphabetically
for opt in Options.OptionList: # Cant reference directly because of circular imports :/
    opt.DisplayOption(Tabs[opt.tab])

def ShowTitleScreenText():
    JSONParser.ChangeJSONLine(["common_ms/menu_ms.json"],[132], ["name"], [f"Randomizer v{Version}"]) # Change Title Version to Randomizer vX.x.x


def GenRandomSeed(randoSeedEntryVar):
    randoSeedEntryVar.set(SeedNames.RandomSeedName())

bdatcommonFrame = ttk.Frame(root, style="NoBackground.TFrame")
bdatcommonFrame.pack(anchor="w", padx=10)
bdatButton = ttk.Button(bdatcommonFrame, width=20, text="Choose Input Folder", command= lambda: Helper.DirectoryChoice("Choose your folder containing common.bdat, common_ms.bdat and common_gmk.bdat", bdatFilePathEntry))
bdatButton.pack(side="left", padx=2, pady=2)
fileEntryVar = StringVar()
bdatFilePathEntry = ttk.Entry(bdatcommonFrame, width=MaxWidth, textvariable=fileEntryVar)
bdatFilePathEntry.pack(side="left", padx=2)
OutputDirectoryFrame = ttk.Frame(root, style="NoBackground.TFrame")
OutputDirectoryFrame.pack(anchor="w", padx=10)
outputDirButton = ttk.Button(OutputDirectoryFrame, width = 20, text='Choose Output Folder', command= lambda: Helper.DirectoryChoice("Choose an output folder", outDirEntry))
outputDirButton.pack(side="left", padx=2, pady=2)
outputDirVar = StringVar()
outDirEntry = ttk.Entry(OutputDirectoryFrame, width=MaxWidth, textvariable=outputDirVar)
outDirEntry.pack(side="left", padx=2)
SeedFrame = ttk.Frame(root, style="NoBackground.TFrame")
SeedFrame.pack(anchor="w", padx=10)
seedDesc = ttk.Button(SeedFrame, text="Seed", command=lambda: GenRandomSeed(seedEntryVar))

seedDesc.pack(side='left', padx=2, pady=2)

GUISettings.RootsForStyling.append(bdatcommonFrame)

# Seed entry box
seedEntryVar = StringVar()
GenRandomSeed(seedEntryVar) # Gen a random seed if you have no save data 
randoSeedEntry = ttk.Entry(SeedFrame, width=30, textvariable=seedEntryVar)
randoSeedEntry.pack(side='left', padx=2)

permalinkVar = StringVar()


        
fileEnt = SavedOptions.SavedEntry("Input Bdats",fileEntryVar)
fileOut = SavedOptions.SavedEntry("Output Bdats", outputDirVar)
permLink = SavedOptions.SavedEntry("Permalink", permalinkVar)
seedVar = SavedOptions.SavedEntry("Seed", seedEntryVar)

# Save and Load Last Options
EntriesToSave = ([fileEnt, fileOut, permLink, seedVar])
SavedOptions.loadData(EntriesToSave + Options.OptionList, SavedOptionsFileName, Game)
EveryObjectToSaveAndLoad = list((x.checkBoxVal for x in EntriesToSave)) + list((x.checkBoxVal for x in Options.OptionList)) + list((x.spinBoxVal for x in Options.OptionList if x.spinBoxVal is not None)) + list((sub.checkBoxVal for x in Options.OptionList for sub in x.subOptions))

# Permalink Options/Variables
permalinkFrame = ttk.Frame(root,style="NoBackground.TFrame")
permalinkEntry = ttk.Entry(permalinkFrame, width=MaxWidth, textvariable=permalinkVar)
CompressedPermalink = PermalinkManagement.GenerateCompressedPermalink(randoSeedEntry.get(), EveryObjectToSaveAndLoad, Version)
permalinkVar.set(CompressedPermalink)
permalinkButton = ttk.Button(permalinkFrame, text="Settings")
permalinkButton.state(["disabled"])
permalinkFrame.pack(padx=10, pady=2, anchor="w")
permalinkButton.pack(side="left", padx=2)
permalinkEntry.pack(side='left', padx=2)
PermalinkManagement.AddPermalinkTrace(EveryObjectToSaveAndLoad, permalinkVar, seedEntryVar, Version, lambda:Options.UpdateAllStates())


# Bottom Left Progress Display Text
randoProgressDisplay = ttk.Label(text="", anchor="e", padding=2, style="BorderlessLabel.TLabel")

# Randomize Button
RandomizeButton = ttk.Button(text='Randomize', command=GUISettings.Randomize)
RandomizeButton.place(relx=0.5, rely=1, y= -10, anchor="s")
RandomizeButton.config(padding=5)

# Options Cog
if isOnefile:  # If the app is running as a bundled executable
    icon_path = os.path.join(sys._MEIPASS, 'Images', 'SmallSettingsCog.png')
else:  # If running as a script (not bundled)
    icon_path = "./XC2/_internal/Images/SmallSettingsCog.png"
Cog = PhotoImage(file=icon_path)
SettingsButton = ttk.Button(image=Cog, command=lambda: GUISettings.OpenSettingsWindow(root, defaultFont, GUISettings.defGUIThemeVar))
SettingsButton.pack(pady=10, padx=10, side='right', anchor='e') 

root.protocol("WM_DELETE_WINDOW", lambda: (SavedOptions.saveData(EntriesToSave + Options.OptionList, SavedOptionsFileName, Game), root.destroy()))
GUISettings.LoadTheme(defaultFont, GUISettings.defGUIThemeVar.get())


root.mainloop()

