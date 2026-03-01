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
# |10|11|12|13|14 = Skell armor
# |15|16|17|18|19 = Skell weapon
# |20|21 = augment ground
# |22|23|24 = augment Skell
# |26 = material
# |27 = collectible
# |28 = data probe
# |29 = important item
# |30 = appendage fragment
# |31 = consumable
# |64 = holofigure
# |65 = blueprint
# |66 = info
# |70 = pet

def FullValTable(GearOpt, GemOpt, SkellGemOpt, MaterOpt, CollOpt, ProbeOpt, PreciousOpt):
    valTable = Values.ValueTable(path = "XCXDE/JsonOutputs/common")
    
    GearWeight = Values.WeightOptionMethod(GearOpt) / 7 # Divide the weight by seven because they use the same weight option to balance it
    valTable.PopulateValues(Values.ValueFile("AMR_PcList"), IDs.HeadIDs, GearWeight, 1)
    valTable.PopulateValues(Values.ValueFile("AMR_PcList"), IDs.BodyIDs, GearWeight, 2)
    valTable.PopulateValues(Values.ValueFile("AMR_PcList"), IDs.ArmRIDs, GearWeight, 3)
    valTable.PopulateValues(Values.ValueFile("AMR_PcList"), IDs.ArmLIDs, GearWeight, 4)
    valTable.PopulateValues(Values.ValueFile("AMR_PcList"), IDs.LegIDs, GearWeight, 5)
    valTable.PopulateValues(Values.ValueFile("WPN_PcList"), IDs.RangedWeaponIDs, GearWeight, 6)
    valTable.PopulateValues(Values.ValueFile("WPN_PcList"), IDs.MeleeWeaponIDs, GearWeight, 7)
    valTable.PopulateValues(Values.ValueFile("BTL_ItemSkill_inner"), IDs.GroundAugmentsIDs, Values.WeightOptionMethod(GemOpt), 20)
    valTable.PopulateValues(Values.ValueFile("BTL_ItemSkill_doll"), IDs.SkellAugmentsIDs, Values.WeightOptionMethod(SkellGemOpt), 22)
    valTable.PopulateValues(Values.ValueFile("ITM_MaterialList"), IDs.MaterialIDs, Values.WeightOptionMethod(MaterOpt), 26)
    valTable.PopulateValues(Values.ValueFile("ITM_CollectList"), IDs.CollectibleIDs, Values.WeightOptionMethod(CollOpt), 27)
    valTable.PopulateValues(Values.ValueFile("ITM_BeaconList"), IDs.ProbeIDs, Values.WeightOptionMethod(ProbeOpt), 28)
    valTable.PopulateValues(Values.ValueFile("ITM_PreciousList", "UI2"), IDs.PreciousItemIDs, Values.WeightOptionMethod(PreciousOpt), 29)
    # valTable.PopulateValues(Values.ValueFile("AMR_DlList"), IDs.SkellArmorIDs, Values.WeightOptionMethod(Options.TboxOption_SkellGear))
    return valTable

def SelectValuedMemberWithCategory(valTable:Values.ValueTable, slot, key, catKey):
    '''Xenoblade X requires a category to be given in all item slots, to know what bdat table the ID refers to'''
    chosen = valTable.SelectValuedMember(slot, key, IDs.PreciousItemIDs, catKey)
    if chosen != None: # SelectValuedMember can fail inside the function 
        slot[catKey] = chosen.category

def TicketShop():
    valTable = FullValTable(Options.TicketExchangeOption_Gear, Options.TicketExchangeOption_Gems, Options.TicketExchangeOption_SkellGems, Options.TicketExchangeOption_Materials, Options.TicketExchangeOption_Collectibles, Options.TicketExchangeOption_Probes, Options.TicketExchangeOption_Precious)
    with open(f"XCXDE/JsonOutputs/common/ITM_TradeList.json", 'r+', encoding='utf-8') as tradFile:
        tradData = json.load(tradFile)
        for trad in tradData["rows"]:
            SelectValuedMemberWithCategory(valTable, trad, "ItemID", "ItemType")
        JSONParser.CloseFile(tradData, tradFile)


def Tbox():
    valTable = FullValTable(Options.TboxOption_Gear, Options.TboxOption_Gems, Options.TboxOption_SkellGems, Options.TboxOption_Materials, Options.TboxOption_Collectibles, Options.TboxOption_Probes, Options.TboxOption_Precious)
    multChoices = [.5, .7, .9, 1.2, 1.5, 1.7, 2.5, 5]
    
    # Randomization
    with open(f"XCXDE/JsonOutputs/common/FLD_TboxAll.json", 'r+', encoding='utf-8') as tboxFile:
        tboxData = json.load(tboxFile)
        for box in tboxData["rows"]:
            if box["item_id"] != 0: # Not all boxes have items some have gold, exp, bp
                SelectValuedMemberWithCategory(valTable, box, "item_id", "item_cat")
            else:
                for key in ["money", "innerExp", "battlePoint"]:   # Apply random mults to the money exp or bp 
                    if box[key] != 0:
                        box[key] = int(box[key] * random.choice(multChoices))
                        break
        JSONParser.CloseFile(tboxData, tboxFile)
