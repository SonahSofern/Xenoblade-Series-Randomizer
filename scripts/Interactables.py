from tkinter import ttk
from tkinter import *
from scripts import PopupDescriptions, ScrollPanel, Theme, Helper

Game = "" # Used to tell what option goes to what games tab at runtime
DescriptionIndicator = "🛈"

class Label():
    def __init__(self):
        pass

class Option():
    def __init__(self, _name:str ="No Name", _tab =1, _desc:str= "No Description", commands:list = [], defState = False, prio = 50, hasSpinBox = False, spinMin = 0, spinMax = 100, spinDesc = "% randomized", spinWidth = 3, spinIncr = 10, spinDefault = 100, descData = None, preRandoCommands:list = [], isDevOption = False, stepSpeed = 0.05, filePlaceCommands:list = []):
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
        self.commands:list = commands
        self.preRandoCommands:list = preRandoCommands
        self.filePlaceCommands:list = filePlaceCommands
        self.hasSpinBox = hasSpinBox
        self.subDefState = defState
        self.prio = prio
        self.stepSpeed = stepSpeed # Controls how fast the progressbar moves during while this setting runs. 
        XenoOptionDict[Game].append(self)
        
        # Custom Spinboxes
        self.spinBoxMin = spinMin
        self.spinBoxMax = spinMax
        self.spinDesc = spinDesc
        self.spinWidth = spinWidth
        self.spinIncr = spinIncr
        
    def DisplayOption(self, tab, root, style):
        self.root = root
        self.GenStandardOption(tab, style)
        self.StateUpdate()
        
    def GenStandardOption(self, parentTab, style):    # This probably shouldnt be a class function what if we want to make a nonstandard option we could make a carveout and let you call a custom function but how would you set everything with a custom function

        # Variables
        global rowIncrement
        self.checkBoxVal = BooleanVar()
        self.spinBoxLabel = ttk.Label()
        self.spinBoxObj = ttk.Spinbox()

        # Parent Frame
        optionPanel = ttk.Frame(parentTab, style=f"{style}.TFrame", padding=(0,0,2000,0))
        optionPanel.grid(row = rowIncrement, column = 0, sticky="ew")
        
        # Major Option Checkbox
        self.checkBox = ttk.Checkbutton(optionPanel, variable= self.checkBoxVal, text=self.name, width=30, style=f"{style}.TCheckbutton", command=lambda: (self.StateUpdate(), [cmd() for cmd in self.clickCommands]))
        self.checkBox.grid(row=rowIncrement, column = 0, sticky="w")
        
        if self.descData == None:
            text = self.desc
        else:
            text = f"{self.desc} {DescriptionIndicator}"
        
        # Description Label or Button
        if self.descData != None:
            self.descObj = ttk.Button(optionPanel, text = text, command=lambda: PopupDescriptions.StyledPopup(self.name, self.descData, self.root), style=f"{style}.TButton", width=60)
            padx = 13
        else:
            self.descObj = ttk.Label(optionPanel, text=self.desc, anchor="w", width=60, style=f"{style}.TLabel", wraplength=400)
            padx= 0
        self.descObj.grid(row=rowIncrement, column = 1, sticky="w", padx=padx)
        
        self.checkBoxVal.trace_add("write", lambda name, index, mode: self.StateUpdate())
        
        # % Boxes
        if self.hasSpinBox:
            self.spinBoxVal = IntVar(value=self.spinDefault)
            self.spinBoxObj = ttk.Spinbox(optionPanel, validate="key", from_=self.spinBoxMin, to=self.spinBoxMax, textvariable=self.spinBoxVal, wrap=True, width=self.spinWidth, increment=self.spinIncr, justify="right")
            self.spinBoxObj.configure(validatecommand=(self.spinBoxObj.register(validateSpinbox), "%P", self.spinBoxMin, self.spinBoxMax))
            self.spinBoxObj.bind("<FocusOut>", lambda e, val=self.spinBoxVal: EmptyboxHandler(val, self.spinBoxMin))
            self.spinBoxObj.grid(row=rowIncrement, column = 3, padx=(15,0))
            self.spinBoxLabel = ttk.Label(optionPanel, text=self.spinDesc, anchor="w", style=f"{style}.TLabel")
            self.spinBoxLabel.grid(row=rowIncrement, column = 4, sticky="w", padx=0)
            disable_spinbox_scroll(self.spinBoxObj)

        count = 0
        for sub in self.subOptions:
            count += 1
            rowIncrement += 1
            sub.checkBoxVal = BooleanVar(value=sub.defState)
            sub.checkBoxVal.trace_add("write", lambda name, index, mode: self.StateUpdate())
            sub.checkBox = ttk.Checkbutton(optionPanel, text=sub.name, variable=sub.checkBoxVal, style=f"{style}Sub.TCheckbutton", width=25)
            sub.checkBox.grid(row=rowIncrement, column=0, sticky="sw")

            if sub.hasSpinBox:
                sub.spinBoxVal = IntVar(value=sub.spinDefault)
                sub.spinBoxObj = ttk.Spinbox(optionPanel, validate="key", from_=sub.spinBoxMin, to=sub.spinBoxMax, textvariable=sub.spinBoxVal, wrap=True, width=sub.spinWidth, increment=sub.spinIncr, justify="right")
                sub.spinBoxObj.configure(validatecommand=(sub.spinBoxObj.register(validateSpinbox), "%P", sub.spinBoxMin, sub.spinBoxMax))
                sub.spinBoxObj.bind("<FocusOut>", lambda e, val=sub.spinBoxVal: EmptyboxHandler(val, sub.spinBoxMin))
                sub.spinBoxObj.grid(row=rowIncrement, column=1, padx=(20,0), pady=(0,0), sticky="w")
                sub.spinBoxLabel = ttk.Label(optionPanel, text=sub.spinDesc, style=f"{style}NoMargin.TLabel")
                sub.spinBoxLabel.grid(row=rowIncrement, column=1, sticky="w", padx=(80,0))
                disable_spinbox_scroll(sub.spinBoxObj)
            
            if count == len(self.subOptions): # If the final suboption add extra padding stupid solution but all this code is stupid and bad
                newPad = (0, 10)
                sub.checkBox.grid_configure(pady=newPad)
                if sub.hasSpinBox:
                    sub.spinBoxObj.grid_configure(pady=newPad)
                    sub.spinBoxLabel.grid_configure(pady=newPad)
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

