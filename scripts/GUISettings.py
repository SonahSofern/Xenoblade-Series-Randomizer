from tkinter import *
from scripts import UI_Colors
from tkinter import ttk
import random, subprocess, shutil, os, threading, traceback, time, datetime
from scripts import SavedOptions, PopupDescriptions


CanvasesForStyling = []
RootsForStyling = []
defFontVar = StringVar(value="Calibri")
defFontSizeVar = IntVar(value=14)
defGUIThemeVar = StringVar(value="Dark Mode")
fontNameVar = StringVar()

fontType = SavedOptions.SavedEntry("Font", defFontVar)
fontSizeSave = SavedOptions.SavedEntry("Font Size", defFontSizeVar)
GUITheme = SavedOptions.SavedEntry("Theme", defGUIThemeVar)

        
def LoadTheme(defaultFont, themeName):
    style= ttk.Style()
    # Initial colors for the themes

    darkThemeColors = {
    "backgroundColor": UI_Colors.DarkerPurple,
    "darkColor": UI_Colors.LightBlack,
    "midColor": UI_Colors.DarkGray,
    "midGray": UI_Colors.MediumGray,
    "lightColor": UI_Colors.White,
    }
    currentTheme = darkThemeColors
    try:
        style.theme_create(themeName, settings={
            "TNotebook": {
                "configure": {
                    "font": defaultFont,
                    "background": currentTheme["backgroundColor"],
                    "borderwidth": 1,
                    "bordercolor": currentTheme["backgroundColor"],
                    "relief": FLAT,
                    "focuscolor":"", # Checkbutton focus border
                    "padding": 0,
                    "tabposition": "nw", # Cool for styling but gonnna kjeep it default for now
                    "tabmargins": 0,
                    "lightcolor": currentTheme["backgroundColor"],
                    "darkcolor": currentTheme["backgroundColor"],
                },
                "map": {
                    "foreground": [("selected", currentTheme["darkColor"]), ("active", currentTheme["darkColor"])],
                    "background": [("selected", currentTheme["darkColor"]), ("active", currentTheme["darkColor"])]                
                }
            },
            "TNotebook.Tab": {
                "configure": {
                    "background": currentTheme["darkColor"],
                    "padding": 10,
                    "font": defaultFont,
                    "foreground": currentTheme["lightColor"],
                    "bordercolor": currentTheme["darkColor"],
                    "borderwidth": 0,
                    "focuscolor":"",# Checkbutton focus border
                    "relief": "flat",
                    "expand": 0,
                },
                "map": {
                    "foreground": [("selected", currentTheme["lightColor"]), ("active", currentTheme["lightColor"])],
                    "background": [("selected", currentTheme["midColor"]), ("active", currentTheme["midColor"])],        
                    # "expand": [("selected", 0), ("active", 2)]                
                }
            },
            "TButton": {
                "configure": {
                    "background": currentTheme["darkColor"],
                    "foreground": currentTheme["lightColor"],
                    "font": defaultFont,
                    "reliefcolor": currentTheme["lightColor"],
                    "padding": (5,3,5,3),
                    "focuscolor":"",
                    "relief": "ridge",
                },
                "map": {
                    "background": [("pressed", currentTheme["darkColor"]),("active", currentTheme["midColor"])],
                    "foreground": [("disabled", currentTheme["midGray"])],
                }
            },
            "TCheckbutton": {
                "configure": {
                    "background": currentTheme["darkColor"],
                    "foreground": currentTheme["midGray"],
                    "padding": (40,3,50,3),
                    "indicatorcolor": currentTheme["darkColor"],
                    "indicatorbackground": currentTheme["darkColor"],
                    "font": defaultFont,
                    "indicatorrelief": "ridge",
                    "focuscolor":"",
                    "indicatormargin": (0,0,10,0),
                },
                "map": {
                    "indicatorcolor": [("disabled", currentTheme["darkColor"]),("selected", currentTheme["lightColor"]),("active", currentTheme["midColor"])],
                    "background": [("disabled", currentTheme["darkColor"]),("active", currentTheme["midColor"])],
                    "foreground": [("disabled", currentTheme["midGray"]),("active", currentTheme["lightColor"]),("selected", currentTheme["lightColor"])],
                    "indicatorbackground": [ ("disabled", currentTheme["darkColor"]),("active", currentTheme["midGray"])],
                }
            },
            "TEntry": {
                "configure": {
                    "foreground": currentTheme["lightColor"],
                    "font": defaultFont,
                    "fieldbackground": currentTheme["darkColor"],
                    "padding": (5,3,5,3),
                    "selectbackground": currentTheme["lightColor"],
                    "selectforeground": currentTheme["darkColor"],
                    "selectborderwidth": 0,
                    "relief":"ridge",
                    "insertcolor": currentTheme["lightColor"],
                }
            },
            "TScrollbar": {
                "configure": {
                    "troughcolor": currentTheme["midColor"],
                    "background": currentTheme["darkColor"],
                    "borderwidth": 1,
                    "relief": "flat",
                    "arrowcolor": currentTheme["lightColor"],
                }
            },
            "TLabel": {
                "configure": {
                    "foreground": currentTheme["lightColor"],
                    "background": currentTheme["darkColor"],
                    "troughcolor": currentTheme["darkColor"],
                    "borderwidth": 0,
                    "padding": (20, 10),
                },
                "map": {
                    "foreground": [("disabled", currentTheme["midGray"])],
                }
            },
            "TFrame": {
                "configure": {
                    "background": currentTheme["darkColor"],
                    "relief": "flat",
                    "borderwidth": 0,
                },
                "map": {
                    "background": [("active", currentTheme["midColor"])],
                    "foreground": [("active", currentTheme["lightColor"]),("selected", currentTheme["lightColor"])],
                }
            },
            "TScale": {
                "configure": {
                    "background": currentTheme["darkColor"],
                    "foreground": currentTheme["lightColor"],
                    "troughrelief": "flat",
                    "groovewidth": 0,
                    "troughcolor": currentTheme["midColor"],
                    "darkcolor": currentTheme["darkColor"],
                    "lightcolor": currentTheme["darkColor"],
                    "borderwidth": 1,
                    "sliderwidth": 100,
                }
            },
            "TSpinbox": {
                "configure": {
                    "background": currentTheme["midColor"],
                    "foreground": currentTheme["lightColor"],
                    "fieldbackground": currentTheme["midColor"],
                    "darkcolor": currentTheme["darkColor"],
                    "lightcolor": currentTheme["darkColor"],
                    "insertcolor": currentTheme["midColor"],
                    # "relief": "ridge",  No longer works lol idk why
                    "padding": (4,0),
                    "focuscolor":"",
                    "selectforeground": currentTheme["lightColor"],
                    "selectbackground": currentTheme["midColor"],
                    "arrowcolor": currentTheme["lightColor"],
                },
                "map": {
                    "foreground": [("disabled", currentTheme["midGray"])],
                    "arrowcolor": [("disabled", currentTheme["midGray"])],
                }
            },
                "TSeparator": {
                "configure": {
                    "background": currentTheme["midColor"],

                },
            },
           "TProgressbar": {
    "configure": {
        "background": currentTheme["lightColor"],
        "troughcolor": currentTheme["midColor"],
        "darkcolor": currentTheme["darkColor"],
        "lightcolor": currentTheme["lightColor"],
        "thickness": 2,
        "padding": 0,
    },
    "map": {
        "background": [("disabled", currentTheme["midGray"])],
    }
}
        })
    except:
        pass
    
    style.theme_use(themeName)
    from tkinter.font import Font
    staticFont = Font(family="Arial", size=16)
    
    # Light
    style.configure("Light.TFrame", background=UI_Colors.OffLightBlack)
    style.configure("Light.TButton", background=UI_Colors.OffLightBlack, relief = FLAT)
    style.configure("Light.TSpinbox", background=UI_Colors.OffLightBlack)
    style.configure("Light.TLabel", background=UI_Colors.OffLightBlack)
    style.configure("Light.TCheckbutton", background=UI_Colors.OffLightBlack, padding=(20, 10))
    style.configure("LightSub.TCheckbutton", background=UI_Colors.OffLightBlack)
    style.configure("LightNoMargin.TLabel", margin=(0,0), padding=(20,0), background=UI_Colors.OffLightBlack)

    # Dark
    style.configure("Dark.TFrame", background=currentTheme["darkColor"])
    style.configure("Dark.TButton", background=currentTheme["darkColor"], relief = FLAT)
    style.configure("Dark.TSpinbox", background=currentTheme["darkColor"])
    style.configure("Dark.TLabel", background=currentTheme["darkColor"])
    style.configure("Dark.TCheckbutton", background=currentTheme["darkColor"], padding=(20, 10))
    style.configure("DarkSub.TCheckbutton", background=currentTheme["darkColor"])
    style.configure("DarkNoMargin.TLabel", margin=(0,0), padding=(20,0), background=currentTheme["darkColor"])
    
    from tkinter.font import Font
    titleFont = Font(family="Calibri", size=25)
    style.configure("Title.TLabel",font=titleFont,foreground="white",background=currentTheme["midColor"],padding=5)
    style.configure("BordlessBtn.TButton", relief = FLAT)
    style.configure("bordered.TFrame", relief = SOLID, borderwidth= 2)
    style.configure("centeredTabs.TNotebook", tabposition= "nw", borderwidth=0)
    style.configure("STATIC.TButton", font=staticFont)
    style.configure("BorderlessLabel.TLabel", background=currentTheme["darkColor"], foreground=UI_Colors.White)
    style.configure("NoBackground.TFrame", background=currentTheme["backgroundColor"])
    style.configure("Header.TButton", borderwidth=0, background=currentTheme["midGray"])
    style.configure("Tag.TLabel", background= currentTheme["midGray"], relief="flat", padding=(9,2), margin=(5,0))
    style.configure("DescriptionImage.TLabel", background= currentTheme["midColor"])
    style.configure("CenteredLabel.TLabel")
    style.configure("CenteredButton.TButton", anchor = "center")

    # Since Canvas and Roots arrent affected by normal styling
    for canvas in CanvasesForStyling:
        try:
            canvas.config(background=currentTheme["darkColor"])
        except:
            pass
        
    for root in RootsForStyling:
        try:
            root.config(background=currentTheme["backgroundColor"])
        except:
            pass

