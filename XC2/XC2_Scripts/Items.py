from XC2.XC2_Scripts import Options, IDs
import json, random
from scripts import Helper, PopupDescriptions, JSONParser, Values

valTable = Values.ValueTable()

def RandomizeAccessoryShops():
    AbyssVest = [1]
    RandomizeNormalShops(IDs.BaseGameAccessoryShopIDs, IDs.AccessoryIDs, AbyssVest)
    RandomizeNormalShops(IDs.TornaAccessoryShopIDs, IDs.AccessoryIDs + IDs.TornaAccessories)

def RandomizePouchItemShops():
    RandomizeNormalShops(IDs.BaseGamePouchShopIDs, IDs.PouchItems)
    
def RandomizeWeaponChipShops():
    RandomizeNormalShops(IDs.BaseGameWeaponChipShopIDs + IDs.TornaWeaponChipShopIDs, IDs.WeaponChipIDs)

def RandomizeNormalShops(shopIDs, allowedIDs, doNotReplaceIDs = []):    
    with open("XC2/JsonOutputs/common/MNU_ShopNormal.json", 'r+', encoding='utf-8') as shopFile:
        shopData = json.load(shopFile)
        for shop in shopData["rows"]:
            
            if shop["$id"] not in shopIDs:
                continue
                
            for i in range(1,11):
                ReplaceWithSimilarValueItem(shop, f"DefItem{i}", [allowedIDs], doNotReplaceIDs)
                
            for j in range(1,6):
                ReplaceWithSimilarValueItem(shop, f"Addtem{j}", [allowedIDs], doNotReplaceIDs)
                            
        JSONParser.CloseFile(shopData, shopFile)

def RandomizeTreasureBoxes():
    sharedArgs = [(IDs.AuxCoreIDs, Options.TreasureChestOption_AuxCores.GetSpinbox()), (IDs.RefinedAuxCoreIDs, Options.TreasureChestOption_RefinedAuxCores.GetSpinbox()), (IDs.WeaponChipIDs, Options.TreasureChestOption_WeaponChips.GetSpinbox()), (IDs.CoreCrystals, Options.TreasureChestOption_CoreCrystals)]
    RandomizeTreasureBoxesHelper(IDs.ValidTboxMapNames, IDs.PreciousItems, sharedArgs + [(IDs.AccessoryIDs, Options.TreasureChestOption_Accessories.GetSpinbox())])
    RandomizeTreasureBoxesHelper(IDs.ValidTornaTboxMapNames, IDs.TornaPreciousIDs, sharedArgs + [(IDs.AccessoryIDs + IDs.TornaAccessories, Options.TreasureChestOption_Accessories.GetSpinbox())])

def RandomizeTreasureBoxesHelper(areas, dontChangeIDs, itemCategories = []):
    for area in areas:        
        with open(area, 'r+', encoding='utf-8') as tboxFile:
            tboxData = json.load(tboxFile)
            for box in tboxData["rows"]:
                for i in range(1,9):
                    ReplaceWithSimilarValueItem(box, f"itm{i}ID", itemCategories, dontChangeIDs)
                
            
                # areaBoxes.append(goldVal)
                # box["RSC_ID"] = GetRarity(originalGoldVal - goldVal) # based on median values of the area
                
            JSONParser.CloseFile(tboxData, tboxFile)

def RandomizeEnemyDrops(): # Up top here we define the RandomGroups instead of just the IDs cause we want to use random groups
    FerisBeastmeat = [30380]
    sharedArgs = [(IDs.AuxCoreIDs, Options.EnemyDropOption_AuxCores.GetSpinbox()), (IDs.RefinedAuxCoreIDs, Options.EnemyDropOption_RefinedAuxCores.GetSpinbox()), (IDs.WeaponChipIDs, Options.EnemyDropOption_WeaponChips.GetSpinbox()), (IDs.CoreCrystals, Options.EnemyDropOption_CoreCrystals)]
    RandomizeEnemyDropsHelper(IDs.BaseDropTableIDs, IDs.PreciousItems, sharedArgs + [(IDs.AccessoryIDs, Options.EnemyDropOption_Accessories.GetSpinbox())])
    RandomizeEnemyDropsHelper(IDs.TornaDropTableIDs, IDs.TornaPreciousIDs + FerisBeastmeat, sharedArgs + [(IDs.AccessoryIDs + IDs.TornaAccessories, Options.EnemyDropOption_Accessories.GetSpinbox())])

def RandomizeEnemyDropsHelper(dropIDs, dontChangeIDs, itemCategories = []):
    with open("XC2/JsonOutputs/common/BTL_EnDropItem.json", 'r+', encoding='utf-8') as dropFile:
        dropData = json.load(dropFile)
        for drop in dropData["rows"]:
            for i in range(1,9):
                ReplaceWithSimilarValueItem(drop, f"ItemID{i}", itemCategories, dontChangeIDs)
            
        JSONParser.CloseFile(dropData, dropFile)

