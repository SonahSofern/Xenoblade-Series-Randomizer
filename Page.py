import tkinter as tk;
from tkinter import PhotoImage
import os
import sys
from tkinter import filedialog
from tkinter import ttk

root = tk.Tk()

root.title("Xenoblade Chronicles 2 Randomizer 0.1.0")
root.configure(background='#632424')
root.geometry('800x800')


tabControl = ttk.Notebook(root) 
  
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
tab3 = ttk.Frame(tabControl) 
tab4 = ttk.Frame(tabControl) 
tab5 = ttk.Frame(tabControl) 
  
tabControl.add(tab1, text ='General') 
tabControl.add(tab2, text ='Drivers') 
tabControl.add(tab3, text ='Blades') 
tabControl.add(tab4, text ='Enemies') 
tabControl.add(tab5, text ='Misc') 

tabControl.pack(expand = 1, fill ="both", padx=10, pady= 10) 


# icon = PhotoImage(file = os.path.join(sys._MEIPASS, 'Images\XC2Icon.png'))
# root.iconphoto(True, icon)


def UploadBDAT(event=None):
    filepath = filedialog.askopenfilename(filetypes=[("BDAT file", "*.bdat")])
    # here is the logic to use rust command on filepath if(filepath)

bdatButton = tk.Button(root, text='Browse', command=UploadBDAT)
msBdatButton = tk.Button(root, text='Browse', command=UploadBDAT)
bdatFilePathEntry = tk.Entry(root,textvariable = "", font=('calibre',10,'normal'))
msBdatFilePathEntry = tk.Entry(root,textvariable = "", font=('calibre',10,'normal'))
RandomizeButton = tk.Button(root, text='Randomize')


bdatButton.pack(anchor="w", padx=10)
bdatFilePathEntry.pack(anchor="w", pady=5,  padx=10)

msBdatButton.pack(anchor="w", padx=10)
msBdatFilePathEntry.pack(anchor="w",  padx=10, pady=5)

RandomizeButton.pack(pady=5)

root.mainloop()