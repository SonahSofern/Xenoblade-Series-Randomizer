from tkinter import *
from UI_Colors import *
from tkinter import font, ttk

def NotebookFocusStyleFix(defaultFont):
    style = ttk.Style()
    style.configure("TNotebook.Tab", font=(defaultFont))  # Change tab font
    style.layout("Tab",
    [('Notebook.tab', {'sticky': 'nswe', 'children':
        [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
            #[('Notebook.focus', {'side': 'top', 'sticky': 'nswe', 'children':
                [('Notebook.label', {'side': 'top', 'sticky': ''})],
            #})],
        })],
    })]
    )

def CheckbuttonFocusStyleFix():
    style = ttk.Style()
    # Modify the layout of the Checkbutton to include focus styling
    style.layout("TCheckbutton",
                 [('Checkbutton.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                     [('Checkbutton.focus', {'side': 'top', 'sticky': 'nswe', 'children':
                        [('Checkbutton.label', {'side': 'top', 'sticky': 'nswe'})],
                    })],
                 })]
    )

def OpenSettingsWindow(rootWindow, defaultFont):
    newWindow = Toplevel(rootWindow)
    iter = 0
    fontNameVar = StringVar()
    fontSizeVar = StringVar()
    GoodFonts = []
    newWindow.title("GUI Settings")
    newWindow.geometry("600x400")
    Label(newWindow).pack()
    allFonts = font.families()
    
    def LoadFontByName(name):
        defaultFont.config(family=name)

    def LoadFontSize(size):
        if ((size != "") and (0 < int(size)) and (int(size) < 60)):
            defaultFont.config(size=int(size))

    def NextFont(event= None):
        nonlocal iter
        iter += 1
        fontName.delete(0, END)
        fontName.insert(0,allFonts[iter])
        fontName.config(text=allFonts[iter])
        defaultFont.config(family=allFonts[iter])

    def PreviousFont(event = None):
        nonlocal iter        
        iter -= 1
        fontName.delete(0, END)
        fontName.insert(0,allFonts[iter])
        defaultFont.config(family=allFonts[iter])

    def GoodFont(event = None):
        nonlocal iter
        if allFonts[iter] not in GoodFonts:
            GoodFonts.append(allFonts[iter])
            print(GoodFonts)

    def IncreaseFontSize(event = None):
        newSize = defaultFont.cget("size") + 1
        LoadFontSize(newSize)
        fontSize.delete(0, END)
        fontSize.insert(0,newSize)
    def DecreaseFontSize(event = None):
        newSize = defaultFont.cget("size") - 1
        LoadFontSize(newSize)
        fontSize.delete(0, END)
        fontSize.insert(0,newSize)

    newWindow.bind("<Right>", NextFont)
    newWindow.bind("<Left>", PreviousFont) 
    newWindow.bind("<Return>", GoodFont)
    newWindow.bind("<Up>", IncreaseFontSize)
    newWindow.bind("<Down>", DecreaseFontSize) 

    # Still dont get these two lines but oh well
    fontNameVar.trace_add("write", lambda name, index, mode: LoadFontByName(fontNameVar.get()))
    fontSizeVar.trace_add("write", lambda name, index, mode: LoadFontSize(fontSizeVar.get()))
    
    fontName = Entry(newWindow, width=20, font=("Arial", 12), textvariable=fontNameVar)
    fontName.pack(side='left', padx=2)
    fontSize = Entry(newWindow, width=3, font=("Arial", 12), textvariable=fontSizeVar)
    fontSize.pack(side='left', padx=2)
    saveFont = Button(newWindow, text="Save Font", command=GoodFont, font=("Arial", 12))
    saveFont.pack(side='left', padx=5, pady=2)
    fontTestBack = Button(newWindow, text="Previous Font", command=PreviousFont, font=("Arial", 12))
    fontTestBack.pack(side='left', padx=5, pady=2)
    fontTestNext = Button(newWindow, text="Next Font", command=NextFont, font=("Arial", 12))
    fontTestNext.pack(side='left', padx=5, pady=2)