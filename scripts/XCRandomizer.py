import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # Allows us to use the scripts folder as a module
from tkinter import PhotoImage, ttk
from tkinter import *
import tkinter as tk
from scripts.GUISettings import *
from PIL import Image, ImageTk

class Tab():
    def __init__(self, name, outer, canvas, inner):
        self.name = name
        self.outer = outer
        self.canvas = canvas
        self.inner = inner

class FilePlacer:
    '''Copy files to the output of the game (used for things like exefs/skyline and other files besides the bdats)'''
    def __init__(self, files, location, newName = None, game = ""):
        self.files = []
        for file in files:
            if isOneFile:
                file = os.path.join(sys._MEIPASS,game, file)
            else:
                file = f"{game}/{file}"
            self.files.append(file)
        self.location = location
        self.newName = newName

if getattr(sys, 'frozen', False):  # If the app is running as a bundled executable
    isOneFile = True
else:
    isOneFile = False

lastWidth = -1
lastHeight = -1
garbageCollectionStopper = [] # Globals to prevent garbage collection
iconCollector = []# Globals to prevent garbage collection

def UserNeedsUpdate(version, root):
    '''Checks the repos latest version tag to see if we have a new release'''
    import requests
    try:
        response = requests.get("https://api.github.com/repos/SonahSofern/Xenoblade-Series-Randomizer/releases/latest")
        data = response.json()
        latest_tag = data.get("tag_name")
        if latest_tag <= version:
            return
        else:
            import webbrowser
            def link():
                webbrowser.open_new(f"https://github.com/SonahSofern/Xenoblade-Series-Randomizer/releases/tag/{latest_tag}")
            updateMessage = ttk.Button(root, command=lambda: link(), text=f"Download Latest Version {latest_tag}")
            updateMessage.pack(pady=10)
    except:
        pass

def CreateImage(imagePath):
    if isOneFile: 
        bg_image = Image.open(os.path.join(sys._MEIPASS, imagePath))
    else:
        bg_image = Image.open(imagePath)
    bg_image = bg_image.resize((40,40))
    newimg = ImageTk.PhotoImage(bg_image)
    iconCollector.append(newimg)
    return newimg

lastHeight = -1
lastWidth = -1
lastGame = "" # Keeps tracks of when to update UI, dont love this solution though

def resize_bg(event, root, bg_image, background, Game):
    global lastWidth, lastHeight

    if (root.winfo_width() != lastWidth) or (root.winfo_height() != lastHeight):
        width, height = event.width, event.height

        if Game == lastGame:
            lastWidth = width
            lastHeight = height

        def resize_and_update(): # Processes the images on another thread because it slows down main thread a lot
            resized_image = bg_image.resize((width, height))
            bg_photo = ImageTk.PhotoImage(resized_image)

            def update_gui(): # Update GUI on main thread because tkinter is not thread safe
                garbageCollectionStopper.append(bg_photo)
                background.delete("all")
                background.create_image(0, 0, image=bg_photo, anchor="nw")

            root.after(0, update_gui)

        threading.Thread(target=resize_and_update, daemon=True).start()

saveCommands = []

