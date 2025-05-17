from scripts import Helper, JSONParser, PopupDescriptions
import json
import random
from IDs import *
import time
import TornaRecipes, TornaQuests, TornaEnemies, TornaAreas, TornaShops, TornaRedBagItems, TornaMiscItems, TornaChests, TornaCollectionPoints, Options
import copy

# make each slate piece worth the same amount of points (1), and make the requirements be 5, 10, 16. 
# This can be done by changing FLD_ConditionFlags 1445, 1446, 1447 to the respective values. Also change 1401 to 16 for min and max.
# need to remove script that removes aegaeon and hugo in early aletta
# need to set up the unlock keys
# remove the npc talking options for all npc quests that are not logically chosen for the playthrough. This lets you place their required items anywhere. This causes issues with items from chests, the chests currently aren't tied to a quest, just an enemy
# Change Quest Point Shops to require only 1 item total, only the logically chosen item, and it gives 1 point. Change the point requirement for said shop to also be 1.
# need to make the quest Unforgotten Promise only require 1 eternity loam, not 4, they're key items with the same id, so you can't make them a one-time reward, like from a boss drop, you need 4 in logic
# hints
# spoiler log

class ItemInfo:
    def __init__(self, inputid, category, addtolist):
        self.id = inputid
        self.type = category
        addtolist.append(self)

class LocationCategory:
    def __init__(self, cat, progbool, fulllocs):
        self.category = cat # what is the category's name
        self.isprogresscategory = progbool # can the category have progression
        self.fullloclist = fulllocs # what is the full list of locations that belong in this category
        self.remlocations = fulllocs.copy() # what is the remaining list of locations that haven't been used yet

class KeyItemParams:
    def __init__(self, name, caption, nameid, captionid, preciousid, addtolist):
        self.name = name
        self.nameid = nameid
        self.caption = caption
        self.captionid = captionid
        self.preciousid = preciousid
        addtolist.append(self)

def AllTornaRando():
    DetermineSettings()
    if ProgressionLocTypes == [0,0,0,0,0,0]:
        print("There are no progression locations enabled, cannot generate seed!")
        return
    #TornaRecipes.CreateTornaRecipeList()
    TornaQuests.SelectRandomPointGoal()
    #global Areas, Enemies, Shops, RedBags, MiscItems, Chests, TornaCollectionPointList, GormottCollectionPointList, NormalEnemies, QuestEnemies, Bosses, UniqueMonsters
    ChosenSupporterAmounts = [1,16,32,48,64] # have a few sliders going forwards to let the player change this amount
    ChosenLevel2Quests, ChosenLevel4Quests, Sidequests, Mainquests = TornaQuests.SelectCommunityQuests(ChosenSupporterAmounts, ProgressionLocTypes[0])
    Areas = TornaAreas.CreateAreaInfo(Sidequests, Mainquests)
    global MaxDropTableID
    Enemies, MaxDropTableID = TornaEnemies.AdjustEnemyRequirements(Sidequests, Mainquests, Areas, ProgressionLocTypes[2])
    Shops = TornaShops.CreateShopInfo(Mainquests, Areas, ProgressionLocTypes[4])
    RedBags = TornaRedBagItems.CreateRedBagInfo(Mainquests, Areas, ProgressionLocTypes[5])
    MiscItems = TornaMiscItems.CreateMiscItems(Mainquests, Areas, ProgressionLocTypes[4]) # for now, is on if shops are on
    Chests = TornaChests.CreateChestInfo(Mainquests, Areas, Enemies, ProgressionLocTypes[3])
    TornaCollectionPointList, GormottCollectionPointList = TornaCollectionPoints.CreateCollectionPointInfo(Mainquests, Areas, Enemies, ProgressionLocTypes[1])
    FullItemList = CreateItemLists()
    NormalEnemies, QuestEnemies, Bosses, UniqueMonsters = SplitEnemyTypes(Enemies)
    PlaceItems(FullItemList, ChosenLevel2Quests, ChosenLevel4Quests, Sidequests, Mainquests, Areas, NormalEnemies, QuestEnemies, Bosses, UniqueMonsters, Shops, RedBags, MiscItems, Chests, TornaCollectionPointList, GormottCollectionPointList)
    AddMissingKeyItems()
    CreateLevelCaps()
    pass

def DetermineSettings():
    global ProgressionLocTypes
    SidequestRewardQty, CollectionPointQty, EnemyDropQty, TreasureChestQty, ShopQty, GroundItemQty = 0,0,0,0,0,0
    
    if Options.TornaOption_SideQuests.GetState(): # if Sidequest Rewards are randomized
        SidequestRewardQty = Options.TornaOption_SideQuests.GetOdds()
    
    if Options.TornaOption_CollectionPoints.GetState(): # if Collection Points are randomized
        CollectionPointQty = Options.TornaOption_CollectionPoints.GetOdds()
    
    if Options.TornaOption_EnemyDrops.GetState(): # if Enemy Drops are randomized
        EnemyDropQty = Options.TornaOption_EnemyDrops.GetOdds()
    
    if Options.TornaOption_TreasureChests.GetState(): # if Treasure Chests are randomized
        TreasureChestQty = Options.TornaOption_TreasureChests.GetOdds()
    
    if Options.TornaOption_Shops.GetState(): # if Shops are randomized
        ShopQty = Options.TornaOption_Shops.GetOdds()
    
    if Options.TornaOption_GroundItems.GetState(): # if Ground Items are randomized
        GroundItemQty = 1

    ProgressionLocTypes = [SidequestRewardQty, CollectionPointQty, EnemyDropQty, TreasureChestQty, ShopQty, GroundItemQty]

