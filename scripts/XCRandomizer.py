import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # Allows us to use the scripts folder as a module
from tkinter import PhotoImage, ttk
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from scripts import Presets, SaveLoad, ScrollPanel, PopupDescriptions, Theme, Onefile, Helper, PermalinkManagement, Seed, Interactables
import random, subprocess, shutil, threading, traceback, time, datetime, webbrowser

lastWidth = -1
lastHeight = -1
garbageCollectionStopper = [] # Globals to prevent garbage collection
iconCollector = [] # Globals to prevent garbage collection

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
            if Onefile.isOneFile:
                file = os.path.join(sys._MEIPASS, game, file)
            else:
                file = f"{game}/{file}"
            self.files.append(file)
        self.location = location
        self.newName = newName

def CheckIfUserNeedsUpdate(version, root):
    '''Checks the repos latest version tag to see if we have a new release'''
    import requests
    try:
        response = requests.get("https://api.github.com/repos/SonahSofern/Xenoblade-Series-Randomizer/releases/latest")
        data = response.json()
        latest_tag = data.get("tag_name")
        if latest_tag <= version:
            return
        else:
            def link():
                webbrowser.open_new(f"https://github.com/SonahSofern/Xenoblade-Series-Randomizer/releases/tag/{latest_tag}")
            updateMessage = ttk.Button(root, command=lambda: link(), text=f"Download Latest Version {latest_tag}")
            updateMessage.pack(pady=10)
    except:
        pass # They probably arent connected to internet

def CreateImage(imagePath, resize = (40,40)):
    imagePath = Onefile.Directory(imagePath)
    bg_image = Image.open(imagePath)
    if resize != None:
        bg_image = bg_image.resize(resize)
    newimg = ImageTk.PhotoImage(bg_image)
    iconCollector.append(newimg)
    return newimg

saveCommands = []

class GameWindowData:
    def __init__(self, game, version, title, seedVar, permalinkVar, tabs, postCommands = [], preCommands = [], mainFolderNames = [], subFolderNames = [], nouns = [], verbs = [], textFolderName = "gb", extraArgs = [], backgroundImages = [], extraFiles = [], setupHelpDesc = None, outputRomfsSpec = "/romfs/bdat"):
        self.game = game
        self.version = version
        self.title = title
        self.seedVar = seedVar
        self.permalinkVar = permalinkVar
        self.tabs = tabs
        self.postCommands = postCommands
        self.preCommands = preCommands
        self.mainFolderNames = mainFolderNames
        self.subFolderNames = subFolderNames
        self.nouns = nouns
        self.verbs = verbs
        self.textFolderName = textFolderName
        self.extraArgs = extraArgs
        self.backgroundImages = backgroundImages
        self.extraFiles:list = extraFiles
        self.setupHelpDesc = setupHelpDesc
        self.outputRomfsSpec = outputRomfsSpec

