from tkinter import *
from UI_Colors import *
from tkinter import font, ttk
import UI_Colors

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
    newWindow.title("GUI Settings")
    newWindow.geometry("800x100")
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

    def SaveUIChanges(event = None):
        import SavedOptions
        SavedOptions.saveData([defaultFont.cget("family"), defaultFont.cget("size")], "GUISavedOptions.txt")

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
    newWindow.bind("<Return>", SaveUIChanges)
    newWindow.bind("<Up>", IncreaseFontSize)
    newWindow.bind("<Down>", DecreaseFontSize) 

    newWindow.config(padx=10, pady=10)
    # Still dont get these two lines but oh well
    fontNameVar.trace_add("write", lambda name, index, mode: LoadFontByName(fontNameVar.get()))
    fontSizeVar.trace_add("write", lambda name, index, mode: LoadFontSize(fontSizeVar.get()))
    
    fontTestBack = Button(newWindow, text="Previous", command=PreviousFont, font=("Arial", 16))
    fontName = Entry(newWindow, width=20, font=("Arial", 16), textvariable=fontNameVar)
    fontTestNext = Button(newWindow, text="Next", command=NextFont, font=("Arial", 16))
    saveFont = Button(newWindow, text="Save", command=SaveUIChanges, font=("Arial", 16))
    fontSize = Entry(newWindow, width=3, font=("Arial", 16), textvariable=fontSizeVar)
    fontSize.delete(0, END)
    fontSize.insert(0,defaultFont.cget("size"))
    fontName.delete(0, END)
    fontName.insert(0,defaultFont.cget("family"))
    fontName.pack(padx=2, pady=2, side='left', anchor="nw")
    fontSize.pack(padx=2, pady=2, side='left', anchor="nw")
    fontTestBack.pack(padx=5, pady=2, side='left', anchor="nw")
    fontTestNext.pack( padx=5, pady=2, side='left', anchor="nw")
    saveFont.pack( padx=5, pady=2, anchor="nw")

    def ToggleLightDarkMode(button, root):
        if button.cget("text") == "Enable Dark Mode":
            button.config(text="Enable Light Mode")
        else:
            button.config(text="Enable Dark Mode")  
    darkMode = Button(newWindow, text="Enable Dark Mode", command=lambda: ToggleLightDarkMode(darkMode, rootWindow), font=("Arial", 16))
    darkMode.pack(padx=2, pady=2, side="left")
    # Make setting that turns off or on all inputs boxes/sliders etc.