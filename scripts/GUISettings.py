from tkinter import *
from scripts import UI_Colors
from tkinter import font, ttk
import random, subprocess, shutil, os, threading, traceback, time, sys, datetime
import json
# I need to figure out this dumb logic where Im repeating variables (for example staticfont) 
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

GUIWindow = None

def OpenSettingsWindow(rootWindow, defaultFont, defaultTheme, Game):
    
    def LoadFontByName(name):
        defaultFont.config(family=name)

    def LoadFontSize(size):
        if ((size != "") and (0 < int(size)) and (int(size) < 60)):
            defaultFont.config(size=int(size))

    def NextFont(event= None):
        nonlocal iter
        iter += 1
        fontName.delete(0, END)
        fontName.insert(0,allFonts[iter])
        defaultFont.config(family=allFonts[iter])

    def PreviousFont(event = None):
        nonlocal iter        
        iter -= 1
        fontName.delete(0, END)
        fontName.insert(0,allFonts[iter])
        defaultFont.config(family=allFonts[iter])

    def SaveUIChanges(event = None):
        fontType.checkBoxVal.set(defaultFont.cget("family"))
        fontSizeSave.checkBoxVal.set(defaultFont.cget("size"))
        SavedOptions.saveData([fontType,fontSizeSave,GUITheme], "GUISavedOptions.txt", f"{Game}/GUI")

    def IncreaseFontSize(event = None):
        newSize = defaultFont.cget("size") + 1
        LoadFontSize(newSize)
        fontSize.delete(0, END)
        fontSize.insert(0,newSize)
        
    def DecreaseFontSize(event = None):
        newSize = defaultFont.cget("size") - 1
        LoadFontSize(newSize)
        fontSize.delete(0, END)
        fontSize.insert(0,newSize)
    
    global GUIWindow
    if GUIWindow == None or (not GUIWindow.winfo_exists()):      
        newWindow = Toplevel(rootWindow)
        GUIWindow = newWindow
        newWindow.protocol("WM_DELETE_WINDOW", lambda: (RootsForStyling.remove(newWindow), newWindow.destroy()))
        iter = 0
        fontSizeVar = StringVar()
        newWindow.title("GUI Settings")
        newWindow.geometry("1000x300")
        RootsForStyling.append(newWindow)
        allFonts = font.families()
        # Font Option Controls
        newWindow.bind("<Right>", NextFont)
        newWindow.bind("<Left>", PreviousFont) 
        newWindow.bind("<Return>", SaveUIChanges)
        newWindow.bind("<Up>", IncreaseFontSize)
        newWindow.bind("<Down>", DecreaseFontSize) 
        newWindow.config(padx=10, pady=10)
        fontNameVar.trace_add("write", lambda name, index, mode: LoadFontByName(fontNameVar.get()))
        fontSizeVar.trace_add("write", lambda name, index, mode: LoadFontSize(fontSizeVar.get()))
        from tkinter.font import Font
        staticFont = Font(family="Arial", size=16)
        fontTestBack = ttk.Button(newWindow, text="Previous", command=PreviousFont, width=10, style="STATIC.TButton")
        fontName = ttk.Entry(newWindow, width=20, textvariable=fontNameVar)
        fontTestNext = ttk.Button(newWindow, text="Next", command=NextFont, style="STATIC.TButton")
        saveGUI = ttk.Button(newWindow, text="Save Changes 🖫", command=SaveUIChanges, style="STATIC.TButton")
        fontSize = ttk.Entry(newWindow, textvariable=fontSizeVar)
        fontSize.delete(0, END)
        fontSize.insert(0,defaultFont.cget("size"))
        fontName.delete(0, END)
        fontName.insert(0,defaultFont.cget("family"))
        fontName.grid(row=0, column=0, padx=5, pady=5)
        fontSize.grid(row=0, column=1, padx=5, pady=5)
        fontTestBack.grid(row=0, column=2, padx=5, pady=5)
        fontTestNext.grid(row=0, column =3, padx=5, pady=5)
        saveGUI.grid(row=2, column=1, padx=5, pady=5)
        fontName.configure(font=staticFont)
        fontSize.configure(font=staticFont) # Have to config them like this for entry it doesnt accept style= whn you make the thing
        LoadTheme(defaultFont, defaultTheme.get())
        
        # # Dark Mode Controls
        # darkMode = ttk.Button(newWindow, text=defaultTheme.get(), command=lambda: ToggleLightDarkMode(darkMode, defaultFont, defaultTheme), style="STATIC.TButton")
        # darkMode.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    else:
        GUIWindow.focus()
        GUIWindow.deiconify() # unminimizes
    
def ToggleLightDarkMode(togButton, defaultFont, defaultTheme):
    if togButton.cget("text") == "Dark Mode":
        togButton.config(text="Light Mode")
        defaultTheme.set("Light Mode")
        LoadTheme(defaultFont, "Light Mode")
    else:
        togButton.config(text="Dark Mode")
        defaultTheme.set("Dark Mode")
        LoadTheme(defaultFont, "Dark Mode")
        