def CreateItemLists():
    CollectionMaterialList, AuxCoreList, WeaponChipList, AccessoryList, WeaponAccessoryList, KeyItemList = [], [], [], [], [], []
    for item in Helper.InclRange(30001, 30445):
        ItemInfo(item, "CollectionMat", CollectionMaterialList)
    for item in TornaAuxCores:
        ItemInfo(item, "AuxCore", AuxCoreList)
    for item in TornaWeaponChips:
        ItemInfo(item, "WeaponChip", WeaponChipList)
    for item in Accessories + Helper.InclRange(657,680):
        ItemInfo(item, "Accessory", AccessoryList)
    for item in Helper.InclRange(585, 647):
        ItemInfo(item, "WeaponAccessory", WeaponAccessoryList)
    UncleanKeyItemList = [25455, Helper.InclRange(25457, 25466), Helper.InclRange(25479, 25494), 25529, Helper.InclRange(25531, 25535),MineralogyKey,SwordplayKey,FortitudeKey,ForestryKey,ManipEtherKey,KeenEyeKey,FocusKey,LightKey,GirlsTalkKey,EntomologyKey,MiningKey,BotanyKey,LockpickKey,IcthyologyKey,ComWaterKey,SuperstrKey,HHC_Key,LC_Key,CLC_Key,HWC_Key,PVC_Key,FVC_Key,AGC_Key,OTC_Key,DDC_Key,HGC_Key,JinAff,HazeAff,MythraAff,MinothAff,BrighidAff,AegaeonAff,HazeKey,AddamKey,MythraKey,MinothKey,HugoKey,BrighidKey,AegaeonKey, ValidRecipeInfoIDs, 26164, 26192, 26193, 26194, 26195, 25473, 25536]
    UncleanKeyItemList = Helper.MultiLevelListToSingleLevelList(UncleanKeyItemList)
    for item in UncleanKeyItemList:
        ItemInfo(item, "KeyItem", KeyItemList)
    FullItemList = [AccessoryList, WeaponAccessoryList, WeaponChipList, AuxCoreList, CollectionMaterialList, KeyItemList]
    return FullItemList

def SplitEnemyTypes(Enemies):
    NormalEnemies, QuestEnemies, BossEnemies, UniqueMonsters = [], [], [], []
    for enemy in Enemies:
        match enemy.type:
            case "uniquemonster":
                UniqueMonsters.append(enemy)
            case "boss":
                BossEnemies.append(enemy)
            case "questenemy":
                QuestEnemies.append(enemy)
            case "normalenemy":
                NormalEnemies.append(enemy)
    return NormalEnemies, QuestEnemies, BossEnemies, UniqueMonsters

