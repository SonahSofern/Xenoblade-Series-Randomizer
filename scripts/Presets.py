import tkinter as tk
from tkinter import ttk
from scripts import SavedOptions, ScrollPanel
import tkinter as tk
import os

garbList = []

def PresetsWindow(parent, interactAbles, game):
    defaultName = "Enter name.txt"
    dir = f"{game}/SaveData"
    premadeDir = f"{game}/Presets"
    
    outerCustomFrame = ttk.Frame(parent)
    outerPremadeFrame = ttk.Frame(parent)
    outerPremadeFrame.pack(side="left", fill="both", expand=True, padx=(0,10))
    outerCustomFrame.pack(side="right", fill="both", expand=True, padx=(10,0))
    
    titleLabel = ttk.Label(outerPremadeFrame, text="Get started with some recommended presets", style="Title.TLabel")
    titleLabel.pack(anchor="w", pady = (5,5))
    PremadePresetScroll = ScrollPanel.ScrollablePanel(outerPremadeFrame)
    customTitleLabel = ttk.Label(outerCustomFrame, text="Use your own custom presets", style="Title.TLabel")
    customTitleLabel.pack(anchor="w", pady = (5,5))
    CustomPresetScroll = ScrollPanel.ScrollablePanel(outerCustomFrame)
    
    saveasPresetBtn = ttk.Button(outerCustomFrame, text="Add Current Settings as Preset", command=lambda: (SavedOptions.saveData(interactAbles, defaultName, f"{game}/SaveData"), CreatePreset(defaultName, CustomPresetScroll.innerFrame, interactAbles, dir, False)))
    saveasPresetBtn.pack(pady=(5,5), padx=(0,0), anchor="nw")
    
    GetPresets(PremadePresetScroll.innerFrame, premadeDir, interactAbles, True)
    GetPresets(CustomPresetScroll.innerFrame, dir, interactAbles, False)
    
def GetPresets(innerFrame, dir, interacts, isFinal): 
    for filename in os.listdir(f"{dir}"):
        CreatePreset(filename, innerFrame, interacts, dir, isFinal)

def CreatePreset(filename, innerFrame, interactables, dir, isFinal):
    # print("Created Preset")
    pnameVar = tk.StringVar(value=filename.replace(".txt", "")) # Used so we have a reference variable that can be updated onNameChange and still load properly
    oldnameVar = tk.StringVar(value=pnameVar.get())
    presetFrame = ttk.Frame(innerFrame)
    presetFrame.pack(padx=3, pady=3, fill="both")
    garbList.append(pnameVar) # Garbage collection strikes again
    
    name = ttk.Entry(presetFrame, textvariable=pnameVar)
    pnameVar.trace_add("write", lambda *args: OnNameChange(dir, pnameVar, oldnameVar))
    name.pack(side="left", padx=(0,5))
    
    loadBtn = ttk.Button(presetFrame, text="📥 Load", command=lambda: SavedOptions.loadData(interactables, f"{pnameVar.get()}.txt", dir))
    loadBtn.pack(side="left", padx=(0,5))
        
    if not isFinal:
        deleteBtn = ttk.Button(presetFrame, text="✖ Delete", command=lambda preset=presetFrame: (DeletePreset(preset, pnameVar, dir)))
        deleteBtn.pack(side="left")
        
    if isFinal:
        name.config(state="readonly")
        
def OnNameChange(dir, var, oldnameVar):
    RenamePreset(dir, var, oldnameVar)
    UpdateOldName(oldnameVar, var)

def UpdateOldName(old, curName):
    old.set(curName.get())
    
# Delete a Preset
def DeletePreset(preset, file, game):
    preset.destroy()
    os.remove(f"{game}/{file.get()}.txt")
    
# Option to name preset
def RenamePreset(dir,  strvar, oldVar):
    full_path = os.path.join(dir, f"{oldVar.get()}.txt")
    os.rename(full_path, f"{dir}/{strvar.get()}.txt")
    # print(f"renamed to {strvar}")