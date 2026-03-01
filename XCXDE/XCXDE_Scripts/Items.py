import json, random
from scripts import JSONParser, Helper, PopupDescriptions, Values
from  XCXDE.XCXDE_Scripts import Options, IDs

# Head 1
# Body 2
# ArmR 3
# ArmL 4
# Leg 5
# Ranged Weap 6
# Melee Weap 7

# Ground Gem 20
# Ground Gem 21
# Skell Gem 22
# Skell Gem 23
# Skell Gem 24
# Probes 28
# Precious 29

# Schematic 65

# 25,26,27 Unknown (Theres like 10 items total with this type idk what their ids link to)


def Tbox():
    valTable = Values.ValueTable(path = "XCXDE/JsonOutputs/common")
    valTable.PopulateValues(Values.ValueFile("AMR_PcList"), IDs.ArmorIDs, Values.WeightOptionMethod(Options.TboxOption_Gear))
    valTable.PopulateValues(Values.ValueFile("WPN_PcList"), IDs.RangedWeaponIDs, Values.WeightOptionMethod(Options.TboxOption_Gear), 6)
    valTable.PopulateValues(Values.ValueFile("WPN_PcList"), IDs.MeleeWeaponIDs, Values.WeightOptionMethod(Options.TboxOption_Gear), 7)
    # valTable.PopulateValues(Values.ValueFile("AMR_DlList"), IDs.SkellArmorIDs, Values.WeightOptionMethod(Options.TboxOption_SkellGear))

    multChoices = [.5, .7, .9, 1.2, 1.5, 1.7, 2.5, 5]
    
    # Randomization
    with open(f"XCXDE/JsonOutputs/common/FLD_TboxAll.json", 'r+', encoding='utf-8') as tboxFile:
        tboxData = json.load(tboxFile)
        for box in tboxData["rows"]:
            if box["item_id"] != 0: # Not all boxes have items some have gold, exp, bp
                chosen = valTable.SelectValuedMember(box, "item_id", IDs.PreciousItemIDs)
                box["item_cat"] = chosen.category
            else:
                for key in ["money", "innerExp", "battlePoint"]:   # Apply random mults to the money exp or bp 
                    if box[key] != 0:
                        box[key] = int(box[key] * random.choice(multChoices))
                        break
        JSONParser.CloseFile(tboxData, tboxFile)