def PlaceItems(FullItemList, ChosenLevel2Quests, ChosenLevel4Quests, Sidequests, Mainquests, Areas, NormalEnemies, QuestEnemies, Bosses, UniqueMonsters, Shops, RedBags, MiscItems, Chests, TornaCollectionPointList, GormottCollectionPointList):
    # loop through main quest reqs, when you get to a story step with a quest, stop, see what requirements there are, and then place those items in valid spots
    #if an item gets placed in a spot with additional requirements, add those requirements to every single type of check that has a corresponding story step above that one
    # Also add those reqs to the current story step's requirements, and add those items to the list of items being placed in this sphere.
    # repeat
    # once done, fill remainder with misc items
    PlacedItems = []
    Locs = [Sidequests, NormalEnemies, QuestEnemies, Bosses, UniqueMonsters, Shops, RedBags, MiscItems, Chests, TornaCollectionPointList, GormottCollectionPointList]
    CatList = [] # list of location categories
    global FilledLocations
    FilledLocations = []
    AllProgressLocations = []
    AllNonProgressLocations = []
    for loc in Locs:
        if loc[0].hasprogression == True:
            CatList.append(LocationCategory(loc[0].type, 1, loc))
            AllProgressLocations.extend(loc)
        else:
            CatList.append(LocationCategory(loc[0].type, 0, loc))
            AllNonProgressLocations.extend(loc)
    global AllLocations
    AllLocations = AllProgressLocations + AllNonProgressLocations    
    for MQ in Mainquests:
        if MQ.itemreqs != []:
            CurrentStepReqs = MQ.itemreqs.copy()
            random.shuffle(CurrentStepReqs)
            CurrentStepReqs = [x for x in CurrentStepReqs if x not in PlacedItems]
            for ChosenItem in CurrentStepReqs:
                if ChosenItem not in PlacedItems:
                    ChosenItemCat = 0
                    for index in range(len(FullItemList)):
                        if ChosenItemCat != 0:
                            break
                        else:
                            for subitem in FullItemList[index]:
                                if ChosenItem == subitem.id:
                                    ChosenItemCat = subitem.type
                                    break
                    ValidLocations = DetermineValidItemSpots(ChosenItem, ChosenItemCat, CatList, MQ.id)
                    ValidLocations = [loc for loc in ValidLocations if loc not in FilledLocations]
                    decidedonlocation = False
                    stucknotice = 0
                    while decidedonlocation == False:
                        try:
                            ChosenLocation = random.choice(ValidLocations)
                            for cat in CatList:
                                for loc in cat.fullloclist:
                                    if loc.name == ChosenLocation.name and loc.type == ChosenLocation.type:
                                        ChosenLocation = loc
                        except:
                            print(f"Generation failed during location selection: No valid locations available for {ChosenItem.name}!")
                        if ChosenItemCat == "KeyItem" and ChosenLocation.type in ["sidequest", "uniquemonster", "boss", "normalenemy"]: # enemy drops need to be handled differently, there's a set spot for key items, only 1 spot is open, not 3, so we need to account for that
                            if ChosenLocation.randomizeditems[3] == -1: # if there's a spot open for a precious item, and there's no spots for other items left, the location needs to be removed from the list of remaining progress locations
                                ChosenLocation.preciousitem = ChosenItem
                                decidedonlocation = True
                            else:
                                ValidLocations.remove(ChosenLocation)
                                continue
                        elif ChosenLocation.type in ["sidequest", "uniquemonster", "boss", "normalenemy"]: #if the location the item is being placed is an enemy, but the item is not a key item, there's 3 slots open for it, so check those for an opening
                            if -1 not in ChosenLocation.randomizeditems[:2]:
                                ValidLocations.remove(ChosenLocation)
                                continue
                            else:
                                for itemspot in range(len(ChosenLocation.randomizeditems[:2])):
                                    if ChosenLocation.randomizeditems[itemspot] == -1: # if we find a progression spot
                                        ChosenLocation.randomizeditems[itemspot] = ChosenItem # put the chosen item into that spot
                                        decidedonlocation = True
                                        break # immediately leave loop, we don't want to replace all important drops
                        else:
                            for itemspot in range(len(ChosenLocation.randomizeditems)):
                                if ChosenLocation.randomizeditems[itemspot] == -1: # if we find a progression spot
                                    ChosenLocation.randomizeditems[itemspot] = ChosenItem # put the chosen item into that spot
                                    decidedonlocation = True
                                    break # immediately leave loop, we don't want to replace all important drops
                        stucknotice += 1
                        if stucknotice > 1000:
                            print(f"Generation got stuck trying to place {ChosenItem.name} !")
                            break
                    CurrentStepReqs.extend(ChosenLocation.itemreqs)
                    CurrentStepReqs = list(set(CurrentStepReqs))
                    CurrentStepReqs = [x for x in CurrentStepReqs if x not in PlacedItems]
                    UpdateAllItemReqs(CurrentStepReqs, Locs, ChosenLocation, ChosenItem, AllLocations, MQ.id)
                    for MQ2 in Mainquests:
                        if MQ2.id > MQ.id:
                            MQ2.itemreqs.extend(CurrentStepReqs)
                            MQ2.itemreqs = list(set(MQ2.itemreqs))
                    PlacedItems.append(ChosenItem)
                    PlacedItems.sort()
                    if ChosenLocation.type in ["sidequest", "uniquemonster", "boss", "normalenemy"] and ChosenLocation.randomizeditems.count(-1) == 1:
                        for cat in CatList:
                            for loc in cat.remlocations:
                                if loc.name == ChosenLocation.name and loc.type == ChosenLocation.type:
                                    ChosenLocation = loc
                            if ChosenLocation in cat.remlocations:
                                cat.remlocations.remove(ChosenLocation)
                                FilledLocations.append(ChosenLocation)
                                break
                    else:
                        if ChosenLocation.randomizeditems.count(-1) == 0:
                            for cat in CatList:
                                for loc in cat.remlocations:
                                    if loc.name == ChosenLocation.name and loc.type == ChosenLocation.type:
                                        ChosenLocation = loc
                                if ChosenLocation in cat.remlocations:
                                    cat.remlocations.remove(ChosenLocation)
                                    FilledLocations.append(ChosenLocation)
                                    break
    # for now, I'm not placing progress items that unlock checks that aren't required for the playthrough
    FullItemReqList = []
    for loc in Locs:
        for check in loc:
            FullItemReqList.extend(check.itemreqs)
    FullItemReqList.extend(ValidRecipeInfoIDs)
    FullItemReqList = list(set(FullItemReqList))
    UnplacedProgressionItems = [x for x in FullItemReqList if x not in PlacedItems] # this holds the items that unlock stuff but don't logically contribute to the playthrough
    #UnplacedLevelUpTokens = [x for x in UnplacedProgressionItems if x in LevelUpTokens] # we want to get only the level up tokens, note down the id number, then determine past what level, you can easily get exp.
    #MinLogicalLevel = UnplacedLevelUpTokens[0] - 25626
    #for loc in AllLocations: # remove the level token requirement from all remaining locations
    #    loc.itemreqs = [x for x in loc.itemreqs if x not in UnplacedLevelUpTokens]
    #AdjustLevelUpReqs(MinLogicalLevel)
    # place filler items in all remaining checks, regardless of if it has progression enabled.
    HelpfulUpgrades = [MineralogyKey,SwordplayKey,FortitudeKey,ForestryKey,ManipEtherKey,KeenEyeKey,FocusKey,LightKey,GirlsTalkKey,EntomologyKey,MiningKey,BotanyKey,LockpickKey,IcthyologyKey,ComWaterKey,SuperstrKey,HHC_Key,LC_Key,CLC_Key,HWC_Key,PVC_Key,FVC_Key,AGC_Key,OTC_Key,DDC_Key,HGC_Key,JinAff,HazeAff,MythraAff,MinothAff,BrighidAff,AegaeonAff,HazeKey,AddamKey,MythraKey,MinothKey,HugoKey,BrighidKey,AegaeonKey]
    HelpfulUpgrades = Helper.MultiLevelListToSingleLevelList(HelpfulUpgrades)
    HelpfulUnplacedUpgrades = []
    for item in FullItemList[5]:
        if item.id in HelpfulUpgrades and item.id not in PlacedItems:
            HelpfulUnplacedUpgrades.append(item)
    PoolMaxItemsPerCategory = 200
    AccessoryList = FullItemList[0]
    WeaponAccessoryList = FullItemList[1]
    WeaponChipList = FullItemList[2]
    AuxCoreList = FullItemList[3]
    CollectionMaterialList = FullItemList[4]
    CollectionMaterialList = [item for item in CollectionMaterialList if item not in FullItemReqList]
    FullItemList[4] = CollectionMaterialList
    FullItemList.append(HelpfulUnplacedUpgrades)
    SelectiveItemPool = []
    for cat in FullItemList:
        SelectiveItemPool.append(random.choices(cat, k = PoolMaxItemsPerCategory))
    SelAccList, SelWAccList, SelChipList, SelXCoreList, SelMatList, SelUpgradeList = SelectiveItemPool[0], SelectiveItemPool[1], SelectiveItemPool[2], SelectiveItemPool[3], SelectiveItemPool[4], SelectiveItemPool[5]
    SelFull = SelAccList + SelWAccList + SelChipList + SelXCoreList + SelMatList + SelUpgradeList
    ValidItemtoLoc = {
        'sidequest': [x for x in SelFull if x not in SelMatList],
        'normalenemy': [x for x in SelFull if x not in SelUpgradeList],
        'questenemy': [x for x in SelFull if x not in SelMatList + SelUpgradeList],
        'boss': [x for x in SelFull if x not in SelMatList + SelUpgradeList],
        'uniquemonster': [x for x in SelFull if x not in SelUpgradeList],
        'shop': SelFull,
        'redbag': [x for x in SelFull if x not in SelMatList],
        'misc': [x for x in SelFull if x not in SelMatList],
        'chest': [x for x in SelFull if x not in SelMatList],
        'tornacollectionpoint': [x for x in SelFull if x not in SelUpgradeList],
        'gormottcollectionpoint': [x for x in SelFull if x not in SelUpgradeList],
    }
    for cat in CatList:
        ValidItems = ValidItemtoLoc[cat.category]
        if cat.category not in ["uniquemonster", "normalenemy", "boss", "questenemy"]:
            for remloc in cat.fullloclist:
                for item in range(len(remloc.randomizeditems)):
                    if remloc.randomizeditems[item] in [0, -1]:
                        remloc.randomizeditems[item] = random.choice(ValidItems).id
                FilledLocations.append(remloc)
        else:
            for remloc in cat.fullloclist:
                for item in range(2):
                    if remloc.randomizeditems[item] in [0, -1]:
                        remloc.randomizeditems[item] = random.choice(ValidItems).id
                if remloc.randomizeditems[3] in [0, -1]:
                    remloc.randomizeditems[3] = random.choice(SelUpgradeList).id
                FilledLocations.append(remloc)
    for cat in CatList:
        for loc in cat.fullloclist:
            if -1 in loc.randomizeditems:
                for item in range(len(loc.randomizeditems)):
                    if loc.randomizeditems[item] == -1:
                        loc.randomizeditems[item] = 0
                        print(f"name: {loc.name}, type: {loc.type}")
    PutItemsInSpots(Locs)

