import json, random
from XC3.XC3_Scripts import Enhancements
from scripts import JSONParser

def AccessoryRando():
    with open("XC3/JsonOutputs/sys/ITM_Accessory.json", 'r+', encoding='utf-8') as itmFile:
        with open(f"XC3/JsonOutputs/btl/BTL_Enhance.json", 'r+', encoding='utf-8') as enhanceFile:
            with open(f"XC3/JsonOutputs/system/msg_item_accessory.json", 'r+', encoding='utf-8') as nameFile:
                enhData = json.load(enhanceFile)
                itmData = json.load(itmFile)
                nameData = json.load(nameFile)
                
                for item in itmData["rows"]:
                    newEnhancement:Enhancements.Enhancement = Enhancements.AccessoryEnhancementList.SelectRandomMember()
                    powerLv = DetermineAccessoryPower(item)
                    DetermineRecommendedCategory(item, newEnhancement)
                    newID = newEnhancement.CreateEffect(enhData, powerPercent=powerLv)
                    item["Enhance"] = newID
                    ApplyNewName(item, nameData, newEnhancement)
                    
                JSONParser.CloseFile(itmData, itmFile)
                JSONParser.CloseFile(enhData, enhanceFile)
                JSONParser.CloseFile(nameData, nameFile)

def DetermineAccessoryPower(item):
    if item["Rarity"] == 2:
        powerLevel = random.randrange(70,101)
    elif item["Rarity"] == 1:
        powerLevel = random.randrange(40,70)
    else:
        powerLevel = random.randrange(0,40)
    return powerLevel//100

def DetermineRecommendedCategory(acce, enhancement:Enhancements.Enhancement):
    acce["Flag_RecTank"] = 0
    acce["Flag_RecAttacker"] = 0
    acce["Flag_RecHealer"] = 0
    if enhancement.roleType == Enhancements.H:
        acce["Flag_RecHealer"] = 1
    elif enhancement.roleType == Enhancements.A:
        acce["Flag_RecAttacker"] = 1
    elif enhancement.roleType == Enhancements.D:
        acce["Flag_RecTank"] = 1
    
def ApplyNewName(acce, nameData, newEnhancement:Enhancements.Enhancement):
    for name in nameData["rows"]:
        if name["$id"] == acce["Name"]:
            name["name"] = newEnhancement.name
            break