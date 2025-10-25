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
    valTable.PopulateValues(Values.ValueFile("ITM_OrbEquip"), IDs.RefinedAuxCoreIDs, Values.WeightOptionMethod(Options.TreasureChestOption_RefinedAuxCores))
    valTable.PopulateValues(Values.ValueFile("ITM_PcWpnChip", mult=5), IDs.WeaponChipIDs, Values.WeightOptionMethod(Options.TreasureChestOption_WeaponChips))
    
    # Torna
    tornaValTable = copy.deepcopy(valTable) # Copy it before we put in just base game accessory IDs or Core Crystals
    tornaValTable.PopulateValues(Values.ValueFile("ITM_PcEquip"), IDs.AllowedTornaAccessories, Values.WeightOptionMethod(Options.TreasureChestOption_Accessories))
    
    valTable.PopulateValues(Values.ValueFile("ITM_Orb"), IDs.AuxCoreIDs, Values.WeightOptionMethod(Options.TreasureChestOption_AuxCores))
    valTable.PopulateValues(Values.ValueFile("ITM_CrystalList", mult=5), IDs.CoreCrystals, Values.WeightOptionMethod(Options.TreasureChestOption_CoreCrystals))
    valTable.PopulateValues(Values.ValueFile("ITM_PcEquip"), IDs.AccessoryIDs, Values.WeightOptionMethod(Options.TreasureChestOption_Accessories))
    valTable.PopulateValues(Values.ValueFile("ITM_CrystalList"), IDs.CustomCrystalIDs, Values.WeightOptionMethod(Options.TreasureChestOption_RareBlades))
    
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
    valTable.PopulateValues(Values.ValueFile("ITM_OrbEquip"), IDs.RefinedAuxCoreIDs, Values.WeightOptionMethod(Options.EnemyDropOption_RefinedAuxCores))
    valTable.PopulateValues(Values.ValueFile("ITM_PcWpnChip", mult=3), IDs.WeaponChipIDs, Values.WeightOptionMethod(Options.EnemyDropOption_WeaponChips))
    
    # Torna
    tornaValTable = copy.deepcopy(valTable) # Copy it before we put in just base game accessory IDs
    FerisBeastmeat = [30380]
    tornaValTable.PopulateValues(Values.ValueFile("ITM_PcEquip"), IDs.AllowedTornaAccessories, Values.WeightOptionMethod(Options.EnemyDropOption_Accessories))
    
    valTable.PopulateValues(Values.ValueFile("ITM_Orb"), IDs.AuxCoreIDs, Values.WeightOptionMethod(Options.EnemyDropOption_AuxCores))
    valTable.PopulateValues(Values.ValueFile("ITM_CrystalList", mult=3), IDs.CoreCrystals, Values.WeightOptionMethod(Options.EnemyDropOption_CoreCrystals))
    valTable.PopulateValues(Values.ValueFile("ITM_PcEquip"), IDs.AccessoryIDs, Values.WeightOptionMethod(Options.EnemyDropOption_Accessories))
    
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

def ColoredString(name, color):    
    return f"[System:Color name={color}]{name}[/System:Color]" 

def ChestTypeMatchesContentsValue():
    class ChestType():
        def __init__(self, name, rscId, msId, percentile, stars = 1):
            self.name = name
            self.rscId = rscId # RSC ID of the chest
            self.msId = msId
            self.percentile = percentile
            self.stars = stars
            
    Common = ChestType("Common", 1, 154, 0, stars=1)
    Uncommon = ChestType("Uncommon", 4, 155, 0.3, stars=2)
    Rare = ChestType("Rare", 2, 156, 0.5, stars=3)
    Epic = ChestType("Epic", 6, 157, 0.7, 4)
    Legendary = ChestType("Legendary", 3, 158, 0.9, 5)
    Rarities:list[ChestType] = [Common, Uncommon, Rare, Epic, Legendary]
    
    with open("XC2/JsonOutputs/common_ms/fld_gmkname.json", 'r+', encoding='utf-8') as nameFile:
        nameData = json.load(nameFile)
        for rar in Rarities:
            nameData["rows"].append({"$id": rar.msId, "style": 36, "name": f"{rar.name} {ColoredString("★"*rar.stars, "tutorial")}"})
        JSONParser.CloseFile(nameData, nameFile)
            
    with open("XC2/JsonOutputs/common/RSC_TboxList.json", 'r+', encoding='utf-8') as tboxFile:
        tboxData = json.load(tboxFile)
        for rar in Rarities:
            for box in tboxData["rows"]:
                box["initWaitTimeRand"] = 0 
                box["initWaitTime"] = 0 
                box["TBOX_open_starttime"] = 0 
                if box["$id"] == rar.rscId:
                    box["MSG_ID"] = rar.msId
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
                
                for rar in Rarities:
                    if percentile >= rar.percentile:
                        rarity = rar
                    else:
                        break
                
                for tbox in tboxData["rows"]:
                    if tbox["$id"] == box.id:
                        tbox["RSC_ID"] = rarity.rscId
                print(f"Value: {box.value} given rarity: {rarity.name}")
                
            JSONParser.CloseFile(tboxData, tboxFile)

def TreasureChestDescription():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.TreasureChestOption.name)
    myDesc.Text("This option will randomize the contents of treasure chests into the chosen categories")
    myDesc.Text("Turning off a category will put its weight to 0")
    myDesc.Text(Values.ItemLogicDesciption)
    myDesc.Image("TreasureChest.png", "XC2")
    myDesc.Header(Options.TreasureChestOption_RareBlades.name)
    myDesc.Text("This adds Custom Core Crystal into the item pool.\n\nThese crystals will guarantee a certain blade and are named after them.")
    myDesc.Image("Custom Core Crystals.png", "XC2", 700)
    return myDesc

def EnemyDropDescription():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.EnemyDropOption.name)
    myDesc.Text("This option will randomize the drops of enemies into the chosen categories")
    myDesc.Text("Turning off a category will put its weight to 0")
    myDesc.Text(Values.ItemLogicDesciption)
    return myDesc

def PouchItemShopDesc():
    desc = PopupDescriptions.Description()
    desc.Header(Options.PouchItemShopOption.name)
    desc.Text("This option will randomize the contents of pouch item shops into other pouch items")
    desc.Text(Values.ItemLogicDesciption)
    desc.Image("PouchItemShops.png", "XC2")
    return desc

def WeaponChipDesc():
    desc = PopupDescriptions.Description()
    desc.Header(Options.WeaponChipShopOption.name)
    desc.Text("Randomizes chips in weapon chip shops.")
    desc.Text(Values.ItemLogicDesciption)
    desc.Image("WeaponChipRando.png", "XC2", 800)
    return desc

def AccessoryShopDescription():
    desc = PopupDescriptions.Description()
    desc.Header(Options.AccessoryShopsOption.name)
    desc.Text("This option randomizes the contents of Accessory Shops into other accessories.")
    desc.Text(Values.ItemLogicDesciption)
    desc.Image("AccessoryShopIcon.png", "XC2")
    return desc