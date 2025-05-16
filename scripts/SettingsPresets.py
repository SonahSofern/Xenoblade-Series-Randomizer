import tkinter as tk
from tkinter import ttk
from scripts import GUISettings, SavedOptions
import tkinter as tk
import os
OpenWindows = []
def GenPopup(optionName, root, defaultFont, dir, interactAbles, game):
    defaultName = "Enter preset name.txt"
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
    
    saveasPresetBtn = ttk.Button(InnerFrame, text="Save Current Settings as Preset", command=lambda: (SavedOptions.saveData(interactAbles, defaultName ,game), CreatePreset(defaultName, InnerFrame, interactAbles, game, dir, top)))
    saveasPresetBtn.pack()

    
    LoadPresets(InnerFrame, dir, interactAbles, game, top)


    
    top.protocol("WM_DELETE_WINDOW", lambda: (OpenWindows.remove(top), top.destroy(), garbList.clear())) # remove windows from list on close

garbList = []

def LoadPresets(innerFrame, dir, interactables, game, top):
    seperator = ttk.Label(innerFrame, text="--- Presets ---")
    seperator.pack()
    for filename in os.listdir(dir):
        CreatePreset(filename, innerFrame, interactables, game, dir, top)

def CreatePreset(filename, innerFrame, interactables, game, dir, top):
    # print("Created Preset")
    pnameVar = tk.StringVar(value=filename.replace(".txt", ""))
    oldnameVar = tk.StringVar(value=pnameVar.get())
    presetFrame = ttk.Frame(innerFrame)
    presetFrame.pack(padx=3, pady=3)
    garbList.append(pnameVar) # Garbage collection strikes again
    
    loadBtn = ttk.Button(presetFrame, text="Load", command=lambda: SavedOptions.loadData(interactables, f"{pnameVar.get()}.txt", game))
    loadBtn.pack(side="left")
    
    name = ttk.Entry(presetFrame, textvariable=pnameVar)
    pnameVar.trace_add("write", lambda *args: OnNameChange(dir, pnameVar, oldnameVar))
    name.pack(side="left")
    
    deleteBtn = ttk.Button(presetFrame, text=" X ", command=lambda preset=presetFrame: (DeletePreset(preset, pnameVar, game), GUISettings.ResizeWindow(top, innerFrame, 20)))
    deleteBtn.pack(side="left")
    GUISettings.ResizeWindow(top, innerFrame, 20)

def OnNameChange(dir, var, oldnameVar):
    RenamePreset(dir, var, oldnameVar)
    UpdateOldName(oldnameVar, var)

def UpdateOldName(old, curName):
    old.set(curName.get())
    
# Delete a Preset
def DeletePreset(preset, file, game):
    preset.destroy()
    os.remove(f"{game}/SaveData/{file.get()}.txt")
    
    
# Option to name preset
def RenamePreset(dir,  strvar, oldVar):
    full_path = os.path.join(dir, f"{oldVar.get()}.txt")
    os.rename(full_path, f"{dir}/{strvar.get()}.txt")
    # print(f"renamed to {strvar}")