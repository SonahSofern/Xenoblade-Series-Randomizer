# This will be the template for when you click a more info thing it will load some markdown into this template to be viewed
from tkinter import *
from tkinter import ttk
import scripts.GUISettings, os, sys
from PIL import Image, ImageTk
ImageGroup = [] # Needed because garbage collection will delete pictures otherwise
OpenWindows = []


if getattr(sys, 'frozen', False):  # If the app is running as a bundled executable
    isOnefile = True
else:
    isOnefile = False

class Description:

    def __init__(self, geometry = (800,800)):
        self.geometry = geometry
        self.data:list[DescriptionObject] = []
        self.order = 0
        
    def Tag(self, text:str):
        self.data.append(PopTag(self.order, text))
        
    def Text(self,text:str):
        self.data.append(PopText(self.order, text))

    def Image(self,imagePath:str, game, size = 400):
        if isOnefile: # Images come from a different path when packed to one file
            imagePath = os.path.join(sys._MEIPASS,"Images", imagePath)
        else:
            imagePath = f"./{game}/_internal/Images/{imagePath}"
        self.data.append(PopImage(self.order, imagePath, size))
    
    def Header(self, text:str):
            self.data.append(PopHeader(self.order, text))

class DescriptionObject():
    def __init__(self, order, data):
        self.order = order
        self.data = data
        self.obj = None
        order += 1

class PopTag(DescriptionObject):
    def __init__(self, order, data):
        super().__init__(order, data)
    def SpecialPack(self):
        self.obj.pack(anchor="w")

class PopText(DescriptionObject):
    def __init__(self, order, data):
        super().__init__(order, data)
    def SpecialPack(self):
        self.obj.pack(anchor="w")
        
class PopImage(DescriptionObject):
    def __init__(self, order, data, size):
        super().__init__(order, data)
        self.size = size
    def SpecialPack(self):
        self.obj.pack()
        
class PopHeader(DescriptionObject): # Give these a hover color change
    def __init__(self, order, data):
        super().__init__(order, data)
        self.childGroup = []
        self.isOn = True
    def SpecialPack(self):
        self.obj.pack(anchor="w")
        
    def Dropdown(self):
        if self.isOn:
            for child in self.childGroup:
                child.obj.pack_forget()
            self.isOn = False
        else:
            for child in self.childGroup:
                child.SpecialPack() 
            self.isOn = True

def GenPopup(optionName, descData, root, defaultFont):
    # Check if a popup with the same title is already open
    for top in OpenWindows:
        if top.winfo_exists() and top.title() == optionName:
            top.focus()
            top.deiconify() # unminimizes
            return  # If it exists, don't create a new one
        
    myDescription:Description = descData()
    top = Toplevel(root, padx=10, pady=10)  # Create a new top-level window
    top.title(optionName)
    scripts.GUISettings.RootsForStyling.append(top)
    OpenWindows.append(top)
    
    Outerframe = ttk.Frame(top) 
    
    canv = Canvas(Outerframe)
    
    curHeader:PopHeader = None # Tracks how to place children under headers
    curFrame:ttk.Frame = None # Groups our options so they can collapse and regroup together
    
    InnerFrame = ttk.Frame(canv)
    scripts.GUISettings.CreateScrollBars([Outerframe], [canv], [InnerFrame])
    scripts.GUISettings.LoadTheme(defaultFont, scripts.GUISettings.defGUIThemeVar.get())
    # loop over data from the description class and parse it
    for descObj in myDescription.data:
        if isinstance(descObj, PopImage): # Image
            img = Image.open(descObj.data)
            img.thumbnail((descObj.size, descObj.size), Image.LANCZOS) # Resizes our image and keeps ratio
            img = ImageTk.PhotoImage(img)
            descObj.obj = ttk.Label(curFrame, image=img, padding=5, style="DescriptionImage.TLabel")
            ImageGroup.append(img)
            descObj.SpecialPack()
            curHeader.childGroup.append(descObj)
            
        elif isinstance(descObj, PopHeader): # Header
            curFrame = ttk.Frame(InnerFrame)
            textLabel = ttk.Button(curFrame,text=descObj.data, style="Header.TButton", padding=10, command=lambda obj= descObj: obj.Dropdown())
            textLabel.pack(fill="x")
            curHeader = descObj
            curFrame.pack(fill="x", expand=True)
            
        elif isinstance(descObj, PopText): # Text
            descObj.obj = ttk.Label(curFrame,text=descObj.data, wraplength=myDescription.geometry[1] - 60)
            descObj.SpecialPack()
            curHeader.childGroup.append(descObj)
        
        elif isinstance(descObj, PopTag):
            descObj.obj = ttk.Label(curFrame, text=descObj.data, style="Header.TButton")
            descObj.SpecialPack()
            curHeader.childGroup.append(descObj)
            
    InnerFrame.update_idletasks()  # Ensure all geometry calculations are up-to-date
    top.geometry(f"{InnerFrame.winfo_width() + 38}x{ min(InnerFrame.winfo_height() + 40, 1000)}")
    top.protocol("WM_DELETE_WINDOW", lambda: (OpenWindows.remove(top), top.destroy())) # remove windows from list on close

            