def EmptyboxHandler(val, minVal):
    '''Because you can delete the entire string in a box if you defocus it while its empty it makes its value 0'''
    try:
        val.get() # If we cannot get the value just safely set it to 0
    except:
        val.set(minVal)

def validateSpinbox(input, min, max):
    '''Because tkinters handling of spinboxes doesn't work when typing values, made one to accomodate typing in values'''
    if input == "": # Allow deleting the whole thing
        return True
    if not input.isdigit():
        return False
    input = int(input)
    if input <= int(max) and input >= int(min):
        return True
    return False

class SubOption():
    def __init__(self, _name, _parent:Option, commands = [], defState = True, prio = 0, spinDefault = 0, spinMin = 0, spinMax = 100, spinWidth = 3, spinIncr = 10, hasSpinBox = False, spinPadX = 15, spinDesc = "", preRandoCommands:list = []):
        self.name = _name
        self.checkBoxVal = BooleanVar
        self.checkBox:ttk.Checkbutton = None
        self.commands = commands    
        self.defState = defState
        self.prio = prio
        self.parent = _parent
        self.hasSpinBox = hasSpinBox
        self.spinBoxVal = None
        self.spinBoxObj:ttk.Spinbox = None
        self.spinBoxMin = spinMin
        self.spinBoxMax = spinMax
        self.spinDefault = spinDefault
        self.spinBoxLabel:ttk.Label = None
        self.spinWidth = spinWidth
        self.spinIncr = spinIncr
        self.spinDesc = spinDesc
        _parent.subOptions.append(self)

    def GetState(self):
        return self.checkBoxVal.get()
    
    def GetSpinbox(self):
        return self.spinBoxVal.get()

def disable_spinbox_scroll(spinbox):
    '''Used to stop spinbox scrollwheel conflicts'''
    def stop(event):
        return "break"
    spinbox.bind("<MouseWheel>", stop)
    spinbox.bind("<Button-4>", stop)
    spinbox.bind("<Button-5>", stop)

rowIncrement = 0   
XenoOptionDict = {
    "XCDE": [],
    "XC2": [],
    "XC3": [],
    "XCXDE": [],
}

class MutuallyExclusivePairing():
    '''For settings that are mutually exclusive'''
    def __init__(self, group1:list[Option], group2:list[Option]):
        for op in group1:
            op.clickCommands.append(lambda op=op: MutuallyExclusiveToggle(op, group2))
        for op in group2:
            op.clickCommands.append(lambda op=op: MutuallyExclusiveToggle(op, group1))

def MutuallyExclusiveToggle(op:Option, pairGroup:list[Option]):
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
            
def AskToChooseOption(enabledOption, conflictingOptions:list[Option]):
    top = PopupDescriptions.GenericPopup("Conflicting Settings")
    top.grab_set()
    top.protocol("WM_DELETE_WINDOW", Helper.NoOP)
    top.attributes(alpha=0)
    Theme.RootsForStyling.append(top)
    
    contolFrame = ttk.Frame(top, padding=3)
    contolFrame.pack(fill=BOTH)
    
    scrollablePanel = ScrollPanel.ScrollablePanel(top)    

    conflictDesc = ttk.Label(scrollablePanel.innerFrame, text= f"The following options are incompatible with the {enabledOption} option:")
    conflictDesc.pack()
    
    for option in conflictingOptions:
        incompatibleOption = ttk.Label(scrollablePanel.innerFrame, text = option.name, padding = (2, 5))
        incompatibleOption.pack()

    opt1Button = ttk.Button(contolFrame, text= "Disable Incompatible Options", command=lambda: (opt1Pressed.set(True), top.destroy()))
    opt1Button.pack(side=LEFT)
    opt2Button = ttk.Button(contolFrame, text= f"Disable {enabledOption}", command=lambda: (opt2Pressed.set(True), top.destroy()))
    opt2Button.pack(side=RIGHT)
    
    opt1Pressed = BooleanVar(scrollablePanel.innerFrame)
    opt2Pressed = BooleanVar(scrollablePanel.innerFrame)

    Theme.ThemeUpdate()
    scrollablePanel.ResizeScrollPanel(top, 70)
    PopupDescriptions.center_window(top)
    top.attributes(alpha=1)
    top.wait_window(top)
    
    if opt1Pressed.get() == True:
        ChosenResolution = True
    else:
        ChosenResolution = False

    return ChosenResolution

