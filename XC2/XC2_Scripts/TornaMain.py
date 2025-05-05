from scripts import Helper, JSONParser, PopupDescriptions
import json
import random
from IDs import *
import time
import TornaRecipes, TornaQuests, TornaEnemies, TornaAreas, TornaShops, TornaRedBagItems, TornaMiscItems, TornaChests, TornaCollectionPoints, Options
import copy

# make each slate piece worth the same amount of points (1), and make the requirements be 5, 10, 16. 
# This can be done by changing FLD_ConditionFlags 1445, 1446, 1447 to the respective values. Also change 1401 to 16 for min and max.
# need to change the required weather and time requirements for all collection points, to make them accessible at any time, except for the ones with seeker requirements or miasma requirements
# need to remove script that removes aegaeon and hugo in early aletta
# need to set up the unlock keys
# need to make SP costs for upgrades much cheaper
# remove all quest, weather, and time requirements for all chests, to make them accessible at any time
# remove the npc talking options for all npc quests that are not logically chosen for the playthrough. This lets you place their required items anywhere.
# make the EXP levels past level 


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
    Enemies = TornaEnemies.AdjustEnemyRequirements(Sidequests, Mainquests, Areas, ProgressionLocTypes[2])
    Shops = TornaShops.CreateShopInfo(Mainquests, Areas, ProgressionLocTypes[4])
    RedBags = TornaRedBagItems.CreateRedBagInfo(Mainquests, Areas, ProgressionLocTypes[5])
    MiscItems = TornaMiscItems.CreateMiscItems(Mainquests, Areas, ProgressionLocTypes[4]) # for now, is on if shops are on
    Chests = TornaChests.CreateChestInfo(Mainquests, Areas, Enemies, ProgressionLocTypes[3])
    TornaCollectionPointList, GormottCollectionPointList = TornaCollectionPoints.CreateCollectionPointInfo(Mainquests, Areas, Enemies, ProgressionLocTypes[1])
    FullItemList = CreateItemLists()
    NormalEnemies, QuestEnemies, Bosses, UniqueMonsters = SplitEnemyTypes(Enemies)
    PlaceItems(FullItemList, ChosenLevel2Quests, ChosenLevel4Quests, Sidequests, Mainquests, Areas, NormalEnemies, QuestEnemies, Bosses, UniqueMonsters, Shops, RedBags, MiscItems, Chests, TornaCollectionPointList, GormottCollectionPointList)
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
    UncleanKeyItemList = [25455, Helper.InclRange(25457, 25466), Helper.InclRange(25479, 25494), 25529, Helper.InclRange(25531, 25535),MineralogyKey,SwordplayKey,FortitudeKey,ForestryKey,ManipEtherKey,KeenEyeKey,FocusKey,LightKey,GirlsTalkKey,EntomologyKey,MiningKey,BotanyKey,LockpickKey,IcthyologyKey,ComWaterKey,SuperstrKey,HHC_Key,LC_Key,CLC_Key,HWC_Key,PVC_Key,FVC_Key,AGC_Key,OTC_Key,DDC_Key,HGC_Key,JinAff,HazeAff,MythraAff,MinothAff,BrighidAff,AegaeonAff,HazeKey,AddamKey,MythraKey,MinothKey,HugoKey,BrighidKey,AegaeonKey,LevelUpTokens, ValidRecipeInfoIDs, 26164, 26192, 26193, 26194, 26195, 25473, 25536]
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
    UnplacedLevelUpTokens = [x for x in UnplacedProgressionItems if x in LevelUpTokens] # we want to get only the level up tokens, note down the id number, then determine past what level, you can easily get exp.
    MinLogicalLevel = UnplacedLevelUpTokens[0] - 25626
    for loc in AllLocations: # remove the level token requirement from all remaining locations
        loc.itemreqs = [x for x in loc.itemreqs if x not in UnplacedLevelUpTokens]
    AdjustLevelUpReqs(MinLogicalLevel)
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
    pass

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