def LoadTheme(defaultFont, themeName):
    style= ttk.Style()
    # Initial colors for the themes
    lightThemeColors = {
    "backgroundColor": UI_Colors.Red,
    "darkColor": UI_Colors.LightGray,
    "midColor": UI_Colors.White,
    "midGray": UI_Colors.MiddleLightGray,
    "lightColor": UI_Colors.LightBlack,
    }

    darkThemeColors = {
    "backgroundColor": UI_Colors.DarkerPurple,
    "darkColor": UI_Colors.LightBlack,
    "midColor": UI_Colors.DarkGray,
    "midGray": UI_Colors.MediumGray,
    "lightColor": UI_Colors.White,
    }
    if themeName == "Dark Mode":
        currentTheme = darkThemeColors
    else:
        currentTheme = lightThemeColors
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
                    "expand": [("selected", 0), ("active", 2)]                
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
                    "background": [("active", currentTheme["midColor"])],
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
    style.configure("BordlessBtn.TButton", relief = FLAT)
    style.configure("midColor.TCheckbutton", padding=(20, 10))
    style.configure("centeredTabs.TNotebook", tabposition= "nw", borderwidth=0)
    style.configure("STATIC.TButton", font=staticFont)
    style.configure("BorderlessLabel.TLabel", background=currentTheme["darkColor"], foreground=UI_Colors.White)
    style.configure("NoBackground.TFrame", background=currentTheme["backgroundColor"])
    style.configure("Header.TButton", borderwidth=0, background=currentTheme["midGray"])
    style.configure("Tag.TLabel", background= currentTheme["midGray"], relief="flat", padding=(9,2), margin=(5,0))
    style.configure("DescriptionImage.TLabel", background= currentTheme["midColor"])
    style.configure("noMargin.TLabel", margin=(0,0), padding=(20,0))

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
 
    
def Randomize(root,RandomizeButton,fileEntryVar, randoProgressDisplay,randoProgressFill,SettingsButton,pb, bdat_path, permalinkVar, randoSeedEntry, JsonOutput, outputDirVar, OptionList, BDATFiles = [],SubBDATFiles = [], ExtraCommands = [], textFolderName = "gb", extraArgs = [], windowPadding = 0, extraFiles=[]):
    def ThreadedRandomize():
        entrySpot = fileEntryVar.get().strip()
        outSpot = f"{outputDirVar.get().strip()}/romfs/bdat"
        # Disable Repeated Button Click
        RandomizeButton.config(state=DISABLED)
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
                subprocess.run([bdat_path, "extract", f"{entrySpot}/{file}.bdat", "-o", JsonOutput, "-f", "json", "--pretty"] + extraArgs, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
            for file in SubBDATFiles:
                subprocess.run([bdat_path, "extract", f"{entrySpot}/{textFolderName}/{file}.bdat", "-o", JsonOutput, "-f", "json", "--pretty"] + extraArgs, check=True, creationflags=subprocess.CREATE_NO_WINDOW)

            # Unpacks BDATs

        except:
            print(f"{traceback.format_exc()}") # shows the full error
            randoProgressDisplay.config(text="Failed Inputs")
            time.sleep(3)
            RandomizeButton.config(state=NORMAL)
            return

        # Runs all randomization
        popup = RunOptions(OptionList, randoProgressDisplay, root, randoSeedEntry.get(), permalinkVar.get(), pb)
        for command in ExtraCommands: # Runs extra commands like show title screen
            command()
            
        randoProgressDisplay.config(text="Packing BDATs")
    
        try:
            # Packs BDATs
            subprocess.run([bdat_path, "pack", JsonOutput, "-o", outSpot, "-f", "json"], check=True, creationflags=subprocess.CREATE_NO_WINDOW)
            
            # for file in 
            # Outputs common_ms in the correct file structure
            os.makedirs(f"{outSpot}/{textFolderName}", exist_ok=True)
            for file in SubBDATFiles:
                # print(f"{outputDirVar.get().strip()}/{file}.bdat")
                # print(f"{outputDirVar.get().strip()}/{textFolderName}/{file}.bdat")
                shutil.move(f"{outSpot}/{file}.bdat", f"{outSpot}/{textFolderName}/{file}.bdat")
            AddFileToOutput(outSpot, extraFiles)
            # Displays Done and Clears Text
            randoProgressDisplay.config(text="Done")
            pb['value'] = 100
            time.sleep(1.5)
            popup()
            randoProgressFill.pack_forget()
            pb.pack_forget()
            
            print(f"Finished at {datetime.datetime.now()}")
        except:
            print(f"{traceback.format_exc()}") # shows the full error
            randoProgressDisplay.config(text="Failed Outputs")

        
        # Re-Enables Randomize Button
        RandomizeButton.config(state=NORMAL)
        pb["value"] = 0

    threading.Thread(target=ThreadedRandomize).start()

def AddFileToOutput(output, files):
    for file in files:
        outputSpot = f"{os.path.dirname(output)}/{file.location}"
        os.makedirs(outputSpot, exist_ok=True)
        shutil.copy(random.choice(file.images), f"{outputSpot}/{file.filename}")



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

    return lambda: PopupDescriptions.GenPopup(f"Log {datetime.datetime.now()}", lambda: ErrorLog(),root,defFontVar)

    

OptionColorLight = UI_Colors.White
OptionColorDark = UI_Colors.Gray

def SlowBurn(progressBar, nextStop):
    while(progressBar['value'] < nextStop):
        time.sleep(0.02)
        progressBar['value'] += 0.05

def RandomizeButtonDice(button:ttk.Button):
    selection = [ "⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    curText = button.cget("text")
    dice1 = random.choice(selection)
    dice2 = random.choice(selection)
    newText = f"{dice1} {curText} {dice2}"
    button.config(text=newText)
    time.sleep(1)
    
    # Place random dice on both sides of the word
    # Randomly swap them every second to simulate movement and randomization