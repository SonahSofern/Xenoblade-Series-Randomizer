from tkinter import *
from scripts import UI_Colors, SavedOptions
from tkinter import ttk
from tkinter.font import Font


CanvasesForStyling = []
RootsForStyling = []
defFontVar = StringVar(value="Calibri")
defFontSizeVar = IntVar(value=14)
defGUIThemeVar = StringVar(value="Dark Mode")
fontNameVar = StringVar()


defaultFont = Font(family="Calibri", size=14)
        
def LoadTheme(themeName):
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
    style.configure("Randomize.TButton")
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
