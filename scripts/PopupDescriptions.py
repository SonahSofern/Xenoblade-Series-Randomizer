# This will be the template for when you click a more info thing it will load some markdown into this template to be viewed
from tkinter import *
from tkinter import ttk
import scripts.GUISettings
from PIL import Image, ImageTk
ImageGroup = [] # Needed because garbage collection will delete pictures otherwise
HeaderText = "HeaderHEAD "
OpenWindows = []

class Description:

    def __init__(self, geometry = (800,800)):
        self.geometry = geometry
        self.data:list[str] = []
        self.sizes:list[int] = []
    def Text(self,text:str):
        self.data.append(text)
    
    def Image(self,imagePath:str, size):
        self.data.append(imagePath)
        self.sizes.append(size)
    
    def Header(self, text:str):
        self.data.append(f"{HeaderText}{text}")

def GenPopup(optionName, descData, root, defaultFont, defTheme):
    # Open a window with the 
    
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
    
    InnerFrame = ttk.Frame(canv)
    scripts.GUISettings.CreateScrollBars([Outerframe], [canv], [InnerFrame])
    scripts.GUISettings.LoadTheme(defaultFont, defTheme)
    # loop over data from the description class and parse it
    for text in Description.data:
        if text.startswith("./"): # if we are a filepath
            img = Image.open(text)
            img.thumbnail((Description.sizes[sizeCount], Description.sizes[sizeCount]), Image.LANCZOS) # Resizes our image and keeps ratio
            img = ImageTk.PhotoImage(img)
            imageLabel = ttk.Label(InnerFrame, image=img, padding=5, style="DescriptionImage.TLabel")
            ImageGroup.append(img)
            imageLabel.pack(anchor="w", padx=15)
            sizeCount += 1 # Keeps track of our list of sizes for each image
            # Handle as filepath image
        elif text.startswith(HeaderText):
            text = text.replace(HeaderText, "")
            textLabel = ttk.Label(InnerFrame,text=f"{text}", style="Header.TLabel")
            textLabel.pack(fill="x", expand=True)
        else:
            # print(Description.geometry[1])
            textLabel = ttk.Label(InnerFrame,text=text, wraplength=Description.geometry[1] - 60)
            textLabel.pack(anchor="w")
            # Handle as text
    InnerFrame.update_idletasks()  # Ensure all geometry calculations are up-to-date
    top.geometry(f"{InnerFrame.winfo_width() + 38}x{ min(InnerFrame.winfo_height() + 40, 1000)}")
    top.protocol("WM_DELETE_WINDOW", lambda: (OpenWindows.remove(top), top.destroy())) # remove windows from list on close

            
    # print(f"Tried to gen popup {Description}.md")