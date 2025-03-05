# This will be the template for when you click a more info thing it will load some markdown into this template to be viewed
from tkinter import *
from tkinter import ttk
import scripts.GUISettings

class Description:
    data:list[str] = []
    def __init__(self, title, geometry = ("500x500")):
        self.title = title
        self.geometry = geometry
    def Text(self,text:str):
        self.data.append(text)
    
    def Image(self,imagePath:str):
        self.data.append(imagePath)

def GenPopup(Description:Description, root, defaultFont, defTheme):
    # Open a window with the 
    top = Toplevel(root)  # Create a new top-level window
    top.title(Description.title)
    top.geometry(Description.geometry)
    scripts.GUISettings.RootsForStyling.append(top)
    scripts.GUISettings.LoadTheme(defaultFont, defTheme)
    # loop over data from the description class and parse it
    # for obj in Description.data:
    #     if obj.startswith("./"): # if we are a filepath
    #         # ttk.
    #         # Handle as filepath image
    #     else:
    #         # Handle as text
            
            
    print(f"Tried to gen popup {Description}.md")

