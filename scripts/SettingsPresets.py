import tkinter as tk
from tkinter import ttk
from scripts import GUISettings, SavedOptions
import tkinter as tk
import os

garbList = []

def PresetsWindow(parent, interactAbles, game):
    defaultName = "Enter preset name.txt"
    dir = f"{game}/SaveData"
    
    Outerframe = ttk.Frame(parent) 
    canv = tk.Canvas(Outerframe)
    InnerFrame = ttk.Frame(canv, style="bordered.TFrame")
    

    LoadPresets(InnerFrame, dir, interactAbles, game)
    GUISettings.CreateScrollBars([Outerframe], [canv], [InnerFrame])
    saveasPresetBtn = ttk.Button(Outerframe, text="Save Current Settings as Preset", command=lambda: (SavedOptions.saveData(interactAbles, defaultName, game), CreatePreset(defaultName, InnerFrame, interactAbles, game, dir)))
    saveasPresetBtn.pack(pady=(0,10),padx=(10,0), anchor="e")

def LoadPresets(innerFrame, dir, interactables, game):
    for filename in os.listdir(dir):
        CreatePreset(filename, innerFrame, interactables, game, dir)

def CreatePreset(filename, innerFrame, interactables, game, dir):
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