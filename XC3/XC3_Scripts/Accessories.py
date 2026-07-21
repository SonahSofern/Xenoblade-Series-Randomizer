import json, random, copy
from XC3.XC3_Scripts import Enhancements, IDs
from scripts import JSONParser, Helper

# Currently allowing future redeemed or base game only skills because the amount of effort to fix like 5 effects would be not worth the time right now.

def AccessoryRando():
    accFile = JSONParser.File("XC3/JsonOutputs/sys/ITM_Accessory.json")
    enhanceFile = JSONParser.File("XC3/JsonOutputs/btl/BTL_Enhance.json")
    nameFile = JSONParser.File("XC3/JsonOutputs/system/msg_item_accessory.json")
    
    # Validation and creation of the enhancement groups for game/item they are being placed on.
    
    def isDLC4Valid(enh:Enhancements.Enhancement):
        return enh.isAccessory and not enh.isBaseGameOnly
    dlc4List = Helper.RandomGroup(Enhancements.EnhancementsList)
    dlc4List.FilterList(isDLC4Valid)
    
    def isBaseValid(enh:Enhancements.Enhancement):
        return enh.isAccessory and not enh.isFutureRedeemedOnly
    baseList = Helper.RandomGroup()
    baseList.ExtendNewData(Enhancements.EnhancementsList)
    baseList.FilterList(isBaseValid)
    
    # Manuals are special items that should only do chain attack things
    def isManualValid(enh:Enhancements.Enhancement):
        return enh.isChainActivation
    manualList = Helper.RandomGroup(Enhancements.EnhancementsList) 
    manualList.FilterList(isManualValid)
    
    for acc in accFile.rows:
        if acc["$id"] not in IDs.BaseAccessoriesIDs + IDs.AccessoryManualIDs + IDs.DLC4AccessoriesIDs: continue
        
        # Choose the group to draw an enhancement from
        if acc["$id"] in IDs.AccessoryManualIDs: targetList = manualList
        elif acc["$id"] in IDs.BaseAccessoriesIDs: targetList = baseList
        elif acc["$id"] in IDs.DLC4AccessoriesIDs: targetList = dlc4List
        else: print(f"No group for accessory id: {acc["$id"]}")
        
        # Get new enhancement from group then apply it and add to the bdats
        newEnhancement:Enhancements.Enhancement = targetList.SelectRandomMember()
        DetermineRecommendedCategory(acc, newEnhancement)
        newID = newEnhancement.CreateEffect(enhanceFile.data, powerPercent=DetermineAccessoryPower(acc))
        acc["Enhance"] = newID
        acc["Name"] = CreateNewName(acc, nameFile.data, newEnhancement, nameFile.originalData)
        
    accFile.Close()
    enhanceFile.Close()
    nameFile.Close()

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
    if enhancement.roleType == Enhancements.Hlr:
        acce["Flag_RecHealer"] = 1
    elif enhancement.roleType == Enhancements.Atk:
        acce["Flag_RecAttacker"] = 1
    elif enhancement.roleType == Enhancements.Def:
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

def AccessoryDesc():
    pass