from XC2.XC2_Scripts import Options, IDs
import json, random, copy
from scripts import Helper, PopupDescriptions, JSONParser, Values


def RandomizeAccessoryShops():
    valTable = Values.ValueTable()
    valTable.PopulateValues(Values.ValueFile("ITM_PcEquip"), IDs.AccessoryIDs)
    tornaValTable = Values.ValueTable()
    tornaValTable.PopulateValues(Values.ValueFile("ITM_PcEquip"), IDs.AccessoryIDs + IDs.TornaAccessories)
    AbyssVest = [1]
    RandomizeNormalShops(IDs.BaseGameAccessoryShopIDs, valTable, AbyssVest)
    RandomizeNormalShops(IDs.TornaAccessoryShopIDs, tornaValTable)

def RandomizePouchItemShops():
    valTable = Values.ValueTable()
    valTable.PopulateValues(Values.ValueFile("ITM_FavoriteList"), IDs.PouchItems)
    RandomizeNormalShops(IDs.BaseGamePouchShopIDs, valTable)
    
def RandomizeWeaponChipShops():
    valTable = Values.ValueTable()
    valTable.PopulateValues(Values.ValueFile("ITM_PcWpnChip"), IDs.WeaponChipIDs)
    RandomizeNormalShops(IDs.BaseGameWeaponChipShopIDs + IDs.TornaWeaponChipShopIDs, valTable)

def RandomizeNormalShops(shopIDs, valTable:Values.ValueTable, doNotReplaceIDs = []):    
    with open("XC2/JsonOutputs/common/MNU_ShopNormal.json", 'r+', encoding='utf-8') as shopFile:
        shopData = json.load(shopFile)
        for shop in shopData["rows"]:
            
            if shop["$id"] not in shopIDs:
                continue
                
            for i in range(1,11):
                valTable.SelectValuedMember(shop, f"DefItem{i}", doNotReplaceIDs)
                
            for j in range(1,6):
                valTable.SelectValuedMember(shop, f"Addtem{j}", doNotReplaceIDs)
                                            
        JSONParser.CloseFile(shopData, shopFile)

def RandomizeTreasureBoxes():
    # Base Game
    valTable = Values.ValueTable()
    valTable.PopulateValues(Values.ValueFile("ITM_Orb"), IDs.AuxCoreIDs, Options.TreasureChestOption_AuxCores.GetSpinbox())
    valTable.PopulateValues(Values.ValueFile("ITM_OrbEquip"), IDs.RefinedAuxCoreIDs, Options.TreasureChestOption_RefinedAuxCores.GetSpinbox())
    valTable.PopulateValues(Values.ValueFile("ITM_PcWpnChip", mult=5), IDs.WeaponChipIDs, Options.TreasureChestOption_WeaponChips.GetSpinbox())
    
    # Torna
    tornaValTable = copy.deepcopy(valTable) # Copy it before we put in just base game accessory IDs or Core Crystals
    tornaValTable.PopulateValues(Values.ValueFile("ITM_PcEquip"), IDs.AllowedTornaAccessories, Options.TreasureChestOption_Accessories.GetSpinbox())
    
    valTable.PopulateValues(Values.ValueFile("ITM_CrystalList", mult=5), IDs.CoreCrystals, Options.TreasureChestOption_CoreCrystals.GetSpinbox())
    valTable.PopulateValues(Values.ValueFile("ITM_PcEquip"), IDs.AccessoryIDs, Options.TreasureChestOption_Accessories.GetSpinbox())
    
    RandomizeTreasureBoxesHelper(IDs.ValidTboxMapNames, IDs.PreciousItems, valTable)
    RandomizeTreasureBoxesHelper(IDs.ValidTornaTboxMapNames, IDs.TornaPreciousIDs, tornaValTable)

