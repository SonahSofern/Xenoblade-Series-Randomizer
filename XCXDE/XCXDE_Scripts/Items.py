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
# |20|21 = augment ground (Weapon, Armor)
# |22|23|24 = augment Skell (Weapon, Armor, Frame)
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

def FullValTable(GearOpt, SkellGearOpt, GemOpt, SkellGemOpt, MaterOpt, CollOpt, ProbeOpt, PreciousOpt, MiscOpt):
    valTable = Values.ValueTable(path = "XCXDE/JsonOutputs/common")
    
    GearWeight = Values.WeightOptionMethod(GearOpt) / 7 # Divide the weight by seven because they use the same weight option to balance it
    valTable.PopulateValues(Values.ValueFile("AMR_PcList"), IDs.HeadIDs, GearWeight, 1)
    valTable.PopulateValues(Values.ValueFile("AMR_PcList"), IDs.BodyIDs, GearWeight, 2)
    valTable.PopulateValues(Values.ValueFile("AMR_PcList"), IDs.ArmRIDs, GearWeight, 3)
    valTable.PopulateValues(Values.ValueFile("AMR_PcList"), IDs.ArmLIDs, GearWeight, 4)
    valTable.PopulateValues(Values.ValueFile("AMR_PcList"), IDs.LegIDs, GearWeight, 5)
    valTable.PopulateValues(Values.ValueFile("WPN_PcList"), IDs.RangedWeaponIDs, GearWeight, 6)
    valTable.PopulateValues(Values.ValueFile("WPN_PcList"), IDs.MeleeWeaponIDs, GearWeight, 7)
    
    SkellGearWeight = Values.WeightOptionMethod(SkellGearOpt) / 10
    valTable.PopulateValues(Values.ValueFile("AMR_DlList"), IDs.SkellHeadIDs, SkellGearWeight, 10)
    valTable.PopulateValues(Values.ValueFile("AMR_DlList"), IDs.SkellBodyIDs, SkellGearWeight, 11)
    valTable.PopulateValues(Values.ValueFile("AMR_DlList"), IDs.SkellArmRIDs, SkellGearWeight, 12)
    valTable.PopulateValues(Values.ValueFile("AMR_DlList"), IDs.SkellArmLIDs, SkellGearWeight, 13)
    valTable.PopulateValues(Values.ValueFile("AMR_DlList"), IDs.SkellLegIDs, SkellGearWeight, 14)
    valTable.PopulateValues(Values.ValueFile("WPN_DlList"), IDs.SkellWpnShoulderIDs, SkellGearWeight, 15)
    valTable.PopulateValues(Values.ValueFile("WPN_DlList"), IDs.SkellWpnBackIDs, SkellGearWeight, 16)
    valTable.PopulateValues(Values.ValueFile("WPN_DlList"), IDs.SkellWpnArmIDs, SkellGearWeight, 17)
    valTable.PopulateValues(Values.ValueFile("WPN_DlList"), IDs.SkellWpnSidearmIDs, SkellGearWeight, 18)
    valTable.PopulateValues(Values.ValueFile("WPN_DlList"), IDs.SkellWpnSpareIDs, SkellGearWeight, 19)
    
    valTable.PopulateValues(Values.ValueFile("BTL_ItemSkill_inner"), IDs.GroundAugmentsIDs, Values.WeightOptionMethod(GemOpt), 20)
    valTable.PopulateValues(Values.ValueFile("BTL_ItemSkill_doll"), IDs.SkellAugmentsIDs, Values.WeightOptionMethod(SkellGemOpt), 22)
    valTable.PopulateValues(Values.ValueFile("ITM_MaterialList"), IDs.MaterialIDs, Values.WeightOptionMethod(MaterOpt), 26)
    valTable.PopulateValues(Values.ValueFile("ITM_CollectList"), IDs.CollectibleIDs, Values.WeightOptionMethod(CollOpt), 27)
    valTable.PopulateValues(Values.ValueFile("ITM_BeaconList"), IDs.ProbeIDs, Values.WeightOptionMethod(ProbeOpt), 28)
    valTable.PopulateValues(Values.ValueFile("ITM_PreciousList", "UI2"), IDs.PreciousItemIDs, Values.WeightOptionMethod(PreciousOpt), 29)
    
    MiscWeight = Values.WeightOptionMethod(MiscOpt) / 6
    valTable.PopulateValues(Values.ValueFile("ITM_PieceList"), IDs.AppendageFragIDs, MiscWeight, 30)
    valTable.PopulateValues(Values.ValueFile("ITM_BattleItem"), IDs.ConsumableIDs, MiscWeight, 31)
    valTable.PopulateValues(Values.ValueFile("ITM_FigList"), IDs.HolofigureIDs, MiscWeight, 64)
    valTable.PopulateValues(Values.ValueFile("ITM_Blueprint", "miraniumu", 3), IDs.BlueprintIDs, MiscWeight, 65)
    valTable.PopulateValues(Values.ValueFile("ITM_InfoList", "category", 500), IDs.InfoIDs, MiscWeight, 66)
    valTable.PopulateValues(Values.ValueFile("BLH_PetList", "FLAG"), IDs.InfoIDs, MiscWeight, 70)
    
    return valTable

def SelectValuedMemberWithCategory(valTable:Values.ValueTable, slot, key, catKey):
    '''Xenoblade X requires a category to be given in all item slots, to know what bdat table the ID refers to'''
    chosen = valTable.SelectValuedMember(slot, key, IDs.PreciousItemIDs, catKey)
    if chosen != None: # SelectValuedMember can fail inside the function 
        slot[catKey] = chosen.category

def TicketShop():
    valTable = FullValTable(Options.TicketExchangeOption_Gear, Options.TicketExchangeOption_SkellGear, Options.TicketExchangeOption_Gems, Options.TicketExchangeOption_SkellGems, Options.TicketExchangeOption_Materials, Options.TicketExchangeOption_Collectibles, Options.TicketExchangeOption_Probes, Options.TicketExchangeOption_Precious, Options.TicketExchangeOption_Misc)
    with open(f"XCXDE/JsonOutputs/common/ITM_TradeList.json", 'r+', encoding='utf-8') as tradFile:
        tradData = json.load(tradFile)
        for trad in tradData["rows"]:
            SelectValuedMemberWithCategory(valTable, trad, "ItemID", "ItemType")
        JSONParser.CloseFile(tradData, tradFile)


def Tbox():
    valTable = FullValTable(Options.TboxOption_Gear, Options.TboxOption_SkellGear, Options.TboxOption_Gems, Options.TboxOption_SkellGems, Options.TboxOption_Materials, Options.TboxOption_Collectibles, Options.TboxOption_Probes, Options.TboxOption_Precious, Options.TboxOption_Misc)
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
