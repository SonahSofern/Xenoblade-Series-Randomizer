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
            if colony["$id"] == 1:
                colony["Level1"] = 0 # Instantly get it
                colony["Reward1"] = 70 # Movespeed
                colony["Condition"] = 0 # Remove the affinity condition
                colony["RespectFlag"] = 21022 # Remove the condition
                break
        JSONParser.CloseFile(colonyData,colonyFile)
    with open(f"XC3//JsonOutputs/fld/FLD_PerkResource.json", 'r+', encoding='utf-8') as perkFile: # Increase the power of the movespeed deeds
        perkData = json.load(perkFile)
        for perk in perkData["rows"]:
            if perk["$id"] == 1:
                newVal = Options.MoveSpeedOption.GetSpinbox() *10
                perk["Value1"] = newVal
                perk["Value2"] = newVal
                break
        JSONParser.CloseFile(perkData, perkFile)
    