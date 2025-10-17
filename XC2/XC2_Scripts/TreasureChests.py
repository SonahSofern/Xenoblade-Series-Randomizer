from XC2.XC2_Scripts import Options, IDs
import json, random
from scripts import Helper, PopupDescriptions, JSONParser

# Rework this rando to be a balanced version of tbox rando (Should make it a system applicable to anything item related so we can balance the entire game and other games too)

valueDict = {}

def PopulateValue(file, key = "Price", mult = 1):
    '''
    Adds dictionary items linking every ITM with a gold value
    This value is useful to balance loot drops
    '''
    with open(f"XC2/JsonOutputs/common/{file}.json", 'r+', encoding='utf-8') as curFile:
        curData = json.load(curFile)
        for data in curData["rows"]:
            valueDict[data["$id"]] = int(data[key] * mult)

def PopulateAll():
    PopulateValue("ITM_Orb")
    PopulateValue("ITM_OrbEquip")
    PopulateValue("ITM_PcEquip")
    PopulateValue("ITM_PreciousList")
    PopulateValue("ITM_PreciousListIra")
    PopulateValue("ITM_SalvageList")
    PopulateValue("ITM_TresureList")
    PopulateValue("ITM_PcWpnChip", mult=5)
    PopulateValue("ITM_CrystalList")
    PopulateValue("ITM_BoosterList")
    PopulateValue("ITM_CollectionList")
    PopulateValue("ITM_FavoriteList")
    PopulateValue("ITM_HanaAssist", key="NeedEther", mult=2)
    PopulateValue("ITM_HanaArtsEnh", key="NeedEther", mult=2)
    PopulateValue("ITM_HanaAtr", key="NeedEther", mult=2)
    PopulateValue("ITM_HanaNArtsSet", key="NeedEther", mult=2)
    PopulateValue("ITM_HanaRole", key="NeedEther", mult=3)
    PopulateValue("ITM_InfoList")

def EvaluateTboxGoldValue(tbox):
    totalGold = 0
    
    # Gold
    avgGold = (tbox["goldMin"] + tbox["goldMax"])/2
    totalGold += avgGold
    
    # Items
    for i in range(1,9):
        if tbox[f"itm{i}ID"] in valueDict:
            itemVal = valueDict[tbox[f"itm{i}ID"]]
            amount = tbox[f"itm{i}Num"]
            totalGold += (itemVal * amount)
        
    return totalGold    
  
def TreasureBoxRando():
    SetBoxDescriptions()
    PopulateAll()
    for area in IDs.MajorAreaIds:
        areaBoxes = []
        try:
            with open(f"XC2/JsonOutputs/common_gmk/ma{area}a_FLD_TboxPop.json", 'r+', encoding='utf-8') as tboxFile:
                tboxData = json.load(tboxFile)
                for box in tboxData["rows"]:
                    goldVal = int(EvaluateTboxGoldValue(box))
                    areaBoxes.append(goldVal)
                
                for box in tboxData["rows"]:
                    box["RSC_ID"] = GetRarity(goldVal) # based on median values of the area
                    
                JSONParser.CloseFile(tboxData, tboxFile)
        except Exception as e:
            print(e)
    
