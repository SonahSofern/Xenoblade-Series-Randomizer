import json, random, time
from tkinter import filedialog
import tkinter as tk

def InclRange(start, end):
     return list(range(start, end+1))

def StartsWith(startingWord, lowNum, highNum, addJson = False):
    listofWords = []
    for i in range(lowNum, highNum + 1):
        newVer = startingWord + str(i)
        if addJson:
            newVer = newVer + ".json"
        listofWords.append(newVer)
    return listofWords

def InsertHelper(insertIndex,  lowNum, highNum, mainString = str, pathTo = str):
    listOfFiles = []
    for i in range(lowNum, highNum):
        listOfFiles.append(pathTo + mainString[:insertIndex] + f"{i:02}" + mainString[insertIndex:]) # fstring allows us to format with 2 digits like xc2 wants
    #print(listOfFiles)
    return listOfFiles

def FindValues(filePath: str, keyWordList: list, keywordBadValueList: list, returnedKeyWordValue: str): # used to find a list of values from a file with certain characteristsics that i want to remove
    bad_values_found = []
    with open(filePath, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data['rows']:
            for key, value in row.items():
                if key in keyWordList and value in keywordBadValueList:
                    bad_values_found.append(row[returnedKeyWordValue]) 
    
    # print("FindValues: " + bad_values_found)
    return(bad_values_found)

def AdjustedFindBadValuesList(filePath, keyWordList, keywordBadValueList, returnedKeyWordValue): # if one keywordBadValueList has 2 matches, it won't return the second one. 
    bad_values_found = []
    with open(filePath, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for j in range(0, len(keyWordList)):
            for i in range(0, len(keywordBadValueList)):
                for row in data['rows']:
                    if row[keyWordList[j]] == keywordBadValueList[i]:
                        bad_values_found.append(row[returnedKeyWordValue])
                        break
    #print(bad_values_found)
    return(bad_values_found)

def FindSubOptionValuesList(filePath: str, dictName: str, subDictName: str, subDictValue, returndictValue):
    bad_values = []
    with open(filePath, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row[dictName][subDictName] == subDictValue:
                bad_values.append(row[returndictValue])
    #print(bad_values)
    return(bad_values)


def DirectoryChoice(FileDescription, EntryField):
    Directory = filedialog.askdirectory(title=FileDescription)
    if (Directory != ""):
        EntryField.delete(0, tk.END)
        EntryField.insert(0, Directory)

def OptionCarveouts(ValidValuesList, ToggleableIndexValues, stateOfButton = None):
    # print("Updated Valid Values: " + str(stateOfButton))
    if stateOfButton.get() == True:
        ValidValuesList += ToggleableIndexValues
    else:
        ValidValuesList[:] = [x for x in ValidValuesList if x not in ToggleableIndexValues]
    # print(ValidValuesList, end='\n\n')

def SubColumnAdjust(filename, colName, adjustedSubColName, desiredValue): #when your column you want to adjust is nested inside a dict
    with open(filename, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            row[colName][adjustedSubColName] = desiredValue
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def ColumnAdjust(filename: str, clearedCols: list, desiredValue):
    with open(filename, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for k in range(0, len(clearedCols)):
            for row in data["rows"]:
                for key, value in row.items():
                    if key != clearedCols[k]:
                        continue
                    row[clearedCols[k]] = desiredValue
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def MathmaticalColumnAdjust(filenames: list, ColumnsChange: list, equation: list): # use an equation to adjust whole columns
    for filename in filenames:
        with open(filename, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for k in range(0, len(ColumnsChange)):
                for row in data["rows"]:
                    for key, value in row.items():
                        if key != ColumnsChange[k]:
                            continue
                        if len(equation) != 1:
                            row[ColumnsChange[k]] = eval(equation[k])
                        else: # if you only want to use 1 equation to change every column, this allows it
                            row[ColumnsChange[k]] = eval(equation[0])
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)

def ExtendListtoLength(inputlist: list, extendtolength: int, extendusingvalues: str): # extends a list to a given length, using values based on an equation
    originallist = inputlist.copy()
    for i in range(len(originallist), extendtolength):
        if len(inputlist) >= extendtolength:
            break
        if len(inputlist) < extendtolength:
            inputlist.append(eval(extendusingvalues))
    outputlist = inputlist.copy()
    return outputlist

def GetMaxValue(filename: str, columnname: str): # Returns the maximum Value for a given column in a given file
    with open(filename, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        MaxRow = max(data["rows"], key = lambda x:x[columnname])
        MaxID = MaxRow[columnname]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    return MaxID

def GetMinValue(filename: str, columnname: str): # Returns the maximum Value for a given column in a given file
    with open(filename, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        MinRow = min(data["rows"], key = lambda x:x[columnname])
        MinID = MinRow[columnname]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    return MinID

def OddsCheck(odds):
    if odds > random.randrange(0,99):
        return True
    else:
        return False
    
def TimeFunction(command):
    start = time.perf_counter() # Make a funciton that does this and just takes any function as an arg
    me = lambda: command
    me()
    end = time.perf_counter()
    print(f"Execution Time: {end - start:.6f} seconds")

def MultiLevelListToSingleLevelList(inputlist: list): # Converts a multi-level list [1, [2, 3], 4, [5]] to a single-level list [1, 2, 3, 4, 5]
    outputlist = []
    for item in inputlist:
        if isinstance(item, list):
            outputlist.extend(item)
        else:
            outputlist.append(item)
    return outputlist