def ReplaceWithSimilarValueItem(ogItem, key, validReplacementIDs = [], doNotReplaceIDs = []):
    
    if valTable.isEmpty():
        PopulateValueCalcXC2()
    
    if ogItem in doNotReplaceIDs:
        return
        
    valuedOgItem:Values.ValuedItem = valTable.GetByID(ogItem[key])
    
    replacementCategory = random.choices(validReplacementIDs, [], k=1)
    
    # Need to filter the valTable to get only what we want (But that might be bad performance to do every call of this maybe filtering happens above)
    # Involve weights and choose from item type not a combined list (since some have way more than others)
    
def PopulateValueCalcXC2():
    files = [
        Values.ValueFile("ITM_Orb"),
        Values.ValueFile("ITM_OrbEquip"),
        Values.ValueFile("ITM_PcEquip"),
        Values.ValueFile("ITM_PreciousList", mult=2),
        Values.ValueFile("ITM_PreciousListIra", mult=2),
        Values.ValueFile("ITM_SalvageList"),
        Values.ValueFile("ITM_TresureList"),
        Values.ValueFile("ITM_PcWpnChip", mult=5),
        Values.ValueFile("ITM_CrystalList"),
        Values.ValueFile("ITM_BoosterList"),
        Values.ValueFile("ITM_CollectionList"),
        Values.ValueFile("ITM_FavoriteList"),
        Values.ValueFile("ITM_HanaAssist", key="NeedEther", mult=2),
        Values.ValueFile("ITM_HanaArtsEnh", key="NeedEther", mult=2),
        Values.ValueFile("ITM_HanaAtr", key="NeedEther", mult=2),
        Values.ValueFile("ITM_HanaNArtsSet", key="NeedEther", mult=2),
        Values.ValueFile("ITM_HanaRole", key="NeedEther", mult=3),
        Values.ValueFile("ITM_InfoList"),  
    ]
    for file in files:
        valTable.PopulateValues(file)

def GetTreasureBoxValue(tbox):
    totalVal = 0
    
    # Gold
    avgGold = (tbox["goldMin"] + tbox["goldMax"])/2
    totalVal += avgGold
    
    # Items
    for i in range(1,9):
        itemID = tbox[f"itm{i}ID"]
        
        if itemID == 0: # Ignore empty slots
            continue
        
        item:Values.ValuedItem = valTable.GetByID(itemID)
        if item:
            amount = tbox[f"itm{i}Num"]
            totalVal += (item.value * amount)

    return int(totalVal)    

def CreateCTMCDescriptions(): # Hardcoded New Boxes and descriptions
    class CreditRarityRelation():
        def __init__(self, name, rscId, msId):
            self.name = name
            self.rscId = rscId # RSC ID of the chest
            self.msId = msId
    
    Common = CreditRarityRelation("Common", 1, 154)
    Rare = CreditRarityRelation("Rare", 2, 155)
    Legendary = CreditRarityRelation("Legendary", 3, 156)
    
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
    if gold < 5000:
        return 1
    elif gold < 10000:
        return 2
    else:
        return 3

def TreasureChestDescription():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.TreasureChestOption.name)
    myDesc.Text("This option randomizes a % of all non-key items in Treasure Chests into the types of items chosen from suboptions.")
    myDesc.Text("If no sub-options are selected this will do nothing.")
    myDesc.Image("TreasureChest.png", "XC2")
    myDesc.Header(Options.CustomCoreCrystalOption.name)
    myDesc.Text("When enabled, a percentage of all the chests in the game (chosen by the spinbox) will have a randomly chosen Custom Core Crystal in them.\n\nThese Custom Core Crystals will be named after the blade inside.")
    myDesc.Image("Custom Core Crystals.png", "XC2", 700)
    return myDesc

def PouchItemShopDesc():
    desc = PopupDescriptions.Description()
    desc.Header(Options.PouchItemShopOption.name)
    # Insert image of accessory shop icon
    desc.Text("This option randomizes a % of all items in Pouch Item Shops into the types of items chosen from suboptions.")
    desc.Text("If no sub-options are selected this will do nothing.")
    desc.Image("PouchItemShops.png", "XC2")
    return desc

def WeaponChipDesc():
    desc = PopupDescriptions.Description()
    desc.Header(Options.WeaponChipShopOption.name)
    desc.Text("Randomizes all chips in each weapon chip shop.\nTheir price is tied to the chip not the shop.")
    desc.Image("WeaponChipRando.png", "XC2", 800)
    desc.Text("This often makes the game very easy as weapon chips are one of the most important things in damage calculations.")
    return desc

def CollectionPointDescriptions():
    desc = PopupDescriptions.Description()
    desc.Header(Options.CollectionPointsOption.name)
    # Insert image of accessory shop icon
    desc.Text("This option randomizes a % of all non-key items in Collection Points into the types of items chosen from suboptions.")
    desc.Text("If no sub-options are selected this will do nothing.")
    desc.Image("ColPointIcon.png", "XC2")
    return desc