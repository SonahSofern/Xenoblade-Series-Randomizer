# This will be the template for when you click a more info thing it will load some markdown into this template to be viewed
from tkinter import *
from tkinter import ttk
import os, sys, scripts.ScrollPanel, scripts.Onefile
from scripts import Theme
from PIL import Image, ImageTk
GarbColImageGroup = [] # Needed because garbage collection will delete pictures otherwise
OpenWindows = []

class Description:

    def __init__(self, geometry = (800,800)):
        self.geometry = geometry
        self.data:list[DescriptionObject] = []
        
    def Tag(self, text:str, padx=(20,20), pady=(0,0), anchor="w", side=None):
        self.data.append(PopTag(text, padx, pady, anchor, side=side))
        
    def Text(self,text:str, padx=(20,20), pady=(5,5), anchor="center", side=None):
        self.data.append(PopText(text,padx,pady, anchor, side=side))

    def Image(self,imagePath:str, game, size = 400, padx=5, pady=(5,5), anchor=None, side=None):
        if scripts.Onefile.isOneFile: # Images come from a different path when packed to one file
            imagePath = os.path.join(sys._MEIPASS,game, "Images", imagePath)
        else:
            imagePath = f"./{game}/Images/{imagePath}"
        self.data.append(PopImage(imagePath, size, padx, pady, anchor, side=side))
    
    def Header(self, text:str, padx=2, pady=(0,5), anchor="w"):
            self.data.append(PopHeader(text, padx, pady, anchor))
            

class DescriptionObject():
    def __init__(self, data, padx,pady, anchor, fill = None, expand = None, side=None):
        self.data = data
        self.obj = None
        self.anchor = anchor
        self.padx = padx
        self.pady = pady
        self.fill = fill
        self.expand = expand
        self.side = side
    def SpecialPack(self):
        self.obj.pack(anchor=self.anchor, padx= self.padx, pady=self.pady, fill=self.fill, expand=self.expand, side=self.side)

class PopTag(DescriptionObject):
    pass

class PopText(DescriptionObject):
    pass
        
class PopImage(DescriptionObject):
    def __init__(self, data, size, padx, pady, anchor, fill=None, expand=None, side=None):
        super().__init__(data, padx, pady, anchor, fill, expand, side=side)
        self.size = size
        
class PopHeader(DescriptionObject):
    def __init__(self, data, padx, pady, anchor, fill="x", expand=True):
        super().__init__(data, padx, pady, anchor, fill, expand)
        self.childGroup = []
        
    def Dropdown(self):
        if any(child.obj.winfo_ismapped() for child in self.childGroup): # Checks if any of the children are packed currently to tell which way to toggle things
            for child in self.childGroup:
                child.obj.pack_forget()
        else:
            for child in self.childGroup:
                child.SpecialPack()

def GenericPopup(title):
    for top in OpenWindows:
        if top.winfo_exists() and top.title() == title:
            top.focus()
            top.deiconify() # unminimizes
            return None # If it exists, don't create a new one
        
    top = Toplevel(padx=10, pady=10)  # Create a new top-level window
    top.title(title)
    OpenWindows.append(top)
    
    top.protocol("WM_DELETE_WINDOW", lambda: (OpenWindows.remove(top), top.destroy())) # remove windows from list on close
    Theme.RootsForStyling.append(top)
    Theme.ThemeUpdate()
    
    return top

def StyledPopup(title, descData, root, isForcedPack = False):
    top = GenericPopup(title)
    if top == None:
        return # Dont do this again if top window already exists
    top.attributes(alpha = 0)
    myDescription:Description = descData()
    scrollPanel = scripts.ScrollPanel.ScrollablePanel(top)
    
    curHeader:PopHeader = None # Tracks how to place children under headers
    curFrame:ttk.Frame = None # Groups our options so they can collapse and regroup together
        
    # loop over data from the description class and parse it
    hasFewHeaders = sum(isinstance(item, PopHeader) for item in myDescription.data) < 3
    for descObj in myDescription.data:
        if isinstance(descObj, PopImage): # Image
            img = Image.open(descObj.data)
            img.thumbnail((descObj.size, descObj.size), Image.LANCZOS) # Resizes our image and keeps ratio
            img = ImageTk.PhotoImage(img)
            descObj.obj = ttk.Label(curFrame, image=img, padding=5, style="DescriptionImage.TLabel")
            GarbColImageGroup.append(img)
            curHeader.childGroup.append(descObj)
            
        elif isinstance(descObj, PopHeader): # Header
            curFrame = ttk.Frame(scrollPanel.innerFrame)
            descObj.obj = ttk.Button(curFrame,text=descObj.data, style="Header.TButton", padding=(10,10,50,10), command=lambda obj= descObj: (obj.Dropdown(), scrollPanel.ResizeScrollPanel(), center(top, root)))
            curHeader = descObj
            curFrame.pack(fill="x", expand=True)
            descObj.SpecialPack()

        elif isinstance(descObj, PopText): # Text
            descObj.obj = ttk.Label(curFrame, text=descObj.data, wraplength=myDescription.geometry[1] - 60)
            curHeader.childGroup.append(descObj)
        
        elif isinstance(descObj, PopTag): # Tag
            descObj.obj = ttk.Label(curFrame, text=descObj.data, style="Tag.TLabel")
            curHeader.childGroup.append(descObj)
            
        if hasFewHeaders or isForcedPack: # If we have less than 3 headers go ahead and pack everything
            descObj.SpecialPack()

    Theme.ThemeUpdate()
    scrollPanel.ResizeScrollPanel()
    center(top, root)
    top.attributes(alpha = 1) # Show after centering (cant use deiconify because then the deiconify dimensions dont get updated) 
    
    top.protocol("WM_DELETE_WINDOW", lambda: (OpenWindows.remove(top), top.destroy())) # remove windows from list on close
    return top
   
def center(win:Toplevel, mainwindow:Toplevel):
    '''Centers a window in top window'''
    mainwindow.update()
    win.update()
    width = win.winfo_width()
    height = win.winfo_height()
    parentwidth = mainwindow.winfo_width()
    parentheight = mainwindow.winfo_height()
    parentxcoord = mainwindow.winfo_rootx()
    parentycoord = mainwindow.winfo_rooty()
    x = parentxcoord + (parentwidth - width) // 2
    y = parentycoord + (parentheight - height) // 2
    win.geometry(f"+{x}+{y}")

def center_window(window:Toplevel):
    '''Centers root window based on screen size'''
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
