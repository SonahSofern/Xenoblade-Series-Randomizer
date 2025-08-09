import json, random, copy
from XC3.XC3_Scripts import Enhancements
from scripts import JSONParser

# Currently allowing future redeemed or base game only skills because the amount of effort to fix like 5 effects would be not worth the time right now.

def AccessoryRando():
    with open("XC3/JsonOutputs/sys/ITM_Accessory.json", 'r+', encoding='utf-8') as itmFile:
        with open(f"XC3/JsonOutputs/btl/BTL_Enhance.json", 'r+', encoding='utf-8') as enhanceFile:
            with open(f"XC3/JsonOutputs/system/msg_item_accessory.json", 'r+', encoding='utf-8') as nameFile:
                enhData = json.load(enhanceFile)
                itmData = json.load(itmFile)
                nameData = json.load(nameFile)
                originalNameData = copy.deepcopy(nameData)
                
                # Filter the list
                newList = copy.deepcopy(Enhancements.EnhancementsList)
                enhList:list[Enhancements.Enhancement] = newList.currentGroup
                for enh in enhList:
                    if enh.isAccessory:
                        continue
                    newList.RemoveMember(enh)
                
                for item in itmData["rows"]:
                    if item["Enhance"] == 0 or item["Name"] == 0: # Ignore debug items
                        continue
                    newEnhancement:Enhancements.Enhancement = Enhancements.EnhancementsList.SelectRandomMember()
                    
                    DetermineRecommendedCategory(item, newEnhancement)
                    newID = newEnhancement.CreateEffect(enhData, powerPercent=DetermineAccessoryPower(item))
                    item["Enhance"] = newID
                    item["Name"] = CreateNewName(item, nameData, newEnhancement, originalNameData)
                    
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
    return powerLevel/100

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
    
def CreateNewName(acce ,nameData, newEnhancement:Enhancements.Enhancement, originalNameData):
    for name in originalNameData["rows"]:
        if name["$id"] == acce["Name"]:
            secondWord = name["name"].split()[-1]
            break

    newNameId = len(nameData["rows"]) + 1
    newName = {
      "$id": newNameId,
      "label": f"{newNameId}", # To ignore error messages over dupe IDs
      "style": 15,
      "name": f"{newEnhancement.name} {secondWord}"
    }
    nameData["rows"].append(newName)
    return newNameId