import json
import tkinter as tk

def saveData(DataList):
    with open('SavedOptions.txt', 'w') as file:
        for saveData in DataList:
            file.write(f"{saveData.get()}" + '\n')



def loadData(DataList):
    with open('SavedOptions.txt', 'r') as file:
        savedLines = file.readlines()
        for i in range(len(DataList)):
            if isinstance(DataList[i], tk.Entry):
                DataList[i].delete(0,tk.END)
                DataList[i].insert(0, savedLines[i].strip())
            else:
                DataList[i].set(savedLines[i].strip())
