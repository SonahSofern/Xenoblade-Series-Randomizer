from tkinter import ttk
from tkinter import *
from scripts import PopupDescriptions, ScrollPanel, Theme, Helper, SaveLoad

DescriptionIndicator = "🛈"
Game = "" # Used to tell what option goes to what games tab at runtime otherwise we would have to specify each time we create an option what game it belongs to
XenoOptionDict = {
    "XCDE": [],
    "XC2": [],
    "XC3": [],
    "XCXDE": [],
}

class Interactable(SaveLoad.SavedEntry):
    def GetState(self):
        pass
    
    def SaveState(self):
        pass
    
    def LoadState(self):
        pass
    
    def Create(self, parent, style, rowIncrement):
        pass
    
    def VisualStateUpdate(self):
        pass
    
class Option(Interactable):
    def __init__(self, name:str ="No Name", parent =1, desc:str= "No Description", commands:list = [], prio = 50, descData = None, preRandoCommands:list = [], isDevOption = False, stepSpeed = 0.05, filePlaceCommands:list = []):
        # Objects
        self.descObj = None
        self.checkBox = None
        self.checkBoxVal = None
        self.descData = descData
        self.isDevOption = isDevOption
        self.clickCommands = []
        self.interactables:list[Interactable] = []
        self.subOptionCount = 0 # Keeping track of padding at the end of suboptions
        self.displayedSubOptionCount = 0 # Keeping track of padding at the end of suboptions
        
        # Initial Data
        self.name =  name
        self.tab = parent
        self.desc = desc
        self.commands:list = commands
        self.preRandoCommands:list = preRandoCommands
        self.filePlaceCommands:list = filePlaceCommands
        self.prio = prio
        self.identifier = self.name
        self.stepSpeed = stepSpeed # Controls how fast the progressbar moves while this setting runs. 
        
        XenoOptionDict[Game].append(self) 
        
    def Create(self, parent, style, rowIncrement): 
        self.style = style # So I can access during runtime for special description styles
        rowIncrement["Count"] += 1
        # Variables
        self.checkBoxVal = BooleanVar()
        self.checkBoxVal.trace_add("write", lambda e, w, z: self.VisualStateUpdate())
        
        self.spinBoxLabel = ttk.Label()
        self.spinBoxObj = ttk.Spinbox()
        
        # Major Option Checkbox
        self.checkBox = ttk.Checkbutton(parent, variable= self.checkBoxVal, text=self.name, width=30, style=f"{style}.TCheckbutton", command=lambda: (self.VisualStateUpdate(), [cmd() for cmd in self.clickCommands]))
        self.checkBox.grid(row=rowIncrement["Count"], column = 0, sticky="w")
        
        # Description Label or Button
        if self.descData == None:
            text = self.desc
            self.descObj = ttk.Label(parent, text=self.desc, anchor="w", width=60, style=f"{style}.TLabel", wraplength=400)
            padx= 0
        else:
            text = f"{self.desc} {DescriptionIndicator}"
            self.descObj = ttk.Button(parent, text = text, command=lambda: PopupDescriptions.StyledPopup(self.name, self.descData, self.root), style=f"{style}.TButton", width=60)
            padx = 13
        self.descObj.grid(row=rowIncrement["Count"], column = 1, sticky="w", padx=padx)
        
        # Option Interactables
        for interact in self.interactables:
            interact.Create(parent, style, rowIncrement)

    
    def VisualStateUpdate(self):
        if self.GetState(): state = "!disabled"
        else: state = "disabled"
        
        if self.descData != None:
            self.descObj.config(style=f"{self.style}{state}.TButton") # Allows descriptions to be always clickable even if the setting is off
        else:
            self.descObj.state([state])
            
        self.spinBoxObj.state([state])

        for int in self.interactables: # Update all the composites
            int.VisualStateUpdate()
    
    def GetSpinbox(self):
        '''Legacy function so that previous code using GetSpinbox still works'''
        for int in self.interactables:
            if isinstance(int, Spinbox):
                return int.GetState()
        raise Exception("No spinbox found on: " + self.name + ".")
    
    def GetState(self):
        return self.checkBoxVal.get()
    
    def Save(self):
        return {self.identifier: self.GetState()}
    
    def Load(self, loadFile):
        self.checkBoxVal.set(loadFile[self.identifier])
        
    def GetPermalinkVar(self):
        return self.checkBoxVal

