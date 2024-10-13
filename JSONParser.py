import json
import random

def Randomize(cmdDescription, filePath, keyWord, lowRange, highRange, odds, ignoreList = []): # make this a function to reuse, check the settings ot see if we even do this
    if (odds == 0):
        return
    print(cmdDescription)   
    with open(filePath, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data['rows']:
            for key, value in row.items():
                if key.startswith(keyWord):
                    if ((random.randint(0,100) <= odds) and (not(row[key] in ignoreList))):
                        row[key] = random.randint(lowRange,highRange)
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)
