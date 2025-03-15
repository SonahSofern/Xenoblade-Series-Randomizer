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
        
    def Text(self,text:str):
        self.data.append(PopText(self.order, text, self.data))

    def Image(self,imagePath:str, game, size = 400):
        if isOnefile: # Images come from a different path when packed to one file
            imagePath = os.path.join(sys._MEIPASS,"Images", imagePath)
        else:
            imagePath = f"./{game}/_internal/Images/{imagePath}"
        self.data.append(PopImage(self.order, imagePath, size, self.data))
    
    def Header(self, text:str):
        self.data.append(PopHeader(self.order, text, self.data))

class DescriptionObject():
    def __init__(self, order, data, list:list):
        self.order = order
        self.data = data
        list.append(self)
        order += 1
        

class PopText(DescriptionObject):
    def __init__(self, order, data, list):
        super().__init__(order, data, list)
    
class PopImage(DescriptionObject):
    def __init__(self, order, data, size, list):
        super().__init__(order, data, list)
        self.size = size
    
class PopHeader(DescriptionObject):
    def __init__(self, order, data, list):
        super().__init__(order, data, list)

def GenPopup(optionName, descData, root, defaultFont):
    # Check if a popup with the same title is already open
    for top in OpenWindows:
        if top.winfo_exists() and top.title() == optionName:
            top.focus()
            top.deiconify() # unminimizes
            return  # If it exists, don't create a new one
        
    Description = descData()
    top = Toplevel(root, padx=10, pady=10)  # Create a new top-level window
    top.title(optionName)
    scripts.GUISettings.RootsForStyling.append(top)
    OpenWindows.append(top)
    sizeCount = 0
    
    Outerframe = ttk.Frame(top) 
    
    canv = Canvas(Outerframe)
    
    # curHeader = None # Tracks how to place children under headers
    
    InnerFrame = ttk.Frame(canv)
    scripts.GUISettings.CreateScrollBars([Outerframe], [canv], [InnerFrame])
    scripts.GUISettings.LoadTheme(defaultFont, scripts.GUISettings.defGUIThemeVar.get())
    # loop over data from the description class and parse it
    for obj in Description.data:
        if isinstance(obj, PopImage): # Image
            img = Image.open(obj.data)
            img.thumbnail((obj.size, obj.size), Image.LANCZOS) # Resizes our image and keeps ratio
            img = ImageTk.PhotoImage(img)
            imageLabel = ttk.Label(InnerFrame, image=img, padding=5, style="DescriptionImage.TLabel")
            ImageGroup.append(img)
            imageLabel.pack(anchor="w", padx=15, pady=5)
            sizeCount += 1 # Keeps track of our list of sizes for each image
            
        elif isinstance(obj, PopHeader): # Header
            textLabel = ttk.Label(InnerFrame,text=obj.data, style="Header.TLabel")
            textLabel.pack(fill="x", expand=True)
            # curHeader = textLabel
            
        elif isinstance(obj, PopText):            # Text
            textLabel = ttk.Label(InnerFrame,text=obj.data, wraplength=Description.geometry[1] - 60)
            textLabel.pack(anchor="w")
    InnerFrame.update_idletasks()  # Ensure all geometry calculations are up-to-date
    top.geometry(f"{InnerFrame.winfo_width() + 38}x{ min(InnerFrame.winfo_height() + 40, 1000)}")
    top.protocol("WM_DELETE_WINDOW", lambda: (OpenWindows.remove(top), top.destroy())) # remove windows from list on close

            
