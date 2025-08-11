import json, random, copy
from scripts import JSONParser, Helper, PopupDescriptions
from XC3.XC3_Scripts import Options

def TalentRando():
    Talents = Helper.InclRange(1,43)
    Talents = [7]
    mainChars = [1,2,3,4,5,6]
    isDefClass = Options.ClassOption_DefaultClasses.GetState()
    if isDefClass:
        with open("XC3/JsonOutputs/sys/CHR_PC.json", 'r+', encoding='utf-8') as charFile:
            charData = json.load(charFile)
            for char in charData["rows"]:
                if char["$id"] in mainChars:
                    char["DefTalent"] = random.choice(Talents)
                
            JSONParser.CloseFile(charData, charFile)
    
