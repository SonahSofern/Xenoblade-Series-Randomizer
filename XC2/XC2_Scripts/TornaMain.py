from scripts import Helper, JSONParser, PopupDescriptions
import json
import random
from IDs import *
import time
import TornaRecipes, TornaQuests, TornaEnemies, TornaAreas, TornaShops, TornaRedBagItems, TornaMiscItems, Options

# make each slate piece worth the same amount of points (1), and make the requirements be 5, 10, 16. 
# This can be done by changing FLD_ConditionFlags 1445, 1446, 1447 to the respective values. Also change 1401 to 16 for min and max.
# need to double check the Aletta region collection points around Lake Sarleigh, Lett Bridge, Ossum Magnum, Olnard's Trail.

def AllTornaRando():
    DetermineSettings()
    TornaRecipes.CreateTornaRecipeList()
    TornaQuests.SelectRandomPointGoal()
    ChosenSupporterAmounts = [1,16,32,48,64] # have a few sliders going forwards to let the player change this amount
    ChosenLevel2Quests, ChosenLevel4Quests, Sidequests, Mainquests = TornaQuests.SelectCommunityQuests(ChosenSupporterAmounts, ProgressionLocTypes[0])
    Areas = TornaAreas.CreateAreaInfo(Sidequests, Mainquests)
    Enemies = TornaEnemies.AdjustEnemyRequirements(Sidequests, Mainquests, Areas, ProgressionLocTypes[2])
    Shops = TornaShops.CreateShopInfo(Mainquests, Areas, ProgressionLocTypes[4])
    RedBags = TornaRedBagItems.CreateRedBagInfo(Mainquests, Areas, ProgressionLocTypes[5])
    MiscItems = TornaMiscItems.CreateMiscItems(Mainquests, Areas, ProgressionLocTypes[4]) # for now, is on if shops are on
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