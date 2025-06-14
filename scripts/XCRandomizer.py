import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # Allows us to use the scripts folder as a module
from tkinter import PhotoImage, ttk
from tkinter import *
import tkinter as tk
from scripts.GUISettings import *
from PIL import Image, ImageTk

seedEntryVar = StringVar()
permalinkVar = StringVar()
fileEntryVar = StringVar()

class Tab():
    def __init__(self, name, outer, canvas, inner):
        self.name = name
        self.outer = outer
        self.canvas = canvas
        self.inner = inner

if getattr(sys, 'frozen', False):  # If the app is running as a bundled executable
    isOneFile = True
else:
    isOneFile = False

lastWidth = -1
lastHeight = -1
bgPhoto = None

def resize_bg(event, root, bg_photo, bg_image, background):
    global lastHeight, lastWidth, bgPhoto
    if (root.winfo_width() != lastWidth) or (root.winfo_height() != lastHeight):
        lastWidth = root.winfo_width()
        lastHeight = root.winfo_height()
        resized_image = bg_image.resize((event.width, event.height))
        bg_photo = ImageTk.PhotoImage(resized_image)
        bgPhoto = bg_photo
        background.delete("all")
        background.create_image(0, 0, image=bgPhoto, anchor="nw")
    
class FileReplacer:
    def __init__(self, images, location, filename, game):
        self.images = []
        for image in images:
            if isOneFile:
                image = os.path.join(sys._MEIPASS, image)
            else:
                image = f"{game}/_internal/{image}"
            self.images.append(image)
        self.location = location
        self.filename = filename


