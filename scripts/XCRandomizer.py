import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # Allows us to use the scripts folder as a module
from tkinter import PhotoImage, ttk
from tkinter import *
import tkinter as tk
from scripts.GUISettings import *

class Tab():
    def __init__(self, name, outer, canvas, inner):
        self.name = name
        self.outer = outer
        self.canvas = canvas
        self.inner = inner

def isPacked():
    if getattr(sys, 'frozen', False):  # If the app is running as a bundled executable
        return True
    else:
        return False

def CreateMainWindow(root, Game, Version, Title, TabDict = {}, Extracommands = [], mainFolderFileNames = [], subFolderFileNames = [], SeedNouns = [], SeedVerbs = []):
    import  os, sys
    from scripts import SavedOptions, Helper, GUISettings, PermalinkManagement, Seed, Interactables, SettingsPresets
    from tkinter.font import Font
    import tkinter as tk
    isOneFile = isPacked()
    SavedOptionsFileName = f"LastSave.txt"
    JsonOutput = f"./{Game}/_internal/JsonOutputs"
    SavedOptions.loadData([GUISettings.fontSizeSave, GUISettings.fontType, GUISettings.GUITheme], "GUISavedOptions.txt", f"{Game}/GUI")
    RootsForStyling.append(root)
    defaultFont = Font(family=GUISettings.defFontVar.get(), size=GUISettings.defFontSizeVar.get())

    root.title(f"{Title} v{Version}")
    root.option_add("*Font", defaultFont)
    root.geometry(f'{windowWidth}x{windowHeight}')
    if isOneFile:
        bdat_path = os.path.join(sys._MEIPASS, 'Toolset', 'bdat-toolset-win64.exe')
    else:
        bdat_path = f"./{Game}/_internal/Toolset/bdat-toolset-win64.exe"

    if isOneFile: 
        icon_path = os.path.join(sys._MEIPASS, 'Images', f'{Game}Icon.png')
    else:
        icon_path = f"./{Game}/_internal/Images/{Game}Icon.png"
    icon = PhotoImage(file=icon_path)
    root.iconphoto(True, icon)


    # The Notebook
    MainWindow = ttk.Notebook(root, height=5)
    outerList = []
    canvasList = []
    innerList = []
    NewTabDictionary:dict = {}
    InnerDict:dict = {}
    for tab, value in TabDict.items():
        outerTab = ttk.Frame(MainWindow)
        canvas = Canvas(outerTab)
        scrollable = ttk.Frame(canvas)
        outerList.append(outerTab)
        canvasList.append(canvas)
        innerList.append(scrollable)
        NewTabDictionary[tab] = outerTab
        InnerDict[tab] = scrollable

    GUISettings.CreateScrollBars(outerList,canvasList,innerList)

    for tab, value in NewTabDictionary.items():
        MainWindow.add(value, text =TabDict[tab]) 
        
    MainWindow.pack(expand = True, fill ="both", padx=10, pady=10) 


    Interactables.OptionList.sort(key= lambda x: x.name) # Sorts alphabetically
    for opt in Interactables.OptionList: # Cant reference directly because of circular imports :/
        opt.DisplayOption(InnerDict[opt.tab], root, defaultFont, GUISettings.defGUIThemeVar.get())

    def GenRandomSeed(randoSeedEntryVar):
        randoSeedEntryVar.set(Seed.RandomSeedName(SeedNouns, SeedVerbs))

    bdatcommonFrame = ttk.Frame(root, style="NoBackground.TFrame")
    bdatcommonFrame.pack(anchor="w", padx=10)
    bdatButton = ttk.Button(bdatcommonFrame, width=17, text="Choose Input Folder", command= lambda: Helper.DirectoryChoice("Choose your folder containing common.bdat, common_ms.bdat and common_gmk.bdat", bdatFilePathEntry))
    bdatButton.pack(side="left", padx=2, pady=2)
    fileEntryVar = StringVar()
    bdatFilePathEntry = ttk.Entry(bdatcommonFrame, width=MaxWidth, textvariable=fileEntryVar)
    bdatFilePathEntry.pack(side="left", padx=2)
    OutputDirectoryFrame = ttk.Frame(root, style="NoBackground.TFrame")
    OutputDirectoryFrame.pack(anchor="w", padx=10)
    outputDirButton = ttk.Button(OutputDirectoryFrame, width = 17, text='Choose Output Folder', command= lambda: Helper.DirectoryChoice("Choose an output folder", outDirEntry))
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
    EveryObjectToSaveAndLoad = list((x.checkBoxVal for x in EntriesToSave)) + list((x.checkBoxVal for x in Interactables.OptionList)) + list((x.spinBoxVal for x in Interactables.OptionList if x.hasSpinBox)) + list((sub.checkBoxVal for x in Interactables.OptionList for sub in x.subOptions)) + list((sub.spinBoxVal for x in Interactables.OptionList for sub in x.subOptions if sub.hasSpinBox))

    # Permalink Options/Variables
    permalinkFrame = ttk.Frame(root,style="NoBackground.TFrame")
    permalinkEntry = ttk.Entry(permalinkFrame, width=MaxWidth, textvariable=permalinkVar)
    CompressedPermalink = PermalinkManagement.GenerateCompressedPermalink(randoSeedEntry.get(), EveryObjectToSaveAndLoad, Version)
    permalinkVar.set(CompressedPermalink)
    permalinkButton = ttk.Button(permalinkFrame, text="Settings", command=lambda: SettingsPresets.PresetsWindow("Presets", root, defaultFont, f"{Game}/SaveData", EntriesToSave + Interactables.OptionList, Game))
    permalinkFrame.pack(padx=10, pady=2, anchor="w")
    permalinkButton.pack(side="left", padx=2)
    permalinkEntry.pack(side='left', padx=2)
    PermalinkManagement.AddPermalinkTrace(EveryObjectToSaveAndLoad, permalinkVar, seedEntryVar, Version, lambda:Interactables.UpdateAllStates())


    # Bottom Left Progress Display Text
    randoProgressDisplay = ttk.Label(text="", anchor="e", padding=2, style="BorderlessLabel.TLabel")

    # Randomize Button
    RandomizeButton = ttk.Button(text='Randomize', command=(lambda: GUISettings.Randomize(root, RandomizeButton,fileEntryVar, randoProgressDisplay, bdat_path, permalinkVar, randoSeedEntry, JsonOutput, outputDirVar, Interactables.OptionList, mainFolderFileNames, subFolderFileNames,Extracommands )))
    RandomizeButton.place(relx=0.5, rely=1, y= -10, anchor="s")
    RandomizeButton.config(padding=5)

    # Options Cog
    if isOneFile:  # If the app is running as a bundled executable
        icon_path = os.path.join(sys._MEIPASS, 'Images', 'SmallSettingsCog.png')
    else:  # If running as a script (not bundled)
        icon_path = "./_internal/Images/SmallSettingsCog.png"
    Cog = PhotoImage(file=icon_path)
    SettingsButton = ttk.Button(image=Cog, command=lambda: GUISettings.OpenSettingsWindow(root, defaultFont, GUISettings.defGUIThemeVar, Game))
    SettingsButton.pack(pady=10, padx=10, side='right', anchor='e') 

    root.protocol("WM_DELETE_WINDOW", lambda: (SavedOptions.saveData(EntriesToSave + Interactables.OptionList, SavedOptionsFileName, Game), root.destroy()))
    GUISettings.LoadTheme(defaultFont, GUISettings.defGUIThemeVar.get())


    root.mainloop()

