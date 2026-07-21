import json
from scripts import JSONParser, Helper, PopupDescriptions
from XC3.XC3_Scripts import Enhancements

def GemRando(): # Match class to skill type probably or at least an option to
    # Validate and create enhancement groups based on where the enhancements belong
    def isBaseValid(enh:Enhancements.Enhancement):
        return enh.isGem and not enh.isFutureRedeemedOnly
    gemEnhList_Base = Helper.RandomGroup(Enhancements.EnhancementsList)
    gemEnhList_Base.FilterList(isBaseValid)
    ReplaceGem(gemEnhList_Base, "Enhance", "Name")
    
    def isDLC4Valid(enh:Enhancements.Enhancement):
        return enh.isGem and not enh.isBaseGameOnly
    gemEnhList_DLC = Helper.RandomGroup(Enhancements.EnhancementsList)
    gemEnhList_DLC.FilterList(isDLC4Valid)
    ReplaceGem(gemEnhList_DLC, "Enhance_dlc04", "Name_dlc04")
    
    

def ReplaceGem(enhList:Helper.RandomGroup, enhIDKey, enhNameIDKey):
    gemFile = JSONParser.File("XC3/JsonOutputs/sys/ITM_Gem.json")
    enhanceFile = JSONParser.File("XC3/JsonOutputs/btl/BTL_Enhance.json")
    nameFile = JSONParser.File("XC3/JsonOutputs/system/msg_item_gem.json")

    HealerGemList = Helper.RandomGroup()
    AttackerGemList = Helper.RandomGroup()
    DefenderGemList = Helper.RandomGroup()
    MiscGemList = Helper.RandomGroup()
    
    MiscCategory = [1,2,3,4,5]
    AttackerCategory = [6,7,8,9,10]
    DefenderCategory = [11,12,13,14,15]
    HealerCategory = [16,17,18,19,20]
    
    # Sort into type groups
    for enh in enhList.originalGroup:
        enh:Enhancements.Enhancement
        if enh.roleType == Enhancements.Atk:
            AttackerGemList.AddNewData(enh)
        elif enh.roleType == Enhancements.Def:
            DefenderGemList.AddNewData(enh)
        elif enh.roleType == Enhancements.Hlr:
            HealerGemList.AddNewData(enh)
        else:
            MiscGemList.AddNewData(enh)
            
    # Replace the gems file
    for gem in gemFile.rows: 
        if (gem["$id"]-1)%10 == 0: # Every 10 gems choose a new skill for level 1-10
            gemCategory = gem["Category"]
            if gemCategory in AttackerCategory:
                chosenEnhancement = AttackerGemList.SelectRandomMember()
            elif gemCategory in DefenderCategory:
                chosenEnhancement = DefenderGemList.SelectRandomMember()
            elif gemCategory in HealerCategory:
                chosenEnhancement = HealerGemList.SelectRandomMember()
            else:
                chosenEnhancement = MiscGemList.SelectRandomMember() 
        
        gem[enhIDKey] = CreateNewGemEffect(chosenEnhancement, enhanceFile.data, gem["GemLv"])        
        gem[enhNameIDKey] = SetNewName(chosenEnhancement, gem, nameFile)
        
    gemFile.Close()
    enhanceFile.Close()
    nameFile.Close()

def CreateNewGemEffect(chosenEnhancement:Enhancements.Enhancement, enhanceData, gemLevel):
    return chosenEnhancement.CreateEffect(enhanceData, powerPercent=Helper.RandomDecimal((gemLevel-1)*10,gemLevel*10))
    

Numerals = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X"
}
 
def SetNewName(chosenSkill:Enhancements.Enhancement, gem, nameData:JSONParser.File):
    '''Creates a new row to name each gem'''
    newID = nameData.rows[-1]["$id"] + 1
    template = {
      "$id": newID,
      "label": "<AE03AD91>",
      "style": 15,
      "name": f"{chosenSkill.name} {Numerals[gem["GemLv"]]}"
    }
    nameData.rows.append(template)
    return newID
 
def EasyGemCrafting():
    gemFile = JSONParser.File("XC3/JsonOutputs/btl/BTL_GemCraft.json")
    for gem in gemFile.rows:
        for i in range(1,7):
            if gem[f"ItemNum{i}"] > 1:
                gem[f"ItemNum{i}"] = 1
        gem["NcNum"] == gem["NcNum"]//5
        gem["Condition"] = 0
    gemFile.Close()
