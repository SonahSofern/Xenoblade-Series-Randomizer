from tkinter import ttk
from tkinter import *
from scripts import PopupDescriptions, GUISettings
from tkinter.font import Font

Game = "" # Used to tell what option goes to what games tab

class Option():
    def __init__(self, _name:str ="No Name", _tab =1, _desc:str= "No Description", _commands:list = [], defState = False, prio = 50,hasSpinBox = False, spinMin = 0, spinMax = 100, spinDesc = "% randomized", spinWidth = 3, spinIncr = 10, spinDefault = 100, descData = None,preRandoCommands:list = [], isDevOption = False):
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
        self.subDefState = defState
        self.prio = prio
        XenoOptionDict[Game].append(self)
        
        # Custom Spinboxes
        self.spinBoxMin = spinMin
        self.spinBoxMax = spinMax
        self.spinDesc = spinDesc
        self.spinWidth = spinWidth
        self.spinIncr = spinIncr
        

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
        
        self.checkBoxVal.trace_add("write",  lambda name, index, mode: self.StateUpdate())
        
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
            sub.checkBoxVal.trace_add("write",  lambda name, index, mode: self.StateUpdate())
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

class MutuallyExclusivePairing():
    def __init__(self, group1:list[Option], group2:list[Option]):
        for op in group1:
            op.clickCommands.append(lambda op=op: MutuallyExclusiveToggle(op, group2))
        for op in group2:
            op.clickCommands.append(lambda op=op: MutuallyExclusiveToggle(op, group1))

def MutuallyExclusiveToggle(op:Option, pairGroup):
    if op.checkBoxVal.get() == False:
        return
    
    conflictingOpt = [opt for opt in pairGroup if opt.GetState() == True]
    if conflictingOpt == []:
        return
    
    if AskToChooseOption(op.name, conflictingOpt):
        for op in pairGroup:
            op.checkBoxVal.set(False)
    else:
        op.checkBoxVal.set(False)
            
def AskToChooseOption(enabledOption, conflictingOptions):
    defaultFont = Font(family="Calibri", size=14)
    conflictWindow = "Conflicting Settings"

    top = Toplevel(padx=10, pady=10)  # Create a new top-level window
    top.title(conflictWindow)
    top.geometry("600x600")
    
    GUISettings.RootsForStyling.append(top)
    Outerframe = ttk.Frame(top) 
    canv = Canvas(Outerframe)
    InnerFrame = ttk.Frame(canv)
    GUISettings.CreateScrollBars([Outerframe], [canv], [InnerFrame])
    GUISettings.LoadTheme(defaultFont, GUISettings.defGUIThemeVar.get())

    conflictDesc = ttk.Label(InnerFrame, text= f"The following options are incompatible with the {enabledOption} option:", justify = "center")
    conflictDesc.grid(column = 1, row = 0, sticky=(N, S, E, W))
    
    CurRow = 1

    InnerFrame.grid_rowconfigure(CurRow, minsize = 20, weight = 1)
    CurRow += 1

    for option in conflictingOptions:
        incompatibleOption = ttk.Label(InnerFrame, text = option.name, style = "CenteredLabel.TLabel", anchor = "center", padding = (0, 5))
        incompatibleOption.grid(column = 1, row = CurRow, sticky = (N, S, E, W))
        CurRow += 1

    opt1Pressed = BooleanVar(InnerFrame)
    opt2Pressed = BooleanVar(InnerFrame)

    opt1Button = ttk.Button(InnerFrame, text= "Disable Incompatible Options", command=lambda: (opt1Pressed.set(True), top.destroy()), style = "CenteredButton.TButton")
    opt1Button.grid(column = 0, row = CurRow + 1, sticky = (N, S, E, W))
    opt2Button = ttk.Button(InnerFrame, text= f"Disable {enabledOption}", command=lambda: (opt2Pressed.set(True), top.destroy()), style = "CenteredButton.TButton")
    opt2Button.grid(column = 2, row = CurRow + 1, sticky = (N, S, E, W))

    InnerFrame.grid_rowconfigure(CurRow, minsize = 20, weight = 1)

    for col in range(3):
        InnerFrame.grid_columnconfigure(col, weight = 1, minsize = 250)

    GUISettings.ResizeWindow(top, InnerFrame)

    top.focus()
    top.deiconify()

    top.wait_window(top)

    
    if opt1Pressed.get() == True:
        ChosenResolution = True
    else:
        ChosenResolution = False

    return ChosenResolution


class Header():
    def __init__(self, childList:list[Option]):
        tab = childList[0].tab
        
        dropdown = ttk.Button()
        # make a dropdown button
        # add children into its care
        pass