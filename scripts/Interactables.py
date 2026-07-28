from tkinter import ttk
from tkinter import *
from scripts import PopupDescriptions, ScrollPanel, Theme, Helper

Game = "" # Used to tell what option goes to what games tab at runtime
DescriptionIndicator = "🛈"
rowIncrement = 0   
XenoOptionDict = {
    "XCDE": [],
    "XC2": [],
    "XC3": [],
    "XCXDE": [],
}

class Interactable():
    def GetState(self):
        pass
    
    def SaveState(self):
        pass
    
    def LoadState(self):
        pass

class Spinbox(Interactable):
    def __init__(self, min = 0, max = 100, increment = 10, default = 100, width = 3, description = "% randomized"):
        self.min = min
        self.max = max
        self.increment = increment
        self.default = default
        self.width = width
        self.description = description
        self.spinBoxObj:ttk.Spinbox = None
        self.spinBoxLabel:ttk.Label = None
        self.spinBoxVal = None

    def Create(self, parent, style):
        self.spinBoxVal = IntVar(value=self.default)
        self.spinBoxObj = ttk.Spinbox(parent, validate="key", from_=self.min, to=self.max, textvariable=self.spinBoxVal, wrap=True, width=self.width, increment=self.increment, justify="right")
        self.spinBoxObj.configure(validatecommand=(self.spinBoxObj.register(self.validateSpinbox), "%P", self.min, self.max))
        self.spinBoxObj.bind("<FocusOut>", lambda e, val=self.spinBoxVal: self.EmptyboxHandler(val))
        self.disableScroll(self.spinBoxObj)
        self.spinBoxLabel = ttk.Label(parent, text=self.description, style=style)

    def validateSpinbox(self, input):
        '''Because tkinters handling of spinboxes doesn't work when typing values, made one to accomodate typing in values'''
        if input == "": # Allow deleting the whole thing
            return True
        if not input.isdigit():
            return False
        input = int(input)
        if input <= int(self.max) and input >= int(self.min):
            return True
        return False
    
    def EmptyboxHandler(self):
        '''Because you can delete the entire string in a box if you defocus it while its empty it makes its value the min val'''
        try:
            self.spinBoxVal.get() # If we cannot get the value just safely set it to 0
        except:
            self.spinBoxVal.set(self.min)
    
    def GetState(self):
        return self.spinBoxVal.get()
    
    def VisualStateUpdate(self):
        pass
    
    def disableScroll(self, spinBox):
        '''Used to stop spinbox scrollwheel conflicts'''
        def stop(event):
            return "break"
        spinBox.bind("<MouseWheel>", stop)
        spinBox.bind("<Button-4>", stop)
        spinBox.bind("<Button-5>", stop)

class Dropdown(Interactable):
    def __init__(self, default, values, width, height):
        self.spinBoxVal = IntVar(default)
        self.default = default
        self.values = values
        self.width = width
        self.height = height
        
    def Create(self, parent):
        self.dropDownObj = ttk.Combobox(parent, width=self.width)
        self.dropDownObj.set(self.default)
        self.dropDownObj['values'] = self.values

    def GetState(self):
        return self.spinBoxVal.get()

