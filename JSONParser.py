import json
import random

def RandomizeBetweenRange(cmdDescription, Filename, keyWord, rangeValuesToReplace, odds, rangeValidReplacements): # make this a function to reuse, check the settings ot see if we even do this
    if (odds == 0):
        return
    print(cmdDescription)   
    with open("./_internal/JsonOutputs/common/" + Filename, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data['rows']:
            for key, value in row.items():
                if key.startswith(keyWord):
                    if ((random.randint(0,100) <= odds) and ((row[key] in rangeValidReplacements))):
                        potentialVal = random.randint(rangeValuesToReplace[0],rangeValuesToReplace[1])
                        while not(potentialVal in rangeValidReplacements):
                            print("Rolled Bad Value")
                            potentialVal = random.randint(rangeValuesToReplace[0],rangeValuesToReplace[1])
                        row[key] = potentialVal
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2)
