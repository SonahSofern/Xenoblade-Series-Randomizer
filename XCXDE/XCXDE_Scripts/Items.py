import json, random, copy
from scripts import JSONParser, Values, PopupDescriptions
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

fullValTable:Values.ValueTable = None

def FullValTable(GearOpt, SkellGearOpt, GemOpt, SkellGemOpt, MaterOpt, CollOpt, ProbeOpt, PreciousOpt, MiscOpt):
    global fullValTable
    if fullValTable == None:
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
        
        MiscWeight = Values.WeightOptionMethod(MiscOpt) / 6 # Divide the weight by six because they use the same weight option to balance it
        valTable.PopulateValues(Values.ValueFile("ITM_PieceList"), IDs.AppendageFragIDs, MiscWeight, 30)
        valTable.PopulateValues(Values.ValueFile("ITM_BattleItem"), IDs.ConsumableIDs, MiscWeight, 31)
        valTable.PopulateValues(Values.ValueFile("ITM_FigList"), IDs.HolofigureIDs, MiscWeight, 64)
        valTable.PopulateValues(Values.ValueFile("ITM_Blueprint", "miraniumu", 3), IDs.BlueprintIDs, MiscWeight, 65)
        valTable.PopulateValues(Values.ValueFile("ITM_InfoList", "category", 500), IDs.InfoIDs, MiscWeight, 66)
        valTable.PopulateValues(Values.ValueFile("BLH_PetList", "FLAG"), IDs.InfoIDs, MiscWeight, 70)
        fullValTable = copy.deepcopy(valTable)
    else:
        valTable = copy.deepcopy(fullValTable)
        
    return valTable

def TicketShop():
    valTable = FullValTable(Options.TicketExchangeOption_Gear, Options.TicketExchangeOption_SkellGear, Options.TicketExchangeOption_Gems, Options.TicketExchangeOption_SkellGems, Options.TicketExchangeOption_Materials, Options.TicketExchangeOption_Collectibles, Options.TicketExchangeOption_Probes, Options.TicketExchangeOption_Precious, Options.TicketExchangeOption_Misc)
    tradFile = JSONParser.File("XCXDE/JsonOutputs/common/ITM_TradeList.json")
    for trad in tradFile.rows:
        valTable.SelectValuedMember(trad, "ItemID", catKey="ItemType")
    tradFile.Close()


def Tbox():
    valTable = FullValTable(Options.TboxOption_Gear, Options.TboxOption_SkellGear, Options.TboxOption_Gems, Options.TboxOption_SkellGems, Options.TboxOption_Materials, Options.TboxOption_Collectibles, Options.TboxOption_Probes, Options.TboxOption_Precious, Options.TboxOption_Misc)
    multChoices = [.5, .7, .9, 1.2, 1.5, 1.7, 2.5, 5]
    
    # Randomization
    tboxFile = JSONParser.File("XCXDE/JsonOutputs/common/FLD_TboxAll.json")
    for box in tboxFile.rows:
        if box["item_id"] != 0: # Not all boxes have items some have gold, exp, bp
            valTable.SelectValuedMember(box, "item_id", IDs.PreciousItemIDs,  "item_cat")
        else:
            for key in ["money", "innerExp", "battlePoint"]:   # Apply random mults to the money exp or bp 
                if box[key] != 0:
                    box[key] = int(box[key] * random.choice(multChoices))
                    break
    tboxFile.Close()
    
def TboxDescription(name):
    tboxDesc = PopupDescriptions.Description()
    tboxDesc.Header(name)
    tboxDesc.Text(f"The rewards for field checks are randomized")
    tboxDesc.Image("fieldchecks.png", "XCXDE", 700)
    return tboxDesc


def QuestRewards(): # DOuble check precious rewards skell liscense exam not woring
    valTable = FullValTable(Options.QuestRewardOption_Gear, Options.QuestRewardOption_SkellGear, Options.QuestRewardOption_Gems, Options.QuestRewardOption_SkellGems, Options.QuestRewardOption_Materials, Options.QuestRewardOption_Collectibles, Options.QuestRewardOption_Probes, Options.QuestRewardOption_Precious, Options.QuestRewardOption_Misc)
    multChoices = [.7, .9, 1.2, 1.5, 1.7]
    
    # Randomization
    with open(f"XCXDE/JsonOutputs/common/QUEST_itemset.json", 'r+', encoding='utf-8') as qstRewardFile:
        qstRewardData = json.load(qstRewardFile)
        for qstRew in qstRewardData["rows"]:
            for i in range(1,5):
                valTable.SelectValuedMember(qstRew, f"item_id{i}", IDs.PreciousItemIDs,  f"ref_item_bdat_{i}")

        for key in ["money", "exp", "friend_point"]:   # Apply random mults to the money exp or bp 
            qstRew[key] = int(qstRew[key] * random.choice(multChoices))
        JSONParser.CloseFile(qstRewardData, qstRewardFile)

def CollectapediaRewards():
    valTable = FullValTable(Options.CollectapediaRewardOption_Gear, Options.CollectapediaRewardOption_SkellGear, Options.CollectapediaRewardOption_Gems, Options.CollectapediaRewardOption_SkellGems, Options.CollectapediaRewardOption_Materials, Options.CollectapediaRewardOption_Collectibles, Options.CollectapediaRewardOption_Probes, Options.CollectapediaRewardOption_Precious, Options.CollectapediaRewardOption_Misc)
    multChoices = [1.2, 1.5, 1.7, 3.4]
    
    # Randomization
    with open(f"XCXDE/JsonOutputs/common/collepediareward.json", 'r+', encoding='utf-8') as colRewardFile:
        colRewardData = json.load(colRewardFile)
        for colRew in colRewardData["rows"]:
            valTable.SelectValuedMember(colRew, "Item_ID", catKey="Lgroup")

        for key in ["battlePoint"]: 
            colRew[key] = int(colRew[key] * random.choice(multChoices))
        JSONParser.CloseFile(colRewardData, colRewardFile)
        
def EnemyDrops():
    valTable = FullValTable(Options.CollectapediaRewardOption_Gear, Options.CollectapediaRewardOption_SkellGear, Options.CollectapediaRewardOption_Gems, Options.CollectapediaRewardOption_SkellGems, Options.CollectapediaRewardOption_Materials, Options.CollectapediaRewardOption_Collectibles, Options.CollectapediaRewardOption_Probes, Options.CollectapediaRewardOption_Precious, Options.CollectapediaRewardOption_Misc)
    
    for boxType in ["Bronze", "Silver", "Gold"]:
        # Randomization
        with open(f"XCXDE/JsonOutputs/common/DRP_{boxType}BoxTable.json", 'r+', encoding='utf-8') as boxFile:
            boxData = json.load(boxFile)
            for box in boxData["rows"]:
                for i in range(1,13):
                    if i > 8 and boxType == "Bronze":
                        break
                    valTable.SelectValuedMember(box, f"Item_{i:02}")
            JSONParser.CloseFile(boxData, boxFile)