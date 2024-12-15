from tkinter import *
from UI_Colors import *
from tkinter import font, ttk

def NotebookFocusStyleFix(defaultFont):
    style = ttk.Style()
    style.configure("TNotebook.Tab", font=(defaultFont), padding=10)  # Change tab font
    style.layout("Tab",
    [('Notebook.tab', {'sticky': 'nswe', 'children':
        [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
            #[('Notebook.focus', {'side': 'top', 'sticky': 'nswe', 'children':
                [('Notebook.label', {'side': 'top', 'sticky': ''})],
            #})],
        })],
    })]
    )

def OpenSettingsWindow(rootWindow, defaultFont):
    newWindow = Toplevel(rootWindow)
    iter = 0
    fontNameVar = StringVar()
    fontSizeVar = StringVar()
    newWindow.title("GUI Settings")
    newWindow.geometry("800x100")
    allFonts = font.families()

    
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
    
    fontTestBack = Button(newWindow, text="Previous", command=PreviousFont, font=("Arial", 16))
    fontName = Entry(newWindow, width=20, font=("Arial", 16), textvariable=fontNameVar)
    fontTestNext = Button(newWindow, text="Next", command=NextFont, font=("Arial", 16))
    saveFont = Button(newWindow, text="Save", command=SaveUIChanges, font=("Arial", 16))
    fontSize = Entry(newWindow, width=3, font=("Arial", 16), textvariable=fontSizeVar)
    fontSize.delete(0, END)
    fontSize.insert(0,defaultFont.cget("size"))
    fontName.delete(0, END)
    fontName.insert(0,defaultFont.cget("family"))
    fontName.pack(padx=2, pady=2, side='left', anchor="nw")
    fontSize.pack(padx=2, pady=2, side='left', anchor="nw")
    fontTestBack.pack(padx=5, pady=2, side='left', anchor="nw")
    fontTestNext.pack( padx=5, pady=2, side='left', anchor="nw")
    saveFont.pack( padx=5, pady=2, anchor="nw")

    def ToggleLightDarkMode(togButton, root):
        style = ttk.Style()
        if togButton.cget("text") == "Dark Mode":
            togButton.config(text="Light Mode")
            style.theme_use('Dark')
            NotebookFocusStyleFix(defaultFont)
        else:
            togButton.config(text="Dark Mode")
            style.theme_use('Light')
            NotebookFocusStyleFix(defaultFont)
            
    darkMode = Button(newWindow, text="Dark Mode", command=lambda: ToggleLightDarkMode(darkMode, rootWindow), font=("Arial", 16))
    darkMode.pack(padx=2, pady=2, anchor="w")
    # Make setting that turns off or on all inputs boxes/sliders etc.
    try:
        style=ttk.Style()
        backgroundColor = Black
        fontColor = White
        style.theme_create('Dark', settings={
                    # ".": {
                    #     "configure": {
                    #         "background": backgroundColor, # All except tabs
                    #         "foreground": fontColor
                    #     }
                    # },
                    "TNotebook": {
                        "configure": {
                            "background":backgroundColor, # Your margin color
                                            "borderwidth": 0,                # Border width
                "relief": "flat",                # Flat style for the button (without borders)
                        }
                        
                    },
                    "TNotebook.Tab": {
                        "configure": {
                            "background": backgroundColor, # tab color when not selected
                            "padding": 10,
                            "font": defaultFont,
                            "foreground": fontColor,
                            "bordercolor": backgroundColor
                        },
                        "map": {
                            "background": [("selected", Gray)], # Tab color when selected
                            "foreground": [("selected", Black)], # Tab color when selected
                        }
                    },
                    "TButton": {
            "configure": {
                "background": backgroundColor,  # Button background color
                "foreground": fontColor,        # Button text color
                "font": defaultFont,            # Button font
                "borderwidth": 1,               # Button border width
                "relief": "flat",               # Button style (flat, raised, sunken, etc.)
            },
            "map": {
                "background": [("active", Gray)],  # Button background when active (pressed)
                "foreground": [("active", Black)],  # Button text color when active (pressed)
            }
        },
                        "TCheckbutton": {
            "configure": {
                "background": backgroundColor,  # Your background color
                "foreground": fontColor,         # Text color
                "font": defaultFont,             # Font for text
                "borderwidth": 0,                # Border width
                "relief": "flat",                # Flat style for the button (without borders)
            },
            "map": {
                "background": [("active", Gray)],  # Background when active (checked or pressed)
                "foreground": [("active", Black)],  # Text color when active
            }
        },
                            "TEntry": {
            "configure": {
                "foreground": fontColor,         # Text color
                "font": defaultFont,             # Font for text
                "fieldbackground": backgroundColor,
                                "borderwidth": 0,                # Border width
                "relief": "flat",                # Flat style for the button (without borders)
            }
        },
                                                        "TScrollbar": {
            "configure": {
                "foreground": fontColor,         # Text color
                "background": backgroundColor,
                "troughcolor": backgroundColor,
                                "borderwidth": 0,                # Border width
                "relief": "flat",                # Flat style for the button (without borders)
            }
        }
                    })
        backgroundColor = White
        fontColor = Black
        style.theme_create('Light', settings={
                    # ".": {
                    #     "configure": {
                    #         "background": backgroundColor, # All except tabs
                    #         "foreground": fontColor
                    #     }
                    # },
                    "TNotebook": {
                        "configure": {
                            "background":backgroundColor, # Your margin color
                        }
                    },
                    "TNotebook.Tab": {
                        "configure": {
                            "background": backgroundColor, # tab color when not selected
                            "font":fontColor,
                            "padding": 10,
                            "font": defaultFont,
                            "foreground": fontColor,
                            "bordercolor": backgroundColor
                        },
                        "map": {
                            "background": [("selected", Gray)], # Tab color when selected
                            "foreground": [("selected", Black)], # Tab color when selected
                        }
                    }
                    })
    except:
        pass
