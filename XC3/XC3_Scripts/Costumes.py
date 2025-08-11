import json, random, copy
from scripts import JSONParser, Helper, PopupDescriptions
import XC3.XC3_Scripts.Options

def CostumeRando():
    with open("XC3/JsonOutputs/sys/RSC_PcCostumeOpen.json", 'r+', encoding='utf-8') as costumeFile:
        costumeData = json.load(costumeFile)
        ignoreKeys = ["Talent", "$id", "ID", "Name1", "Name2", "Name3", "Name4", "Name5", "Name6"]
        CostumeGroup = Helper.RandomGroup()
        CostumeGroup.GenData(costumeData["rows"])
        
        for costume in costumeData["rows"]:
            newCostume = CostumeGroup.SelectRandomMember()
            Helper.CopyKeys(costume, newCostume, ignoreKeys)

        JSONParser.CloseFile(costumeData, costumeFile)
        
