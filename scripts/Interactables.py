from tkinter import ttk
from tkinter import *
from scripts import PopupDescriptions

Game = "" # Used to tell what option goes to what games tab

class Option():
    def __init__(self, _name:str, _tab, _desc:str, _commands:list = [], _defState = False, _prio = 50,hasSpinBox = False, _spinMin = 0, _spinMax = 100, _spinDesc = "% randomized", _spinWidth = 3, _spinIncr = 10, spinDefault = 100, descData = None,preRandoCommands:list = [], isDevOption = False):
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
        self.isDevOption = isDevOption
        self.clickCommands = []
        
        # Initial Data
        self.name =  _name
        self.tab = _tab
        self.desc = _desc
        self.commands:list = _commands
        self.preRandoCommands:list = preRandoCommands
        self.hasSpinBox = hasSpinBox
        self.subDefState = _defState
        self.prio = _prio
        XenoOptionDict[Game].append(self)
        
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
        optionPanel.grid(row = rowIncrement, column = 0, sticky="ew")
        
        # Major Option Checkbox
        self.checkBox = ttk.Checkbutton(optionPanel, variable= self.checkBoxVal, text=self.name, width=30, style="midColor.TCheckbutton", command=lambda: (self.StateUpdate(), [cmd() for cmd in self.clickCommands]))
        self.checkBox.grid(row=rowIncrement, column = 0, sticky="w")
        
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
        self.descObj.grid(row=rowIncrement, column = 1, sticky="w", padx=padx)
        
        # % Boxes
        if self.hasSpinBox:
            self.spinBoxVal = IntVar(value=self.spinDefault)
            self.spinBoxObj = ttk.Spinbox(optionPanel, from_=self.spinBoxMin, to=self.spinBoxMax, textvariable=self.spinBoxVal, wrap=True, width=self.spinWidth, increment=self.spinIncr, justify="right")
            self.spinBoxObj.grid(row=rowIncrement, column = 3, padx=(15,0))
            self.spinBoxLabel = ttk.Label(optionPanel, text=self.spinDesc, anchor="w")
            self.spinBoxLabel.grid(row=rowIncrement, column = 4, sticky="w", padx=0)


        for sub in self.subOptions:
            rowIncrement += 1
            sub.checkBoxVal = BooleanVar(value=sub.defState)
            sub.checkBox = ttk.Checkbutton(optionPanel, text=sub.name, variable=sub.checkBoxVal, width=25)
            sub.checkBox.grid(row=rowIncrement, column=0, sticky="sw")
            if sub.hasSpinBox:
                sub.spinBoxVal = IntVar(value=sub.spinDefault)
                sub.spinBoxObj = ttk.Spinbox(optionPanel, from_=sub.spinBoxMin, to=sub.spinBoxMax, textvariable=sub.spinBoxVal, wrap=True, width=sub.spinWidth, increment=sub.spinIncr, justify="right")
                sub.spinBoxObj.grid(row=rowIncrement, column=1, padx=(20,0), pady=(0,0), sticky="w")
                sub.spinBoxLabel = ttk.Label(optionPanel, text=sub.spinDesc, style="noMargin.TLabel")
                sub.spinBoxLabel.grid(row=rowIncrement, column=1, sticky="w", padx=(80,0))

        rowIncrement += 1

    
    def StateUpdate(self):
        if self.GetState():
            for sub in self.subOptions:
                sub.checkBox.state(["!disabled"])
                sub.checkBox.grid()
                if sub.spinBoxObj != None:
                    if sub.GetState():
                        sub.spinBoxObj.state(["!disabled"])
                        sub.spinBoxLabel.state(["!disabled"])
                        
                    else:
                        sub.spinBoxObj.state(["disabled"])
                        sub.spinBoxLabel.state(["disabled"])
                    sub.spinBoxObj.grid()
                    sub.spinBoxLabel.grid()
            self.descObj.state(["!disabled"])
            self.spinBoxObj.state(["!disabled"])
            if self.spinBoxLabel != None: # If we dont have one
                self.spinBoxLabel.state(["!disabled"])
        else:
            for sub in self.subOptions:
                sub.checkBox.state(["disabled"])
                sub.checkBox.grid_remove()
                if sub.spinBoxObj != None:
                    sub.spinBoxObj.grid_remove()
                    sub.spinBoxLabel.grid_remove()
            self.descObj.state(["disabled"])
            self.spinBoxObj.state(["disabled"])
            if self.spinBoxLabel != None:
                self.spinBoxLabel.state(["disabled"])
    
    def GetSpinbox(self):
        return self.spinBoxVal.get()
    
    def GetState(self):
        return self.checkBoxVal.get()

class SubOption():
    def __init__(self, _name, _parent:Option, _commands = [], _defState = True, _prio = 0, spinDefault = 0, spinMin = 0, spinMax = 100, spinWidth = 3, spinIncr = 10, hasSpinBox = False, spinPadX = 15, spinDesc = "", preRandoCommands:list = []):
        self.name = _name
        self.checkBoxVal = BooleanVar
        self.checkBox:ttk.Checkbutton = None
        self.commands = _commands    
        self.defState = _defState
        self.prio = _prio
        self.parent = _parent
        self.hasSpinBox = hasSpinBox
        self.spinBoxVal = None
        self.spinBoxObj = None
        self.spinBoxMin = spinMin
        self.spinBoxMax = spinMax
        self.spinDefault = spinDefault
        self.spinBoxLabel = None
        self.spinWidth = spinWidth
        self.spinIncr = spinIncr
        self.spinDesc = spinDesc
        _parent.subOptions.append(self)


    def GetState(self):
        return self.checkBoxVal.get()
    
    def GetSpinbox(self):
        return self.spinBoxVal.get()

rowIncrement = 0   
XenoOptionDict = {
    "XCDE": [],
    "XC2": [],
    "XC3": [],
    "XCXDE": [],
}

def UpdateAllStates(Game):
    for opt in XenoOptionDict[Game]:
        opt.StateUpdate()

class MutuallyExclusivePairing():
    def __init__(self, group1:list[Option], group2:list[Option]):
        for op in group1:
            op.clickCommands.append(lambda op=op: MutuallyExclusiveToggle(op, group2))
        for op in group2:
            op.clickCommands.append(lambda op=op: MutuallyExclusiveToggle(op, group1))

def MutuallyExclusiveToggle(op, pairGroup):
    if op.checkBoxVal.get() == False:
        pass
    else:
        for op in pairGroup:
            op.checkBoxVal.set(False)