def _on_mousewheel(event, canvas:Canvas):
    canvas.update_idletasks()
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    # print(canvas.cget("scrollregion"))
    
def CreateScrollBars(OuterFrames:list[ttk.Frame], Canvases:list[Canvas], InnerFrames:list[ttk.Frame], genScrollbar = True):
    for i in range(len(Canvases)):
        InnerFrames[i].pack(fill=BOTH, expand=True)

        scrollbar = ttk.Scrollbar(OuterFrames[i], orient="vertical", command=Canvases[i].yview)
        Canvases[i].config(yscrollcommand=scrollbar.set, borderwidth=0, relief="flat", highlightthickness=0)
        CanvasesForStyling.append(Canvases[i])
        # OuterFrames[i].config(borderwidth=0, relief="flat")
        InnerFrames[i].bind("<Configure>", lambda e, canvas=Canvases[i]: canvas.configure(scrollregion=canvas.bbox("all")))

        Canvases[i].create_window((0, 0), window=InnerFrames[i], anchor="nw")

        Canvases[i].pack(side="left", fill=BOTH, expand=True)
        if genScrollbar:
            scrollbar.pack(side="right", fill="y")

        OuterFrames[i].bind("<Enter>", lambda e, canvas=Canvases[i]: canvas.bind_all("<MouseWheel>", lambda event: _on_mousewheel(event, canvas)))
        OuterFrames[i].bind("<Leave>", lambda e, canvas=Canvases[i]: canvas.unbind_all("<MouseWheel>"))
        
        OuterFrames[i].pack_propagate(False)
        OuterFrames[i].pack(fill=BOTH, expand=True)


