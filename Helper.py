import json
import os
from tkinter import filedialog
import tkinter as tk
import JSONParser

def inclRange(start, end):
     return list(range(start, end+1))

def StartsWithHelper(startingWord, lowNum, highNum):
    listofWords = []
    for i in range(lowNum, highNum + 1):
        listofWords.append(startingWord + str(i))
    return listofWords

def InsertHelper(insertIndex,  lowNum, highNum, mainString = str, pathTo = str):
    listOfFiles = []
    for i in range(lowNum, highNum):
        listOfFiles.append(pathTo + mainString[:insertIndex] + f"{i:02}" + mainString[insertIndex:]) # fstring allows us to format with 2 digits like xc2 wants
    #print(listOfFiles)
    return listOfFiles

def FindBadValuesList(filePath, keyWordList, keywordBadValueList, returnedKeyWordValue): # used for me to find a list of values from a file with certain characteristsics that i want to remove
    bad_values_found = []
    
    with open(filePath, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        
        for row in data['rows']:
            for key, value in row.items():
                if key in keyWordList and value in keywordBadValueList:
                    bad_values_found.append(row[returnedKeyWordValue]) 
    
    print(bad_values_found)


def DirectoryChoice(FileDescription, EntryField):
    Directory = filedialog.askdirectory(title=FileDescription)
    EntryField.delete(0, tk.END)
    EntryField.insert(0, Directory)

def OptionCarveouts( ValidValuesList = list, ToggleableIndexValue = int, stateOfButton = int):
    if stateOfButton == 1:
        if ToggleableIndexValue not in ValidValuesList:
            ValidValuesList.append(ToggleableIndexValue)
    elif stateOfButton == 0:
        if ToggleableIndexValue in ValidValuesList:
            ValidValuesList.remove(ToggleableIndexValue)
    #print(ValidValuesList)
    
OptionsRunList = []
rowIncrement = 0
def GenOption(optionName, parentTab, desc, randomize_parameters=[], ForcedBadValuesList = [],  OptionNameANDIndexValue = []):
    global rowIncrement
    global OptionsRunList
    parentTab.bind("<FocusIn>", lambda e: parentTab.state(["!focus"])) # removes highlights of inner tabs
    optionPanel = tk.Frame(parentTab, padx=10, pady=10)
    optionPanel.grid(row=rowIncrement, column= 0, sticky="sw")

    if (rowIncrement %2 == 0):
        desColor = "#ffffff"
    else:
        desColor ="#D5D5D5"
    
    optionPanel.config(background=desColor)
    option = tk.Label(optionPanel, text=optionName, background=desColor, width=30, anchor="w")
    option.grid(row=rowIncrement, column=0, sticky="sw")
    optionSlider = tk.Scale(optionPanel, from_=0, to=100, orient=tk.HORIZONTAL, sliderlength=10, background=desColor, highlightthickness=0)
    optionSlider.grid(row=rowIncrement, column=1, sticky='n')
    optionDesc = tk.Label(optionPanel, text=desc, background=desColor, width=900, anchor='w')
    optionDesc.grid(row=rowIncrement, column=2, sticky="sw")
    for i in range((len(OptionNameANDIndexValue))//2):
        var = tk.IntVar()
        OptionCarveouts(randomize_parameters[3], OptionNameANDIndexValue[i+1], var.get()) # run it initially
        box = tk.Checkbutton(optionPanel, background=desColor, text=OptionNameANDIndexValue[2*i], variable=var, command=lambda i=i: OptionCarveouts(randomize_parameters[3], OptionNameANDIndexValue[i+1], var.get()))
        box.grid(row=rowIncrement+i+1, column=0, sticky="sw")
    rowIncrement += 1

    print(len(randomize_parameters))
    if len(randomize_parameters) <= 4:
        randomize_parameters.append("")
        randomize_parameters.append([])
    print(len(ForcedBadValuesList))
    if len(ForcedBadValuesList) > 0:
        randomize_parameters[3] = [i for i in randomize_parameters[3] if i not in ForcedBadValuesList]
    OptionsRunList.append(lambda: JSONParser.RandomizeBetweenRange("Randomizing " + optionName, randomize_parameters[0], randomize_parameters[1], randomize_parameters[2], optionSlider.get(), randomize_parameters[3]))
