import json
import random

def RandomizeBetweenRange(cmdDescription, Filename, keyWord, rangeValuesToReplace, sliderOdds, rangeValidReplacements): # make this a function to reuse, check the settings ot see if we even do this
    if (sliderOdds == 0):
        # print(cmdDescription + " Slider at zero") 
        return
    print(cmdDescription)   
    for name in Filename:
      with open("./_internal/JsonOutputs/common/" + name, 'r+', encoding='utf-8') as file:
          data = json.load(file)
          for row in data['rows']:
              for key, value in row.items():
                  if any((key == k) for k in keyWord):
                      if ((random.randint(0,100) <= sliderOdds) and ((row[key] in rangeValuesToReplace))):
                          row[key] = random.choice(rangeValidReplacements)
          file.seek(0)
          file.truncate()
          json.dump(data, file, indent=2)