def ResizeWindow(top, innerFrame, padx = 37):
    innerFrame.update_idletasks()  # Ensure the geometry is up to date
    w = innerFrame.winfo_width() + padx
    h = min(innerFrame.winfo_height() + 20, 700)
    top.geometry(f"{w}x{h}")
    top.update()
 
    
def Randomize(root, RandomizeButton, fileEntryVar, bdat_path, permalinkVar, randoSeedEntry, JsonOutput, outputDirVar, OptionList, BDATFiles = [],SubBDATFiles = [], ExtraCommands = [], textFolderName = "gb", extraArgs = [], windowPadding = 0, extraFiles=[], isOneFile = False):
    def ThreadedRandomize():
        entrySpot = fileEntryVar
        outSpot = f"{outputDirVar.get().strip()}/romfs/bdat"
        
        # Disable Repeated Button Click
        RandomizeButton.config(state=DISABLED)
        
        
        # Make Popup
        progressPopup = PopupDescriptions.GenericPopup(root, f"Log {datetime.datetime.now()}", defFontVar)

        randoProgressFill = ttk.Frame(progressPopup, padding=0)
        randoProgressDisplay = ttk.Label(randoProgressFill, padding=5)
        randoProgressDisplay.pack(pady=0)
        pb = ttk.Progressbar(progressPopup ,orient='horizontal',mode='determinate',length=500)
        progressPopup.deiconify() # Wait until things are ready to show
    
        # Showing Progress Diplay 
        randoProgressDisplay.config(text="Unpacking BDATs")
        randoProgressFill.pack(pady=(30,0))
        pb.pack(padx=0,pady=(0,20))
        random.seed(permalinkVar.get())
        print("Seed: " + randoSeedEntry.get())
        print("Permalink: "+  permalinkVar.get())
        os.makedirs(outSpot, exist_ok=True) # Make the directory for them
        try:
            for file in BDATFiles:
                # print("BDAT:", JsonOutput, "Exists:", os.path.exists(JsonOutput))
                subprocess.run([bdat_path, "extract", f"{entrySpot}/{file}.bdat", "-o", JsonOutput, "-f", "json", "--pretty"] + extraArgs, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
            for file in SubBDATFiles:
                subprocess.run([bdat_path, "extract", f"{entrySpot}/{textFolderName}/{file}.bdat", "-o", JsonOutput, "-f", "json", "--pretty"] + extraArgs, check=True, creationflags=subprocess.CREATE_NO_WINDOW)

            # Unpacks BDATs

        except:
            print(f"{traceback.format_exc()}") # shows the full error
            time.sleep(3)
            RandomizeButton.config(state=NORMAL)
            return

        # Runs all randomization
        popup = RunOptions(OptionList, randoProgressDisplay, root, randoSeedEntry.get(), permalinkVar.get(), pb)
        for command in ExtraCommands: # Runs extra commands like show title screen
            command()
            
        randoProgressDisplay.config(text="Packing BDATs")
    
        # Packs BDATs
        # If we are packed for users we dont want to create a window. For us we want this window to see errors from bdat-rs
        if isOneFile:
            creationFlags = subprocess.CREATE_NO_WINDOW
        else:
            creationFlags = 0
        try:
            subprocess.run([bdat_path, "pack", JsonOutput, "-o", outSpot, "-f", "json"],check=True,stderr=None,stdout=None, creationflags=creationFlags)
            # for file in 
            # Outputs common_ms in the correct file structure
            os.makedirs(f"{outSpot}/{textFolderName}", exist_ok=True)
            for file in SubBDATFiles:
                shutil.move(f"{outSpot}/{file}.bdat", f"{outSpot}/{textFolderName}/{file}.bdat")
            AddFileToOutput(outSpot, extraFiles)
            # Displays Done and Clears Text
            randoProgressDisplay.config(text="Done")
            pb['value'] = 100
            randoProgressFill.destroy()
            pb.destroy()
            
            print(f"Finished at {datetime.datetime.now()}")
        except:
            # print(f"{traceback.format_exc()}") # shows the full error
            randoProgressDisplay.config(text="Failed Outputs")

        
        # Re-Enables Randomize Button
        RandomizeButton.config(state=NORMAL)

    threading.Thread(target=ThreadedRandomize).start()

def AddFileToOutput(output, files):
    try:
        for file in files:
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

def RunOptions(OptionList, randoProgressDisplay, root, seed, permalink, pb):
    
    OptionList.sort(key=lambda x: x.prio) # Sort main options by priority
    
    errorMsgObj = PopupDescriptions.Description(bonusWidth= 15)
    errorMsgObj.Header("Randomization Finished")
    errorMsgObj.Tag(f"Seed: {seed}", pady=5, anchor="center") # Seed
    # errorMsgObj.Tag(f"Settings: {permalink}", pady=5, anchor="center") # Permalink
    errorMsgObj.Tag(f"Time: {datetime.datetime.now()}", pady=5, anchor="center") # Time
    
    def ErrorLog():
        return errorMsgObj

    for opt in OptionList: # runs pre-randomization commands before the actual options
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
        threading.Thread(target=lambda: SlowBurn(pb, nextStep)).start()

        for command in opt.commands:
            try:
                errorMsg = command()
                    
            except Exception as error:
                status = "FAILED Randomization"
                print(f"ERROR: {opt.name} | {error}")
                print(traceback.format_exc()) # shows the full error
                if errorMsg == None:
                    errorMsg = error
                errorMsgObj.Header(f"Error: {opt.name}")
                errorMsgObj.Text(errorMsg)
        pb['value'] = nextStep

    return lambda: PopupDescriptions.GenPopup(f"Log {datetime.datetime.now()}", lambda: ErrorLog(), root, defFontVar)

OptionColorLight = UI_Colors.White
OptionColorDark = UI_Colors.Gray

def SlowBurn(progressBar, nextStop):
    while(progressBar['value'] < nextStop):
        time.sleep(0.02)
        progressBar['value'] += 0.05
