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

root.title(f"Xenoblade Chronicles Series Randomizer")
root.option_add("*Font", defaultFont)
root.geometry(f'{windowWidth}x{windowHeight}')
GUISettings.LoadTheme(defaultFont, GUISettings.defGUIThemeVar.get())

if XCRandomizer.isOneFile: 
    icon_path = os.path.join(sys._MEIPASS, 'images', 'XCIcon.png')
else:
    icon_path = "images/XCIcon.png"
    
icon = PhotoImage(file=icon_path)
root.iconphoto(True, icon)

import XCDE.XCDE_Scripts.XCDE_Settings as XCDE
import XC2.XC2_Scripts.XC2_Settings as XC2
import XC3.XC3_Scripts.XC3_Settings as XC3
import XCXDE.XCXDE_Scripts.XCXDE_Settings as XCXDE
XCRandomizer.CreateMainWindow(root, MainWindow, "XCDE", XCDE.Version, "Xenoblade Chronicles DE Randomizer", XCDE.Options.Tabs, XCDE.extraCommands, XCDE.mainFolderNames, XCDE.subFolderNames, XCDE.SeedNames.Nouns, XCDE.SeedNames.Verbs, backgroundImages=XCDE.backgrounds, extraFiles=[XCDE.TitlescreenSplash])
XCRandomizer.CreateMainWindow(root, MainWindow, "XC2", XC2.Version, "Xenoblade Chronicles 2 Randomizer", XC2.Options.Tabs, XC2.extraCommands, XC2.mainFolderNames, XC2.subFolderNames, XC2.SeedNames.Nouns, XC2.SeedNames.Verbs, backgroundImages=XC2.backgrounds, extraFiles=[XC2.TitlescreenSplash])
XCRandomizer.CreateMainWindow(root, MainWindow, "XC3", XC3.Version, "Xenoblade Chronicles 3 Randomizer", XC3.Options.Tabs, XC3.extraCommands, XC3.mainFolderNames, XC3.subFolderNames, XC3.SeedNames.Nouns, XC3.SeedNames.Verbs, XC3.textFolderName,extraArgs=XC3.extraArgs, backgroundImages=XC3.backgrounds)
XCRandomizer.CreateMainWindow(root, MainWindow, "XCXDE", XCXDE.Version, "Xenoblade Chronicles X DE Randomizer", XCXDE.Options.Tabs, XCXDE.extraCommands, XCXDE.mainFolderNames, XCXDE.subFolderNames, XCXDE.SeedNames.Nouns, XCXDE.SeedNames.Verbs, backgroundImages=XCXDE.backgrounds)

root.protocol("WM_DELETE_WINDOW", lambda: ([cmd() for cmd in XCRandomizer.saveCommands] and root.destroy()))

root.mainloop()