def CreateMainWindow(root, Game, Version, Title, TabDict = {}, Extracommands = [], mainFolderFileNames = [], subFolderFileNames = [], SeedNouns = [], SeedVerbs = [], textFolderName = "gb", extraArgs = [], backgroundImages = [], extraFiles = []):
    import  os, sys
    from scripts import SavedOptions, Helper, GUISettings, PermalinkManagement, Seed, Interactables, SettingsPresets
    from tkinter.font import Font
    import tkinter as tk
    windowPadding = 50
    global isOneFile
    SavedOptionsFileName = f"LastSave.txt"
    JsonOutput = f"./{Game}/_internal/JsonOutputs"
    SavedOptions.loadData([GUISettings.fontSizeSave, GUISettings.fontType, GUISettings.GUITheme], "GUISavedOptions.txt", f"{Game}/GUI")
    RootsForStyling.append(root)
    defaultFont = Font(family=GUISettings.defFontVar.get(), size=GUISettings.defFontSizeVar.get())


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

    bg = random.choice(backgroundImages)
    if isOneFile: 
        bg_image = Image.open(os.path.join(sys._MEIPASS, 'Images', bg))
    else:
        bg_image = Image.open(f"./{Game}/_internal/Images/{bg}")
    bg_photo = ImageTk.PhotoImage(bg_image)

    background = tk.Canvas(root)
    background.pack(fill="both", expand=True, padx=0, pady=0)
    background.create_image(0, 0, image=bg_photo, anchor="nw")

    
    # The Notebook
    MainWindow = ttk.Notebook(background)
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
        
    MainWindow.pack(expand = True, fill ="both", padx=windowPadding, pady=(windowPadding, 5))


    Interactables.OptionList.sort(key= lambda x: x.name) # Sorts alphabetically
    for opt in Interactables.OptionList: # Cant reference directly because of circular imports :/
        
        if isOneFile and opt.isDevOption: # Dont show dev options when packed for users
            continue
        
        opt.DisplayOption(InnerDict[opt.tab], root, defaultFont, GUISettings.defGUIThemeVar.get())

    def GenRandomSeed(randoSeedEntryVar):
        randoSeedEntryVar.set(Seed.RandomSeedName(SeedNouns, SeedVerbs))

    bottomFrame = ttk.Frame(background, style="NoBackground.TFrame", padding=(0,0))
    bottomFrame.pack(anchor="w", padx=windowPadding, fill=X)
    
    bdatButton = ttk.Button(bottomFrame, width=17, text="Choose Input Folder", command= lambda: Helper.DirectoryChoice("Choose your folder containing common.bdat, common_ms.bdat and common_gmk.bdat", bdatFilePathEntry))
    bdatButton.pack(side="left", pady=0)
    bdatFilePathEntry = ttk.Entry(bottomFrame, textvariable=fileEntryVar)
    bdatFilePathEntry.pack(side="left", expand=True, fill=X, pady=0)
    
    OutputDirectoryFrame = ttk.Frame(background, style="NoBackground.TFrame", padding=(0,0))
    OutputDirectoryFrame.pack(anchor="w", padx=windowPadding, fill=X)
    
    outputDirButton = ttk.Button(OutputDirectoryFrame, width = 17, text='Choose Output Folder', command= lambda: Helper.DirectoryChoice("Choose an output folder", outDirEntry))
    outputDirButton.pack(side="left", pady=0)
    outputDirVar = StringVar()
    outDirEntry = ttk.Entry(OutputDirectoryFrame, textvariable=outputDirVar)
    outDirEntry.pack(side="left", expand=True, fill=X)
    
    SeedFrame = ttk.Frame(background, style="NoBackground.TFrame")
    seedDesc = ttk.Button(SeedFrame, text="Seed", command=lambda: GenRandomSeed(seedEntryVar))


    GUISettings.RootsForStyling.append(bottomFrame)

    # Seed entry box
    GenRandomSeed(seedEntryVar) # Gen a random seed if you have no save data 
    randoSeedEntry = ttk.Entry(SeedFrame, textvariable=seedEntryVar)



            
    fileEnt = SavedOptions.SavedEntry("Input Bdats",fileEntryVar)
    fileOut = SavedOptions.SavedEntry("Output Bdats", outputDirVar)
    permLink = SavedOptions.SavedEntry("Permalink", permalinkVar)
    seedVar = SavedOptions.SavedEntry("Seed", seedEntryVar)
    SeedFrame.pack(anchor="w", padx=windowPadding, fill=X)
    seedDesc.pack(side='left')
    randoSeedEntry.pack(side='left', fill=X, expand=True)
    # Save and Load Last Options
    EntriesToSave = ([fileEnt, fileOut, permLink, seedVar])
    SavedOptions.loadData(EntriesToSave + Interactables.OptionList, SavedOptionsFileName, Game)
    EveryObjectToSaveAndLoad = list((x.checkBoxVal for x in EntriesToSave)) + list((x.checkBoxVal for x in Interactables.OptionList)) + list((x.spinBoxVal for x in Interactables.OptionList if x.hasSpinBox)) + list((sub.checkBoxVal for x in Interactables.OptionList for sub in x.subOptions)) + list((sub.spinBoxVal for x in Interactables.OptionList for sub in x.subOptions if sub.hasSpinBox))

    # Permalink Options/Variables
    permalinkFrame = ttk.Frame(background,style="NoBackground.TFrame")
    permalinkEntry = ttk.Entry(permalinkFrame, textvariable=permalinkVar)
    CompressedPermalink = PermalinkManagement.GenerateCompressedPermalink(randoSeedEntry.get(), EveryObjectToSaveAndLoad, Version)
    permalinkVar.set(CompressedPermalink)
    permalinkButton = ttk.Button(permalinkFrame, text="Preset", command=lambda: SettingsPresets.PresetsWindow("Presets", root, defaultFont, f"{Game}/SaveData", EntriesToSave + Interactables.OptionList, Game))
    permalinkFrame.pack(padx=windowPadding, anchor="w", fill=X)
    permalinkButton.pack(side="left")
    permalinkEntry.pack(side='left', fill=X, expand=True)
    PermalinkManagement.AddPermalinkTrace(EveryObjectToSaveAndLoad, permalinkVar, seedEntryVar, Version, lambda:Interactables.UpdateAllStates())


    # Bottom Left Progress Display Text
    randoProgressFill = ttk.Frame(background, padding=0)
    randoProgressDisplay = ttk.Label(randoProgressFill, padding=5)
    randoProgressDisplay.pack(pady=0, side=LEFT)

    # Randomize Button
    RandomizeButton = ttk.Button(background,text='Randomize', padding=5,command=(lambda: GUISettings.Randomize(root, RandomizeButton,fileEntryVar, randoProgressDisplay,randoProgressFill,SettingsButton,pb, bdat_path, permalinkVar, randoSeedEntry, JsonOutput, outputDirVar, Interactables.OptionList, mainFolderFileNames, subFolderFileNames,Extracommands, textFolderName,extraArgs=extraArgs, windowPadding=windowPadding, extraFiles=extraFiles)))
    RandomizeButton.pack(pady=(5,windowPadding),side="left", padx=(windowPadding, 0), anchor=CENTER)
    
    # Options Cog
    if isOneFile:  # If the app is running as a bundled executable
        icon_path = os.path.join(sys._MEIPASS, 'Images', 'SmallSettingsCog.png')
    else:  # If running as a script (not bundled)
        icon_path = "./_internal/Images/SmallSettingsCog.png"
    Cog = PhotoImage(file=icon_path)
    SettingsButton = ttk.Button(background,padding=5, image=Cog, command=lambda: GUISettings.OpenSettingsWindow(root, defaultFont, GUISettings.defGUIThemeVar, Game))
    SettingsButton.pack(pady=(5,windowPadding),anchor="e",expand=True, side=RIGHT, padx=windowPadding) 
    
    root.protocol("WM_DELETE_WINDOW", lambda: (SavedOptions.saveData(EntriesToSave + Interactables.OptionList, SavedOptionsFileName, Game), root.destroy()))
    GUISettings.LoadTheme(defaultFont, GUISettings.defGUIThemeVar.get())

    pb = ttk.Progressbar(
        background,
        orient='horizontal',
        mode='determinate',
        length=3000
    )

    root.bind("<Configure>", lambda event: resize_bg(event, root, bg_photo, bg_image, background))
    root.mainloop()

