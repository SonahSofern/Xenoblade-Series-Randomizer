import json
import os
from tkinter import filedialog
import tkinter as tk

def inclRange(start, end):
     return list(range(start, end+1))

def StartsWith(startingWord, lowNum, highNum):
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
    
    #print(bad_values_found)


def DirectoryChoice(FileDescription, EntryField):
    Directory = filedialog.askdirectory(title=FileDescription)
    EntryField.delete(0, tk.END)
    EntryField.insert(0, Directory)

def OptionCarveouts(ValidValuesList, ToggleableIndexValues, stateOfButton = None):
    if stateOfButton.get() == True:
        ValidValuesList += ToggleableIndexValues
    else:
        ValidValuesList[:] = [x for x in ValidValuesList if x not in ToggleableIndexValues]
    print(ValidValuesList)
    print()
    print()
    
