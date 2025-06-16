import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) # Allows us to use the scripts folder as a module
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import tkinter as tk
root = Tk()
from scripts import GUISettings

GUISettings.RootsForStyling.append(root)

windowWidth = "1600"
windowHeight = "900"
defaultFont = Font(family="Calibri", size=14)

# The Notebook
MainWindow = ttk.Notebook(root)
XenobladeDE = ttk.Frame(MainWindow)
Xenoblade2  = ttk.Frame(MainWindow)
Xenoblade3 = ttk.Frame(MainWindow)
XenobladeXDE  = ttk.Frame(MainWindow)
MainWindow.add(XenobladeDE, text ="Xenoblade DE") 
MainWindow.add(Xenoblade2, text ="Xenoblade 2") 
MainWindow.add(Xenoblade3, text ="Xenoblade 3") 
MainWindow.add(XenobladeXDE, text ="Xenoblade X DE")
MainWindow.pack()

root.title(f"Xenoblade Series Randomizer")
root.option_add("*Font", defaultFont)
root.geometry(f'{windowWidth}x{windowHeight}')
GUISettings.LoadTheme(defaultFont, GUISettings.defGUIThemeVar.get())


from XC2.XC2_Scripts.XC2_Randomizer import *
scripts.XCRandomizer.CreateMainWindow(Xenoblade2, "XC2", Version, "Xenoblade Chronicles 2 Randomizer", Options.Tabs, extraCommands, mainFolderNames, subFolderNames, SeedNames.Nouns, SeedNames.Verbs, backgroundImages=backgrounds, extraFiles=[TitlescreenSplash])




root.mainloop()