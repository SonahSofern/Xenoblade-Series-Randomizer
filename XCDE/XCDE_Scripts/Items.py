import json, random, copy
from scripts import JSONParser, Helper, PopupDescriptions, Values
from  XCDE.XCDE_Scripts import Options, IDs

def AllItemPricer():
    '''Adds prices to all items so they can be valued, basically just combines the tables since prices are held in seperate file'''
    AddPriceValuesToItemList("ITM_materiallist", IDs.MaterialIDs)
    AddPriceValuesToItemList("ITM_collectlist", IDs.CollectableIDs)
    AddPriceValuesToItemList("ITM_equiplist", IDs.ArmorIDs)
    AddPriceValuesToItemList("ITM_wpnlist", IDs.WeaponIDs)
    AddPriceValuesToItemList("BTL_skilllist", IDs.GemIDs)
    AddPriceValuesToItemList("ITM_artslist", IDs.ArtBookIDs)
    
# Not randomizing crystals because the effects can already be randomized from gem rando. Crystals cant be randomized in anything besides enemies. And there no point in randomizing them in enemies, because it would only be the strength of the crystal but strength is intended to be matched by item rando.

# Some extra logic because Xenoblade DE keeps its prices seperate from the items
# Add the price to the data at the start of rando then remove before packing
def AddPriceValuesToItemList(itemPriceFile, targetIDs):
    with open(f"XCDE/JsonOutputs/bdat_common/ITM_itemlist.json", 'r+', encoding='utf-8') as itmFile:
        with open(f"XCDE/JsonOutputs/bdat_common/{itemPriceFile}.json", 'r+', encoding='utf-8') as priceFile:
            itmData = json.load(itmFile)
            priceData = json.load(priceFile)
            for itm in itmData["rows"]:
                if itm["$id"] in targetIDs:
                    for price in priceData["rows"]:
                        if price["$id"] == itm["itemID"]:
                            itm["Price"] = price["money"]
                            break
            JSONParser.CloseFile(itmData, itmFile)

def RemovePriceValuesFromItemList():
    '''Runs at the end to remove the added prices, so the files will pack'''
    with open(f"XCDE/JsonOutputs/bdat_common/ITM_itemlist.json", 'r+', encoding='utf-8') as itmFile:
        itmData = json.load(itmFile)
        for row in itmData["rows"]:
            if "Price" in row:
                del row["Price"]
        JSONParser.CloseFile(itmData, itmFile)

def Collectables():
    valTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.MaterialIDs, Values.WeightOptionMethod(Options.CollectableOptions_Materials))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.CollectableIDs, Values.WeightOptionMethod(Options.CollectableOptions_Collectables))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.ArmorIDs, Values.WeightOptionMethod(Options.CollectableOptions_Armor))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.WeaponIDs, Values.WeightOptionMethod(Options.CollectableOptions_Weapons))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.GemIDs, Values.WeightOptionMethod(Options.CollectableOptions_Gems))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.ArtBookIDs, Values.WeightOptionMethod(Options.CollectableOptions_ArtBooks))
    
    # Randomization
    for area in IDs.areasWithCollectables:  
        with open(f"XCDE/JsonOutputs/bdat_ma{area}/Litemlist{area}.json", 'r+', encoding='utf-8') as colFile:
            colData = json.load(colFile)
            for col in colData["rows"]:
                for i in range(1,9):
                    valTable.SelectValuedMember(col, f"itm{i}ID", IDs.KeyItemIDs)
            
            JSONParser.CloseFile(colData, colFile)

def CollectDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.CollectableOptions.name)
    myDesc.Text("Randomizes collectables in the field. Collectibles have 8 different possible items per orb per location. You can also choose weights for the categories you have chosen.")
    myDesc.Image("orb.png","XCDE", 500)
    return myDesc


def Collectapedia():
    valTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.MaterialIDs, Values.WeightOptionMethod(Options.CollectapediaOptions_Materials))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.CollectableIDs, Values.WeightOptionMethod(Options.CollectapediaOptions_Collectables))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.ArmorIDs, Values.WeightOptionMethod(Options.CollectapediaOptions_Armor))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.WeaponIDs, Values.WeightOptionMethod(Options.CollectapediaOptions_Weapons))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.GemIDs, Values.WeightOptionMethod(Options.CollectapediaOptions_Gems))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.ArtBookIDs, Values.WeightOptionMethod(Options.CollectapediaOptions_ArtBooks))
    
    # Randomization
    with open(f"XCDE/JsonOutputs/bdat_menu_item/MNU_col.json", 'r+', encoding='utf-8') as colFile:
        colData = json.load(colFile)
        for col in colData["rows"]:
            valTable.SelectValuedMember(col, "itemID", IDs.KeyItemIDs)
        JSONParser.CloseFile(colData, colFile)
    
def CollectapediaDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.CollectapediaOptions.name)
    myDesc.Text("Randomizes rewards from the collectapedia. You can choose the weights for the categories you have chosen.")
    return myDesc


def GiantsChests():
    valTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.MaterialIDs, Values.WeightOptionMethod(Options.GiantsChestOptions_Materials))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.CollectableIDs, Values.WeightOptionMethod(Options.GiantsChestOptions_Collectables))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.ArmorIDs, Values.WeightOptionMethod(Options.GiantsChestOptions_Armor))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.WeaponIDs, Values.WeightOptionMethod(Options.GiantsChestOptions_Weapons))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.GemIDs, Values.WeightOptionMethod(Options.GiantsChestOptions_Gems))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.ArtBookIDs, Values.WeightOptionMethod(Options.GiantsChestOptions_ArtBooks))
    
    # Randomization
    with open(f"XCDE/JsonOutputs/bdat_common/FLD_tboxlist.json", 'r+', encoding='utf-8') as tboxFile:
        tboxData = json.load(tboxFile)
        for col in tboxData["rows"]:
            for i in range(1,5):
                valTable.SelectValuedMember(col, f"item{i}ID", IDs.KeyItemIDs + IDs.ArtBookIDs)
        JSONParser.CloseFile(tboxData, tboxFile)
        
def GiantsChestsDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.GiantsChestOption.name)
    myDesc.Text("Randomizes the contents of giants chests. You can choose the weights for the categories you have chosen.")
    return myDesc

def Shops():
    wpnValTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    wpnValTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.WeaponIDs)
    headValTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    headValTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.HeadIDs)
    leggValTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    leggValTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.LegIDs)
    artValTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    artValTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.ArtBookIDs)
    waistValTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    waistValTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.WaistIDs)
    armValTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    armValTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.ArmIDs)
    bodyValTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    bodyValTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.ChestIDs)
    
    
    # Randomization
    with open(f"XCDE/JsonOutputs/bdat_common/FLD_tboxlist.json", 'r+', encoding='utf-8') as shopFile:
        shopData = json.load(shopFile)
        for shop in shopData["rows"]:
            for i in range(1,13):
                wpnValTable.SelectValuedMember(shop, f"wpn{i}")
                headValTable.SelectValuedMember(shop, f"head{i}")
                headValTable.SelectValuedMember(shop, f"head{i}")
                armValTable.SelectValuedMember(shop, f"arm{i}")
                waistValTable.SelectValuedMember(shop, f"waist{i}")
                leggValTable.SelectValuedMember(shop, f"legg{i}")
                artValTable.SelectValuedMember(shop, f"arts{i}")
                
        JSONParser.CloseFile(shopData, shopFile)

def ShopsDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.ShopOption.name)
    myDesc.Text("Randomizes the contents of shops, keeping the original item type.")
    return myDesc


def EnemyDrops():
    valTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.MaterialIDs, Values.WeightOptionMethod(Options.GiantsChestOptions_Materials))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.CollectableIDs, Values.WeightOptionMethod(Options.GiantsChestOptions_Collectables))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.ArmorIDs, Values.WeightOptionMethod(Options.GiantsChestOptions_Armor))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.WeaponIDs, Values.WeightOptionMethod(Options.GiantsChestOptions_Weapons))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.GemIDs, Values.WeightOptionMethod(Options.GiantsChestOptions_Gems))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.ArtBookIDs, Values.WeightOptionMethod(Options.GiantsChestOptions_ArtBooks))
    
    # Randomization
    with open(f"XCDE/JsonOutputs/bdat_common/FLD_tboxlist.json", 'r+', encoding='utf-8') as tboxFile:
        tboxData = json.load(tboxFile)
        for col in tboxData["rows"]:
            for i in range(1,5):
                valTable.SelectValuedMember(col, f"item{i}ID", IDs.KeyItemIDs + IDs.ArtBookIDs)
        JSONParser.CloseFile(tboxData, tboxFile)
    
    nmlFiles = []
    rarFiles = []
    sprFiles = []
    for file in IDs.areaFileListNumbers:
        nmlFiles.append(f"bdat_ma{file}/drop_nmllist{file}")
        rarFiles.append(f"bdat_ma{file}/drop_rarlist{file}")
        sprFiles.append(f"bdat_ma{file}/drop_sprlist{file}")
        
    sprKeys = ["wpn1", "wpn2", "wpn3", "wpn4"]
    for i in range(1,9):
        sprKeys.append(f"arts{i}")
        sprKeys.append(f"uni_equip{i}")
        sprKeys.append(f"uni_wpn{i}")
    
    ItemRandomization([col, mat, arm, wep, gem, cry, art, key], nmlFiles, odds,"XCDE",  ["materia1", "materia2"], keepType=keepType.GetState())
    ItemRandomization([col, mat, arm, wep, gem, cry, art, key], rarFiles, odds,"XCDE",  ["crystal1", "crystal2", "wpn1", "wpn2", "wpn3", "wpn4", "equip1", "equip2", "equip3", "equip4"], keepType=keepType.GetState())
    ItemRandomization([col, mat, arm, wep, gem, cry, art, key], sprFiles, odds,"XCDE",  sprKeys, keepType=keepType.GetState())

def EnemyDropsDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.EnemyDropOption.name)
    myDesc.Text("Randomizes the contents of chests dropped from enemies. You can choose the weights for the categories you have chosen.")
    myDesc.Header(Options.QuestRewardsOption_KeepType.name)
    myDesc.Text(keepTypeDescriptions)
    return myDesc


# def QuestRewards():
#     col = ItemType(IDs.CollectableIDs, Options.QuestRewardsOptions_Collectables)
#     mat = ItemType(IDs.MaterialIDs, Options.QuestRewardsOptions_Materials)
#     arm = ItemType(IDs.ArmorIDs, Options.QuestRewardsOptions_Armor)
#     wep = ItemType(IDs.WeaponIDs, Options.QuestRewardsOptions_Weapons)
#     gem = ItemType(IDs.GemIDs, Options.QuestRewardsOptions_Gems)
#     cry = ItemType(IDs.CrystalIDs, Options.QuestRewardsOptions_Crystals)
#     art = ItemType(IDs.ArtBookIDs, Options.QuestRewardsOptions_ArtBooks)
#     key = ItemType(IDs.KeyItemIDs, Options.QuestRewardsOptions_KeyItems)
#     keepType = Options.QuestRewardsOption_KeepType
    
#     odds = Options.QuestRewardsOption.GetSpinbox()
    
#     areas = []
#     for area in IDs.areaFileListNumbers:
#         areas.append(f"bdat_common/JNL_quest{area}")
    
#     ItemRandomization([col, mat, arm, wep, gem, cry, art, key], areas, odds,"XCDE",  ["reward_A1","reward_A2","reward_A3","reward_B1","reward_B2","reward_B3"], keepType=keepType.GetState())

# def QuestRewardsDesc():
#     myDesc = PopupDescriptions.Description()
#     myDesc.Header(Options.QuestRewardsOption.name)
#     myDesc.Text("Randomizes rewards from quests. You can choose the weights for the categories you have chosen.")
#     myDesc.Header(Options.QuestRewardsOption_KeepType.name)
#     myDesc.Text(keepTypeDescriptions)
#     return myDesc


# def TradeOptions():
#     col = ItemType(IDs.CollectableIDs, Options.TradeOptions_Collectables)
#     mat = ItemType(IDs.MaterialIDs, Options.TradeOptions_Materials)
#     arm = ItemType(IDs.ArmorIDs, Options.TradeOptions_Armor)
#     wep = ItemType(IDs.WeaponIDs, Options.TradeOptions_Weapons)
#     gem = ItemType(IDs.GemIDs, Options.TradeOptions_Gems)
#     cry = ItemType(IDs.CrystalIDs, Options.TradeOptions_Crystals)
#     art = ItemType(IDs.ArtBookIDs, Options.TradeOptions_ArtBooks)
#     key = ItemType(IDs.KeyItemIDs, Options.TradeOptions_KeyItems)
#     keepType = Options.TradeOption_KeepType
    
#     odds = Options.TradeOption.GetSpinbox()
    
#     areas = []
#     for area in IDs.areaFileListNumbers:
#         areas.append(f"bdat_ma{area}/exchangelist{area}")
    
#     ItemRandomization([col, mat, arm, wep, gem, cry, art, key], areas, odds,"XCDE",  ["wpn1", "head1", "body1", "arm1", "waist1", "legg1", "kessyou1", "kessyou2", "collect1", "collect2", "materia1", "materia2"], keepType=keepType.GetState())

# def TradeOptionsDesc():
#     myDesc = PopupDescriptions.Description()
#     myDesc.Header(Options.TradeOption.name)
#     myDesc.Text("Randomizes the trades NPCs make. Only the chosen suboptions will be randomized.\nThe categories will stay the same so helms will always replace helms and so on.")
#     myDesc.Image("rondinecap.png", "XCDE", 800)
#     myDesc.Header(Options.QuestRewardsOption_KeepType.name)
#     myDesc.Text(keepTypeDescriptions)
#     return myDesc

