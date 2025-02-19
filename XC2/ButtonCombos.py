import Options, json, random
from scripts import Helper
def BladeSpecialButtonChallenges():
    Buttons = []
    if Options.BladeSpecialButtonsOption_A.GetState():
        Buttons.extend(1)
    if Options.BladeSpecialButtonsOption_B.GetState():
        Buttons.extend(2)
    if Options.BladeSpecialButtonsOption_X.GetState():
        Buttons.extend(3)
    if Options.BladeSpecialButtonsOption_Y.GetState():
        Buttons.extend(4)
    if Options.BladeSpecialButtonsOption_Mystery.GetState():
        Buttons.extend(5)
        
    with open(f"./XC2/_internal/JsonOutputs/common/MNU_BtnChallenge2.json", 'r+', encoding='utf-8') as btnFile:
        btnData = json.load(btnFile)
        for btn in btnData["rows"]:
            for i in range(1,4):
                if btn[f"BtnType{i}"] == 0 or btn[f"BtnType{i}"] != 2: # Ignore empty spots in points and ignore non blade special commands
                    continue
                btn[f"BtnType{i}"] = random.choice(Buttons) # Make our selection
        btnFile.seek(0)
        btnFile.truncate()
        json.dump(btnData, btnFile, indent=2, ensure_ascii=False)