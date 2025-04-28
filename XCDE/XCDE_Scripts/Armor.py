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
    
    # rolls for unique augment and the flag associated with it
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


def GearAppearance():
    with open(f"./XCDE/_internal/JsonOutputs/bdat_common/ITM_equiplist.json", 'r+', encoding='utf-8') as equipFile:
        eqData = json.load(equipFile)
        isCrazy = Options.EquipmentOption_CrazyArmors.GetState()
        invalidArmor = [190]
        dontReplace = [1,2,3,4,5,6,7,212,8,9,10,4,4,332,336,328]
        # Nested lists
        armorList = [[[] for _ in range(16)] for _ in range(6)]

        
        # Add the possible choices of cosmetic to the pool
        for eq in eqData["rows"]:
            # Loop over the characters and create our accessory lists
            
            # Dont add invalid ones
            if eq["$id"] in invalidArmor:
                continue
            
            for i in range(0, 16):      
                cosmID = eq["pc"][i]
            
                # 0 Means you cant equip it so we dont want to spread the armors they just dissapear
                if cosmID == 0:
                    continue
                
                # For some reason Parlour Jacket is listed as gloves so this fixes that (tested in game and this is good)
                if eq["$id"] == 57:
                    eq["parts"] = 2
                
                # Ensure that head cosmetic id stays on head pieces to maintain proper cosmetics
                armorList[eq["parts"]][i].append(cosmID)
        
        
        # Loop over characters and Dole out the choices to the armours
            
        for eq in eqData["rows"]:
            
            # Defined here so that each new equipment 
            
            

            if eq["$id"] in invalidArmor + dontReplace:
                continue
            for i in range(0, 16):
                if eq["pc"][i] == 0: # Ignore armors that you couldnt normally equip
                    continue
                # If crazy armor we want to randomly choose a list, otherwise choose the list corresponsing with the current character (i)
                if isCrazy:
                    # Used to seperate nopon and human cosmetics they dont mix well and even crash sometimes
                    human = [0,1,2,3,4,6,7,8,9,10,11,12,15]
                    nopon = [5,13,14]
                    if i in human:
                        group = human
                    elif i in nopon:
                        group = nopon # Nopon can have human cosmetics but humans crash with nopon cosmetics
                    else:
                        group = None
                    
                    
                    j = random.choice(group)
                    while armorList[eq["parts"]][j] == []:
                        group.remove(j)
                        j = random.choice(group)
                else:
                    j = i
                
                # Choose list
                possibleList = armorList[eq["parts"]][j]
                

                cosmID = random.choice(possibleList)
                possibleList.remove(cosmID)    
                eq["pc"][i] = cosmID

        JSONParser.CloseFile(eqData, equipFile)


def RemoveStartingGear():
    removeStartingGearCharacters = [1,2,3,4,5,6,7,8]
    armorKeys = ["def_head", "def_body", "def_arm", "def_waist", "def_legg","melia_def_head", "melia_def_body", "melia_def_arm", "melia_def_waist", "melia_def_legg"]
    with open("./XCDE/_internal/JsonOutputs/bdat_common/BTL_pclist.json", 'r+', encoding='utf-8') as charFile:
        charData = json.load(charFile)
        for char in charData["rows"]:
            if char["$id"] not in removeStartingGearCharacters:
                continue
            for key in armorKeys:
                char[key] = 0

        JSONParser.CloseFile(charData, charFile)