class SubOption(Option):
    def __init__(self, name, parent:Option, commands = [], defState = True, prio = 0, preRandoCommands:list = [], filePlaceCommands = []):
        super().__init__(name, None, "", commands, prio, None, preRandoCommands, filePlaceCommands=filePlaceCommands)
        self.defState = defState
        self.parent = parent
        self.identifier = f"{parent.name} {self.name} Suboption"
        self.parent.subOptionCount += 1
        self.padding = None # Keeping track of padding at the end of suboptions
        parent.interactables.append(self)
    
    def Create(self, parent, style, rowIncrement):
        rowIncrement["Count"] += 1
        self.checkBoxVal = BooleanVar(value=self.defState)
        self.checkBoxVal.trace_add("write", lambda e, w, z: self.VisualStateUpdate())
        self.checkBox = ttk.Checkbutton(parent, text=self.name, variable=self.checkBoxVal, style=f"{style}Sub.TCheckbutton", width=25)
        self.checkBox.grid(row=rowIncrement["Count"], column=0, sticky="sw")
        self.parent.displayedSubOptionCount += 1
        
        for interactable in self.interactables:
            interactable.Create(parent, style, rowIncrement)

        if self.parent.displayedSubOptionCount == self.parent.subOptionCount: # If the final suboption add extra padding
            rowIncrement["Count"] += 1
            self.padding = ttk.Frame(parent, height=10)
            self.padding.grid(row=rowIncrement["Count"], column=0, pady=0)
    
    def VisualStateUpdate(self):
        # Shows/Hides dropdown based on parent state
        if self.parent.GetState(): 
            self.checkBox.grid()
            if self.padding:
                self.padding.grid()
        else: 
            self.checkBox.grid_remove()
            if self.padding:
                self.padding.grid_remove()
            
        for int in self.interactables:
            int.VisualStateUpdate()

class Spinbox(Interactable):
    def __init__(self, parent:Option, min = 0, max = 100, increment = 10, default = 100, width = 3, description = "% randomized"):
        self.min = min
        self.max = max
        self.increment = increment
        self.default = default
        self.width = width
        self.description = description
        self.spinBoxObj:ttk.Spinbox = None
        self.spinBoxLabel:ttk.Label = None
        self.spinBoxVal = None
        self.parent = parent
        self.identifier = f"{self.parent.name} Spinbox"
        parent.interactables.append(self)
        XenoOptionDict[Game].append(self) 

    def Create(self, parent, style, rowIncrement):
        self.spinBoxVal = IntVar(value=self.default)
        self.spinBoxObj = ttk.Spinbox(parent, validate="key", from_=self.min, to=self.max, textvariable=self.spinBoxVal, wrap=True, width=self.width, increment=self.increment, justify="right")
        self.spinBoxObj.configure(validatecommand=(self.spinBoxObj.register(self.validateSpinbox), "%P"))
        self.spinBoxObj.bind("<FocusOut>", self.EmptyboxHandler)
        self.spinBoxLabel = ttk.Label(parent, text=self.description, style=f"{style}.TLabel")
        disableScroll(self.spinBoxObj)
        self.GridDisplay(rowIncrement, style)
    
    def GridDisplay(self, rowIncrement, style):
        self.spinBoxObj.grid(row=rowIncrement["Count"], column = 3, padx=(15,0))
        self.spinBoxLabel.config(anchor="w")
        self.spinBoxLabel.grid(row=rowIncrement["Count"], column = 4, sticky="w", padx=0)
        
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
    
    def EmptyboxHandler(self, event=None):
        '''Because you can delete the entire string in a box if you defocus it while its empty it makes its value the min val'''
        try:
            self.spinBoxVal.get() # If we cannot get the value just safely set it to 0
        except:
            self.spinBoxVal.set(self.min)
    
    def GetState(self):
        return self.spinBoxVal.get()
    
    def VisualStateUpdate(self):
        if self.parent.GetState():
            self.spinBoxObj.state(["!disabled"])
            self.spinBoxLabel.state(["!disabled"])     
        else:
            self.spinBoxObj.state(["disabled"])
            self.spinBoxLabel.state(["disabled"])
    
    def Save(self):
        return {self.identifier:f"{self.GetState()}"}
    
    def Load(self, loadFile):
        self.spinBoxVal.set(loadFile[self.identifier])
        
    def GetPermalinkVar(self):
        return self.spinBoxVal

class SubSpinbox(Spinbox):
    def __init__(self, parent:Option, min = 0, max = 100, increment = 10, default = 100, width = 3, description = ""):
        super().__init__(parent, min, max, increment, default, width, description)
        self.identifier = f"{self.parent.parent.name} {self.parent.name} Spinbox"
    
    def GridDisplay(self, rowIncrement, style):
        self.spinBoxLabel.config(style=f"{style}NoMargin.TLabel")
        self.spinBoxObj.grid(row=rowIncrement["Count"], column=1, padx=(20,0), pady=(0,0), sticky="w")
        self.spinBoxLabel.grid(row=rowIncrement["Count"], column=1, sticky="w", padx=(80,0))
        
    def VisualStateUpdate(self):
        # Hide when main option is on/off
        if self.parent.parent.GetState():
            self.spinBoxObj.grid()
            self.spinBoxLabel.grid()
        else:
            self.spinBoxObj.grid_remove()
            self.spinBoxLabel.grid_remove()
        
        # Toggle state when suboption is on/off
        if self.parent.GetState():
            self.spinBoxObj.state(["!disabled"])
            self.spinBoxLabel.state(["!disabled"])
        else:
            self.spinBoxObj.state(["disabled"])
            self.spinBoxLabel.state(["disabled"])