# Game, Version, Title, seedEntryVar, permalinkVar, TabDict = {}, postCommands = [], preCommands = [], mainFolderFileNames = [], subFolderFileNames = [], SeedNouns = [], SeedVerbs = [], textFolderName = "gb", extraArgs = [], backgroundImages = [], extraFiles = [], setupHelpDesc = None, outputRomfsSpec = "/romfs/bdat"
# Some of the oldest code and messy for sure. 
def CreateMainWindow(root, window, gameData:GameWindowData): 
    windowPadding = 30
    if Onefile.isOneFile:
        fileEntryVar = os.path.join(sys._MEIPASS, gameData.game, 'bdat')
    else:
        fileEntryVar = f"{gameData.game}/bdat"
    SavedOptionsFileName = f"Last Save.txt"
    JsonOutput = f"./{gameData.game}/JsonOutputs"
    saveCommand = lambda: SaveLoad.saveData(EntriesToSave + Interactables.XenoOptionDict[gameData.game], SavedOptionsFileName, f"{gameData.game}/SaveData")
    XCFrame = ttk.Frame(window) # Outer Frame
    Theme.RootsForStyling.append(XCFrame)

    window.add(XCFrame, text =gameData.version, image=CreateImage(f"{gameData.game}/Images/{gameData.game}Icon.png"), compound="left") 

    if Onefile.isOneFile:
        bdat_path = os.path.join(sys._MEIPASS, 'toolset', 'bdat-toolset-win64.exe')
    else:
        bdat_path = f"toolset/bdat-toolset-win64.exe"

    background = tk.Canvas(XCFrame)
    background.pack(fill="both", expand=True, padx=0, pady=0)

    # The Notebook
    MainWindow = ttk.Notebook(background)
    NewTabDictionary:dict = {}
    InnerDict:dict = {}
    for tab, value in gameData.tabs.items():
        scroll = ScrollPanel.ScrollablePanel(MainWindow)
        NewTabDictionary[tab] = scroll.outerFrame
        InnerDict[tab] = scroll.innerFrame

    # Frames/Tabs
    outerPresetFrame = ttk.Frame(MainWindow, padding=10)
    MainWindow.add(outerPresetFrame, text="Presets")
    
    for tab, value in NewTabDictionary.items():
        MainWindow.add(value, text =gameData.tabs[tab]) 
        
    MainWindow.pack(expand = True, fill ="both", padx=windowPadding, pady=(windowPadding, 5))
    
    def AlternateStyle(curStyle):
        if curStyle == "Dark":
            return "Light"
        else:
            return "Dark"
        
    style= "Dark"
    for opt in Interactables.XenoOptionDict[gameData.game]:
        style = AlternateStyle(style)
        opt.DisplayOption(InnerDict[opt.tab], XCFrame, style)

    def GenRandomSeed(randoSeedEntryVar):
        randoSeedEntryVar.set(Seed.RandomSeedName(gameData.nouns, gameData.verbs))

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
    seedDesc = ttk.Button(SeedFrame, text="Seed", command=lambda: GenRandomSeed(gameData.seedVar))

    Theme.RootsForStyling.append(bottomFrame)

    # Seed entry box
    GenRandomSeed(gameData.seedVar) # Gen a random seed if you have no save data 
    randoSeedEntry = ttk.Entry(SeedFrame, textvariable=gameData.seedVar)
    
    # Bottom Menu Options
    fileOut = SaveLoad.SavedEntry("Output Bdats", outputDirVar)
    permLink = SaveLoad.SavedEntry("Permalink", gameData.permalinkVar)
    seedVar = SaveLoad.SavedEntry("Seed", gameData.seedVar)
    SeedFrame.pack(anchor="w", padx=windowPadding, fill=X)
    seedDesc.pack(side='left')
    randoSeedEntry.pack(side='left', fill=X, expand=True)
    
    # Save and Load Last Options
    EntriesToSave = ([fileOut, permLink, seedVar])
    SaveLoad.loadData(EntriesToSave + Interactables.XenoOptionDict[gameData.game], SavedOptionsFileName, f"{gameData.game}/SaveData")
    EveryObjectToSaveAndLoad = list((x.checkBoxVal for x in EntriesToSave)) + list((x.checkBoxVal for x in Interactables.XenoOptionDict[gameData.game])) + list((x.spinBoxVal for x in Interactables.XenoOptionDict[gameData.game] if x.hasSpinBox)) + list((sub.checkBoxVal for x in Interactables.XenoOptionDict[gameData.game] for sub in x.subOptions)) + list((sub.spinBoxVal for x in Interactables.XenoOptionDict[gameData.game] for sub in x.subOptions if sub.hasSpinBox))

    # Permalink Options/Variables
    permalinkFrame = ttk.Frame(background,style="NoBackground.TFrame")
    permalinkEntry = ttk.Entry(permalinkFrame, textvariable=gameData.permalinkVar)
    CompressedPermalink = PermalinkManagement.GenerateCompressedPermalink(randoSeedEntry.get(), EveryObjectToSaveAndLoad, gameData.version)
    gameData.permalinkVar.set(CompressedPermalink)
    permalinkButton = ttk.Button(permalinkFrame, text="Settings String")
    permalinkFrame.pack(padx=windowPadding, anchor="w", fill=X)
    permalinkButton.pack(side="left")
    permalinkEntry.pack(side='left', fill=X, expand=True)
    PermalinkManagement.AddPermalinkTrace(EveryObjectToSaveAndLoad, gameData.permalinkVar, gameData.seedVar, gameData.version)

    # Randomize Button
    RandomizeButton = ttk.Button(background, style="Randomize.TButton",text='Randomize', padding=5,command=(lambda: (saveCommand(), Randomize(gameData, XCFrame, RandomizeButton, fileEntryVar, bdat_path, randoSeedEntry, JsonOutput, outputDirVar, Interactables.XenoOptionDict[gameData.game]))))
    RandomizeButton.pack(pady=(5,windowPadding), padx=(windowPadding, 0), anchor="w", side="left")
    saveCommands.append(saveCommand)

    Presets.PresetsWindow(outerPresetFrame,  [seedVar] + Interactables.XenoOptionDict[gameData.game], gameData.game)
    
    SettingsButton = ttk.Button(background, text="Help", command=lambda: PopupDescriptions.StyledPopup(f"{gameData.title} Randomizer Version {gameData.version}", gameData.setupHelpDesc , window), padding=5)
    SettingsButton.pack(anchor="e", side="right", pady=(5,windowPadding), padx=(0, windowPadding))

    DiscordButton = ttk.Button(background, image=CreateImage(f"Images/Discord-Symbol-White.png", (28,23)), text="Discord", compound=LEFT, command=lambda: webbrowser.open_new(f"https://discord.gg/64FK78ScvJ"), padding=5)
    DiscordButton.pack(anchor="e", side="right", pady=(5,windowPadding), padx=(0, 5)) 

    Theme.ThemeUpdate()
    
    # Background Images
    bg = random.choice(gameData.backgroundImages)
    if Onefile.isOneFile: 
        bg_image = Image.open(os.path.join(sys._MEIPASS, gameData.game, 'Images', bg))
    else:
        bg_image = Image.open(f"./{gameData.game}/Images/{bg}")
    
    # hardcoded because thats the height of the window that actually uses the background. But that height is unaccessable when this is called.
    resized = bg_image.resize((int(Theme.windowWidth), int(Theme.windowHeight)))
    bg_photo = ImageTk.PhotoImage(resized)
    garbageCollectionStopper.append(bg_photo)
    background.create_image(0, 0, image=bg_photo, anchor="nw")
    
    # Tkinter is so bad at this, winfowidth does not work the only way to get the right dimensions is through a configure event... crazy.
    XCFrame.update()
    XCFrame.bind("<Configure>", lambda event: resize_bg(event, root, bg_image, background))
    # root.bind("<Configure>", lambda event: resize_bg(event, XCFrame, root, bg_image, background), add="+")

