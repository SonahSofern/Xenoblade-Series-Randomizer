import Options, json, random
from scripts import JSONParser, Helper

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

    # Choose multiplier range based on total defense
    if total > 200:
        multiplier_range = [0.7, 1.3]
    elif total > 100:
        multiplier_range = [0.3, 1.5]
    else:
        multiplier_range = [0.1, 1.7]

    mult = round(random.uniform(*multiplier_range), 2)

    arm["arm_phy"] = min(int(arm["arm_phy"] * mult), 255)
    arm["arm_eth"] = min(int(arm["arm_eth"] * mult), 255)

def GemSlots(arm):
    if arm["uni_flag"] != 1:
        isSlotted = random.choice([0,0,0,1,1])
        arm["jwl_slot"] = isSlotted
    
    # # rolls for unique augment and the flag associated with it
    # isUnique = Helper.OddsCheck(10)
    # if isUnique:
    #     uniFlag = 1
    #     arm["jwl_skill1"] = random.choice(skills)
    # else:
    #     uniFlag = 0
    # arm["uni_flag"] = uniFlag
        
def WeightClass(arm):
    # 1 Light
    # 2 Medium
    # 3 Heavy 
    # 4-12 Fiora Drones changes level of her talent art
    # 13 Fiora Only Armor
    changeAbleTypes = [1,2,3]
    if arm["arm_type"] in changeAbleTypes:
        arm["arm_type"] = random.choice(changeAbleTypes)


class Accessory:
    def __init__(self, parts, char, cosmID, list:list):
        self.parts = parts
        self.char = char
        self.cosmID = cosmID
        list.append(self)

def GearAppearance():
    with open(f"./XCDE/_internal/JsonOutputs/bdat_common/ITM_equiplist.json", 'r+', encoding='utf-8') as equipFile:
        eqData = json.load(equipFile)
        isCrazy = Options.EquipmentOption_CrazyArmors.GetState()
        
    
        accessoryLists = []
        headLists = []
        chestLists = []
        armLists = []
        legLists = []
        bootLists = []
        
        # Loop over the characters and create our accessory lists
        for i in range(0, 16):      
            
            # Add a new subList for each character                  
            accessoryLists.append([])
            headLists.append([])
            chestLists.append([])
            armLists.append([])
            legLists.append([])
            bootLists.append([])
            
            
            # Add the possible choices of cosmetic to the pool
            for eq in eqData["rows"]:
                cosmID = eq["pc"][i]
                
                # 0 Means you cant equip it so we dont want to spread the armors they just dissapear
                if cosmID == 0:
                    continue
                
                # For some reason Parlour Jacket is listed as gloves so this fixes that (tested in game and this is good)
                if eq["$id"] == 57:
                    eq["parts"] = 2
                
                # Ensure that head cosmetic id stays on head pieces to maintain proper cosmetics
                if eq["parts"] == 0:
                    accessoryLists[i].append(cosmID)
                elif eq["parts"] == 1:
                    headLists[i].append(cosmID)
                elif eq["parts"] == 2:
                    chestLists[i].append(cosmID)     
                elif eq["parts"] == 3:
                    armLists[i].append(cosmID)                         
                elif eq["parts"] == 4:
                    legLists[i].append(cosmID)           
                elif eq["parts"] == 5:
                    bootLists[i].append(cosmID)   
        
        # Loop over characters and Dole out the choices to the armours
        for i in range(0, 16):
                        
            for eq in eqData["rows"]:
                
                if eq["pc"][i] == 0: # Ignore armors that you couldnt normally equip
                    continue
                
                # If crazy armor we want to randomly choose a list, otherwise choose the list corresponsing with the current character (i)
                if isCrazy:
                    j = random.choice([0,1,2,3,4,5,6,7,11,12])
                else:
                    j = i
                    
                if  eq["parts"] == 0:
                    possibleList = accessoryLists[j]
                elif eq["parts"] == 1:
                    possibleList = headLists[j]
                elif eq["parts"] == 2:
                    possibleList = chestLists[j]
                elif eq["parts"] == 3:
                    possibleList = armLists[j]
                elif eq["parts"] == 4:
                    possibleList = legLists[j]
                elif eq["parts"] == 5:
                    possibleList = bootLists[j]
                
                try:
                    cosmID = random.choice(possibleList)
                except:
                    pass
                eq["pc"][i] = cosmID
                possibleList.remove(cosmID)

        JSONParser.CloseFile(eqData, equipFile)


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