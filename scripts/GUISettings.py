from tkinter import *
from scripts import UI_Colors
from tkinter import font, ttk
import random, subprocess, shutil, os, threading, traceback, time, sys, datetime

# I need to figure out this dumb logic where Im repeating variables (for example staticfont) 
from scripts import SavedOptions


CanvasesForStyling = []
RootsForStyling = []
defFontVar = StringVar(value="Arial")
defFontSizeVar = IntVar(value=13)
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
        saveGUI = ttk.Button(newWindow, text="Save Changes", command=SaveUIChanges, style="STATIC.TButton")
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
        
        # Dark Mode Controls
        darkMode = ttk.Button(newWindow, text=defaultTheme.get(), command=lambda: ToggleLightDarkMode(darkMode, defaultFont, defaultTheme), style="STATIC.TButton")
        darkMode.grid(row=1, column=0, sticky="w", padx=5, pady=5)
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
                    "borderwidth": 4,
                    "relief": "flat",
                }
            },
            "TNotebook.Tab": {
                "configure": {
                    "background": currentTheme["darkColor"],
                    "padding": 10,
                    "font": defaultFont,
                    "foreground": currentTheme["lightColor"],
                    "bordercolor": currentTheme["darkColor"],
                    "borderwidth": 2,
                    "focuscolor":"",# Checkbutton focus border
                    "relief": "flat",
                },
                "map": {
                    "foreground": [("selected", currentTheme["lightColor"]), ("active", currentTheme["lightColor"])],
                    "background": [("selected", currentTheme["midColor"]), ("active", currentTheme["midColor"])]                
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
            
        })
    except:
        pass
    
    style.theme_use(themeName)
    from tkinter.font import Font
    staticFont = Font(family="Arial", size=16)
    style.configure("BordlessBtn.TButton", relief = FLAT)
    style.configure("midColor.TCheckbutton", padding=(20, 10))
    style.configure("STATIC.TButton", font=staticFont)
    style.configure("BorderlessLabel.TLabel", background=currentTheme["backgroundColor"], foreground=UI_Colors.White)
    style.configure("NoBackground.TFrame", background=currentTheme["backgroundColor"])
    style.configure("Header.TButton", borderwidth=0, background=currentTheme["midGray"])
    style.configure("Tag.TLabel", background= currentTheme["midGray"], relief="flat", padding=(9,2), margin=(5,0))
    style.configure("DescriptionImage.TLabel", background= currentTheme["midColor"])
    # Since Canvas and Roots arrent affected by normal styling
    for canvas in CanvasesForStyling:
        try:
            canvas.config(background=currentTheme["darkColor"], border=0)
        except:
            pass
        
    for root in RootsForStyling:
        try:
            root.config(background=currentTheme["backgroundColor"])
        except:
            pass
        
def CreateScrollBars(OuterFrames:list[ttk.Frame], Canvases:list[Canvas], InnerFrames:list[ttk.Frame], genScrollbar = True): # I never want to touch this code again lol what a nightmare
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

        def _on_mousewheel(event, canvas=Canvases[i]):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        OuterFrames[i].bind("<Enter>", lambda e, canvas=Canvases[i]: canvas.bind_all("<MouseWheel>", lambda event: _on_mousewheel(event, canvas)))
        OuterFrames[i].bind("<Leave>", lambda e, canvas=Canvases[i]: canvas.unbind_all("<MouseWheel>"))
        
        OuterFrames[i].pack_propagate(False)
        OuterFrames[i].pack(fill=BOTH, expand=True)
        

def Randomize(RandomizeButton,fileEntryVar, randoProgressDisplay, bdat_path, permalinkVar, randoSeedEntry, JsonOutput, outputDirVar, OptionList, BDATFiles = [],SubBDATFiles = [], ExtraCommands = []):
    def ThreadedRandomize():
        # Disable Repeated Button Click
        RandomizeButton.config(state=DISABLED)

        # Showing Progress Diplay 
        randoProgressDisplay.pack(side='left', anchor='w', pady=10, padx=10)
        randoProgressDisplay.config(text="Unpacking BDATs")

        random.seed(permalinkVar.get())
        print("Seed: " + randoSeedEntry.get())
        print("Permalink: "+  permalinkVar.get())
        try:
            for file in BDATFiles:
                subprocess.run([bdat_path, "extract", f"{fileEntryVar.get().strip()}/{file}.bdat", "-o", JsonOutput, "-f", "json", "--pretty"], check=True, creationflags=subprocess.CREATE_NO_WINDOW)
            for file in SubBDATFiles:
                subprocess.run([bdat_path, "extract", f"{fileEntryVar.get().strip()}/gb/{file}.bdat", "-o", JsonOutput, "-f", "json", "--pretty"], check=True, creationflags=subprocess.CREATE_NO_WINDOW)

            # Unpacks BDATs

        except:
            print(f"{traceback.format_exc()}") # shows the full error
            randoProgressDisplay.config(text="Failed Inputs")
            time.sleep(3)
            randoProgressDisplay.config(text="")
            RandomizeButton.config(state=NORMAL)
            return

        # Runs all randomization
        RunOptions(OptionList, randoProgressDisplay)
        for command in ExtraCommands: # Runs extra commands like show title screen
            command()
        randoProgressDisplay.config(text="Packing BDATs")
    
        try:
            # Packs BDATs
            subprocess.run([bdat_path, "pack", JsonOutput, "-o", outputDirVar.get().strip(), "-f", "json"], check=True, creationflags=subprocess.CREATE_NO_WINDOW)
            
            # for file in 
            # Outputs common_ms in the correct file structure
            os.makedirs(f"{outputDirVar.get().strip()}/gb", exist_ok=True)
            for file in SubBDATFiles:
                shutil.move(f"{outputDirVar.get().strip()}/{file}.bdat", f"{outputDirVar.get().strip()}/gb/{file}.bdat")

            # Displays Done and Clears Text
            randoProgressDisplay.config(text="Done")
            time.sleep(1.5)
            randoProgressDisplay.config(text="")
            randoProgressDisplay.pack_forget()
            
            print(f"Finished at {datetime.datetime.now()}")
        except:
            print(f"{traceback.format_exc()}") # shows the full error
            randoProgressDisplay.config(text="Failed Outputs")

        
        # Re-Enables Randomize Button
        RandomizeButton.config(state=NORMAL)

    threading.Thread(target=ThreadedRandomize).start()

def RunOptions(OptionList, randoProgressDisplay):
    
    OptionList.sort(key=lambda x: x.prio) # Sort main options by priority
    
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
        for command in opt.commands:
            try:
                command()
            except Exception as error:
                print(f"ERROR: {opt.name} | {error}")
                print(f"{traceback.format_exc()}") # shows the full error
    
MaxWidth = 1000
windowWidth = "1550"
windowHeight = "900"
OptionColorLight = UI_Colors.White
OptionColorDark = UI_Colors.Gray

