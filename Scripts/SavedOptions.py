import tkinter as tk

def saveData(DataList):
    with open('SavedOptions.txt', 'w') as file:
        for saveData in DataList:
            file.write(f"{saveData.get()}" + '\n')



def loadData(DataList):
    try:
        with open('SavedOptions.txt', 'a+') as file:
            file.seek(0)
            savedLines = file.readlines()
            for i in range(len(savedLines)):
                if isinstance(DataList[i], tk.Entry):
                    DataList[i].delete(0,tk.END)
                    DataList[i].insert(0, savedLines[i].strip())
                else:
                    DataList[i].set(savedLines[i].strip())
    except:
        print("Error Loading Save Data (Likely an option was added or removed)")