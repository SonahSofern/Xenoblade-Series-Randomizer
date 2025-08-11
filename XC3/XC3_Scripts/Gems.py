import json, random, copy
from scripts import JSONParser, Helper, PopupDescriptions
from XC3.XC3_Scripts import Enhancements



def GemRando(): # Match class to skill type probably or at least an option to
    ignoreKeys = ["$id", "Category", "GemLv", "Name", "Rarity", "Price", "Craft", "Craft2", "Icon", "Name_dlc04", "<227CA3FA>"]
    MiscCategory = [1,2,3,4,5]
    AttackerCategory = [6,7,8,9,10]
    DefenderCategory = [11,12,13,14,15]
    HealerCategory = [16,17,18,19,20]
    with open("XC3/JsonOutputs/sys/ITM_Gem.json", 'r+', encoding='utf-8') as gemFile:
        with open(f"XC3/JsonOutputs/btl/BTL_Enhance.json", 'r+', encoding='utf-8') as enhanceFile:
            with open(f"XC3/JsonOutputs/system/msg_item_gem.json", 'r+', encoding='utf-8') as nameFile:
                enhanceData = json.load(enhanceFile)
                gemData = json.load(gemFile)
                nameData = json.load(nameFile)
                
                HealerGemList = Helper.RandomGroup()
                AttackerGemList = Helper.RandomGroup()
                DefenderGemList = Helper.RandomGroup()
                MiscGemList = Helper.RandomGroup()
                
                # Generate Custom Skill List
                copyList = copy.deepcopy(Enhancements.EnhancementsList)
                copyListCurrentGroup:list[Enhancements.Enhancement] = copyList.currentGroup
                for enh in copyListCurrentGroup:
                    if not enh.isGem:
                        continue
                    if enh.isChainActivation:
                        continue
                    if enh.isChainOrder:
                        continue
                    if enh.roleType == Enhancements.Atk:
                        AttackerGemList.AddNewData(enh)
                    elif enh.roleType == Enhancements.Def:
                        DefenderGemList.AddNewData(enh)
                    elif enh.roleType == Enhancements.Hlr:
                        HealerGemList.AddNewData(enh)
                    else:
                        MiscGemList.AddNewData(enh)
                # Replace the gems file
                for gem in gemData["rows"]: 
                    if gem["$id"]%10 == 0 or gem["$id"] == 12001: # Every 10 gems choose a new skill for level 1-10
                        gemCategory  = gem["Category"]
                        if gemCategory in AttackerCategory:
                            chosenEnhancement = AttackerGemList.SelectRandomMember()
                        elif gemCategory in DefenderCategory:
                            chosenEnhancement = DefenderGemList.SelectRandomMember()
                        elif gemCategory in HealerCategory:
                            chosenEnhancement = HealerGemList.SelectRandomMember()
                        else:
                            chosenEnhancement = MiscGemList.SelectRandomMember() 
                    
                    newGem = CreateNewGem(chosenEnhancement, enhanceData, gem["GemLv"])                    
                    Helper.CopyKeys(gem, newGem, ignoreKeys)

                    DetermineName(chosenEnhancement, gem, nameData)

                JSONParser.CloseFile(gemData, gemFile)
                JSONParser.CloseFile(enhanceData, enhanceFile)
                JSONParser.CloseFile(nameData, nameFile)

def CreateNewGem(chosenEnhancement:Enhancements.Enhancement, enhanceData, gemLevel):
    newEffect = chosenEnhancement.CreateEffect(enhanceData, powerPercent=Helper.RandomDecimal((gemLevel-1)*10,gemLevel*10))
    return {
      "$id": "Null",
      "ID": "Null",
      "Name": 1,
      "DebugName": "",
      "Category": 1,
      "GemLv": "Null",
      "Icon": "Null",
      "Enhance": newEffect,
      "Price": 610,
      "Rarity": 0,
      "Sell": 0,
      "ForgePoint": 0,
      "Craft": 1,
      "<227CA3FA>": "Null",
      "Craft2": 201,
      "Name_dlc04": 1,
      "Enhance_dlc04": newEffect
    }

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
 
def DetermineName(chosenSkill:Enhancements.Enhancement, gem, nameData):
    for name in nameData["rows"]:
        if name["$id"] == gem["Name"]:
            name["name"] = f"{chosenSkill.name} {Numerals[gem["GemLv"]]}"
            break
 