def DetermineValidItemSpots(ChosenItem, ChosenItemCat, CatList, CurrentStoryStep = -1): # certain item types cannot coexist with certain location types. collectible items cannot be put as quest rewards, since there is no renewable source of them in case the player uses them all up, for instance.
    ValidItemSpots = []
    if ChosenItem == 30266:
        pass
    match ChosenItemCat:
        case "CollectionMat":
            for cat in CatList:
                if cat.isprogresscategory == 1 and cat.category in ["uniquemonster", "normalenemy", "shop", "tornacollectionpoint", "gormottcollectionpoint"]:
                    ValidItemSpots.extend(cat.remlocations)
        case "KeyItem":
            for cat in CatList:
                if cat.isprogresscategory == 1 and cat.category in ["sidequest", "uniquemonster", "boss", "normalenemy", "redbag", "misc", "chest", "shop", "tornacollectionpoint", "gormottcollectionpoint"]:
                    ValidItemSpots.extend(cat.remlocations)
        case _:
            for cat in CatList:
                ValidItemSpots.extend(cat.remlocations)
    TempValidItemSpots = [loc for loc in ValidItemSpots if ChosenItem not in loc.itemreqs] # make sure the item isn't put in a spot locked by itself
    if TempValidItemSpots == []:
        print(f"Ran out of valid locations when trying to ensure {ChosenItem} was not locked by itself!")
    else:
        ValidItemSpots = TempValidItemSpots
    if CurrentStoryStep != -1:
        TempValidItemSpots = [loc for loc in ValidItemSpots if loc.mainreq < CurrentStoryStep + 1] # make sure the item isn't past the spot in the story where it can be accessed
        if TempValidItemSpots == []:
            print(f"Ran out of valid locations when trying to ensure {ChosenItem} was not placed further ahead in the story than the player can reach!")
        else:
            ValidItemSpots = TempValidItemSpots
    #TempValidItemSpots = [loc for loc in ValidItemSpots if len(loc.itemreqs) < len(MainQuestStep.itemreqs) + 25] # make sure we aren't adding a bunch more requirements
    #if TempValidItemSpots == []:
    #    pass
    #else:
    #    ValidItemSpots = TempValidItemSpots
    return ValidItemSpots

def UpdateAllItemReqs(CurrentStepReqs, Locations, ChosenLocation, ChosenItem, AllLocations, CurrentStepNumber = -1):
    for loc in AllLocations:
        if ChosenItem in loc.itemreqs:
            loc.itemreqs += ChosenLocation.itemreqs
            loc.itemreqs = list(set(loc.itemreqs))
    if CurrentStepNumber != -1:
        if CurrentStepReqs != []:
            for loctype in Locations:
                for subloc in loctype:
                    if subloc.mainreq > CurrentStepNumber:
                        try:
                            subloc.itemreqs.extend(CurrentStepReqs)
                            subloc.itemreqs = list(set(subloc.itemreqs))
                        except:
                            print(f"Generation failed to update item requirements: Invalid item placed at {subloc}!")

