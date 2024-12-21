from tkinter import *
from UI_Colors import *
from tkinter import font, ttk

def OpenSettingsWindow(rootWindow, defaultFont):
    newWindow = Toplevel(rootWindow)
    iter = 0
    fontNameVar = StringVar()
    fontSizeVar = StringVar()
    newWindow.title("GUI Settings")
    newWindow.geometry("800x100")
    allFonts = font.families()
    newWindow.config(background=DarkerPurple)
    
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
        fontName.config(text=allFonts[iter])
        defaultFont.config(family=allFonts[iter])

    def PreviousFont(event = None):
        nonlocal iter        
        iter -= 1
        fontName.delete(0, END)
        fontName.insert(0,allFonts[iter])
        defaultFont.config(family=allFonts[iter])

    def SaveUIChanges(event = None):
        import SavedOptions
        SavedOptions.saveData([defaultFont.cget("family"), defaultFont.cget("size"), darkMode.cget("text")], "GUISavedOptions.txt")

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

    newWindow.bind("<Right>", NextFont)
    newWindow.bind("<Left>", PreviousFont) 
    newWindow.bind("<Return>", SaveUIChanges)
    newWindow.bind("<Up>", IncreaseFontSize)
    newWindow.bind("<Down>", DecreaseFontSize) 

    newWindow.config(padx=10, pady=10)
    # Still dont get these two lines but oh well
    fontNameVar.trace_add("write", lambda name, index, mode: LoadFontByName(fontNameVar.get()))
    fontSizeVar.trace_add("write", lambda name, index, mode: LoadFontSize(fontSizeVar.get()))
    
    fontTestBack = ttk.Button(newWindow, text="Previous", command=PreviousFont, width=10)
    fontName = ttk.Entry(newWindow, width=20, textvariable=fontNameVar)
    fontTestNext = ttk.Button(newWindow, text="Next", command=NextFont)
    saveFont = ttk.Button(newWindow, text="Save", command=SaveUIChanges)
    fontSize = ttk.Entry(newWindow, textvariable=fontSizeVar)
    fontSize.delete(0, END)
    fontSize.insert(0,defaultFont.cget("size"))
    fontName.delete(0, END)
    fontName.insert(0,defaultFont.cget("family"))
    fontName.pack(padx=2, pady=2, side='left', anchor="nw")
    fontSize.pack(padx=2, pady=2, side='left', anchor="nw")
    fontTestBack.pack(padx=5, pady=2, side='left', anchor="nw")
    fontTestNext.pack( padx=5, pady=2, side='left', anchor="nw")
    saveFont.pack( padx=5, pady=2, anchor="nw")
    darkMode = ttk.Button(newWindow, text="Light Mode", command=lambda: ToggleLightDarkMode(darkMode))
    darkMode.pack(padx=2, pady=2, anchor="w")
    
def ToggleLightDarkMode(togButton):
    if togButton.cget("text") == "Dark Mode":
        togButton.config(text="Light Mode")
    else:
        togButton.config(text="Dark Mode")
    
darkColor = LightBlack
lightColor = White
backgroundColor = DarkerPurple
midColor = DarkGray
midGray = MediumGray

def LoadTheme(defaultFont, root):
    
    style=ttk.Style()
    
    style.theme_create('Main', settings={
        "TNotebook": {
            "configure": {
                "font": defaultFont,
                "background": backgroundColor,
                "borderwidth": 4,
                "relief": "ridge",
            }
        },
        "TNotebook.Tab": {
            "configure": {
                "background": darkColor,
                "padding": 10,
                "font": defaultFont,
                "foreground": midGray,
                "bordercolor": darkColor,
                "borderwidth": 2,
                "focuscolor":"",# Checkbutton focus border
            },
            "map": {
                "foreground": [("selected", lightColor), ("active", lightColor)],
                "background": [("selected", midColor), ("active", midColor)]                
            }
        },
        "TButton": {
            "configure": {
                "background": darkColor,
                "foreground": lightColor,
                "font": defaultFont,
                "reliefcolor": lightColor,
                "padding": (5,3,5,3),
                "focuscolor":"",
                "relief": "ridge",
                
            },
            "map": {
                "background": [("active", midColor)],
            }
        },
        "TCheckbutton": {
            "configure": {
                "background": darkColor,
                "foreground": midGray,
                "padding": (40,3,50,3),
                "indicatorcolor": midColor,
                "indicatorbackground": midColor,
                "font": defaultFont,
                "indicatorrelief": "flat",
                "focuscolor":"",
                "indicatormargin": (0,0,10,0),
            },
            "map": {
                "indicatorcolor": [("selected", lightColor),("active", midColor)],
                "background": [("active", midColor)],
                "foreground": [("active", lightColor),("selected", lightColor)],
                "indicatorbackground": [("active", midColor)],
            }
        },
        "TEntry": {
            "configure": {
                "foreground": lightColor,
                "font": defaultFont,
                "fieldbackground": darkColor,
                "padding": (5,3,5,3),
                "selectbackground": lightColor,
                "selectforeground": darkColor,
                "selectborderwidth": 0,
                "relief":"ridge",
                "insertcolor": lightColor,
            }
        },
        "TScrollbar": {
            "configure": {
                "troughcolor": midColor,
                "background": darkColor,
                "borderwidth": 3,
                "relief": "ridge",
                "arrowcolor": lightColor,
            }
        },
        "TLabel": {
            "configure": {
                "foreground": midGray,
                "background": darkColor,
                "troughcolor": darkColor,
                "borderwidth": 0,
                "padding": (20, 10),
            }
        },
        "TFrame": {
            "configure": {
                "background": darkColor,
                "relief": "flat",
            },
                        "map": {
                "background": [("active", midColor)],
                "foreground": [("active", lightColor),("selected", lightColor)],
            }
        },
        "TScale": {
            "configure": {
                "background": darkColor,
                "foreground": lightColor,
                "troughrelief": "flat",
                "groovewidth": 0,
                "troughcolor": midColor,
                "darkcolor": darkColor,
                "lightcolor": darkColor,
                "borderwidth": 1,
                "sliderwidth": 100,
            }
        },
        "TSpinbox": {
            "configure": {
                "background": darkColor,
                "foreground": midGray,
                "fieldbackground": midColor,
                "darkcolor": darkColor,
                "lightcolor": darkColor,
                "insertcolor": midColor,
                "relief": "ridge",
                "padding": (1,0,0,0),
                "focuscolor":"",
                "selectforeground": midGray,
                "selectbackground": midColor,
            }
        }
    })
    style.configure("midColor.TCheckbutton", background=lightColor)
    style.configure("darkColor.TCheckbutton", background=darkColor)
    style.theme_use('Main')
    
    
    
    
# Light mode
# Toggle Light/Dark Button
# Load theme at start
# Make custom topbar
# Alternating colors or Seperator

# Make setting that turns off or on all inputs boxes/sliders etc.