class Option(Interactable):
    def __init__(self, _name:str ="No Name", _tab =1, _desc:str= "No Description", commands:list = [], defState = False, prio = 50, descData = None, preRandoCommands:list = [], isDevOption = False, stepSpeed = 0.05, filePlaceCommands:list = [], dropDown:Dropdown = None, spinBox:Spinbox = None):
        # Objects
        self.descObj = None
        self.checkBox = None
        self.checkBoxVal = None
        self.subOptions:list[SubOption] = []
        self.descData = descData
        self.isDevOption = isDevOption
        self.clickCommands = []
        
        # Initial Data
        self.name =  _name
        self.tab = _tab
        self.desc = _desc
        self.commands:list = commands
        self.preRandoCommands:list = preRandoCommands
        self.filePlaceCommands:list = filePlaceCommands
        self.subDefState = defState
        self.prio = prio
        self.stepSpeed = stepSpeed # Controls how fast the progressbar moves while this setting runs. 
        XenoOptionDict[Game].append(self)
        
        self.spinBox:Spinbox = spinBox
        self.dropDown:Dropdown = dropDown
        
    def DisplayOption(self, tab, root, style):
        self.root = root
        self.GenStandardOption(tab, style)
        self.VisualStateUpdate()
        
    def GenStandardOption(self, parentTab, style): # This probably shouldnt be a class function what if we want to make a nonstandard option we could make a carveout and let you call a custom function but how would you set everything with a custom function
        # Variables
        global rowIncrement
        self.checkBoxVal = BooleanVar()
        self.checkBoxVal.trace_add("write", lambda e: self.VisualStateUpdate())
        
        self.spinBoxLabel = ttk.Label()
        self.spinBoxObj = ttk.Spinbox()

        # Parent Frame
        optionPanel = ttk.Frame(parentTab, style=f"{style}.TFrame", padding=(0,0,2000,0))
        optionPanel.grid(row = rowIncrement, column = 0, sticky="ew")
        
        # Major Option Checkbox
        self.checkBox = ttk.Checkbutton(optionPanel, variable= self.checkBoxVal, text=self.name, width=30, style=f"{style}.TCheckbutton", command=lambda: (self.VisualStateUpdate(), [cmd() for cmd in self.clickCommands]))
        self.checkBox.grid(row=rowIncrement, column = 0, sticky="w")
        
        # Description Label or Button
        if self.descData == None:
            text = self.desc
            self.descObj = ttk.Label(optionPanel, text=self.desc, anchor="w", width=60, style=f"{style}.TLabel", wraplength=400)
            padx= 0
        else:
            text = f"{self.desc} {DescriptionIndicator}"
            self.descObj = ttk.Button(optionPanel, text = text, command=lambda: PopupDescriptions.StyledPopup(self.name, self.descData, self.root), style=f"{style}.TButton", width=60)
            padx = 13
        self.descObj.grid(row=rowIncrement, column = 1, sticky="w", padx=padx)
        
        # % Boxes
        if self.spinBox != None:
            self.spinBox.Create(optionPanel, f"{style}.TLabel")
            self.spinBox.spinBoxObj.grid(row=rowIncrement, column = 3, padx=(15,0))
            self.spinBox.spinBoxLabel.config(anchor="w")
            self.spinBox.spinBoxLabel.grid(row=rowIncrement, column = 4, sticky="w", padx=0)
        elif self.dropDown != None:
            self.dropDown.Create(optionPanel)
            self.dropDown.dropDownObj.grid(row=rowIncrement, column = 3, padx=(15,0))
            
        subCount = 0
        for sub in self.subOptions:
            subCount += 1
            rowIncrement += 1
            sub.Display(optionPanel, style, subCount == len(self.subOptions))
        rowIncrement += 1
        
    def VisualStateUpdate(self): # This is obviously terrible, I need to fix this entire script 
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
            if self.spinBoxLabel != None:
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
    
    def VisualStateUpdate(self): # I dont want to update this every time I add a new type of setting though?
        if self.GetState():
            self.descObj.state(["!disabled"])
            self.spinBoxObj.state(["!disabled"])
            if self.spinBoxLabel != None:
                self.spinBoxLabel.state(["!disabled"])
            for sub in self.subOptions:
                sub.VisualStateUpdate()
            self.spinBox.VisualStateUpdate()
    
    def GetSpinbox(self):
        return self.spinBox.GetState()
    
    def GetState(self):
        return self.checkBoxVal.get()

class SubOption(Interactable):
    def __init__(self, name, parent:Option, commands = [], defState = True, prio = 0, preRandoCommands:list = [], filePlaceCommands = [], dropDown = None, spinBox = None):
        self.name = name
        self.checkBoxVal = BooleanVar
        self.checkBox:ttk.Checkbutton = None
        self.commands = commands    
        self.defState = defState
        self.prio = prio
        self.parent = parent
        self.filePlaceCommands = filePlaceCommands
        self.spinBox:Spinbox = spinBox
        self.dropDown:Dropdown = dropDown
        parent.subOptions.append(self)
    
    def Display(self, parent, style, isFinal):
        self.checkBoxVal = BooleanVar(value=self.defState)
        self.checkBoxVal.trace_add("write", lambda e: self.VisualStateUpdate())
        self.checkBox = ttk.Checkbutton(parent, text=self.name, variable=self.checkBoxVal, style=f"{style}Sub.TCheckbutton", width=25)
        self.checkBox.grid(row=rowIncrement, column=0, sticky="sw")

        if self.spinBox != None:
            spinBox:Spinbox = self.spinBox.Create(parent, f"{style}NoMargin.TLabel")
            spinBox.spinBoxObj.grid(row=rowIncrement, column=1, padx=(20,0), pady=(0,0), sticky="w")
            spinBox.spinBoxLabel.grid(row=rowIncrement, column=1, sticky="w", padx=(80,0))

        if isFinal: # If the final suboption add extra padding
            newPad = (0, 10)
            self.checkBox.grid_configure(pady=newPad)
            if self.spinBox != None:
                spinBox.spinBoxObj.grid_configure(pady=newPad)
                spinBox.spinBoxLabel.grid_configure(pady=newPad)
    
    def VisualStateUpdate():
        pass

    def GetState(self):
        return self.checkBoxVal.get()
    
    def GetSpinbox(self):
        return self.spinBox.GetState()

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

