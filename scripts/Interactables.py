from tkinter import ttk
from tkinter import *
from scripts import PopupDescriptions

class Option():
    def __init__(self, _name:str, _tab, _desc:str, _commands:list = [], _defState = False, _prio = 50, _hasSpinBox = False, _spinMin = 0, _spinMax = 100, _spinDesc = "% randomized", _spinWidth = 3, _spinIncr = 10, spinDefault = 100, descData = None, _resetCommands:list = []):
        # Objects
        self.descObj = None
        self.spinBoxObj = None
        self.spinBoxLabel = None
        self.spinBoxVal = None
        self.checkBox = None
        self.checkBoxVal = None
        self.subOptions:list[SubOption] = []
        self.descData = descData
        self.spinDefault = spinDefault
        
        # Initial Data
        self.name =  _name
        self.tab = _tab
        self.desc = _desc
        self.commands:list = _commands
        self.resetCommands:list = _resetCommands
        self.hasSpinBox = _hasSpinBox
        self.subDefState = _defState
        self.prio = _prio
        OptionList.append(self)
        
        # Custom Spinboxes
        self.spinBoxMin = _spinMin
        self.spinBoxMax = _spinMax
        self.spinDesc = _spinDesc
        self.spinWidth = _spinWidth
        self.spinIncr = _spinIncr

    def DisplayOption(self, tab, root, defFont, defTheme):
        self.root = root
        self.defFont = defFont
        self.defTheme = defTheme
        self.GenStandardOption(tab)
        self.StateUpdate()
        
    def GenStandardOption(self, parentTab):    # This probably shouldnt be a class function what if we want to make a nonstandard option we could make a carveout and let you call a custom function but how would you set everything with a custom function
        # Variables
        global rowIncrement
        self.checkBoxVal = BooleanVar()
        self.spinBoxLabel = ttk.Label()
        self.spinBoxObj = ttk.Spinbox()

        # Parent Frame
        optionPanel = ttk.Frame(parentTab)
        optionPanel.grid(row = rowIncrement, column= 0, sticky="ew")
        
        # Major Option Checkbox
        self.checkBox = ttk.Checkbutton(optionPanel, variable= self.checkBoxVal, text=self.name, width=40, style="midColor.TCheckbutton", command=lambda: self.StateUpdate())
        self.checkBox.grid(row=rowIncrement, column=0, sticky="w")
        
        if self.descData == None:
            text = self.desc
        else:
            text = f"{self.desc} 🗗"
            # ◆ ◈ ✉ ⮚ ⸙ 🗗 🕮 🔎 📗 📜 🏴
        
        # Description Label or Button
        if self.descData != None:
            self.descObj = ttk.Button(optionPanel, text = text, command=lambda: PopupDescriptions.GenPopup(self.name, self.descData, self.root, self.defFont), style="BordlessBtn.TButton", width=60)
            padx = 13
        else:
            self.descObj = ttk.Label(optionPanel, text=self.desc, anchor="w", width=60, wraplength=400)
            padx= 0
        self.descObj.grid(row=rowIncrement, column=1, sticky="w", padx=padx)
        
        # % Boxes
        if self.hasSpinBox:
            self.spinBoxVal = IntVar(value=self.spinDefault)
            self.spinBoxObj = ttk.Spinbox(optionPanel, from_=self.spinBoxMin, to=self.spinBoxMax, textvariable=self.spinBoxVal, wrap=True, width=self.spinWidth, increment=self.spinIncr, justify="center")
            self.spinBoxObj.grid(row=rowIncrement, column=2, padx=(15,0))
            self.spinBoxLabel = ttk.Label(optionPanel, text=self.spinDesc, anchor="w")
            self.spinBoxLabel.grid(row=rowIncrement, column=3, sticky="w", padx=0)


        for sub in self.subOptions:
            rowIncrement += 1
            sub.checkBoxVal = BooleanVar(value=sub.defState)
            sub.checkBox = ttk.Checkbutton(optionPanel, text=sub.name, variable=sub.checkBoxVal, width=30)
            sub.checkBox.grid(row=rowIncrement, column=0, sticky="sw")
        rowIncrement += 1

    
    def StateUpdate(self):
        if self.GetState():
            for sub in self.subOptions:
                sub.checkBox.state(["!disabled"])
            self.descObj.state(["!disabled"])
            self.spinBoxObj.state(["!disabled"])
            if self.spinBoxLabel != None: # If we dont have one
                self.spinBoxLabel.state(["!disabled"])
            for sub in self.subOptions: # Handles Dropdown
                sub.checkBox.grid()     
        else:
            for sub in self.subOptions:
                sub.checkBox.state(["disabled"])
            self.descObj.state(["disabled"])
            self.spinBoxObj.state(["disabled"])
            if self.spinBoxLabel != None:
                self.spinBoxLabel.state(["disabled"])
            for sub in self.subOptions: # Handles Dropdown
                sub.checkBox.grid_remove()
    
    def GetSpinbox(self):
        return self.spinBoxVal.get()
    
    def GetState(self):
        return self.checkBoxVal.get()

class SubOption():
    def __init__(self, _name, _parent:Option, _commands = [], _defState = True, _prio = 0, _resetCommands:list = []):
        self.name = _name
        self.checkBoxVal = BooleanVar
        self.checkBox:ttk.Checkbutton = None
        self.commands = _commands
        self.resetCommands = _resetCommands
        self.defState = _defState
        self.prio = _prio
        self.parent = _parent
        _parent.subOptions.append(self)

    def GetState(self):
        return self.checkBoxVal.get()
rowIncrement = 0   

OptionList:list[Option] = []

def UpdateAllStates():
    for opt in OptionList:
        opt.StateUpdate()