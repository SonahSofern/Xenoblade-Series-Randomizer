# This will be the template for when you click a more info thing it will load some markdown into this template to be viewed
from tkinter import *
from tkinter import ttk
import scripts.GUISettings
from PIL import Image, ImageTk
ImageGroup = [] # Needed because garbage collection will delete pictures otherwise


class Description:
    data:list[str] = []
    sizes:list[int] = []
    def __init__(self, title, geometry = (800,800)):
        self.title = title
        self.geometry = geometry
    def Text(self,text:str):
        self.data.append(text)
    
    def Image(self,imagePath:str, size):
        self.data.append(imagePath)
        self.sizes.append(size)
    
    def Header(self, text:str):
        self.data.append(text)

def GenPopup(Description:Description, root, defaultFont, defTheme):
    # Open a window with the 
    top = Toplevel(root, padx=10, pady=10)  # Create a new top-level window
    top.title(Description.title)
    top.geometry(f"{Description.geometry[0]}x{Description.geometry[1]}")
    scripts.GUISettings.RootsForStyling.append(top)
    scripts.GUISettings.LoadTheme(defaultFont, defTheme)
    sizeCount = 0
    
    Outerframe = ttk.Frame(top, padding=3) 
    Outerframe.pack(fill=BOTH, expand=True)
    
    canv = Canvas(Outerframe)
    scripts.GUISettings.CanvasesForStyling.append(canv)
    canv.pack(fill=BOTH, expand=True)
    
    InnerFrame = ttk.Frame(canv)
    InnerFrame.pack(fill=BOTH, expand=True)
    
    scripts.GUISettings.CreateScrollBars([Outerframe], [canv], [InnerFrame])
    scripts.GUISettings.LoadTheme(defaultFont, defTheme)
    
    # loop over data from the description class and parse it
    for obj in Description.data:
        if obj.startswith("./"): # if we are a filepath
            img = Image.open(obj)
            img.thumbnail((Description.sizes[sizeCount], Description.sizes[sizeCount]), Image.LANCZOS) # Resizes our image and keeps ratio
            img = ImageTk.PhotoImage(img)
            imageLabel = ttk.Label(canv, image=img, padding=5)
            ImageGroup.append(img)
            imageLabel.pack(anchor="w")
            sizeCount += 1 # Keeps track of our list of sizes for each image
            # Handle as filepath image
        else:
            print(Description.geometry[1])
            text = ttk.Label(canv,text=obj, wraplength=Description.geometry[1] - 60)
            text.pack(anchor="w")
            # Handle as text
    
            
    print(f"Tried to gen popup {Description}.md")