def SetBoxDescriptions(): # Hardcoded New Boxes and descriptions
    class CreditRarityRelation():
        def __init__(self, name, rscId, credits, msId):
            self.name = name
            self.rscId = rscId # RSC ID of the chest
            self.credits = credits # credits to belong to this category
            self.msId = msId
    
    Common = CreditRarityRelation("Common", 1, 100, 154)
    Rare = CreditRarityRelation("Rare", 2, 200, 155)
    Legendary = CreditRarityRelation("Legendary", 3, 300, 156)
    
    with open("XC2/JsonOutputs/common_ms/fld_gmkname.json", 'r+', encoding='utf-8') as nameFile:
        nameData = json.load(nameFile)
        nameData["rows"].append({"$id": Common.msId, "style": 36, "name": Common.name})
        nameData["rows"].append({"$id": Rare.msId, "style": 36, "name": Rare.name})
        nameData["rows"].append({"$id": Legendary.msId, "style": 36, "name": Legendary.name})
        JSONParser.CloseFile(nameData, nameFile)
            
    with open("XC2/JsonOutputs/common/RSC_TboxList.json", 'r+', encoding='utf-8') as tboxFile:
        tboxData = json.load(tboxFile)
        for box in tboxData["rows"]:
            box["initWaitTimeRand"] = 0.1 # reduces wait time for chest down to 0.1 sec
            if box["$id"] == Common.rscId:
                box["MSG_ID"] = Common.msId
            elif box["$id"] == Rare.rscId:
                box["MSG_ID"] = Rare.msId
            elif box["$id"] == Legendary.rscId:
                box["MSG_ID"] = Legendary.rscId
            else:
                break
        JSONParser.CloseFile(tboxData, tboxFile)

def GetRarity(gold):
    if gold < 100:
        return 1
    elif gold > 200:
        return 2
    else:
        return 3

# def RandoTreasureBoxes():
#     ValidReplacements = []
#     if not Options.RaceModeOption.GetState(): # if race mode is on, we don't want to do any of this
#         if Options.TreasureChestOption_Accessories.GetState():
#             ValidReplacements.extend(IDs.AccessoryIDs)
#         if Options.TreasureChestOption_TornaAccessories.GetState():
#             ValidReplacements.extend(IDs.TornaAccessories)
#         if Options.TreasureChestOption_WeaponChips.GetState():
#             ValidReplacements.extend(IDs.WeaponChipIDs)
#         if Options.TreasureChestOption_AuxCores.GetState():
#             ValidReplacements.extend(IDs.AuxCoreIDs)
#         if Options.TreasureChestOption_RefinedAuxCores.GetState():
#             ValidReplacements.extend(IDs.RefinedAuxCores)
#         if Options.TreasureChestOption_CoreCrystals.GetState() and not Options.CustomCoreCrystalOption.GetState():
#                 ValidReplacements.extend(IDs.CoreCrystals)
#         if Options.TreasureChestOption_Deeds.GetState():
#             if not Options.StartwithIncreasedMovespeedOption.GetState(): # if we have the bonus movespeed starting deed on, we want to exclude it from the deeds found in chests.
#                 ValidReplacements.extend(IDs.Deeds)
#             else:
#                 ValidReplacements.extend(Helper.InclRange(25250, 25300))
#         if Options.TreasureChestOption_CollectionPointMaterials.GetState():
#             ValidReplacements.extend(IDs.CollectionPointMaterials)
#     odds = Options.TreasureChestOption.GetSpinbox()

#     if ValidReplacements == []: # In case they dont select anything
#         return
    
#     for area in IDs.MajorAreaIds:
#         try:
#             with open(f"./XC2/JsonOutputs/common_gmk/ma{area}a_FLD_TboxPop.json", 'r+', encoding='utf-8') as tboxFile:
#                 boxData = json.load(tboxFile)
#                 for box in boxData["rows"]:
#                     for i in range(1,9):
#                         if not Helper.OddsCheck(odds): # Check spinbox
#                             continue
#                         if box[f"itm{i}ID"] in [0] + IDs.PreciousItems: # Ignore empty spots in points
#                             continue
#                         box[f"itm{i}ID"] = random.choice(ValidReplacements) # Make our selection
#                 tboxFile.seek(0)
#                 tboxFile.truncate()
#                 json.dump(boxData, tboxFile, indent=2, ensure_ascii=False)
#         except:
#             pass # Ignores wrong files


def TreasureChestDescription():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.TreasureChestOption.name)
    myDesc.Text("This option randomizes a % of all non-key items in Treasure Chests into the types of items chosen from suboptions.")
    myDesc.Text("If no sub-options are selected this will do nothing.")
    myDesc.Image("TreasureChest.png", "XC2")
    return myDesc