def CreateMainWindow(root, window, Game, Version, Title, seedEntryVar, permalinkVar, TabDict = {}, Extracommands = [], mainFolderFileNames = [], subFolderFileNames = [], SeedNouns = [], SeedVerbs = [], textFolderName = "gb", extraArgs = [], backgroundImages = [], extraFiles = [], optionsList= [], setupHelpDesc = None):
    import  os, sys
    from scripts import SavedOptions, Helper, GUISettings, PermalinkManagement, Seed, Interactables, SettingsPresets
    from tkinter.font import Font
    import tkinter as tk

    windowPadding = 50
    global isOneFile
    if isOneFile:
        fileEntryVar = os.path.join(sys._MEIPASS, Game, 'bdat')
    else:
        fileEntryVar = f"{Game}/bdat"
    SavedOptionsFileName = f"LastSave.txt"
    JsonOutput = f"./{Game}/JsonOutputs"
    SavedOptions.loadData([GUISettings.fontSizeSave, GUISettings.fontType, GUISettings.GUITheme], "GUISavedOptions.txt", f"{Game}/GUI")
    defaultFont = Font(family=GUISettings.defFontVar.get(), size=GUISettings.defFontSizeVar.get())
    
    XCFrame = ttk.Frame(window) # Outer Frame
    RootsForStyling.append(XCFrame)

    window.add(XCFrame, text =Version, image=CreateImage(f"{Game}/Images/{Game}Icon.png"), compound="left") 

    if isOneFile:
        bdat_path = os.path.join(sys._MEIPASS, 'Toolset', 'bdat-toolset-win64.exe')
    else:
        bdat_path = f"Toolset/bdat-toolset-win64.exe"

    bg = random.choice(backgroundImages)
    if isOneFile: 
        bg_image = Image.open(os.path.join(sys._MEIPASS, Game, 'Images', bg))
    else:
        bg_image = Image.open(f"./{Game}/Images/{bg}")
    bg_photo = ImageTk.PhotoImage(bg_image)

    background = tk.Canvas(XCFrame)
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


    Interactables.XenoOptionDict[Game].sort(key= lambda x: x.name) # Sorts alphabetically
    for opt in Interactables.XenoOptionDict[Game]:
        
        if isOneFile and opt.isDevOption: # Dont show dev options when packed for users
            continue
        
        opt.DisplayOption(InnerDict[opt.tab], XCFrame, defaultFont, GUISettings.defGUIThemeVar.get())

    def GenRandomSeed(randoSeedEntryVar):
        randoSeedEntryVar.set(Seed.RandomSeedName(SeedNouns, SeedVerbs))

    bottomFrame = ttk.Frame(background, style="NoBackground.TFrame", padding=(0,0))
    bottomFrame.pack(anchor="w", padx=windowPadding, fill=X)

    
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
    
    fileOut = SavedOptions.SavedEntry("Output Bdats", outputDirVar)
    permLink = SavedOptions.SavedEntry("Permalink", permalinkVar)
    seedVar = SavedOptions.SavedEntry("Seed", seedEntryVar)
    SeedFrame.pack(anchor="w", padx=windowPadding, fill=X)
    seedDesc.pack(side='left')
    randoSeedEntry.pack(side='left', fill=X, expand=True)
    # Save and Load Last Options
    EntriesToSave = ([fileOut, permLink, seedVar])
    SavedOptions.loadData(EntriesToSave + Interactables.XenoOptionDict[Game], SavedOptionsFileName, Game)
    EveryObjectToSaveAndLoad = list((x.checkBoxVal for x in EntriesToSave)) + list((x.checkBoxVal for x in Interactables.XenoOptionDict[Game])) + list((x.spinBoxVal for x in Interactables.XenoOptionDict[Game] if x.hasSpinBox)) + list((sub.checkBoxVal for x in Interactables.XenoOptionDict[Game] for sub in x.subOptions)) + list((sub.spinBoxVal for x in Interactables.XenoOptionDict[Game] for sub in x.subOptions if sub.hasSpinBox))

    # Permalink Options/Variables
    permalinkFrame = ttk.Frame(background,style="NoBackground.TFrame")
    permalinkEntry = ttk.Entry(permalinkFrame, textvariable=permalinkVar)
    CompressedPermalink = PermalinkManagement.GenerateCompressedPermalink(randoSeedEntry.get(), EveryObjectToSaveAndLoad, Version)
    permalinkVar.set(CompressedPermalink)
    permalinkButton = ttk.Button(permalinkFrame, text="Preset", command=lambda: SettingsPresets.PresetsWindow("Presets", XCFrame, defaultFont, f"{Game}/SaveData", EntriesToSave + Interactables.XenoOptionDict[Game], Game))
    permalinkFrame.pack(padx=windowPadding, anchor="w", fill=X)
    permalinkButton.pack(side="left")
    permalinkEntry.pack(side='left', fill=X, expand=True)
    PermalinkManagement.AddPermalinkTrace(EveryObjectToSaveAndLoad, permalinkVar, seedEntryVar, Version)


    # Bottom Left Progress Display Text
    randoProgressFill = ttk.Frame(background, padding=0)
    randoProgressDisplay = ttk.Label(randoProgressFill, padding=5)
    randoProgressDisplay.pack(pady=0, side=LEFT)

    # Randomize Button
    RandomizeButton = ttk.Button(background,text='Randomize', padding=5,command=(lambda: GUISettings.Randomize(XCFrame, RandomizeButton, fileEntryVar, randoProgressDisplay,randoProgressFill,SettingsButton,pb, bdat_path, permalinkVar, randoSeedEntry, JsonOutput, outputDirVar, Interactables.XenoOptionDict[Game], mainFolderFileNames, subFolderFileNames,Extracommands, textFolderName,extraArgs=extraArgs, windowPadding=windowPadding, extraFiles=extraFiles, isOneFile=isOneFile)))
    RandomizeButton.pack(pady=(5,windowPadding),side="left", padx=(windowPadding, 0), anchor=CENTER)
    
    # Options Cog
    if isOneFile:  # If the app is running as a bundled executable
        icon_path = os.path.join(sys._MEIPASS, 'images', 'LinesIcon.png')
    else:  # If running as a script (not bundled)
        icon_path = "images/LinesIcon.png"
    HelpIcon = PhotoImage(file=icon_path)
    iconCollector.append(HelpIcon)
    SettingsButton = ttk.Button(background,padding=5,image=HelpIcon, command=lambda: PopupDescriptions.GenPopup(f"{Title} Randomizer Version {Version}", setupHelpDesc , window, defaultFont))
    SettingsButton.pack(pady=(5,windowPadding),anchor="e",expand=True, side=RIGHT, padx=windowPadding) 
    saveCommands.append(lambda: SavedOptions.saveData(EntriesToSave + Interactables.XenoOptionDict[Game], SavedOptionsFileName, Game))
    GUISettings.LoadTheme(defaultFont, GUISettings.defGUIThemeVar.get())

    pb = ttk.Progressbar(
        background,
        orient='horizontal',
        mode='determinate',
        length=3000
    )
    global lastGame
    lastGame = Game
    root.bind("<Configure>", lambda event: resize_bg(event, root, bg_image, background, Game), add="+")

