import json, random, copy
from scripts import JSONParser, Helper, PopupDescriptions
from XC3.XC3_Scripts import Options

def TalentRando():
    ValidTalents = [1,2,3,4,5,6,7]
    TestClasses = []
    invalidTalents = [13,27,28,29,30,31]
    mainChars = [1,2,3,4,5,6]
    isDefClass = Options.ClassOption_DefaultClasses.GetState()
    if isDefClass:
        with open("XC3/JsonOutputs/sys/CHR_PC.json", 'r+', encoding='utf-8') as charFile:
            charData = json.load(charFile)
            for char in charData["rows"]:
                if char["$id"] in mainChars:
                    char["DefTalent"] = random.choice(ValidTalents)
                
            JSONParser.CloseFile(charData, charFile)
    
