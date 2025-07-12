import json, random
from scripts import JSONParser, Helper, PopupDescriptions
from XC3.XC3_Scripts import Options

def ClassAptitude():
    with open(f"XC3/JsonOutputs/btl/BTL_Talent.json", 'r+', encoding='utf-8') as talentFile:
        talentData = json.load(talentFile)
        mult = Options.ClassLearningOption.GetSpinbox()
        for talent in talentData["rows"]:
            for i in range(2,21):
                talent[f"NeedExpLv{i:02}"] = int(talent[f"NeedExpLv{i:02}"]//mult)
        JSONParser.CloseFile(talentData,talentFile)
    
def EarlyMoveSpeed():
    with open(f"XC3//JsonOutputs/fld/FLD_ColonyList.json", 'r+', encoding='utf-8') as colonyFile: # Make it a movespeed deed
        colonyData = json.load(colonyFile)
        for colony in colonyData["rows"]:
            if colony["$id"] == 4:
                colony["Level1"] = 10 # Instantly get it
                colony["Reward1"] = 70 # Movespeed
                colony["Condition"] = 253 # Remove the affinity condition (Setting it to a required quest early on)
                break
        JSONParser.CloseFile(colonyData,colonyFile)
    with open(f"XC3//JsonOutputs/fld/FLD_PerkResource.json", 'r+', encoding='utf-8') as perkFile: # Increase the power of the movespeed deeds
        perkData = json.load(perkFile)
        for perk in perkData["rows"]:
            if perk["$id"] == 1:
                newVal = Options.MoveSpeedOption.GetSpinbox()
                perk["Value1"] = newVal
                perk["Value2"] = newVal
                perk["Value3"] = newVal # Add this because im not removing the old value so u can get 3 of these
                break
        JSONParser.CloseFile(perkData, perkFile)
    
def AscendedClassEarly():
    with open(f"XC3//JsonOutputs/mnu/MNU_HeroDictionary.json", 'r+', encoding='utf-8') as charFile: # Increase the power of the movespeed deeds
        charData = json.load(charFile)
        for char in charData["rows"]:
            char["WakeupCondition"] = 21022
            char["WakeupQuest"] = 120
        JSONParser.CloseFile(charData, charFile)