def RandomizeTreasureBoxesHelper(areas, dontChangeIDs, valTable:Values.ValueTable):
    for area in areas:        
        with open(area, 'r+', encoding='utf-8') as tboxFile:
            tboxData = json.load(tboxFile)
            for box in tboxData["rows"]:
                for i in range(1,9):
                    valTable.SelectValuedMember(box, f"itm{i}ID", dontChangeIDs)
            JSONParser.CloseFile(tboxData, tboxFile)

def RandomizeEnemyDrops(): # Up top here we define the RandomGroups instead of just the IDs cause we want to use random groups
    # Base Game
    valTable = Values.ValueTable()
    valTable.PopulateValues(Values.ValueFile("ITM_Orb"), IDs.AuxCoreIDs, Options.EnemyDropOption_AuxCores.GetSpinbox())
    valTable.PopulateValues(Values.ValueFile("ITM_OrbEquip"), IDs.RefinedAuxCoreIDs, Options.EnemyDropOption_RefinedAuxCores.GetSpinbox())
    valTable.PopulateValues(Values.ValueFile("ITM_PcWpnChip", mult=5), IDs.WeaponChipIDs, Options.EnemyDropOption_WeaponChips.GetSpinbox())
    valTable.PopulateValues(Values.ValueFile("ITM_CrystalList", mult=5), IDs.CoreCrystals, Options.EnemyDropOption_CoreCrystals.GetSpinbox())
    
    # Torna
    tornaValTable = copy.deepcopy(valTable) # Copy it before we put in just base game accessory IDs
    FerisBeastmeat = [30380]
    tornaValTable.PopulateValues(Values.ValueFile("ITM_PcEquip"), IDs.AllowedTornaAccessories, Options.EnemyDropOption_Accessories.GetSpinbox())
    valTable.PopulateValues(Values.ValueFile("ITM_PcEquip"), IDs.AccessoryIDs, Options.EnemyDropOption_Accessories.GetSpinbox())
    
    RandomizeEnemyDropsHelper(IDs.BaseDropTableIDs, IDs.PreciousItems, valTable)
    RandomizeEnemyDropsHelper(IDs.TornaDropTableIDs, IDs.TornaPreciousIDs + FerisBeastmeat, tornaValTable)

def RandomizeEnemyDropsHelper(dropIDs, dontChangeIDs, valTable:Values.ValueTable):
    with open("XC2/JsonOutputs/common/BTL_EnDropItem.json", 'r+', encoding='utf-8') as dropFile:
        dropData = json.load(dropFile)
    
        for drop in dropData["rows"]:
            
            if drop["$id"] not in dropIDs:
                continue
            
            for i in range(1,9):
                valTable.SelectValuedMember(drop, f"ItemID{i}", dontChangeIDs)
            
        JSONParser.CloseFile(dropData, dropFile)

def GetTreasureBoxValue(tbox, valTable:Values.ValueTable):
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

def ColoredName(name, colors):
    newName = ""
    for char in name:
        newName+= f"[System:Color name={random.choice(colors)}]{char}[/System:Color]" 
    return newName

