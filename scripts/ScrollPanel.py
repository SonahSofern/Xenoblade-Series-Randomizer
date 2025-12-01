garbList = []
import tkinter as tk
from tkinter import ttk
from tkinter import *
from scripts import Theme

# Horrid setup variables for getting correctly sized window. Can't figure out how to get the correct width.
PaddedValueWithScrollbar = 36
PaddedValueWithoutScrollbar = 18
maxHeight = int(int(Theme.windowHeight) * 0.5)

class ScrollablePanel():
    def __init__(self, parent:Toplevel):
        self.top = parent
        self.outerFrame = ttk.Frame(parent) 
        self.canvas = tk.Canvas(self.outerFrame)
        self.innerFrame = ttk.Frame(self.canvas)
        self.CreateScrollBar()
        garbList.append(self)
        Theme.CanvasesForStyling.append(self.canvas)
           
    def CreateScrollBar(self):
        self.scrollbar = ttk.Scrollbar(self.outerFrame, orient="vertical", command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set, borderwidth=0, relief="flat", highlightthickness=0)
        Theme.CanvasesForStyling.append(self.canvas)
        self.innerFrame.bind("<Configure>", lambda e, canvas=self.canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        self.canvas.create_window((0, 0), window=self.innerFrame, anchor="nw")
        
        self.ScrollbarShowCheck(isForced=True)
        
        self.canvas.pack(side="left", fill=BOTH, expand=True)
        
        self.outerFrame.bind("<Enter>", lambda e, canvas=self.canvas: canvas.bind_all("<MouseWheel>", lambda event: self._on_mousewheel(event, canvas)))
        self.outerFrame.bind("<Leave>", lambda e, canvas=self.canvas: canvas.unbind_all("<MouseWheel>"))
        
        self.outerFrame.pack(fill=BOTH, expand=True)

    def _on_mousewheel(self, event, canvas:Canvas):
        canvas.update_idletasks()
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        
    def ScrollbarShowCheck(self, isForced = False):
        '''Checks if the height of an the innerframe warrants showing the scrollbar.'''
        self.innerFrame.update()  # Ensure the geometry is up to date
        if isForced or self.innerFrame.winfo_height() >= maxHeight:
            self.scrollbar.pack(side="right", fill="y")
            return PaddedValueWithScrollbar
        else:
            self.scrollbar.pack_forget()
            return PaddedValueWithoutScrollbar
        
    def ResizeScrollPanel(self, pady=15):
        self.innerFrame.update()  # Ensure the geometry is up to date
        w = self.innerFrame.winfo_width() + self.ScrollbarShowCheck()
        h = min(self.innerFrame.winfo_height() + pady, maxHeight)
        self.top.geometry(f"{w}x{h}")
        self.top.update()
        
        
        

    

 
    