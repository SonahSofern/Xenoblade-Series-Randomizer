import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # Allows us to use the scripts folder as a module
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
root = Tk()
from scripts import GUISettings, XCRandomizer

GUISettings.RootsForStyling.append(root)

windowWidth = "1600"
windowHeight = "900"
defaultFont = Font(family="Calibri", size=14)

# The Notebook
MainWindow = ttk.Notebook(root, padding=0, style = "centeredTabs.TNotebook")
MainWindow.pack(fill="both", expand=True, padx=0, pady=0)

root.title(f"Xenoblade Chronicles Randomizer")
root.option_add("*Font", defaultFont)
root.geometry(f'{windowWidth}x{windowHeight}')
GUISettings.LoadTheme(defaultFont, GUISettings.defGUIThemeVar.get())

if XCRandomizer.isOneFile: 
    icon_path = os.path.join(sys._MEIPASS, 'images', 'XCIcon.png')
else:
    icon_path = "images/XCIcon.png"
    
icon = PhotoImage(file=icon_path)
root.iconphoto(True, icon)

from XCDE.XCDE_Scripts.XCDE_Settings import *
XCRandomizer.CreateMainWindow(root, MainWindow, "XCDE", Version, "Xenoblade Chronicles DE Randomizer", Options.Tabs, extraCommands, mainFolderNames, subFolderNames, SeedNames.Nouns, SeedNames.Verbs, backgroundImages=backgrounds, extraFiles=[TitlescreenSplash])

from XC2.XC2_Scripts.XC2_Settings import *
XCRandomizer.CreateMainWindow(root, MainWindow, "XC2", Version, "Xenoblade Chronicles 2 Randomizer", Options.Tabs, extraCommands, mainFolderNames, subFolderNames, SeedNames.Nouns, SeedNames.Verbs, backgroundImages=backgrounds, extraFiles=[TitlescreenSplash])

from XC3.XC3_Scripts.XC3_Settings import *
XCRandomizer.CreateMainWindow(root, MainWindow, "XC3", Version, "Xenoblade Chronicles 3 Randomizer", Options.Tabs, extraCommands, mainFolderNames, subFolderNames, SeedNames.Nouns, SeedNames.Verbs, textFolderName,extraArgs=extraArgs, backgroundImages=backgrounds)

from XCXDE.XCXDE_Scripts.XCXDE_Settings import *
XCRandomizer.CreateMainWindow(root, MainWindow, "XCXDE", Version, "Xenoblade Chronicles X DE Randomizer", Options.Tabs, extraCommands, mainFolderNames, subFolderNames, SeedNames.Nouns, SeedNames.Verbs, backgroundImages=backgrounds)

root.protocol("WM_DELETE_WINDOW", lambda: ([cmd() for cmd in XCRandomizer.saveCommands] and root.destroy()))

root.mainloop()