lastHeight = -1
lastWidth = -1

def resize_bg(event, root, bg_image, background):
    global lastWidth, lastHeight

    if (root.winfo_width() != lastWidth) or (root.winfo_height() != lastHeight):
        width, height = event.width, event.height

        def resize_and_update(): # Processes the images on another thread because it slows down main thread a lot
            try:
                resized_image = bg_image.resize((width, height))
                bg_photo = ImageTk.PhotoImage(resized_image)

                def update_gui(): # Update GUI on main thread because tkinter is not thread safe
                    garbageCollectionStopper.append(bg_photo)
                    background.delete("all")
                    background.create_image(0, 0, image=bg_photo, anchor="nw")

                root.after(0, update_gui)
            except:
                pass

        threading.Thread(target=resize_and_update, daemon=True).start()

def Randomize(gameData:GameWindowData, root, RandomizeButton, fileEntryVar, bdat_path, randoSeedEntry, JsonOutput, outputDirVar, OptionList:list[Interactables.Option]):
    def ThreadedRandomize():
        if outputDirVar.get().strip() == "":
            errorMsgObj = PopupDescriptions.Description()
            errorMsgObj.Header("Select an Output Location Before Randomizing")
            errorMsgObj.Text("This is where the randomizer will output the randomized mod. See the help button for instructions on how to use mods.")
            PopupDescriptions.StyledPopup(f"{gameData.title} {datetime.datetime.now()}", lambda: errorMsgObj, root)
            return
        entrySpot = fileEntryVar
        outSpot = f"{outputDirVar.get().strip()}/{gameData.outputRomfsSpec}"
        
        # Disable Repeated Button Click
        RandomizeButton.config(state=DISABLED)
        
        # Make Popup
        progressPopup = PopupDescriptions.GenericPopup(f"Randomizing {gameData.title}") 
        progressPopup.attributes(alpha = 0)
        
        def progressClose():
            progressPopup.destroy()
            RandomizeButton.config(state=NORMAL)
        
        progressPopup.protocol("WM_DELETE_WINDOW", progressClose)
        progressPopup.grab_set()
        
        outerBorder = ttk.Frame(progressPopup, padding=10)
        outerBorder.pack(expand=True, fill=BOTH)
        
        randoProgressDisplay = ttk.Label(outerBorder, anchor=CENTER, padding=(0,0,0,5))
        pb = ttk.Progressbar(outerBorder, orient='horizontal', mode='determinate', length=500, value=1)
        progressPopup.attributes(alpha = 1)

        # Showing Progress Diplay 
        randoProgressDisplay.config(text="Unpacking BDATs")
        randoProgressDisplay.pack()
        pb.pack()
        PopupDescriptions.center(progressPopup, root)
        
        random.seed(gameData.permalinkVar.get())
        print("Seed: " + randoSeedEntry.get())
        print("Permalink: "+  gameData.permalinkVar.get())
        os.makedirs(outSpot, exist_ok=True) # Make the directory for them
        try:
            for file in gameData.mainFolderNames:
                # print("BDAT:", JsonOutput, "Exists:", os.path.exists(JsonOutput))
                # print(bdat_path)
                # print(f"{entrySpot}/{file}.bdat")
                # print(JsonOutput)
                # print(gameData.extraArgs)
                subprocess.run([bdat_path, "extract", f"{entrySpot}/{file}.bdat", "-o", JsonOutput, "-f", "json", "--pretty"] + gameData.extraArgs, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
            for file in gameData.subFolderNames:
                # print(f"{entrySpot}/{gameData.textFolderName}/{file}.bdat")
                subprocess.run([bdat_path, "extract", f"{entrySpot}/{gameData.textFolderName}/{file}.bdat", "-o", JsonOutput, "-f", "json", "--pretty"] + gameData.extraArgs, check=True, creationflags=subprocess.CREATE_NO_WINDOW)

            # Unpacks BDATs

        except:
            print(f"{traceback.format_exc()}") # shows the full error
            time.sleep(3)
            RandomizeButton.config(state=NORMAL)
            return

        # Runs all randomization
        for option in gameData.preCommands: 
            option()
            
        runLog = RunOptions(gameData.title, OptionList, randoProgressDisplay, root, randoSeedEntry.get(), pb)
        
        for option in gameData.postCommands: # Runs post commands like show title screen
            option()
        
        # Need to delete previous skyline folder each time
        extraFilePlaced = [] # Conditionally some files (skyline plugins are placed)
        for option in OptionList: # Commands that add files to the output (I want to rework this entire logic but would be time consuming)
            if (len(option.filePlaceCommands) > 0) and option.GetState():
                for command in option.filePlaceCommands:
                    extraFilePlaced.append(command())
            
        randoProgressDisplay.config(text="Packing BDATs")
    
        # Packs BDATs
        # If we are packed for users we dont want to create a window. For us we want this window to see errors from bdat-rs
        if Onefile.isOneFile:
            creationFlags = subprocess.CREATE_NO_WINDOW
        else:
            creationFlags = 0
        try:
            subprocess.run([bdat_path, "pack", JsonOutput, "-o", outSpot, "-f", "json"],check=True,stderr=None,stdout=None, creationflags=creationFlags)
            # for file in 
            # Outputs common_ms in the correct file structure
            os.makedirs(f"{outSpot}/{gameData.textFolderName}", exist_ok=True)
            for file in gameData.subFolderNames:
                shutil.move(f"{outSpot}/{file}.bdat", f"{outSpot}/{gameData.textFolderName}/{file}.bdat")
                
            for file in gameData.extraFiles + extraFilePlaced:
                AddFileToOutput(outSpot, file)
            
            # Displays Done and Clears Text
            randoProgressDisplay.config(text="Done")
            progressPopup.destroy()
            runLog()
            print(f"Finished at {datetime.datetime.now()}")
        except:
            # print(f"{traceback.format_exc()}") # shows the full error
            randoProgressDisplay.config(text="Failed Outputs")

        # Re-Enables Randomize Button
        RandomizeButton.config(state=NORMAL)
        

    threading.Thread(target=ThreadedRandomize).start()

def AddFileToOutput(output, file):
    try:
        outputFolder = os.path.join(output, file.location)
        os.makedirs(outputFolder, exist_ok=True)

        src = random.choice(file.files)

        if os.path.isdir(src):  # Handle Folders
            destPath = os.path.join(outputFolder, file.newName or os.path.basename(src))
            shutil.copytree(src, destPath, dirs_exist_ok=True)

        else: # Handle file
            destPath = os.path.join(outputFolder, file.newName or os.path.basename(src))
            shutil.copy(src, destPath)
    except Exception as e:
        print(e)
        
def SumTotalCommands(OptionList):
    TotalCommands = 1
    for opt in OptionList:
        if opt.GetState(): # Checks state
            TotalCommands += 1
    return TotalCommands

def RunOptions(GameTitle, OptionList:list[Interactables.Option], randoProgressDisplay, root, seed, pb):
    
    OptionList.sort(key=lambda x: x.prio) # Sort main options by priority
    
    errorMsgObj = PopupDescriptions.Description()
    errorMsgObj.Header(f"{GameTitle} Randomization Finished")
    errorMsgObj.Tag(f"Seed: {seed}", pady=5, anchor="center") # Seed
    
    def ErrorLog():
        return errorMsgObj

    for opt in OptionList: # runs pre-randomization commands before the actual options
        if not opt.GetState():
            continue
        for command in opt.preRandoCommands:
            try:
                command()
            except Exception as error:
                print(f"ERROR: {opt.name} | {error}")
                print(f"{traceback.format_exc()}") # shows the full error
    TotalCommands = SumTotalCommands(OptionList)       

    for opt in OptionList:
        if not opt.GetState(): # Checks state
            continue
        opt.subOptions.sort(key= lambda x: x.prio) # Sort suboptions by priority
            
        for sub in opt.subOptions:
            if not sub.checkBoxVal.get(): # Checks state
                continue
            try:
                for command in sub.commands:
                    command()
            except Exception as error:
                print(f"ERROR: {opt.name}: {sub.name} | {error}")
                print(f"{traceback.format_exc()}") # shows the full error
                
        randoProgressDisplay.config(text=opt.name)
        
        nextStep =  pb['value'] + (100/TotalCommands) # Cache it here so it doesnt matter how far the bar goes 
        threading.Thread(target=lambda: SlowBurn(pb, nextStep, opt.stepSpeed)).start()

        for command in opt.commands:
            try:
                errorMsg = command()
                    
            except Exception as error:
                print(f"ERROR: {opt.name} | {error}")
                print(traceback.format_exc()) # shows the full error
                if errorMsg == None:
                    errorMsg = error
                errorMsgObj.Header(f"Error: {opt.name}")
                errorMsgObj.Text(errorMsg)
        pb['value'] = nextStep

    return lambda: PopupDescriptions.StyledPopup(f"{GameTitle} {datetime.datetime.now()}", lambda: ErrorLog(), root)

def SlowBurn(progressBar, nextStop, stepSpeed):
    try: # Throwing a try excpet here because I have had times in Debug mode where this throws errors saying something about pb. 
        while(progressBar['value'] < nextStop):
            time.sleep(0.02)
            progressBar['value'] += stepSpeed
    except Exception as e:
        print(e)
