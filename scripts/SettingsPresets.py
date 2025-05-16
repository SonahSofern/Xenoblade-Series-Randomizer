import tkinter as tk
from tkinter import ttk
from scripts import GUISettings, SavedOptions
import tkinter as tk
import os
OpenWindows = []
def GenPopup(optionName, root, defaultFont, dir, interactAbles, game):
    # Check if a popup with the same title is already open
    for top in OpenWindows:
        if top.winfo_exists() and top.title() == optionName:
            top.focus()
            top.deiconify() # unminimizes
            return  # If it exists, don't create a new one
        
    top = tk.Toplevel(root, padx=10, pady=10)  # Create a new top-level window
    top.geometry("600x600")
    top.title(optionName)
    GUISettings.RootsForStyling.append(top)
    OpenWindows.append(top)
    
    Outerframe = ttk.Frame(top) 
    
    canv = tk.Canvas(Outerframe)
    
    InnerFrame = ttk.Frame(canv)
    GUISettings.CreateScrollBars([Outerframe], [canv], [InnerFrame])
    GUISettings.LoadTheme(defaultFont, GUISettings.defGUIThemeVar.get())
    LoadPresets(InnerFrame, dir, interactAbles, game)
    GUISettings.ResizeWindow(top, InnerFrame)


    
    top.protocol("WM_DELETE_WINDOW", lambda: (OpenWindows.remove(top), top.destroy(), garbList.clear())) # remove windows from list on close

garbList = []

def LoadPresets(innerFrame, dir, interactables, game):
    for filename in os.listdir(dir):
        presetFrame = ttk.Frame(innerFrame)
        presetFrame.pack(padx=3, pady=3)
        
        loadBtn = ttk.Button(presetFrame, text="Load", command=lambda: SavedOptions.loadData(interactables, filename, game))
        loadBtn.pack(side="left")
        
        pname = tk.StringVar(value=filename.replace(".txt", ""))
        name = ttk.Entry(presetFrame, textvariable=pname)
        name.bind("<FocusOut>", RenamePreset(f"{dir}/{filename}", pname))
        name.pack(side="left")
        garbList.append(pname) # Garbage collection strikes again
        
        deleteBtn = ttk.Button(presetFrame, text="Delete", command=lambda: DeletePreset(presetFrame, filename))
        deleteBtn.pack(side="left")
        
        # Save Current Settings as Preset Button
        # Delete a Preset
        # Option to name preset

def DeletePreset(preset, file):
    preset.destroy()
    os.remove(f"XCDE/SaveData/{file}")
    
def RenamePreset(file, strvar):
    os.rename(file, strvar.get())