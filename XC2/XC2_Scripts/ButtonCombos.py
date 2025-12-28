from XC2.XC2_Scripts import Options
import json, random
from scripts import JSONParser

def BladeSpecialButtonChallenges():
    Buttons = []
    if Options.BladeSpecialButtonsOption_ABXY.GetState():
        Buttons += [1,2,3,4]
    if Options.BladeSpecialButtonsOption_Mystery.GetState():
        Buttons.append(5)
        
    with open(f"./XC2/JsonOutputs/common/MNU_BtnChallenge2.json", 'r+', encoding='utf-8') as btnFile:
        btnData = json.load(btnFile)
        for btn in btnData["rows"]:
            for i in range(1,4):
                if btn[f"BtnType{i}"] == 0 or btn[f"BtnType{i}"] != 2: # Ignore empty spots in points and ignore non blade special commands
                    continue
                btn[f"BtnType{i}"] = random.choice(Buttons) # Make our selection
        JSONParser.CloseFile(btnData, btnFile)