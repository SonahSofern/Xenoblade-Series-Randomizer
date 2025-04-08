import Options, json, random

def ArmorRando():
    isRemoveStartingGear = Options.EquipmentOption_RemoveStartingEq.GetState()
    isAppearance = Options.EquipmentOption_Appearance.GetState()
    
    if isRemoveStartingGear:
        RemoveStartingGear()
    
    if isAppearance:
        GearAppearance()
   

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
                    

            armFile.seek(0)
            armFile.truncate()
            json.dump(armData, armFile, indent=2, ensure_ascii=False)

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