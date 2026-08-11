from tkinter import *
from tkinter import ttk
root = Tk()
from scripts import Theme, XCRandomizer
import XCDE.XCDE_Scripts.XCDE_Settings as XCDE
# import XC2.XC2_Scripts.XC2_Settings as XC2
# import XC3.XC3_Scripts.XC3_Settings as XC3
# import XCXDE.XCXDE_Scripts.XCXDE_Settings as XCXDE

# Set the width and height based on the primary monitor pixel count
Theme.windowWidth = str(int(root.winfo_screenwidth() * 0.8))
Theme.windowHeight = str(int(root.winfo_screenheight() * 0.8))

Theme.RootsForStyling.append(root)
Version = "1.4.2"
title = f"Xenoblade Chronicles Series Randomizer {Version}"

XCRandomizer.CheckIfUserNeedsUpdate(Version, root)

# The Notebook
MainWindow = ttk.Notebook(root, padding=0, style = "centeredTabs.TNotebook")
MainWindow.pack(fill="both", expand=True, padx=0, pady=0)

root.title(title)
root.option_add("*Font", Theme.defaultFont)
root.geometry(f'{Theme.windowWidth}x{Theme.windowHeight}')
    
icon = PhotoImage(file=XCRandomizer.Onefile.Directory("images/XCIcon.png"))
root.iconphoto(True, icon)
root.attributes(alpha=0)

# Test =1
# Tabs = {
#     Test: 'Test',
# }
# XCRandomizer.Interactables.Game = "XC2" 

# TboxOption = XCRandomizer.Interactables.Option("Field Checks", Test, "Randomizes treasures from field checks into the chosen types")
# # TboxOption_Dropdown = XCRandomizer.Interactables.Dropdown(TboxOption)
# TboxOptionSub = XCRandomizer.Interactables.SubOption("Test", TboxOption)
# TboxOptionSub_Spinbox = XCRandomizer.Interactables.SubDropdown(TboxOptionSub, values=[XCRandomizer.Interactables.DropdownOption("Test", 123), XCRandomizer.Interactables.DropdownOption("Test1", 12223)])
# TboxOptionSub2 = XCRandomizer.Interactables.SubOption("Test2", TboxOption)
# TboxOptionSub2_Spinbox = XCRandomizer.Interactables.SubSpinbox(TboxOptionSub2)
# TboxOptionSub3 = XCRandomizer.Interactables.SubOption("Test3", TboxOption)
# TestOption = XCRandomizer.Interactables.Option("Field Checks", Test, "Randomizes treasures from field checks into the chosen types")
# TestOption_Spinbox = XCRandomizer.Interactables.Spinbox(TestOption)
# XCRandomizer.CreateMainWindow(root, MainWindow, XCRandomizer.GameWindowData("XC2", "1", "Test", XCRandomizer.StringVar(), XCRandomizer.StringVar(), Tabs, nouns=["Test"], verbs=["Test"]))

XCRandomizer.CreateMainWindow(root, MainWindow, XCDE.WindowData)
# XCRandomizer.CreateMainWindow(root, MainWindow, XC2.WindowData)
# XCRandomizer.CreateMainWindow(root, MainWindow, XC3.WindowData)
# XCRandomizer.CreateMainWindow(root, MainWindow, XCXDE.WindowData)

root.attributes(alpha=1)

def CloseProtocol(): # Save before closing
    for cmd in XCRandomizer.saveCommands:
        cmd() 
    root.destroy()

root.protocol("WM_DELETE_WINDOW", CloseProtocol)

XCRandomizer.PopupDescriptions.center_window(root)
root.mainloop()