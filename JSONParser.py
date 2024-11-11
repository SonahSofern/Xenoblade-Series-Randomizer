import json
import random
import os

def ChangeJSON(cmdDescription, Filename, keyWords, rangeofValuesToReplace, sliderOdds, rangeValidReplacements, InvalidTargetIDs): # make this a function to reuse, check the settings ot see if we even do this
    if (sliderOdds == 0):
        #print(cmdDescription + " Slider at zero") 
        return
    if (cmdDescription != ""):
        print("Randomizing " + cmdDescription)   
    for name in Filename:
        filePath = "./_internal/JsonOutputs/" + name
        if not os.path.exists(filePath):
          #print(filePath + " filepath does not exist.")
          continue
        with open(filePath, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for item in data['rows']:
                if not item["$id"] in InvalidTargetIDs:
                    for key, value in item.items():
                        if any((key == k) for k in keyWords):
                            if ((random.randint(0,100) <= sliderOdds) and ((item[key] in rangeofValuesToReplace))):
                                item[key] = random.choice(rangeValidReplacements)
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
