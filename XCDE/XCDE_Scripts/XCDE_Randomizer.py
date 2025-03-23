import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # Allows us to use the scripts folder as a module
from tkinter import PhotoImage, ttk
from tkinter import *
import tkinter as tk
root = Tk()
import Options, SeedNames, IDs
import  os, sys, subprocess
from scripts import SavedOptions, JSONParser, Helper, GUISettings, PermalinkManagement, UI_Colors, Seed, Interactables
from tkinter.font import Font
import tkinter as tk
from scripts.GUISettings import *


Game = "XCDE"
Version = "1.0.0"
JsonOutput = "./XCDE/_internal/JsonOutputs"

SavedOptionsFileName = f"SavedOptionsv{Version}.txt"
if getattr(sys, 'frozen', False):  # If the app is running as a bundled executable
    isOnefile = True
else:
    isOnefile = False
    
SavedOptions.loadData([GUISettings.fontSizeSave, GUISettings.fontType, GUISettings.GUITheme], "GUISavedOptions.txt", f"{Game}/GUI")


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
TabGameModeOuter = ttk.Frame(MainWindow)
TabFunnyOuter = ttk.Frame(MainWindow)

# Canvas 
TabGeneralCanvas = Canvas(TabGeneralOuter) 
TabCharactersCanvas = Canvas(TabCharactersOuter) 
TabEnemiesCanvas = Canvas(TabEnemiesOuter) 
TabMiscCanvas = Canvas(TabMiscOuter)
TabQOLCanvas = Canvas(TabQOLOuter)
TabGameModeCanvas = Canvas(TabGameModeOuter)
TabFunnyCanvas = Canvas(TabFunnyOuter)

# Actual Scrollable Content
TabGeneral = ttk.Frame(TabGeneralCanvas)
TabCharacters = ttk.Frame(TabCharactersCanvas) 
TabEnemies = ttk.Frame(TabEnemiesCanvas) 
TabMisc = ttk.Frame(TabMiscCanvas)
TabQOL = ttk.Frame(TabQOLCanvas)
TabGameMode = ttk.Frame(TabGameModeCanvas)
TabFunny = ttk.Frame(TabFunnyCanvas)


GUISettings.CreateScrollBars([TabGeneralOuter, TabCharactersOuter, TabEnemiesOuter, TabMiscOuter, TabQOLOuter, TabGameModeOuter, TabFunnyOuter],[TabGeneralCanvas, TabCharactersCanvas, TabEnemiesCanvas, TabMiscCanvas, TabQOLCanvas, TabGameModeCanvas, TabFunnyCanvas],[TabGeneral, TabCharacters, TabEnemies, TabMisc, TabQOL, TabGameMode, TabFunny])

# Tabs
MainWindow.add(TabGeneralOuter, text ='General') 
MainWindow.add(TabCharactersOuter, text ='Characters') 
MainWindow.add(TabEnemiesOuter, text ='Enemies') 
MainWindow.add(TabQOLOuter, text = 'Quality of Life')
MainWindow.add(TabGameModeOuter, text='Game Modes')
MainWindow.add(TabFunnyOuter, text='Funny')
MainWindow.add(TabMiscOuter, text ='Misc.') 
MainWindow.pack(expand = True, fill ="both", padx=10, pady=10) 

Tabs = {
    1: TabGeneral,
    2: TabCharacters,
    3: TabEnemies,
    4: TabMisc,
    5: TabQOL,
    6: TabFunny,
    7: TabGameMode
}

Interactables.OptionList.sort(key= lambda x: x.name) # Sorts alphabetically
for opt in Interactables.OptionList: # Cant reference directly because of circular imports :/
    opt.DisplayOption(Tabs[opt.tab], root, defaultFont, GUISettings.defGUIThemeVar.get())

def ShowTitleScreenText():
    JSONParser.ChangeJSONLine(["bdat_common_ms/MNU_title_ms.json"],[8], ["name"], f"Randomizer v{Version}", Game="XCDE") # Change Title Version to Randomizer vX.x.x


def GenRandomSeed(randoSeedEntryVar):
    randoSeedEntryVar.set(Seed.RandomSeedName(SeedNames.Nouns, SeedNames.Verbs))

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
SavedOptions.loadData(EntriesToSave + Interactables.OptionList, SavedOptionsFileName, Game)
EveryObjectToSaveAndLoad = list((x.checkBoxVal for x in EntriesToSave)) + list((x.checkBoxVal for x in Interactables.OptionList)) + list((x.spinBoxVal for x in Interactables.OptionList if x.spinBoxVal is not None)) + list((sub.checkBoxVal for x in Interactables.OptionList for sub in x.subOptions))

# Permalink Options/Variables
permalinkFrame = ttk.Frame(root,style="NoBackground.TFrame")
permalinkEntry = ttk.Entry(permalinkFrame, width=MaxWidth, textvariable=permalinkVar)
CompressedPermalink = PermalinkManagement.GenerateCompressedPermalink(randoSeedEntry.get(), EveryObjectToSaveAndLoad, Version)
permalinkVar.set(CompressedPermalink)
permalinkButton = ttk.Button(permalinkFrame, text="Settings")
permalinkFrame.pack(padx=10, pady=2, anchor="w")
permalinkButton.pack(side="left", padx=2)
permalinkEntry.pack(side='left', padx=2)
PermalinkManagement.AddPermalinkTrace(EveryObjectToSaveAndLoad, permalinkVar, seedEntryVar, Version, lambda:Interactables.UpdateAllStates())


# Bottom Left Progress Display Text
randoProgressDisplay = ttk.Label(text="", anchor="e", padding=2, style="BorderlessLabel.TLabel")
areaFiles = []
for id in IDs.areaFileListNumbers:
    areaFiles.append(f"bdat_ma{id}")
# Randomize Button
RandomizeButton = ttk.Button(text='Randomize', command=(lambda: GUISettings.Randomize(RandomizeButton,fileEntryVar, randoProgressDisplay, bdat_path, permalinkVar, randoSeedEntry, JsonOutput, outputDirVar, Interactables.OptionList, ["bdat_common", "bdat_menu_psv", "bdat_menu_ttrl"] + areaFiles, ["bdat_common_ms", "bdat_menu_psv_ms"],[lambda: ShowTitleScreenText()] )))
RandomizeButton.place(relx=0.5, rely=1, y= -10, anchor="s")
RandomizeButton.config(padding=5)

# Options Cog
if isOnefile:  # If the app is running as a bundled executable
    icon_path = os.path.join(sys._MEIPASS, 'Images', 'SmallSettingsCog.png')
else:  # If running as a script (not bundled)
    icon_path = "./_internal/Images/SmallSettingsCog.png"
Cog = PhotoImage(file=icon_path)
SettingsButton = ttk.Button(image=Cog, command=lambda: GUISettings.OpenSettingsWindow(root, defaultFont, GUISettings.defGUIThemeVar, Game))
SettingsButton.pack(pady=10, padx=10, side='right', anchor='e') 

root.protocol("WM_DELETE_WINDOW", lambda: (SavedOptions.saveData(EntriesToSave + Interactables.OptionList, SavedOptionsFileName, Game), root.destroy()))
GUISettings.LoadTheme(defaultFont, GUISettings.defGUIThemeVar.get())


root.mainloop()

