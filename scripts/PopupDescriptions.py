# This will be the template for when you click a more info thing it will load some markdown into this template to be viewed
from tkinter import *
from tkinter import ttk
import scripts.GUISettings
from PIL import Image, ImageTk
ImageGroup = [] # Needed because garbage collection will delete pictures otherwise
HeaderText = "HeaderHEAD "

class Description:
    data:list[str] = []
    sizes:list[int] = []
    def __init__(self, geometry = (800,800)):
        self.geometry = geometry
        
    def Text(self,text:str):
        self.data.append(text)
    
    def Image(self,imagePath:str, size):
        self.data.append(imagePath)
        self.sizes.append(size)
    
    def Header(self, text:str):
        self.data.append(f"{HeaderText}{text}")

def GenPopup(optionName, descData, root, defaultFont, defTheme):
    # Open a window with the 
    Description = descData()
    top = Toplevel(root, padx=10, pady=10)  # Create a new top-level window
    top.title(optionName)
    top.geometry(f"{Description.geometry[0]}x{Description.geometry[1]}")
    scripts.GUISettings.RootsForStyling.append(top)
    scripts.GUISettings.LoadTheme(defaultFont, defTheme)
    sizeCount = 0
    
    Outerframe = ttk.Frame(top) 
    Outerframe.pack(fill=BOTH, expand=True)
    
    canv = Canvas(Outerframe)
    scripts.GUISettings.CanvasesForStyling.append(canv)
    canv.pack(fill=BOTH, expand=True)
    
    InnerFrame = ttk.Frame(canv)
    InnerFrame.pack(fill=BOTH, expand=True)
    
    scripts.GUISettings.LoadTheme(defaultFont, defTheme)
    
    # loop over data from the description class and parse it
    for text in Description.data:
        if text.startswith("./"): # if we are a filepath
            img = Image.open(text)
            img.thumbnail((Description.sizes[sizeCount], Description.sizes[sizeCount]), Image.LANCZOS) # Resizes our image and keeps ratio
            img = ImageTk.PhotoImage(img)
            imageLabel = ttk.Label(canv, image=img, padding=5)
            ImageGroup.append(img)
            imageLabel.pack()
            sizeCount += 1 # Keeps track of our list of sizes for each image
            # Handle as filepath image
        elif text.startswith(HeaderText):
            text = text.replace(HeaderText, "")
            textLabel = ttk.Label(canv,text=f"{text}", style="Header.TLabel")
            textLabel.pack(fill="x", expand=True)
        else:
            # print(Description.geometry[1])
            textLabel = ttk.Label(canv,text=text, wraplength=Description.geometry[1] - 60)
            textLabel.pack()
            # Handle as text
    scripts.GUISettings.CreateScrollBars([Outerframe], [canv], [InnerFrame])

            
    # print(f"Tried to gen popup {Description}.md")