# Gems, Skills, Arts, Accessories, Archsage Gauntlet ↓
    # {
    #   "$id": 16,
    #   "label": "<22D84240>",
    #   "style": 79,
    #   "name": "Increases Critical Rate by [ML:EnhanceParam paramtype=1 ]\npercentage points."
    # },
import json

EnhancementsList = []

class Enhancement:
    def __init__(self, name, effID, captionID, field3E70C175, param1 = [], param2 = []):
        self.name = name
        self.effID = effID
        self.captionID = captionID
        self.field3E70C175 = field3E70C175
        self.param1 = param1
        self.param2 = param2
        EnhancementsList.append(self)
    
    def CreateEffect(self, BTL_EnhanceData, param1 = None, param2 = None):
        '''Returns the new ID'''
        newID = len(BTL_EnhanceData["rows"])+1
        newEffect = {
        "$id": newID,
        "ID": "",
        "EnhanceEffect": self.effID,
        "Param1": 20.0,
        "Param2": 0.0,
        "Caption": self.captionID,
        "DebugName": "",
        "AcceSetCheck": self.effID,
        "<3E70C175>": self.field3E70C175
        }
        BTL_EnhanceData["rows"].append(newEffect)  
        return newID    

with open(f"XC3/JsonOutputs/btl/BTL_Enhance.json", 'r+', encoding='utf-8') as enhanceFile:
    with open(f"XC3/JsonOutputs/btl/BTL_EnhanceEff.json", 'r+', encoding='utf-8') as enhanceEffFile:
        with open(f"XC3/JsonOutputs/battle/msg_btl_enhance_cap.json", 'r+', encoding='utf-8') as captionFile:
            with open(f"XC3/JsonOutputs/battle/msg_btl_enhance_name.json", 'r+', encoding='utf-8') as nameFile:
                enhanceData = json.load(enhanceFile)
                enhanceEffData = json.load(enhanceEffFile)
                captionData = json.load(captionFile)
                nameData = json.load(nameFile)
                TestList = []
                PreviousEffects = [0]
                for enh in enhanceData["rows"]:
                    if enh["EnhanceEffect"] not in PreviousEffects:
                        TestList.append(enh)
                        PreviousEffects.append(enh["EnhanceEffect"])
                        for enhEff in enhanceEffData["rows"]:
                            if enhEff["$id"] == enh["EnhanceEffect"]:
                                for name in nameData["rows"]:
                                    if name["$id"] == enhEff["Name"]:
                                        enh["ID"] = name["name"]
                                break
                            
                for enh in TestList:
                    param1 = ""
                    param2 = ""
                    if enh["Param1"] != 0:
                        param1 = ", []"
                    if enh["Param2"] != 0:
                        param2 = ", []"
                    raw_id = enh["ID"]
                    # Keep only alphanumeric characters
                    clean_id = ''.join(c for c in raw_id if c.isalnum())
                    print(f"{clean_id} = Enhancement('', {enh["EnhanceEffect"]}, {enh["Caption"]}, {enh["<3E70C175>"]}{param1}{param2})")
                    
MaxHPUp = Enhancement('Healthy', 1, 1, 1, [10,100])
AttackUp = Enhancement('Strong', 2, 3, 1, [10,100])
HealingUp = Enhancement('Restorer', 3, 4, 1, [10,100])
DexterityUp = Enhancement('Dextrous', 4, 5, 1, [10,100])
AgilityUp = Enhancement('Agile', 5, 6, 1, [10,100])
CriticalRateUp = Enhancement('Critical', 6, 7, 1, [10,100])
PhysicalDefenseUp = Enhancement('Iron', 7, 8, 1, [10,50])
EtherDefenseUp = Enhancement('Willpower', 8, 9, 1, [10,50])
BlockRateUp = Enhancement('Deflection', 9, 10, 1, [10,50])