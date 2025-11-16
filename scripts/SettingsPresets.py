import tkinter as tk
from tkinter import ttk
from scripts import GUISettings, SavedOptions, Interactables, ScrollPanel
import tkinter as tk
import os

garbList = []

def PresetsWindow(parent, interactAbles, game):
    defaultName = "Enter name.txt"
    dir = f"{game}/SaveData"
    premadeDir = f"{game}/Presets"
    
    outerCustomFrame = ttk.Frame(parent)
    outerPremadeFrame = ttk.Frame(parent)
    outerPremadeFrame.pack(side="left", fill="both", expand=True)
    outerCustomFrame.pack(side="left", fill="both", expand=True)
    
    titleLabel = ttk.Label(outerPremadeFrame, text="Get started with some recommended presets",style="Title.TLabel")
    titleLabel.pack(anchor="w", pady = (5,5))
    PremadePresetScroll = ScrollPanel.ScrollablePanel(outerPremadeFrame)
    customTitleLabel = ttk.Label(outerCustomFrame, text="Add your own custom presets",style="Title.TLabel")
    customTitleLabel.pack(anchor="w", pady = (5,5))
    CustomPresetScroll = ScrollPanel.ScrollablePanel(outerCustomFrame)
    
    saveasPresetBtn = ttk.Button(outerCustomFrame, text="Save Current Settings as Preset", command=lambda: (SavedOptions.saveData(interactAbles, defaultName, game), CreatePreset(defaultName, CustomPresetScroll.innerFrame, interactAbles, game, dir, True)))
    saveasPresetBtn.pack(pady=(5,5),padx=(0,0), anchor="nw")
    
    GetPresets(PremadePresetScroll.innerFrame, premadeDir, interactAbles, game, False)
    GetPresets(CustomPresetScroll.innerFrame, dir, interactAbles, game, True)
    
def GetPresets(innerFrame, dir, interacts, game, isDeletable): 
    for filename in os.listdir(dir):
        CreatePreset(filename, innerFrame, interacts, game, dir, isDeletable)

def CreatePreset(filename, innerFrame, interactables, game, dir, isDeletable):
    # print("Created Preset")
    pnameVar = tk.StringVar(value=filename.replace(".txt", ""))
    oldnameVar = tk.StringVar(value=pnameVar.get())
    presetFrame = ttk.Frame(innerFrame)
    presetFrame.pack(padx=3, pady=3, fill="both")
    garbList.append(pnameVar) # Garbage collection strikes again
    
    name = ttk.Entry(presetFrame, textvariable=pnameVar)
    pnameVar.trace_add("write", lambda *args: OnNameChange(dir, pnameVar, oldnameVar))
    name.pack(side="left", padx=(0,5))
    
    loadBtn = ttk.Button(presetFrame, text="📥 Load", command=lambda: SavedOptions.loadData(interactables, f"{pnameVar.get()}.txt", game))
    loadBtn.pack(side="left", padx=(0,5))
    
    if isDeletable:
        deleteBtn = ttk.Button(presetFrame, text="✖ Delete", command=lambda preset=presetFrame: (DeletePreset(preset, pnameVar, game)))
        deleteBtn.pack(side="left")

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