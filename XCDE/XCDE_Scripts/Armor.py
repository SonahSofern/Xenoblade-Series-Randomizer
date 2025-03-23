import Options, json

def ArmorRando():
    isRemoveStartingGear = Options.EquipmentOption_RemoveStartingEq.GetState()
    removeStartingGearCharacters = [1,2,3,4,5,6,7,8]
    with open("./XCDE/_internal/JsonOutputs/bdat_common/BTL_pclist.json", 'r+', encoding='utf-8') as charFile:
        charData = json.load(charFile)
        for char in charData["rows"]:
            
            if isRemoveStartingGear and (char["$id"] in removeStartingGearCharacters):
                char["def_head"] = 0
                char["def_body"] = 0
                char["def_arm"] = 0
                char["def_waist"] = 0
                char["def_legg"] = 0

        charFile.seek(0)
        charFile.truncate()
        json.dump(charData, charFile, indent=2, ensure_ascii=False)
    
