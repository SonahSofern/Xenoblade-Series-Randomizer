garbList = []
import tkinter as tk
from tkinter import ttk
from tkinter import *

class ScrollablePanel():
    def __init__(self, parent):
        self.outerFrame = ttk.Frame(parent) 
        self.canvas = tk.Canvas(self.outerFrame)
        self.innerFrame = ttk.Frame(self.canvas)
        self.Scroll()
        garbList.append(self)
        
    def Scroll(self):
        CreateScrollBars([self.outerFrame], [self.canvas], [self.innerFrame])

def CreateScrollBars(OuterFrames:list[ttk.Frame], Canvases:list[Canvas], InnerFrames:list[ttk.Frame], genScrollbar = True):
    for i in range(len(Canvases)):
        InnerFrames[i].pack(fill=BOTH, expand=True)

        scrollbar = ttk.Scrollbar(OuterFrames[i], orient="vertical", command=Canvases[i].yview)
        Canvases[i].config(yscrollcommand=scrollbar.set, borderwidth=0, relief="flat", highlightthickness=0)
        CanvasesForStyling.append(Canvases[i])
        # OuterFrames[i].config(borderwidth=0, relief="flat")
        InnerFrames[i].bind("<Configure>", lambda e, canvas=Canvases[i]: canvas.configure(scrollregion=canvas.bbox("all")))

        Canvases[i].create_window((0, 0), window=InnerFrames[i], anchor="nw")

        Canvases[i].pack(side="left", fill=BOTH, expand=True)
        if genScrollbar:
            scrollbar.pack(side="right", fill="y")

        OuterFrames[i].bind("<Enter>", lambda e, canvas=Canvases[i]: canvas.bind_all("<MouseWheel>", lambda event: _on_mousewheel(event, canvas)))
        OuterFrames[i].bind("<Leave>", lambda e, canvas=Canvases[i]: canvas.unbind_all("<MouseWheel>"))
        
        OuterFrames[i].pack_propagate(False)
        OuterFrames[i].pack(fill=BOTH, expand=True)

def _on_mousewheel(event, canvas:Canvas):
    canvas.update_idletasks()
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    # print(canvas.cget("scrollregion"))