def AdjustLevelUpReqs(MinLogicalLevel):
    with open("./XC2/_internal/JsonOutputs/common/BTL_Grow.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in [2,3]:
                row["LevelExp2"] == 1
            if 4 <= row["$id"] <= MinLogicalLevel:
                row["LevelExp2"] == 9999
            if row["$id"] > MinLogicalLevel - 1:
                row["LevelExp2"] = 1
            if row["$id"] > 99:
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def PutItemsInSpots(Locs2): # now we actually feed the items into their corresponding pipelines in the bdats
    # Locs = ConsolidateLevelUpTokens(Locs2) no longer need to consolidate levelup tokens, since we use level cap now
    Locs = Locs2
    # sidequests
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/FLD_QuestReward.json", ["EXP", "ItemID1", "ItemNumber1", "ItemID2", "ItemNumber2", "ItemID3", "ItemNumber3", "ItemID4", "ItemNumber4"], 0)
    with open("./XC2/_internal/JsonOutputs/common/FLD_QuestReward.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for sidequest in Locs[0]:
            for rewardid in sidequest.rewardids: # currently only one quest has multiple reward ids, but they all need to have the same ending rewards.
                for row in data["rows"]:
                    if row["$id"] == rewardid:
                        for i in range(4):
                            row[f"ItemID{i+1}"] = sidequest.randomizeditems[i]
                            row[f"ItemNumber{i+1}"] = 1
                        break      
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    # enemy drops    
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/BTL_EnDropItem.json", Helper.ExtendListtoLength(["ItemID1", "DropProb1", "NoGetByEnh1", "FirstNamed1"], 32, "inputlist[i-4][:-1] +  str(int(inputlist[i-4][-1:])+1)"), 0)
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/BTL_EnDropItem.json", ["DropProb1"], 100) # the first loot item in each row has a 100% chance to drop every time.
    MaxEnemyLootID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/BTL_EnDropItem.json", "$id")
    if MaxDropTableID > MaxEnemyLootID: # need to add a row to BTL_EnDropItem for each regular loot drop 
        NewLootIDRows = []
        for tableid in range(MaxEnemyLootID + 1, MaxDropTableID + 1):
            NewLootIDRows.append([{"$id": tableid, "LimitNum": 0, "SelectType": 0, "ItemID1": 0, "DropProb1": 0, "NoGetByEnh1": 0, "FirstNamed1": 0, "ItemID2": 0, "DropProb2": 0, "NoGetByEnh2": 0, "FirstNamed2": 0, "ItemID3": 0, "DropProb3": 0, "NoGetByEnh3": 0, "FirstNamed3": 0, "ItemID4": 0, "DropProb4": 0, "NoGetByEnh4": 0, "FirstNamed4": 0, "ItemID5": 0, "DropProb5": 0, "NoGetByEnh5": 0, "FirstNamed5": 0, "ItemID6": 0, "DropProb6": 0, "NoGetByEnh6": 0, "FirstNamed6": 0, "ItemID7": 0, "DropProb7": 0, "NoGetByEnh7": 0, "FirstNamed7": 0, "ItemID8": 0, "DropProb8": 0, "NoGetByEnh8": 0, "FirstNamed8": 0}])
        JSONParser.ExtendJSONFile("common/BTL_EnDropItem.json", NewLootIDRows)
    with open("./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for enemytype in range(1, 5):
            for enemy in Locs[enemytype]:
                for row in data["rows"]:
                    if row["$id"] == enemy.id:
                        row["DropTableID"] = enemy.droptableids[0]
                        row["DropTableID2"] = enemy.droptableids[1]
                        #row["DropTableID3"] = enemy.droptableids[2] # this should always be 0, but in case I decide to change the future behavior
                        row["PreciousID"] = enemy.randomizeditems[3] # the precious id just gets the id itself plugged in here
                        break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False) 
    with open("./XC2/_internal/JsonOutputs/common/BTL_EnDropItem.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for enemytype in range(1, 5):
            for enemy in Locs[enemytype]:
                for row in data["rows"]:
                    if row["$id"] in enemy.droptableids:
                        if row["$id"] == enemy.droptableids[0]:
                            row["ItemID1"] = enemy.randomizeditems[0]
                            break
                        if row["$id"] == enemy.droptableids[1]:
                            row["ItemID1"] = enemy.randomizeditems[1]
                            break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    
    # shops
    with open("./XC2/_internal/JsonOutputs/common_gmk/ma40a_FLD_NpcPop.json", 'r+', encoding='utf-8') as file: # alters the NpcPop file to make the bards call different Event IDs and different Shop IDs
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 40660:
                row["Condition"] = 0
                row["EventID"] = 40339
                row["ShopID"] = 67
            if row["$id"] == 40662:
                row["Condition"] = 0
                row["EventID"] = 40442
                row["ShopID"] = 68      
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/MNU_ShopList.json", 'r+', encoding='utf-8') as file: # Changing ShopList
        data = json.load(file)
        for shop in Locs[5]:
            for row in data["rows"]:
                if row["$id"] == shop.shoplistid:
                    row["ShopType"] = 0 # need to convert all shops to Normal shops if they aren't already
                    row["TableID"] = shop.shopnormalid
                    for i in range(1,6):
                        row[f"Discount{i}"] = 0
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/_internal/JsonOutputs/common/MNU_ShopNormal.json", 'r+', encoding='utf-8') as file: # Adding items to ShopNormal
        data = json.load(file)
        for shop in Locs[5]:
            for row in data["rows"]:
                if row["$id"] == shop.shopnormalid:
                    for key, value in row.items(): # clear out the other stuff in the row
                        if key != "$id":
                            row[key] = 0
                    for defnum in range(0, 10):
                        row[f"DefItem{defnum + 1}"] = shop.randomizeditems[defnum]
                    for addtemnum in range(10, 15):
                        row[f"Addtem{addtemnum - 9}"] = shop.randomizeditems[addtemnum]
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    
    # redbags
    with open("./XC2/_internal/JsonOutputs/common_gmk/ma40a_FLD_PreciousPopList.json", 'r+', encoding='utf-8') as file: # adding the redbag items
        data = json.load(file)
        for redbag in Locs[6]:
            for row in data["rows"]:
                if row["$id"] == redbag.id:
                    row["QuestFlag"], row["QuestFlagMin"], row["QuestFlagMax"] = 0, 0, 0
                    row["itmID"] = redbag.randomizeditems[0]
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    
    # misc
    with open("./XC2/_internal/JsonOutputs/common/FLD_AddItem.json", 'r+', encoding='utf-8') as file: # adding the misc items
        data = json.load(file)
        for miscitem in Locs[7]:
            for row in data["rows"]:
                if row["$id"] == miscitem.fldadditemid:
                    row["ItemID1"] = miscitem.randomizeditems[0]
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    # chests
    with open("./XC2/_internal/JsonOutputs/common_gmk/ma40a_FLD_TboxPop.json", 'r+', encoding='utf-8') as fileT: # Torna chests
        dataT = json.load(fileT)
        with open("./XC2/_internal/JsonOutputs/common_gmk/ma41a_FLD_TboxPop.json", 'r+', encoding='utf-8') as fileG: # Gormott chests
            dataG = json.load(fileG)
            for chest in Locs[8]:
                if chest.continent == "Torna":
                    for rowT in dataT["rows"]:
                        if rowT["$id"] == chest.id:
                            for i in range(1, 8):
                                rowT[f"itm{i}ID"] = chest.randomizeditems[i-1]
                                rowT[f"itm{i}Num"] = 1
                                rowT[f"itm{i}Per"] = 100
                            break
                else:
                    for rowG in dataG["rows"]:
                        if rowG["$id"] == chest.id:
                            for i in range(1, 8):
                                rowG[f"itm{i}ID"] = chest.randomizeditems[i-1]
                                rowG[f"itm{i}Num"] = 1
                                rowG[f"itm{i}Per"] = 100
                            break
            fileG.seek(0)
            fileG.truncate()
            json.dump(dataG, fileG, indent=2, ensure_ascii=False)
        fileT.seek(0)
        fileT.truncate()
        json.dump(dataT, fileT, indent=2, ensure_ascii=False)
    
    # collectionpoints
    with open("./XC2/_internal/JsonOutputs/common_gmk/ma40a_FLD_CollectionPopList.json", 'r+', encoding='utf-8') as file: # Torna collection points
        data = json.load(file)
        for collectionpoint in Locs[9]:
            for row in data["rows"]:
                if row["$id"] == collectionpoint.id:
                    row["POP_TIME"] = 256
                    row["popWeather"] = 0
                    row["CollectionTable"] = collectionpoint.collectiontableid
                    if row["Condition"] not in [3230, 3231]: # we only care about the gold and silver seeker conditions
                        row["Condition"] = 0
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
       
    with open("./XC2/_internal/JsonOutputs/common_gmk/ma41a_FLD_CollectionPopList.json", 'r+', encoding='utf-8') as file: # Gormott collection points
        data = json.load(file)
        for collectionpoint in Locs[10]:
            for row in data["rows"]:
                if row["$id"] == collectionpoint.id:
                    row["POP_TIME"] = 256
                    row["popWeather"] = 0
                    row["CollectionTable"] = collectionpoint.collectiontableid
                    if row["Condition"] not in [3230, 3231]: # we only care about the gold and silver seeker conditions
                        row["Condition"] = 0
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    
    DesiredMaxCollectionTableID = 501 # known, will always be the case, 1 collection point -> 1 collection table
    CurMaxCollectionTableID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common/FLD_CollectionTable.json", "$id")
    NewCollectionTableRows = []
    for i in range(CurMaxCollectionTableID + 1, DesiredMaxCollectionTableID + 1):
        NewCollectionTableRows.append([{"$id": i, "FSID": 0, "randitmPopMin": 0, "randitmPopMax": 0, "itm1ID": 0, "itm1Per": 0, "itm2ID": 0, "itm2Per": 0, "itm3ID": 0, "itm3Per": 0, "itm4ID": 0, "itm4Per": 0, "goldMin": 0, "goldMax": 0, "goldPopMin": 0, "goldPopMax": 0, "rsc_paramID": 0, "categoryName": 0, "ZoneID": 0}])
    JSONParser.ExtendJSONFile("common/FLD_CollectionTable.json", NewCollectionTableRows)
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/FLD_CollectionTable.json", ["randitmPopMin", "randitmPopMax"], 10)
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/FLD_CollectionTable.json", ["itm1Per", "itm2Per", "itm3Per", "itm4Per"], 100)
    with open("./XC2/_internal/JsonOutputs/common/FLD_CollectionTable.json", 'r+', encoding='utf-8') as file: # collection table file
        data = json.load(file)
        for i in range(9, 11):
            for collectionpoint in Locs[i]:
                for row in data["rows"]:
                    if row["$id"] == collectionpoint.collectiontableid:
                        row["FSID"] = random.choice(Helper.InclRange(68, 72)) # add a bonus for a random field skill
                        for item in range(1, 5):
                            row[f"itm{item}ID"] = collectionpoint.randomizeditems[item-1]
                        break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def ConsolidateLevelUpTokens(Locs): # need to now remove all level up tokens and replace them with 1 singular level up token, so the shop will only require 1 input trade.
    for cat in Locs:
        for loc in cat:
            for req in range(len(loc.itemreqs)):
                if loc.itemreqs[req] in LevelUpTokens:
                    loc.itemreqs[req] = 25631
    return Locs

def AddMissingKeyItems():
    NewDescID = Helper.GetMaxValue("./XC2/_internal/JsonOutputs/common_ms/itm_precious.json", "$id") + 1
    KeyItemNames = ["Mineralogy Lv. 1 Unlock", "Mineralogy Lv. 2 Unlock", "Mineralogy Lv. 3 Unlock", "Swordplay Lv. 1 Unlock", "Swordplay Lv. 2 Unlock", "Swordplay Lv. 3 Unlock", "Fortitude Lv. 1 Unlock", "Fortitude Lv. 2 Unlock", "Fortitude Lv. 3 Unlock", "Forestry Lv. 1 Unlock", "Forestry Lv. 2 Unlock", "Forestry Lv. 3 Unlock", "Manipulate Ether Lv. 1 Unlock", "Manipulate Ether Lv. 2 Unlock", "Manipulate Ether Lv. 3 Unlock", "Keen Eye Lv. 1 Unlock", "Keen Eye Lv. 2 Unlock", "Keen Eye Lv. 3 Unlock", "Focus Lv. 1 Unlock", "Focus Lv. 2 Unlock", "Focus Lv. 3 Unlock", "Power of Light Lv. 1 Unlock", "Power of Light Lv. 2 Unlock", "Power of Light Lv. 3 Unlock", "Girls' Talk Unlock", "Entomology Lv. 1 Unlock", "Entomology Lv. 2 Unlock", "Entomology Lv. 3 Unlock", "Mining Lv. 1 Unlock", "Mining Lv. 2 Unlock", "Mining Lv. 3 Unlock", "Botany Lv. 1 Unlock", "Botany Lv. 2 Unlock", "Botany Lv. 3 Unlock", "Lockpick Lv. 1 Unlock", "Lockpick Lv. 2 Unlock", "Lockpick Lv. 3 Unlock", "Icthyology Lv. 1 Unlock", "Icthyology Lv. 2 Unlock", "Icthyology Lv. 3 Unlock", "Command Water Lv. 1 Unlock", "Command Water Lv. 2 Unlock", "Command Water Lv. 3 Unlock", "Superstrength Lv. 1 Unlock", "Superstrength Lv. 2 Unlock", "Superstrength Lv. 3 Unlock", "Aletta Garrison Camp Unlock", "Coolley Lake Camp Unlock", "Dannagh Desert Camp Unlock", "Feltley Village Camp Unlock", "Hidden Hunting Camp Unlock", "Hoary Weald Camp Unlock", "Holy Gate Camp Unlock", "Lakeshore Campsite Unlock", "Olnard's Trail Campsite Unlock", "Porton Village Camp Unlock", "Jin Affinity Lv. 2 Unlock", "Jin Affinity Lv. 3 Unlock", "Jin Affinity Lv. 4 Unlock", "Jin Affinity Lv. 5 Unlock", "Haze Affinity Lv. 2 Unlock", "Haze Affinity Lv. 3 Unlock", "Haze Affinity Lv. 4 Unlock", "Haze Affinity Lv. 5 Unlock", "Mythra Affinity Lv. 2 Unlock", "Mythra Affinity Lv. 3 Unlock", "Mythra Affinity Lv. 4 Unlock", "Mythra Affinity Lv. 5 Unlock", "Minoth Affinity Lv. 2 Unlock", "Minoth Affinity Lv. 3 Unlock", "Minoth Affinity Lv. 4 Unlock", "Minoth Affinity Lv. 5 Unlock", "Brighid Affinity Lv. 2 Unlock", "Brighid Affinity Lv. 3 Unlock", "Brighid Affinity Lv. 4 Unlock", "Brighid Affinity Lv. 5 Unlock", "Aegaeon Affinity Lv. 2 Unlock", "Aegaeon Affinity Lv. 3 Unlock", "Aegaeon Affinity Lv. 4 Unlock", "Aegaeon Affinity Lv. 5 Unlock", "Haze Unlock Key", "Addam Unlock Key", "Mythra Unlock Key", "Minoth Unlock Key", "Hugo Unlock Key", "Brighid Unlock Key", "Aegaeon Unlock Key", "Level Up Token"]
    KeyItemDescriptions = ["Unlocks the Mineralogy Lv. 1 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Mineralogy Lv. 2 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Mineralogy Lv. 3 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Swordplay Lv. 1 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Swordplay Lv. 2 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Swordplay Lv. 3 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Fortitude Lv. 1 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Fortitude Lv. 2 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Fortitude Lv. 3 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Forestry Lv. 1 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Forestry Lv. 2 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Forestry Lv. 3 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Manipulate Ether Lv. 1 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Manipulate Ether Lv. 2 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Manipulate Ether Lv. 3 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Keen Eye Lv. 1 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Keen Eye Lv. 2 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Keen Eye Lv. 3 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Focus Lv. 1 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Focus Lv. 2 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Focus Lv. 3 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Power of Light Lv. 1 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Power of Light Lv. 2 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Power of Light Lv. 3 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Girls' Talk Field Skill when the correct trust level is reached for that blade.", "Unlocks the Entomology Lv. 1 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Entomology Lv. 2 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Entomology Lv. 3 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Mining Lv. 1 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Mining Lv. 2 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Mining Lv. 3 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Botany Lv. 1 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Botany Lv. 2 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Botany Lv. 3 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Lockpick Lv. 1 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Lockpick Lv. 2 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Lockpick Lv. 3 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Icthyology Lv. 1 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Icthyology Lv. 2 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Icthyology Lv. 3 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Command Water Lv. 1 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Command Water Lv. 2 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Command Water Lv. 3 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Superstrength Lv. 1 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Superstrength Lv. 2 Field Skill when the correct trust level is reached for that blade.", "Unlocks the Superstrength Lv. 3 Field Skill when the correct trust level is reached for that blade.", "Unlocks the ability to rest at the Aletta Garrison Campsite.", "Unlocks the ability to rest at the Coolley Lake Campsite.", "Unlocks the ability to rest at the Dannagh Desert Campsite.", "Unlocks the ability to rest at the Feltley Village Campsite.", "Unlocks the ability to rest at the Hidden Hunting Campsite.", "Unlocks the ability to rest at the Hoary Weald Campsite.", "Unlocks the ability to rest at the Holy Gate Campsite.", "Unlocks the ability to rest at the Lakeshore Campsite.", "Unlocks the ability to rest at the Olnard's Trail Campsite.", "Unlocks the ability to rest at the Porton Village Campsite.", "Unlocks Level 2 of Jin's Affinity Chart.", "Unlocks Level 3 of Jin's Affinity Chart.", "Unlocks Level 4 of Jin's Affinity Chart.", "Unlocks Level 5 of Jin's Affinity Chart.", "Unlocks Level 2 of Haze's Affinity Chart.", "Unlocks Level 3 of Haze's Affinity Chart.", "Unlocks Level 4 of Haze's Affinity Chart.", "Unlocks Level 5 of Haze's Affinity Chart.", "Unlocks Level 2 of Mythra's Affinity Chart.", "Unlocks Level 3 of Mythra's Affinity Chart.", "Unlocks Level 4 of Mythra's Affinity Chart.", "Unlocks Level 5 of Mythra's Affinity Chart.", "Unlocks Level 2 of Minoth's Affinity Chart.", "Unlocks Level 3 of Minoth's Affinity Chart.", "Unlocks Level 4 of Minoth's Affinity Chart.", "Unlocks Level 5 of Minoth's Affinity Chart.", "Unlocks Level 2 of Brighid's Affinity Chart.", "Unlocks Level 3 of Brighid's Affinity Chart.", "Unlocks Level 4 of Brighid's Affinity Chart.", "Unlocks Level 5 of Brighid's Affinity Chart.", "Unlocks Level 2 of Aegaeon's Affinity Chart.", "Unlocks Level 3 of Aegaeon's Affinity Chart.", "Unlocks Level 4 of Aegaeon's Affinity Chart.", "Unlocks Level 5 of Aegaeon's Affinity Chart.", 'Unlocks the ability to add Haze to your party.', 'Unlocks the ability to add Addam to your party.', 'Unlocks the ability to add Mythra to your party.', 'Unlocks the ability to add Minoth to your party.', 'Unlocks the ability to add Hugo to your party.', 'Unlocks the ability to add Brighid to your party.', 'Unlocks the ability to add Aegaeon to your party.', "Can be exchanged for 1 level's worth of EXP at the Token Exchange."]
    KeyItemPreciousIDs = [25544, 25545, 25546, 25547, 25548, 25549, 25550, 25551, 25552, 25553, 25554, 25555, 25556, 25557, 25558, 25559, 25560, 25561, 25562, 25563, 25564, 25565, 25566, 25567, 25568, 25569, 25570, 25571, 25572, 25573, 25574, 25575, 25576, 25577, 25578, 25579, 25580, 25581, 25582, 25583, 25584, 25585, 25586, 25587, 25588, 25589, 25590, 25591, 25592, 25593, 25594, 25595, 25596, 25597, 25598, 25599, 25600, 25601, 25602, 25603, 25604, 25605, 25606, 25607, 25608, 25609, 25610, 25611, 25612, 25613, 25614, 25615, 25616, 25617, 25618, 25619, 25620, 25621, 25622, 25623, 25624, 25625, 25626, 25627, 25628, 25629, 25630, 25631]
    KeyItemList = []
    for name in range(len(KeyItemNames)):
        KeyItemParams(f"{KeyItemNames[name]}",f"{KeyItemDescriptions[name]}", NewDescID, NewDescID + 1, KeyItemPreciousIDs[name], KeyItemList)
        NewDescID += 2
    NewPreciousListItems, NewDescList = [], []
    for item in KeyItemList:
        NewPreciousListItems.append([{"$id": item.preciousid, "Name": item.nameid, "Caption": item.captionid, "Category": 29, "Type": 0, "Price": 1, "ValueMax": 1, "ClearNewGame": 1, "NoMultiple": 0, "sortJP": item.preciousid, "sortGE": item.preciousid, "sortFR": item.preciousid, "sortSP": item.preciousid, "sortIT": item.preciousid, "sortGB": item.preciousid, "sortCN": item.preciousid, "sortTW": item.preciousid, "sortKR": item.preciousid}])
        NewDescList.append([{"$id": item.nameid, "style": 36, "name": item.name}])
        NewDescList.append([{"$id": item.captionid, "style": 61, "name": item.caption}])
    JSONParser.ExtendJSONFile("common/ITM_PreciousList.json", NewPreciousListItems)
    JSONParser.ExtendJSONFile("common_ms/itm_precious.json", NewDescList)

def CreateLevelCaps(): 
    # makes the level caps in the files, removing all other xp sources than the story bosses, which give max xp possible. all other sources will give 1 xp.
    # it takes max xp to level up past a level cap, and 1 xp otherwise.
    # technically this is cheeseable with fights where there are multiple enemies, if you defeat the one that lets you pass the level cap, then die to another, you can get that same xp again, I believe.
    with open("./XC2/_internal/JsonOutputs/common/BTL_Grow.json", 'r+', encoding='utf-8') as file: # xp requirements file
        data = json.load(file)
        for row in data["rows"]:
            match row["$id"]:
                case [15, 20, 26, 35, 38, 46, 100]:
                    row["LevelExp2"] = 99999 # LevelExp2 is for Torna, LevelExp is for base game
                case _:
                    row["LevelExp2"] = 1
            row["EnemyExp"] = 1000 # believe this is the base xp gained by defeating an enemy of this level, before accounting for level differences
            row["EnemyWP"] = row["EnemyWP"] * 10
            row["EnemySP"] = row["EnemySP"] * 10
            row["EnemyGold"] = row["EnemyGold"] * 10
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/BTL_Lv_Rev.json", ["ExpRevHigh", "ExpRevLow", "ExpRevLow2"], 100) # make it so you always get 100% of the exp you earn, regardless of level difference.
    with open("./XC2/_internal/JsonOutputs/common/CHR_EnArrange.json", 'r+', encoding='utf-8') as file: # enemy file
        data = json.load(file)
        for row in data["rows"]:
            match row["$id"]:
                case [1430, 1433, 1434, 1437, 1442, 1632, 1443]: # all enemies that raise level cap upon defeat
                    row["ExpRev"] = 100 # 1000*1000 = 100000, but caps at 99999
                case _:
                    row["ExpRev"] = 0 # all other enemies get 0*1000 = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    LandmarkFiles = ["./XC2/_internal/JsonOutputs/common_gmk/ma40a_FLD_LandmarkPop.json", "./XC2/_internal/JsonOutputs/common_gmk/ma41a_FLD_LandmarkPop.json"]
    for map in LandmarkFiles:
        with open(map, 'r+', encoding='utf-8') as file:
                data = json.load(file)
                for row in data["rows"]:
                    row["getEXP"] = 10
                    row["getSP"] = row["getSP"] * 10 # amp the SP gains by 10, to reduce grinding
                    row["developZone"] = 0
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=2, ensure_ascii=False)
    Helper.ColumnAdjust("./XC2/_internal/JsonOutputs/common/FLD_QuestReward.json", ["EXP"], 0) # doing quests doesn't reward any xp
    Helper.MathmaticalColumnAdjust(["./XC2/_internal/JsonOutputs/common/FLD_QuestReward.json"], ["Gold", "SP"], ['row[key] * 10']) # quests reward 10x gold and sp

