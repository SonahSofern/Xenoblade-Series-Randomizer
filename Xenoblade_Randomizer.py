import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # Allows us to use the scripts folder as a module
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import tkinter as tk
root = Tk()
from scripts import GUISettings, XCRandomizer

GUISettings.RootsForStyling.append(root)

windowWidth = "1600"
windowHeight = "900"
defaultFont = Font(family="Calibri", size=14)

# The Notebook
MainWindow = ttk.Notebook(root, padding=0)
XenobladeDE = ttk.Frame(MainWindow)
Xenoblade2  = ttk.Frame(MainWindow)
Xenoblade3 = ttk.Frame(MainWindow)
XenobladeXDE  = ttk.Frame(MainWindow)
MainWindow.add(XenobladeDE, text ="Xenoblade DE") 
MainWindow.add(Xenoblade2, text ="Xenoblade 2") 
MainWindow.add(Xenoblade3, text ="Xenoblade 3") 
MainWindow.add(XenobladeXDE, text ="Xenoblade X DE")
MainWindow.pack(fill="both", expand=True, padx=0, pady=0)

root.title(f"Xenoblade Series Randomizer")
root.option_add("*Font", defaultFont)
root.geometry(f'{windowWidth}x{windowHeight}')
GUISettings.LoadTheme(defaultFont, GUISettings.defGUIThemeVar.get())

if XCRandomizer.isOneFile: 
    icon_path = os.path.join(sys._MEIPASS, 'Images', 'XCIcon.ico')
else:
    icon_path = "_internal/Images/XCIcon.png"
    
icon = PhotoImage(file=icon_path)
root.iconphoto(True, icon)


from XC2.XC2_Scripts.XC2_Randomizer import *
XCRandomizer.CreateMainWindow(root, Xenoblade2, "XC2", Version, "Xenoblade Chronicles 2 Randomizer", Options.Tabs, extraCommands, mainFolderNames, subFolderNames, SeedNames.Nouns, SeedNames.Verbs, backgroundImages=backgrounds, extraFiles=[TitlescreenSplash])

from XCDE.XCDE_Scripts.XCDE_Randomizer import *
XCRandomizer.CreateMainWindow(root, XenobladeDE, "XCDE", Version, "Xenoblade Chronicles DE Randomizer", Options.Tabs, extraCommands, mainFolderNames, subFolderNames, SeedNames.Nouns, SeedNames.Verbs, backgroundImages=backgrounds, extraFiles=[TitlescreenSplash])

from XC3.XC3_Scripts.XC3_Randomizer import *
XCRandomizer.CreateMainWindow(root, Xenoblade3,  "XC3", Version, "Xenoblade Chronicles 3 Randomizer", Options.Tabs, extraCommands, mainFolderNames, subFolderNames, SeedNames.Nouns, SeedNames.Verbs, textFolderName,extraArgs=extraArgs, backgroundImages=backgrounds)

from XCXDE.XCXDE_Scripts.XCXDE_Randomizer import *
XCRandomizer.CreateMainWindow(root, XenobladeXDE, "XCXDE", Version, "Xenoblade Chronicles X DE Randomizer", Options.Tabs, extraCommands, mainFolderNames, subFolderNames, SeedNames.Nouns, SeedNames.Verbs, backgroundImages=backgrounds)


root.mainloop()