class DropdownOption():
    '''So that dropdowns can display one thing but do another behind the scenes: e.g. Users select Jin from a dropdown but the real value we use in code is his id'''
    def __init__(self, displayVal, realVal):
        self.displayVal = displayVal
        self.realVal = realVal
    
class Dropdown(Interactable):
    def __init__(self, parent:Option, values:list[DropdownOption] = [], width = 40, height = 10):
        # Updated when a new option is selected
        self.curDisplayVal = StringVar(value="") # Text value of the currently selected option
        self.curRealVal = IntVar(value=0) # Index of the currently selected option
        self.curDisplayVal.trace_add("write", self.SetValueByDisplayVal)
        
        self.values:list[DropdownOption] = values
        self.width = width
        self.height = height
        self.parent = parent
        self.curDisplayVal.set(values[0].displayVal) # set default
        parent.interactables.append(self)
        XenoOptionDict[Game].append(self) 
        self.identifier = f"{self.parent.name} Dropdown"
        
        self.values.sort(key= lambda x: x.displayVal)
           
    def Create(self, parent, style, rowIncrement):
        self.dropDownObj = ttk.Combobox(parent, width=self.width, textvariable=self.curDisplayVal, state="readonly")
        self.dropDownObj['values'] = [x.displayVal for x in self.values]
        self.dropDownObj.grid(row=rowIncrement["Count"], column = 3, padx=(15,0))
        disableScroll(self.dropDownObj)
    
    def SetValueByDisplayVal(self, *args):
        '''The string itself controls the values'''
        # print(f"Cur Display Val: {self.curDisplayVal.get()}")
        for val in self.values:
            if val.displayVal == self.curDisplayVal.get():
                self.curRealVal.set(val.realVal)
                self.curDropdownOption = val
                break
      
    def GetState(self):
        '''Returns the real value for the currently displayed option'''
        return self.curDropdownOption.realVal
        # return self.curDropdownOption.displayVal
    
    def VisualStateUpdate(self):
        if self.parent.GetState():
            self.dropDownObj.state(["!disabled"])
        else:
            self.dropDownObj.state(["disabled"])
      
    def Save(self):
        '''Dropdowns are saved by the index of the option chosen, otherwise we would have massive permalinks if we wanted to save the string value'''
        index = 0
        for i in range(0,len(self.values)):
            if self.values[i] == self.curDropdownOption:
                index = i
        return {self.identifier: index}

    def Load(self, loadFile):
        '''Loads the dropdown by the saved index'''
        index = loadFile.get(self.identifier)
        if index is not None:
            dropdownOption:DropdownOption = self.values[index]
            self.curDropdownOption = dropdownOption
            self.curDisplayVal.set(dropdownOption.displayVal)
            self.curRealVal.set(dropdownOption.realVal)

    def GetPermalinkVar(self):
        return self.curRealVal

class SubDropdown(Dropdown):
    def Create(self, parent, style, rowIncrement):
        super().Create(parent, style, rowIncrement)
        self.dropDownObj.grid(row=rowIncrement["Count"], column=1, padx=(20,0), pady=(0,0), sticky="w")
        self.identifier = f"{self.parent.parent.name} {self.parent.name} Dropdown"
 
    def VisualStateUpdate(self):
        # Hide when main option is on/off
        if self.parent.parent.GetState():
            self.dropDownObj.grid()
        else:
            self.dropDownObj.grid_remove()
        
        # Toggle state when suboption is on/off
        if self.parent.GetState():
            self.dropDownObj.state(["!disabled"])
        else:
            self.dropDownObj.state(["disabled"])

# def disableScroll(self, obj:Widget):
#     '''Used to stop spinbox scrollwheel conflicts'''
#     def stop(event):
#         return "break"
#     self.spinBoxObj.bind("<MouseWheel>", stop)
#     self.spinBoxObj.bind("<Button-4>", stop)
#     self.spinBoxObj.bind("<Button-5>", stop)
    
def disableScroll(obj:Widget):
    '''Used to stop spinbox scrollwheel conflicts'''
    def stop(event):
        return "break"
    obj.bind("<MouseWheel>", stop)
    obj.bind("<Button-4>", stop)
    obj.bind("<Button-5>", stop)
  
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