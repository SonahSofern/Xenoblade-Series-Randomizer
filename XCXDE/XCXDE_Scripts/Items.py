import json, random
from scripts import JSONParser, Helper, PopupDescriptions, Values
from  XCXDE.XCXDE_Scripts import Options, IDs

# Categories:
# Head 1
# Body 2
# ArmR 3
# ArmL 4
# Leg 5
# Ranged Weap 6
# Melee Weap 7
# Unknown 15
# Ground Gem 20
# Ground Gem 21
# Skell Gem 22
# Skell Gem 23
# Skell Gem 24
# Unknown 25
# Materials (Enemy Drops) 26
# Collectibles 27
# Probes 28
# Precious 29
# Schematic 65


def Tbox():
    valTable = Values.ValueTable(path = "XCXDE/JsonOutputs/common")
    
    GearWeight = Values.WeightOptionMethod(Options.TboxOption_Gear) / 7 # Divide the weight by seven because they use the same weight option to balance it
    valTable.PopulateValues(Values.ValueFile("AMR_PcList"), IDs.HeadIDs, GearWeight, 1)
    valTable.PopulateValues(Values.ValueFile("AMR_PcList"), IDs.BodyIDs, GearWeight, 2)
    valTable.PopulateValues(Values.ValueFile("AMR_PcList"), IDs.ArmRIDs, GearWeight, 3)
    valTable.PopulateValues(Values.ValueFile("AMR_PcList"), IDs.ArmLIDs, GearWeight, 4)
    valTable.PopulateValues(Values.ValueFile("AMR_PcList"), IDs.LegIDs, GearWeight, 5)
    valTable.PopulateValues(Values.ValueFile("WPN_PcList"), IDs.RangedWeaponIDs, GearWeight, 6)
    valTable.PopulateValues(Values.ValueFile("WPN_PcList"), IDs.MeleeWeaponIDs, GearWeight, 7)
    valTable.PopulateValues(Values.ValueFile("BTL_ItemSkill_inner"), IDs.GroundAugmentsIDs, Values.WeightOptionMethod(Options.TboxOption_Gems), 20)
    valTable.PopulateValues(Values.ValueFile("BTL_ItemSkill_doll"), IDs.SkellAugmentsIDs, Values.WeightOptionMethod(Options.TboxOption_SkellGems), 22)
    valTable.PopulateValues(Values.ValueFile("ITM_MaterialList"), IDs.MaterialIDs, Values.WeightOptionMethod(Options.TboxOption_Materials), 26)
    valTable.PopulateValues(Values.ValueFile("ITM_CollectList"), IDs.CollectibleIDs, Values.WeightOptionMethod(Options.TboxOption_Collectibles), 27)
    valTable.PopulateValues(Values.ValueFile("ITM_BeaconList"), IDs.ProbeIDs, Values.WeightOptionMethod(Options.TboxOption_Probes), 28)
    valTable.PopulateValues(Values.ValueFile("ITM_PreciousList", "UI2"), IDs.PreciousItemIDs, Values.WeightOptionMethod(Options.TboxOption_Precious), 29)
    # valTable.PopulateValues(Values.ValueFile("AMR_DlList"), IDs.SkellArmorIDs, Values.WeightOptionMethod(Options.TboxOption_SkellGear))

    multChoices = [.5, .7, .9, 1.2, 1.5, 1.7, 2.5, 5]
    
    # Randomization
    with open(f"XCXDE/JsonOutputs/common/FLD_TboxAll.json", 'r+', encoding='utf-8') as tboxFile:
        tboxData = json.load(tboxFile)
        for box in tboxData["rows"]:
            if box["item_id"] != 0: # Not all boxes have items some have gold, exp, bp
                chosen = valTable.SelectValuedMember(box, "item_id", IDs.PreciousItemIDs)
                if chosen != None: # SelectValuedMember can fail inside the function 
                    box["item_cat"] = chosen.category
            else:
                for key in ["money", "innerExp", "battlePoint"]:   # Apply random mults to the money exp or bp 
                    if box[key] != 0:
                        box[key] = int(box[key] * random.choice(multChoices))
                        break
        JSONParser.CloseFile(tboxData, tboxFile)
