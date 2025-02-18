from tkinter import *
from UI_Colors import *
from tkinter import font, ttk

# I need to figure out this dumb logic where Im repeating variables (for example staticfont) 
import SavedOptions


CanvasesForStyling = []
RootsForStyling = []
defFontVar = StringVar(value="Arial")
defFontSizeVar = IntVar(value=13)
defGUIThemeVar = StringVar(value="Dark Mode")

fontType = SavedOptions.SavedEntry("Font", defFontVar)
fontSizeSave = SavedOptions.SavedEntry("Font Size", defFontSizeVar)
GUITheme = SavedOptions.SavedEntry("Theme", defGUIThemeVar)

GUIWindow = None

def OpenSettingsWindow(rootWindow, defaultFont, defaultTheme):
    
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
        SavedOptions.saveData([fontType,fontSizeSave,GUITheme], "GUISavedOptions.txt")

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
        fontNameVar = StringVar()
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
        # Still dont get these two lines but oh well
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
    "backgroundColor": Red,
    "darkColor": LightGray,
    "midColor": White,
    "midGray": MiddleLightGray,
    "lightColor": LightBlack,
    }

    darkThemeColors = {
    "backgroundColor": DarkerPurple,
    "darkColor": LightBlack,
    "midColor": DarkGray,
    "midGray": MediumGray,
    "lightColor": White,
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
                    "borderwidth": 3,
                    "relief": "ridge",
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
                    "background": currentTheme["darkColor"],
                    "foreground": currentTheme["lightColor"],
                    "fieldbackground": currentTheme["midColor"],
                    "darkcolor": currentTheme["darkColor"],
                    "lightcolor": currentTheme["darkColor"],
                    "insertcolor": currentTheme["midColor"],
                    "relief": "ridge",
                    "padding": (1,0,0,0),
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
            }
        })
    except:
        pass
    
    style.theme_use(themeName)
    from tkinter.font import Font
    staticFont = Font(family="Arial", size=16)
    style.configure("midColor.TCheckbutton", padding=(20, 10))
    style.configure("STATIC.TButton", font=staticFont)
    style.configure("BorderlessLabel.TLabel", background=currentTheme["backgroundColor"], foreground=White)
    style.configure("NoBackground.TFrame", background=currentTheme["backgroundColor"])

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