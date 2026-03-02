import json, os
from scripts import JSONParser, Helper, PopupDescriptions, Values
from  XCDE.XCDE_Scripts import Options, IDs

# Gems have no way to reconcile the rank right now they are all treated the same,  ideally when making it would just have a handler that multiplies the price found in skillist by the gems rank which is found in itemlist

def AllItemPricer():
    '''Adds prices to all items so they can be valued, basically just combines the tables since prices are held in seperate file'''
    AddPriceValuesToItemList("ITM_materiallist", IDs.MaterialIDs)
    AddPriceValuesToItemList("ITM_collectlist", IDs.CollectableIDs)
    AddPriceValuesToItemList("ITM_equiplist", IDs.ArmorIDs)
    AddPriceValuesToItemList("ITM_wpnlist", IDs.WeaponIDs)
    AddPriceValuesToItemList("BTL_skilllist", IDs.GemIDs, True)
    AddPriceValuesToItemList("ITM_artslist", IDs.ArtBookIDs)
    
# Not randomizing crystals because the effects can already be randomized from gem rando. Crystals cant be randomized in anything besides enemies. And there no point in randomizing them in enemies, because it would only be the strength of the crystal but strength is intended to be matched by item rando.

# Some extra logic because Xenoblade DE keeps its prices seperate from the items
# Add the price to the data at the start of rando then remove before packing
def AddPriceValuesToItemList(itemPriceFile, targetIDs, useRankType = False):
    with open(f"XCDE/JsonOutputs/bdat_common/ITM_itemlist.json", 'r+', encoding='utf-8') as itmFile:
        with open(f"XCDE/JsonOutputs/bdat_common/{itemPriceFile}.json", 'r+', encoding='utf-8') as priceFile:
            itmData = json.load(itmFile)
            priceData = json.load(priceFile)
            for itm in itmData["rows"]:
                if itm["$id"] in targetIDs:
                    for price in priceData["rows"]:
                        if price["$id"] == itm["itemID"]:
                            
                            if useRankType:
                                priceValue = price["money"] * itm["rankType"] * 2
                            else:
                                priceValue = price["money"] 
                                
                            itm["Price"] = priceValue
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
                valTable.SelectValuedMember(col, f"itm{i}ID", IDs.KeyItemIDs + IDs.ArtBookIDs)
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
    with open(f"XCDE/JsonOutputs/bdat_common/shoplist.json", 'r+', encoding='utf-8') as shopFile:
        shopData = json.load(shopFile)
        for shop in shopData["rows"]:
            for i in range(1,13):
                wpnValTable.SelectValuedMember(shop, f"wpn{i}")
                headValTable.SelectValuedMember(shop, f"head{i}")
                bodyValTable.SelectValuedMember(shop, f"body{i}")
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
    matValTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    matValTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.MaterialIDs)
    wpnValTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    wpnValTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.WeaponIDs)
    armorValTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    armorValTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.ArmorIDs)
    artValTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    artValTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.ArtBookIDs)
    
    nmlFiles = []
    rarFiles = []
    sprFiles = []
    for file in IDs.areaFileListNumbers:
        if os.path.exists(f"XCDE/JsonOutputs/bdat_ma{file}/drop_sprlist{file}.json"):
            nmlFiles.append(f"bdat_ma{file}/drop_nmllist{file}")
            rarFiles.append(f"bdat_ma{file}/drop_rarlist{file}")
            sprFiles.append(f"bdat_ma{file}/drop_sprlist{file}")
             
    isWpn = Options.EnemyDropOptions_Weapons.GetState()
    isArm = Options.EnemyDropOptions_Armor.GetState()
    isArt = Options.EnemyDropOptions_ArtBooks.GetState()
    isMat = Options.EnemyDropOptions_Materials.GetState()
    
    # Randomization
    if isMat:
        for file in nmlFiles:
            with open(f"XCDE/JsonOutputs/{file}.json", 'r+', encoding='utf-8') as dropFile:
                dropData = json.load(dropFile)
                for drop in dropData["rows"]:
                    for i in range(1,3):
                        matValTable.SelectValuedMember(drop, f"materia{i}", IDs.KeyItemIDs)
                JSONParser.CloseFile(dropData, dropFile)
    
    for file in rarFiles:
        with open(f"XCDE/JsonOutputs/{file}.json", 'r+', encoding='utf-8') as dropFile:
            dropData = json.load(dropFile)
            for drop in dropData["rows"]:
                for i in range(1,5):
                    if isWpn:
                        wpnValTable.SelectValuedMember(drop, f"wpn{i}")
                    if isArm:
                        armorValTable.SelectValuedMember(drop, f"equip{i}")
            JSONParser.CloseFile(dropData, dropFile)
            
    for file in sprFiles:
        with open(f"XCDE/JsonOutputs/{file}.json", 'r+', encoding='utf-8') as dropFile:
            dropData = json.load(dropFile)
            for drop in dropData["rows"]:
                for i in range(1,5):
                    if isWpn:
                        wpnValTable.SelectValuedMember(drop, f"wpn{i}")
                for i in range(1,9):
                    if isWpn:
                        wpnValTable.SelectValuedMember(drop, f"uni_wpn{i}")
                    if isArm:
                        armorValTable.SelectValuedMember(drop, f"uni_equip{i}")
                    if isArt:
                        artValTable.SelectValuedMember(drop, f"arts{i}")
            JSONParser.CloseFile(dropData, dropFile)
    
def EnemyDropsDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.EnemyDropOption.name)
    myDesc.Text("Randomizes the contents of chests dropped from enemies, the types are predetermined and unchanged. Crystals are not randomized through this setting.")
    return myDesc

def QuestRewards():
    valTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.MaterialIDs, Values.WeightOptionMethod(Options.QuestRewardsOptions_Materials))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.CollectableIDs, Values.WeightOptionMethod(Options.QuestRewardsOptions_Collectables))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.ArmorIDs, Values.WeightOptionMethod(Options.QuestRewardsOptions_Armor))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.WeaponIDs, Values.WeightOptionMethod(Options.QuestRewardsOptions_Weapons))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.GemIDs, Values.WeightOptionMethod(Options.QuestRewardsOptions_Gems))
    valTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.ArtBookIDs, Values.WeightOptionMethod(Options.QuestRewardsOptions_ArtBooks))
    
    areas = []
    rewardTypes = ["A1", "A2", "A3", "B1", "B2", "B3"]
    for area in IDs.areaFileListNumbers:
        testArea = f"XCDE/JsonOutputs/bdat_common/JNL_quest{area}.json"
        if os.path.exists(testArea):
            areas.append(testArea)
        
    for area in areas:
        with open(area, 'r+', encoding='utf-8') as rewFile:
            rewData = json.load(rewFile)
            for rew in rewData["rows"]:
                for type in rewardTypes:
                    valTable.SelectValuedMember(rew, f"reward_{type}", IDs.KeyItemIDs)
            JSONParser.CloseFile(rewData, rewFile)

def QuestRewardsDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.QuestRewardsOption.name)
    myDesc.Text("Randomizes rewards from quests. You can choose the weights for the categories you have chosen.")
    return myDesc

def TradeOptions():
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
    gemValTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    gemValTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.GemIDs)
    colValTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    colValTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.CollectableIDs)
    matValTable = Values.ValueTable(path = "XCDE/JsonOutputs/bdat_common")
    matValTable.PopulateValues(Values.ValueFile("ITM_itemlist"), IDs.MaterialIDs)
    
    
    areas = []
    for area in IDs.areaFileListNumbers:
        testArea = f"XCDE/JsonOutputs/bdat_ma{area}/exchangelist{area}.json"
        if os.path.exists(testArea):
            areas.append(testArea)
    
    for area in areas:
        with open(area, 'r+', encoding='utf-8') as exchFile:
            exchData = json.load(exchFile)
            for exch in exchData["rows"]:
                wpnValTable.SelectValuedMember(exch, "wpn1")
                headValTable.SelectValuedMember(exch, "head1")
                headValTable.SelectValuedMember(exch, "body1")
                armValTable.SelectValuedMember(exch, "arm1")
                waistValTable.SelectValuedMember(exch, "waist1")
                leggValTable.SelectValuedMember(exch, "legg1")
                for i in range(1,3):
                    gemValTable.SelectValuedMember(exch, f"kessyou{i}")
                    colValTable.SelectValuedMember(exch, f"collect{i}")
                    matValTable.SelectValuedMember(exch, f"materia{i}")
                
            JSONParser.CloseFile(exchData, exchFile)
    

def TradeOptionsDesc():
    myDesc = PopupDescriptions.Description()
    myDesc.Header(Options.TradeOption.name)
    myDesc.Text("Randomizes the trades NPCs make. Only the chosen suboptions will be randomized.\nThe categories will stay the same so helms will always replace helms and so on.")
    myDesc.Image("rondinecap.png", "XCDE", 800)
    return myDesc

