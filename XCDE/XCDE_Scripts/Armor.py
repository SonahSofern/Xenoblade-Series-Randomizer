import Options, json, random
from scripts import JSONParser

def ArmorRando():
    isRemoveStartingGear = Options.EquipmentOption_RemoveStartingEq.GetState()
    isAppearance = Options.EquipmentOption_Appearance.GetState()
    isDefenses = Options.EquipmentOption_Defenses.GetState()
    isGemSlots = Options.EquipmentOption_GemSlots.GetState()
    isWeightClass = Options.EquipmentOption_WeightClass.GetState()
    
    if isRemoveStartingGear:
        RemoveStartingGear()
    
    if isAppearance:
        GearAppearance()
   
    with open("./XCDE/_internal/JsonOutputs/bdat_common/ITM_equiplist.json", 'r+', encoding='utf-8') as armorFile:
        armData = json.load(armorFile)
        funcs = []
        
        if isDefenses:
            funcs.append(lambda arm: DefenseStats(arm))
                    
        if isGemSlots:
            funcs.append(lambda arm: GemSlots(arm))
                    
        if isWeightClass:
            funcs.append(lambda arm: WeightClass(arm))

        for arm in armData["rows"]:    
            for op in funcs:
                op(arm)

        JSONParser.CloseFile(armData, armorFile)
        
def DefenseStats(arm):
    total = arm["arm_phy"] + arm["arm_eth"]

    # The higher the items original stat total the less drastic the mult will be
    if total > 200:
        range = [0.9, 1.3]
    elif total > 100:
        range = [0.7, 2]
    else:
        range = [0.3, 3]
        
    mult = round(random.uniform(range[0],range[1]), 0.1)
    
    arm["arm_eth"] = min(int(arm["arm_eth"] * mult), 255)
    arm["arm_phy"] = min(int(arm["arm_phy"] * mult), 255)

def GemSlots(arm):
    arm["jwl_slot"]
    arm["uni_flag"]
    arm["jwl_skill1"]
    
def WeightClass(arm):
    arm["arm_type"]





def GearAppearance():
    armorTypes = ["armlist", "bodylist", "headlist", "waistlist", "legglist"]

    for type in armorTypes:
        Armorlist = []
        
        class Armor:
            def __init__(self, resource, style, pcid):
                self.resource = resource
                self.style = style
                self.pcid = pcid
                Armorlist.append(self)
                
        with open(f"./XCDE/_internal/JsonOutputs/bdat_common/ITM_{type}.json", 'r+', encoding='utf-8') as armFile:
            armData = json.load(armFile)
            
            for armor in armData["rows"]: # Create the list of armors
                Armor(armor["resource"], armor["style"], armor["pcid"])

            random.shuffle(Armorlist) # Shuffle the list
            
            # Considering how to handle this, kinda want the armor to be the same for each char, if you got makna gloves it will have makna appearance for all
                    

            JSONParser.CloseFile(armData, armFile)
    

def RemoveStartingGear():
    removeStartingGearCharacters = [1,2,3,4,5,6,7,8]
    with open("./XCDE/_internal/JsonOutputs/bdat_common/BTL_pclist.json", 'r+', encoding='utf-8') as charFile:
        charData = json.load(charFile)
        for char in charData["rows"]:
            if char["$id"] not in removeStartingGearCharacters:
                continue
            char["def_head"] = 0
            char["def_body"] = 0
            char["def_arm"] = 0
            char["def_waist"] = 0
            char["def_legg"] = 0

        charFile.seek(0)
        charFile.truncate()
        json.dump(charData, charFile, indent=2, ensure_ascii=False)