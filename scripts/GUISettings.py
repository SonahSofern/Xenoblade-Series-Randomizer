from tkinter import *
from UI_Colors import *
from tkinter import font, ttk



def OpenSettingsWindow(rootWindow, defaultFont):
    newWindow = Toplevel(rootWindow)
    iter = 0
    fontNameVar = StringVar()
    fontSizeVar = StringVar()
    newWindow.title("GUI Settings")
    newWindow.geometry("1000x300")
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
    
    # Font Option Controls
    from tkinter.font import Font
    staticFont = Font(family="Arial", size=16)
    style= ttk.Style()
    style.configure("STATIC.TButton", font=staticFont)
    fontTestBack = ttk.Button(newWindow, text="Previous", command=PreviousFont, width=10, style="STATIC.TButton")
    fontName = ttk.Entry(newWindow, width=20, textvariable=fontNameVar)
    fontTestNext = ttk.Button(newWindow, text="Next", command=NextFont, style="STATIC.TButton")
    saveFont = ttk.Button(newWindow, text="Save", command=SaveUIChanges, style="STATIC.TButton")
    fontSize = ttk.Entry(newWindow, textvariable=fontSizeVar)
    fontSize.delete(0, END)
    fontSize.insert(0,defaultFont.cget("size"))
    fontName.delete(0, END)
    fontName.insert(0,defaultFont.cget("family"))
    fontName.grid(row=0, column=0, padx=5, pady=5)
    fontSize.grid(row=0, column=1, padx=5, pady=5)
    fontTestBack.grid(row=0, column=2, padx=5, pady=5)
    fontTestNext.grid(row=0, column =3, padx=5, pady=5)
    saveFont.grid(row=0, column=4, padx=5, pady=5)
    fontName.configure(font=staticFont)
    fontSize.configure(font=staticFont) # Have to config them like this for entry it doesnt accept style= whn you make the thing
    # Dark Mode Controls
    darkMode = ttk.Button(newWindow, text="Light Mode", command=lambda: ToggleLightDarkMode(darkMode, defaultFont, rootWindow), style="STATIC.TButton")
    darkMode.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    
def ToggleLightDarkMode(togButton, defaultFont, root):
    global currentTheme
    if togButton.cget("text") == "Dark Mode":
        togButton.config(text="Light Mode")
        LoadTheme(defaultFont, darkThemeColors, "Dark", root)
    else:
        togButton.config(text="Dark Mode")
        LoadTheme(defaultFont, lightThemeColors, "Light", root)


# Initial colors for the themes
lightThemeColors = {
    "backgroundColor": "white",
    "darkColor": "gray",
    "midColor": "lightgray",
    "midGray": "darkgray",
    "lightColor": "black",
}

darkThemeColors = {
    "backgroundColor": DarkerPurple,
    "darkColor": LightBlack,
    "midColor": DarkGray,
    "midGray": MediumGray,
    "lightColor": White,
}

def LoadTheme(defaultFont, currentTheme, themeName, root):
    style= ttk.Style()
    try:
        style.theme_create(themeName, settings={
            "TNotebook": {
                "configure": {
                    "font": defaultFont,
                    "background": currentTheme["backgroundColor"],
                    "borderwidth": 4,
                    "relief": "ridge",
                }
            },
            "TNotebook.Tab": {
                "configure": {
                    "background": currentTheme["darkColor"],
                    "padding": 10,
                    "font": defaultFont,
                    "foreground": currentTheme["midGray"],
                    "bordercolor": currentTheme["darkColor"],
                    "borderwidth": 2,
                    "focuscolor":"",# Checkbutton focus border
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
                    "indicatorcolor": currentTheme["midColor"],
                    "indicatorbackground": currentTheme["midColor"],
                    "font": defaultFont,
                    "indicatorrelief": "flat",
                    "focuscolor":"",
                    "indicatormargin": (0,0,10,0),
                },
                "map": {
                    "indicatorcolor": [  ("disabled", currentTheme["midColor"]),("selected", currentTheme["lightColor"]),("active", currentTheme["midColor"])],
                    "background": [("disabled", currentTheme["darkColor"]),("active", currentTheme["midColor"])],
                    "foreground": [("disabled", currentTheme["midGray"]),("active", currentTheme["lightColor"]),("selected", currentTheme["lightColor"])],
                    "indicatorbackground": [ ("disabled", currentTheme["midColor"]),("active", currentTheme["midColor"])],
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
                },
                "map": {
                    "foreground": [("disabled", currentTheme["midGray"])],
                }
            }
        })
    except:
        pass
    style.theme_use(themeName)
    style.configure("midColor.TCheckbutton", padding=(20, 10))
    root.config(background=currentTheme["backgroundColor"])