def ChestTypeMatchesContentsValue():
    class ChestType():
        def __init__(self, name, rscId, msId):
            self.name = name
            self.rscId = rscId # RSC ID of the chest
            self.msId = msId
    
    Common = ChestType("Common", 1, 154)
    Rare = ChestType("Rare", 2, 155)
    Legendary = ChestType("Legendary", 3, 156)
    
     # Hardcoded New Boxes and descriptions
    with open("XC2/JsonOutputs/common_ms/fld_gmkname.json", 'r+', encoding='utf-8') as nameFile:
        nameData = json.load(nameFile)
        nameData["rows"].append({"$id": Common.msId, "style": 36, "name": ColoredName(Common.name, ["blue"])})
        nameData["rows"].append({"$id": Rare.msId, "style": 36, "name": ColoredName(Rare.name,["red"])})
        nameData["rows"].append({"$id": Legendary.msId, "style": 36, "name": ColoredName(Legendary.name, ["green", "red", "tutorial", "blue"] )})
        JSONParser.CloseFile(nameData, nameFile)
            
    with open("XC2/JsonOutputs/common/RSC_TboxList.json", 'r+', encoding='utf-8') as tboxFile:
        tboxData = json.load(tboxFile)
        for box in tboxData["rows"]:
            box["initWaitTimeRand"] = 0 
            box["initWaitTime"] = 0 
            box["TBOX_open_starttime"] = 0 
            if box["$id"] == Common.rscId:
                box["MSG_ID"] = Common.msId
            elif box["$id"] == Rare.rscId:
                box["MSG_ID"] = Rare.msId
            elif box["$id"] == Legendary.rscId:
                box["MSG_ID"] = Legendary.rscId
            else:
                break
        JSONParser.CloseFile(tboxData, tboxFile)
    
    valTable = Values.ValueTable()
    valTable.PopulateValues(Values.ValueFile("ITM_Orb"), IDs.AuxCoreIDs)
    valTable.PopulateValues(Values.ValueFile("ITM_OrbEquip"), IDs.RefinedAuxCoreIDs)
    valTable.PopulateValues(Values.ValueFile("ITM_PcWpnChip", mult=5), IDs.WeaponChipIDs)
    valTable.PopulateValues(Values.ValueFile("ITM_CrystalList", mult=5), IDs.CoreCrystals)
    valTable.PopulateValues(Values.ValueFile("ITM_PcEquip"), IDs.AccessoryIDs + IDs.TornaAccessories)
    
    for area in IDs.ValidTboxMapNames + IDs.ValidTornaTboxMapNames:        
        with open(area, 'r+', encoding='utf-8') as tboxFile:
            tboxData = json.load(tboxFile)
            
            # Get Area Box Value Distribution
            boxesTotalValues:list[Values.ValuedItem] = []
            for box in tboxData["rows"]:
                boxesTotalValues.append(Values.ValuedItem(box["$id"], GetTreasureBoxValue(box, valTable)))
                        
            boxesTotalValues.sort(key=lambda x: x.value)
            
            # Assign rarities based on percentile in the sorted list
            for i, box in enumerate(boxesTotalValues):
                percentile = i / len(boxesTotalValues)
                
                if percentile > 0.8:
                    rarity = Legendary
                elif percentile > 0.5:
                    rarity = Rare
                else:
                    rarity = Common
                
                for tbox in tboxData["rows"]:
                    if tbox["$id"] == box.id:
                        tbox["RSC_ID"] = rarity.rscId
                # print(f"Value: {box.value} given rarity: {rarity.name}")
                
            JSONParser.CloseFile(tboxData, tboxFile)

def TreasureChestDescription():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.TreasureChestOption.name)
    myDesc.Text("This option randomizes a % of all non-key items in Treasure Chests into the types of items chosen from suboptions.")
    myDesc.Text("If no sub-options are selected this will do nothing.")
    myDesc.Image("TreasureChest.png", "XC2")
    myDesc.Header(Options.TreasureChestOption_RareBlades.name)
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

def AccessoryShopDescription():
    desc = PopupDescriptions.Description()
    desc.Header(Options.AccessoryShopsOption.name)
    desc.Text("This option randomizes a % of all non-key items in Accessory Shops into the types of items chosen from suboptions.")
    desc.Text("If no sub-options are selected this will do nothing.")
    desc.Image("AccessoryShopIcon.png", "XC2")
    return desc

def CollectionPointDescriptions():
    desc = PopupDescriptions.Description()
    desc.Header(Options.CollectionPointsOption.name)
    # Insert image of accessory shop icon
    desc.Text("This option randomizes a % of all non-key items in Collection Points into the types of items chosen from suboptions.")
    desc.Text("If no sub-options are selected this will do nothing.")
    desc.Image("ColPointIcon.png", "XC2")
    return desc
