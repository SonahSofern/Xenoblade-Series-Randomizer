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
    filepath = filedialog.askopenfilename(filetypes=[("BDAT files", "*.bdat")])
    # here is the logic to use rust command on filepath if(filepath)

bdatButton = tk.Button(root, text='Browse', command=UploadBDAT)
msBdatButton = tk.Button(root, text='Browse', command=UploadBDAT)

bdatButton.config(anchor="w")
msBdatButton.config(anchor="w")
bdatButton.pack(anchor="ne", padx=5, pady=5)
msBdatButton.pack(anchor="ne", padx=5, pady=5)

root.mainloop()