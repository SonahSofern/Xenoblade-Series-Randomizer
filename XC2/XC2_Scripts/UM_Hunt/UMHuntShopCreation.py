import json, random,  math,  time
from XC2.XC2_Scripts import IDs,Options
from XC2.XC2_Scripts.Race_Mode import RaceMode
from XC2.XC2_Scripts.Enhancements import *
from XC2.XC2_Scripts.CharacterRandomization import ReplacementCharacter2Original
from scripts import Helper

# ShopID: [ShopType: EventID, Name]
ShopEventNameDict = {'Normal': {36: [40321, 30], 37: [40322, 31], 38: [40323, 32], 39: [40324, 33], 40: [40325, 34], 41: [40326, 35], 42: [40327, 36], 43: [40328, 37], 44: [40329, 38], 45: [40330, 39], 46: [40332, 40], 47: [40331, 41], 48: [41000, 42], 49: [40333, 43], 64: [40438, 50], 65: [40338, 66], 66: [40441, 51], 67: [40339, 72], 68: [40442, 52], 69: [40340, 68], 70: [40443, 53], 71: [40444, 54], 72: [40445, 55], 73: [40446, 56], 75: [40341, 69], 76: [40342, 70], 77: [40447, 58], 78: [40448, 59], 80: [40449, 60], 81: [40450, 61], 82: [40343, 71], 83: [40451, 62], 84: [41001, 45], 85: [41002, 46], 92: [40663, 91], 93: [40664, 92], 94: [40665, 93], 95: [40666, 94], 96: [40667, 95], 97: [40668, 96], 98: [40669, 97], 99: [40670, 98], 100: [40671, 99], 102: [40672, 100], 103: [40673, 101], 104: [41003, 102], 105: [40674, 103], 113: [40675, 112], 115: [40758, 114], 116: [40760, 115], 117: [40676, 116], 118: [40723, 117], 119: [40757, 118], 120: [40684, 119], 121: [40756, 120], 122: [40685, 122], 123: [41004, 121], 145: [41040, 143], 146: [41041, 144], 147: [40810, 145], 148: [40806, 146], 149: [40808, 147], 150: [40805, 148], 151: [40811, 149], 152: [40807, 150], 153: [41005, 151], 201: [41556, 117], 249: [42020, 228], 250: [42019, 229], 251: [42022, 230], 252: [42021, 231], 253: [41628, 232], 254: [41678, 233], 255: [42023, 234]},
                     'Exchange': {16: [40058, 245], 17: [40054, 239], 18: [40045, 238], 21: [40048, 241], 23: [40050, 244], 24: [40051, 240], 26: [40052, 242], 27: [40053, 246], 33: [40320, 23], 54: [40439, 49], 55: [40337, 65], 74: [41042, 57], 89: [40662, 88], 109: [40724, 108], 110: [40761, 109], 114: [40731, 243], 144: [40809, 142], 154: [41039, 152], 156: [40982, 155], 186: [41564, 183], 189: [40980, 154], 202: [41044, 191], 257: [42027, 236]},
                    'Inn': {12: [40057, 2], 31: [40318, 21], 50: [40436, 47], 51: [40335, 63], 87: [40660, 86], 106: [40762, 105], 107: [40952, 106], 143: [41053, 141], 225: [41578, 204]},
                    'AuxCore': {32: [40319, 22], 52: [40440, 48], 53: [40336, 64], 88: [40661, 87], 108: [40759, 107]}}

FullShopEventNameDict = {36: [40321, 30], 37: [40322, 31], 38: [40323, 32], 39: [40324, 33], 40: [40325, 34], 41: [40326, 35], 42: [40327, 36], 43: [40328, 37], 44: [40329, 38], 45: [40330, 39], 46: [40332, 40], 47: [40331, 41], 48: [41000, 42], 49: [40333, 43], 64: [40438, 50], 65: [40338, 66], 66: [40441, 51], 67: [40339, 72], 68: [40442, 52], 69: [40340, 68], 70: [40443, 53], 71: [40444, 54], 72: [40445, 55], 73: [40446, 56], 75: [40341, 69], 76: [40342, 70], 77: [40447, 58], 78: [40448, 59], 80: [40449, 60], 81: [40450, 61], 82: [40343, 71], 83: [40451, 62], 84: [41001, 45], 85: [41002, 46], 92: [40663, 91], 93: [40664, 92], 94: [40665, 93], 95: [40666, 94], 96: [40667, 95], 97: [40668, 96], 98: [40669, 97], 99: [40670, 98], 100: [40671, 99], 102: [40672, 100], 103: [40673, 101], 104: [41003, 102], 105: [40674, 103], 113: [40675, 112], 115: [40758, 114], 116: [40760, 115], 117: [40676, 116], 118: [40723, 117], 119: [40757, 118], 120: [40684, 119], 121: [40756, 120], 122: [40685, 122], 123: [41004, 121], 145: [41040, 143], 146: [41041, 144], 147: [40810, 145], 148: [40806, 146], 149: [40808, 147], 150: [40805, 148], 151: [40811, 149], 152: [40807, 150], 153: [41005, 151], 201: [41556, 117], 249: [42020, 228], 250: [42019, 229], 251: [42022, 230], 252: [42021, 231], 253: [41628, 232], 254: [41678, 233], 255: [42023, 234], 16: [40058, 245], 17: [40054, 239], 18: [40045, 238], 21: [40048, 241], 23: [40050, 244], 24: [40051, 240], 26: [40052, 242], 27: [40053, 246], 33: [40320, 23], 54: [40439, 49], 55: [40337, 65], 74: [41042, 57], 89: [40662, 88], 109: [40724, 108], 110: [40761, 109], 114: [40731, 243], 144: [40809, 142], 154: [41039, 152], 156: [40982, 155], 186: [41564, 183], 189: [40980, 154], 202: [41044, 191], 257: [42027, 236], 12: [40057, 2], 31: [40318, 21], 50: [40436, 47], 51: [40335, 63], 87: [40660, 86], 106: [40762, 105], 107: [40952, 106], 143: [41053, 141], 225: [41578, 204], 32: [40319, 22], 52: [40440, 48], 53: [40336, 64], 88: [40661, 87], 108: [40759, 107]}

FullShopEventList = [40321, 40322, 40323, 40324, 40325, 40326, 40327, 40328, 40329, 40330, 40332, 40331, 41000, 40333, 40438, 40338, 40441, 40339, 40442, 40340, 40443, 40444, 40445, 40446, 40341, 40342, 40447, 40448, 40449, 40450, 40343, 40451, 41001, 41002, 40663, 40664, 40665, 40666, 40667, 40668, 40669, 40670, 40671, 40672, 40673, 41003, 40674, 40675, 40758, 40760, 40676, 40723, 40757, 40684, 40756, 40685, 41004, 41040, 41041, 40810, 40806, 40808, 40805, 40811, 40807, 41005, 20262, 41556, 21256, 42020, 42019, 42022, 42021, 41628, 41678, 42023, 40058, 40054, 40045, 40048, 40050, 40051, 40052, 40053, 40320, 40439, 40337, 20805, 20806, 20807, 41042, 40662, 20441, 20444, 40724, 40761, 40731, 40809, 41039, 40982, 20121, 20119, 20124, 20125, 20126, 20265, 20268, 41564, 40980, 41044, 21383, 21393, 21394, 21470, 21448, 21623, 21660, 21694, 21727, 21729, 21740, 21741, 21760, 42027, 40319, 40440, 40336, 40661, 40759]

FullShopList = [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 92, 93, 94, 95, 96, 97, 98, 99, 100, 102, 103, 104, 105, 113, 115, 116, 117, 118, 119, 120, 121, 122, 123, 145, 146, 147, 148, 149, 150, 151, 152, 153, 201, 249, 250, 251, 252, 253, 254, 255, 16, 17, 18, 21, 23, 24, 26, 27, 33, 54, 55, 74, 89, 109, 110, 114, 144, 154, 156, 186, 189, 202, 257, 12, 31, 50, 51, 87, 106, 107, 143, 225, 32, 52, 53, 88, 108]

UsedShopIDs = [18,24,16] + Helper.InclRange(65, 73) + [81]

FullUnusedShopList = [x for x in FullShopList if x not in UsedShopIDs]

ContinentInfo = {"Gormott": [10043, 10044, "ma05a", 6], "Uraya": [10088, 10079, "ma07a", 9], "Mor Ardain": [10156, 10149, "ma08a", 10], "Leftheria": [10197, 10192, "ma15a", 14], "Temperantia": [10233, 10224, "ma10a", 11], "Tantal": [10272, 10269, "ma13a", 13], "Spirit Crucible": [10325, 10323, "ma16a", 15], "Cliffs of Morytha": [10351, 10345, "ma17a", 16], "Land of Morytha": [10369, 10363, "ma18a", 18], "World Tree": [10399, 10393, "ma20a", 20]}

#NPC IDs (used to give a shop to)
UnusedBazaarNPCRowIDs = [2109, 2362, 2086, 2205, 2069, 2206, 2236, 2085, 2091, 2426, 2177, 2041, 2038, 2092, 2352, 2136, 2342, 2128, 2001, 2361, 2126, 2068, 2111, 2070, 2415, 2425, 2316, 2176, 2343, 2417, 2419, 2080, 2250, 2341, 2127, 2112, 2351, 2089, 2197, 2110, 2164, 2418, 2090, 2163, 2039, 2003, 2084, 2040, 2125, 2002, 2416, 2393, 2011, 2359, 2208, 2182, 2424, 2251, 2083, 2165, 2012]

UniqueNPCs = [2236, 2088, 2359, 2362, 2092, 2361, 2087, 2080, 2089] #NPCs that only show up once in the Bazaar

# NpcID: name
NPCIDtoName = {2109: 'npc41300011_02', 2236: 'npc42350117_01', 2038: 'npc00600111_02', 2001: 'npc000401_01', 2415: 'npc43400391_01', 2419: 'npc42450291_01', 2351: 'npc42320112_01', 2090: 'npc42350115_02', 2125: 'npc41300012_05', 2088: 'npc42350113_01', 2359: 'npc42420251_02', 2362: 'npc42320191_02', 2085: 'npc42350112_02', 2092: 'npc42350114_01', 2361: 'npc42420192_02', 2087: 'npc42350111_01', 2425: 'npc42350192_01', 2080: 'npc42300017_01', 2089: 'npc42350116_01', 2163: 'npc42400013_07', 2002: 'npc000401_02', 2182: 'npc42450114_01', 2086: 'npc42350112_01', 2091: 'npc42350115_01', 2352: 'npc42320112_02', 2126: 'npc41300012_04', 2316: 'npc45200112_02', 2250: 'npc47100012_01', 2197: 'npc43400013_02', 2039: 'npc00600111_06', 2416: 'npc43400391_02', 2424: 'npc42450291_02', 2205: 'npc45300012_05', 2426: 'npc42350192_02', 2136: 'npc42300012_01', 2068: 'npc00640111_02', 2176: 'npc42450111_01', 2341: 'npc42350212_05', 2110: 'npc41300011_01', 2040: 'npc00600111_05', 2393: 'npc45200112_03', 2251: 'npc47100012_03', 2069: 'npc00640111_03', 2177: 'npc42450111_02', 2342: 'npc42350212_02', 2111: 'npc41300011_03', 2417: 'npc43400391_03', 2127: 'npc41300012_01', 2164: 'npc42400013_01', 2003: 'npc00040111_11', 2011: 'npc45450111_01', 2083: 'npc42340112_03', 2206: 'npc45300012_03', 2041: 'npc00600111_03', 2128: 'npc41300012_02', 2070: 'npc00640111_04', 2343: 'npc42350212_03', 2112: 'npc41300011_04', 2418: 'npc43400391_04', 2084: 'npc42340112_04', 2208: 'npc45300012_07', 2165: 'npc42400013_02', 2012: 'npc45450111_02'}

InvalidMapNPCs = [8284, 5487]

# Custom Shop Stuff

# Cost Distributions
TokenExchangeRewards = []
for i in range(0, 10):
    TokenExchangeRewards.append(3 + 4*i)
ManualCostDistribution = [3, 6, 9, 35, 50, 9, 17, 33]

PouchItemShopCostDistribution = [5,5,5,5,10,5,5,5,15,15,15,10,10,15,10,5]

PoppiswapShopCosts = [10, 20, 30, 40, 50, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44]

# Filler Lists
TokenFillerList = Helper.ExtendListtoLength([], 10, "0") # This gets used so much, I'd rather not screw up typing it out, also by initializing it here, it doesn't calculate the value every time in the dictionary
EmptyFillerList = Helper.ExtendListtoLength([], 16, "0") # Empty list of full size
FullFillerList = Helper.ExtendListtoLength([], 16, "1") # Full list of full size
ManualFillerList = Helper.ExtendListtoLength([], 8, "0") # Empty list for manual shop

ProofofPurchaseIDs = Helper.InclRange(25306, 25321)

#25333->25348 for Casino Vouchers
#25479->25488 for Bounty Tokens
#25405->25407 for WP Manuals
#25349->25351 for SP Manuals
#25489 for Doubloons (1)

def ReAddFileGlobals(SetCount2, UMHuntDisableCondListID2, UMHuntEnableCondListIDs2, ChosenDifficulty2, ExtraSuperbosses2, SuperbossCount2, ChosenSuperbosses2, SuperbossMaps2, OneScenarioConditionList2):
    global SetCount, UMHuntDisableCondListID, UMHuntEnableCondListIDs, ChosenDifficulty, ExtraSuperbosses, SuperbossCount, ChosenSuperbosses, SuperbossMaps, OneScenarioConditionList
    SetCount, UMHuntDisableCondListID, UMHuntEnableCondListIDs, ChosenDifficulty, ExtraSuperbosses, SuperbossCount, ChosenSuperbosses, SuperbossMaps, OneScenarioConditionList = SetCount2, UMHuntDisableCondListID2, UMHuntEnableCondListIDs2, ChosenDifficulty2, ExtraSuperbosses2, SuperbossCount2, ChosenSuperbosses2, SuperbossMaps2, OneScenarioConditionList2

def CreateShopDictionaries():
    global TokenExchangeShop, CoreCrystalShop, WPManualShop, WeaponChipShop, AuxCoreShop, PouchItemShop, DriverAccessoryShop, PoppiswapShop, GambaShop, FullShopTemplateList
    
    TokenExchangeShop = {
        "NewNPCModel": 2002, # from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Bana
        "ChosenMapRowID": 2079, # ma02a_FLD_NpcPop $id
        "ShopIcon": 420, # MNU_ShopList ShopIcon
        "ShopIDtoReplace": 18, # MNU_ShopList $id
        "ShopName": "[System:Color name=green]Bounty Token[/System:Color] Bartering", # fld_shopname name
        "TradeCount": 10, # Number of Trades the shop will have
        "InputItemIDs": [Helper.InclRange(25479, 25488), TokenFillerList, TokenFillerList, TokenFillerList, TokenFillerList], # MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs
        "InputItemQtys": [Helper.ExtendListtoLength([], 10, "1"), TokenFillerList, TokenFillerList, TokenFillerList, TokenFillerList], # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
        "RewardItemIDs": [Helper.ExtendListtoLength([], 10, "25489"), TokenFillerList, TokenFillerList, TokenFillerList], # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
        "RewardQtys": [TokenExchangeRewards, TokenFillerList, TokenFillerList, TokenFillerList], # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
        "RewardNames": ["Doubloons + SP", "Doubloons + EXP + SP", "Doubloons + EXP + SP", "Doubloons + EXP + SP", "Doubloons + EXP + SP", "Doubloons + EXP + SP", "Doubloons + EXP + SP", "Doubloons + EXP + SP", "Doubloons + EXP + SP", "Doubloons + EXP + SP"], # names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs
        "RewardSP": Helper.ExtendListtoLength([250], 10, "inputlist[i-1] + 40"), #FLD_QuestReward Sp
        "RewardXP": [0, 630, 630, 630, 630, 630, 630, 630, 630, 630], # FLD_QuestReward EXP
        "HideReward": TokenFillerList, # Whether or not to hide the reward, MNU_ShopChangeTask "HideReward"
    }

    CoreCrystalShop = {
        "NewNPCModel": 2008,# from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Amalthus
        "ChosenMapRowID": 2080, # ma02a_FLD_NpcPop $id
        "ShopIcon": 427, # MNU_ShopList ShopIcon
        "ShopIDtoReplace": 17, # MNU_ShopList $id
        "ShopName": "Core Crystal Cache", # fld_shopname name
        "TradeCount": 4, # Number of Trades the shop will have
    }

    WPManualShop = {
        "NewNPCModel": 2001,# from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Gramps
        "ChosenMapRowID": 2088, # ma02a_FLD_NpcPop $id
        "ShopIcon": 442, # MNU_ShopList ShopIcon
        "ShopIDtoReplace": 24, # MNU_ShopList $id
        "ShopName": "Manual Marketplace", # fld_shopname name
        "TradeCount": 8, # Number of Trades the shop will have
        "InputItemIDs": [Helper.ExtendListtoLength([], 8, "25489"), ManualFillerList, ManualFillerList, ManualFillerList, ManualFillerList], # MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs
        "InputItemQtys": [ManualCostDistribution, ManualFillerList, ManualFillerList, ManualFillerList, ManualFillerList], # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
        "RewardItemIDs": [[25405, 25406, 25407, 25305, 25450, 25349, 25350, 25351], ManualFillerList, ManualFillerList, ManualFillerList], # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
        "RewardQtys": [Helper.ExtendListtoLength([], 8, "1"), ManualFillerList, ManualFillerList, ManualFillerList], # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
        "RewardNames": ["250 Art WP", "500 Art WP", "1000 Art WP", "Pouch Expander", "Accessory Expander", "2500 Driver SP", "5000 Driver SP", "10000 Driver SP"], # names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs
        "RewardSP": [0, 0, 0, 0, 0, 2500, 5000, 10000], #FLD_QuestReward Sp
        "RewardXP": ManualFillerList, # FLD_QuestReward EXP
        "HideReward": ManualFillerList, # Whether or not to hide the reward, MNU_ShopChangeTask "HideReward"
    }

    WeaponChipShop = {
        "NewNPCModel": 3457,# from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Padraig
        "ChosenMapRowID": 2089, # ma02a_FLD_NpcPop $id
        "ShopIcon": 430, # MNU_ShopList ShopIcon
        "ShopIDtoReplace": 21, # MNU_ShopList $id
        "ShopName": "Weapon Warehouse", # fld_shopname name
        "TradeCount": 5, # Number of Trades the shop will have
    }

    AuxCoreShop = {
        "NewNPCModel": 3106,# from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Yumyum the Burglar
        "ChosenMapRowID": 2090, # ma02a_FLD_NpcPop $id Replaces Amumu
        "ShopIcon": 432, # MNU_ShopList ShopIcon
        "ShopIDtoReplace": 26, # MNU_ShopList $id
        "ShopName": "Aux Core Auction", # fld_shopname name
        "TradeCount": 9, # Number of Trades the shop will have
    }

    PouchItemShop = {
        "NewNPCModel": 2534,# from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Head Fire Dragon
        "ChosenMapRowID": 2092, # ma02a_FLD_NpcPop $id
        "ShopIcon": 426, # MNU_ShopList ShopIcon
        "ShopIDtoReplace": 114, # MNU_ShopList $id
        "ShopName": "Pouch Item Patisserie", # fld_shopname name
        "TradeCount": 5, # Number of Trades the shop will have
    }

    DriverAccessoryShop = {
        "NewNPCModel": 2031,# from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Yew
        "ChosenMapRowID": 2097, # ma02a_FLD_NpcPop $id
        "ShopIcon": 446, # MNU_ShopList ShopIcon
        "ShopIDtoReplace": 23, # MNU_ShopList $id
        "ShopName": "Excess Accessories", # fld_shopname name
        "TradeCount": 9, # Number of Trades the shop will have
    }

    PoppiswapShop = {
        "NewNPCModel": 3576,# from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Soosoo
        "ChosenMapRowID": 2087, # ma02a_FLD_NpcPop $id Replaces Bonbon
        "ShopIcon": 433, # MNU_ShopList ShopIcon
        "ShopIDtoReplace": 16, # MNU_ShopList $id
        "ShopName": "The Poppishop", # fld_shopname name
        "TradeCount": 16, # Number of Trades the shop will have
        "InputItemIDs": [Helper.ExtendListtoLength([], 16, "25489"), EmptyFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs
        "InputItemQtys": [PoppiswapShopCosts, EmptyFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
        "RewardItemIDs": [Helper.ExtendListtoLength(Helper.ExtendListtoLength([25218], 5, "inputlist[i-1]+1") + [25322], 16, "inputlist[i-1]+1"), EmptyFillerList, EmptyFillerList, EmptyFillerList], # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
        "RewardQtys": [FullFillerList, EmptyFillerList, EmptyFillerList, EmptyFillerList], # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
        "RewardNames": ["Poppiswap Manual 1", "Poppiswap Manual 2", "Poppiswap Manual 3", "Poppiswap Manual 4", "Poppiswap Manual 5", "Ether Crystal Pack 1", "Ether Crystal Pack 2", "Ether Crystal Pack 3", "Ether Crystal Pack 4", "Ether Crystal Pack 5", "Ether Crystal Pack 6", "Ether Crystal Pack 7", "Ether Crystal Pack 8", "Ether Crystal Pack 9", "Ether Crystal Pack 10", "Ether Crystal Pack 11"], # names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs
        "RewardSP": EmptyFillerList, #FLD_QuestReward Sp
        "RewardXP": EmptyFillerList, # FLD_QuestReward EXP
        "HideReward": EmptyFillerList, # Whether or not to hide the reward, MNU_ShopChangeTask "HideReward"
    }

    GambaShop = {
        "NewNPCModel": 3351, # from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Alec
        "ChosenMapRowID": 2188, # ma02a_FLD_NpcPop $id
        "ShopIcon": 443, # MNU_ShopList ShopIcon
        "ShopIDtoReplace": 27, # MNU_ShopList $id
        "ShopName": "The [System:Color name=tutorial]Casino[/System:Color]", # fld_shopname name
        "TradeCount": 3, # Number of Trades the shop will have
    }

    FullShopTemplateList = [CoreCrystalShop, WeaponChipShop, AuxCoreShop, PouchItemShop, DriverAccessoryShop, GambaShop, TokenExchangeShop, WPManualShop, PoppiswapShop]


def CreateNewReceipts(): # Adds more Precious Items as Reciepts for shops
    ReceiptNames = []
    global CoreCrystalReceiptIDs, GambaShopReceiptIDs
    CoreCrystalReceiptIDs = Helper.InclRange(25001, 25000 + CoreCrystalShop["TradeCount"]*SetCount)
    GambaShopReceiptIDs = Helper.InclRange(25000 + CoreCrystalShop["TradeCount"]*SetCount + 1, 25000 + CoreCrystalShop["TradeCount"]*SetCount + 1 + GambaShop["TradeCount"]*SetCount)
    for CurrentSet in range(1, SetCount + 1):
        for i in range(0, CoreCrystalShop["TradeCount"]): # there will always be CoreCrystalShop["TradeCount"]*SetCount receipts
            ReceiptNames.append(f"CC {CurrentSet} Item {i + 1} Receipt")
    for CurrentSet in range(1, SetCount + 1):
        for i in range(0, GambaShop["TradeCount"]): # there will always be GambaShop["TradeCount"]*SetCount receipts
            match i:
                case 0:
                    ReceiptNames.append(f"Casino {CurrentSet} S. Scratchoff")
                case 1:
                    ReceiptNames.append(f"Casino {CurrentSet} M. Scratchoff") 
                case 2:
                    ReceiptNames.append(f"Casino {CurrentSet} L. Scratchoff")
    NewestPreciousName = Helper.GetMaxValue("./XC2/JsonOutputs/common_ms/itm_precious.json", "$id") + 1
    StartingPreciousName = NewestPreciousName
    with open("./XC2/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Caption
        data = json.load(file)
        for i in range(0, len(ReceiptNames)):
            data["rows"].append({"$id": StartingPreciousName, "style": 36, "name": ReceiptNames[i]})
            StartingPreciousName += 1
        data["rows"].append({"$id": StartingPreciousName, "style": 61, "name": "Proves you bought this item."})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file: # Item
        data = json.load(file)
        for i in range(0, len(ReceiptNames)):
            for row in data["rows"]:
                if row["$id"] == 25001 + i:
                    row["Name"] = NewestPreciousName
                    row["Caption"] = StartingPreciousName
                    row["Category"] = 29
                    row["Type"] = 0
                    row["Price"] = 0
                    row["ValueMax"] = 1
                    row["ClearNewGame"] = 0
                    row["NoMultiple"] = 0
                    NewestPreciousName += 1
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def ShopChanges(ChosenAreaOrder): # Moved these out since they were cluttering the main function up. Order probably matters
    UMRewardDropChanges()
    CoreCrystalIdentification()
    WeaponPowerLevel()
    AddDLCRewards(ChosenAreaOrder)
    CustomShopSetup(ChosenAreaOrder)
    InnShopCosts()
    ReplaceBana()
    SecretShopMaker(ChosenAreaOrder)
    ReAddInns()

def UMRewardDropChanges(): #Changes text for the UM drops we want
    with open("./XC2/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in Helper.InclRange(25479, 25489): # Custom Shop/UM Drop Token IDs
                row["ValueMax"] = 255
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes name text file
        data = json.load(file)
        for i in range(1, 11):
            for row in data["rows"]:
                if row["$id"] == 962 + i:
                    row["name"] = f"[System:Color name=green]Bounty Token Lv {i}[/System:Color]"
                if row["$id"] == 978 + i:
                    row["name"] = "Can be traded at the \nBounty Token Exchange for upgrades."
                    break
        for row in data["rows"]:
            if row["$id"] == 973:
                row["name"] = "[System:Color name=tutorial]Doubloon[/System:Color]"
            if row["$id"] == 989:
                row["name"] = "Can be traded at shops for upgrades."
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def CoreCrystalIdentification(): # Figuring out the groups that each Core Crystal Belongs to, then picking items from each group for the shop
    ShuffleCoreCrystals()
    AllBladeCrystalIDs = Helper.InclRange(45002,45004) + Helper.InclRange(45006, 45009) + [45016] + Helper.InclRange(45017,45049) + [45056, 45057]
    global NGPlusBladeCrystalIDs
    NGPlusBladeCrystalIDs = RaceMode.DetermineNGPlusBladeCrystalIDs()
    RemainingBladeCrystalIDs = [x for x in AllBladeCrystalIDs if x not in NGPlusBladeCrystalIDs]
    global DLCBladeCrystalIDs
    DLCBladeCrystalIDs = IdentifyDLCBladeCrystals(RemainingBladeCrystalIDs)
    RemainingBladeCrystalIDs = [x for x in RemainingBladeCrystalIDs if x not in DLCBladeCrystalIDs]
    global TankBladeCrystalIDs, AttackerBladeCrystalIDs, HealerBladeCrystalIDs
    TankBladeCrystalIDs, AttackerBladeCrystalIDs, HealerBladeCrystalIDs = IdentifyClassBladeCrystals(RemainingBladeCrystalIDs)
    CoreCrystalGroupCreation(NGPlusBladeCrystalIDs, DLCBladeCrystalIDs, TankBladeCrystalIDs, AttackerBladeCrystalIDs, HealerBladeCrystalIDs)

def ShuffleCoreCrystals(): # first we need to shuffle the blade ids into the core crystal pool
    AllBladeCrystalIDs = Helper.InclRange(45002,45004) + Helper.InclRange(45006, 45009) + [45016] + Helper.InclRange(45017,45049) + [45056, 45057]
    BladeIDs = [1008, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1050, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1104, 1108, 1109, 1105, 1106, 1107, 1111]
    with open("./XC2/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        RandomBlades = BladeIDs.copy()
        random.shuffle(RandomBlades)
        for i in range(0, len(AllBladeCrystalIDs)):
            for row in data["rows"]:
                if row["$id"] == AllBladeCrystalIDs[i]:
                    row["BladeID"] = RandomBlades[i]
                    row["ValueMax"] = 1
                    row["NoMultiple"] = i + 11
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def IdentifyDLCBladeCrystals(CrystalList):
    DLCBladeIDs = [1105, 1106, 1107, 1108, 1109, 1111]
    if Options.BladesOption.GetState():
        RandomizedBladeIDs = []
        for originalblade in DLCBladeIDs:
            RandomizedBladeIDs.append(ReplacementCharacter2Original[originalblade])
        DLCBladeIDs = RandomizedBladeIDs
    DLCBladeCrystalList = []
    with open("./XC2/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as file: # Adds the exchange tasks
        data = json.load(file)
        for i in range(0, len(CrystalList)):
            for row in data["rows"]:
                if (row["$id"] == CrystalList[i]) and (row["BladeID"] in DLCBladeIDs):
                    DLCBladeCrystalList.append(row["$id"])
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    return DLCBladeCrystalList

def IdentifyClassBladeCrystals(CrystalList): # go from ITM_CrystalList $id->bladeID-> CHR_Bl $id->WeaponType-> ITM_PcWpnType $id->Role
    CrystalBladeIDList = []
    CrystalWeaponTypeIDList = []
    CrystalWeaponRoleList = []
    AttackerList = []
    HealerList = []
    TankList = []
    with open("./XC2/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as file: # Getting BladeIDs for a Crystal $id
        data = json.load(file)
        for i in range(0, len(CrystalList)):
            for row in data["rows"]:
                if row["$id"] == CrystalList[i]:
                    CrystalBladeIDList.append(row["BladeID"])
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common/CHR_Bl.json", 'r+', encoding='utf-8') as file: # Getting WeaponType for a Blade $id
        data = json.load(file)
        for i in range(0, len(CrystalBladeIDList)):
            for row in data["rows"]:
                if row["$id"] == CrystalBladeIDList[i]:
                    CrystalWeaponTypeIDList.append(row["WeaponType"])
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common/ITM_PcWpnType.json", 'r+', encoding='utf-8') as file: # Getting Role for a WeaponType $id
        data = json.load(file)
        for i in range(0, len(CrystalWeaponTypeIDList)):
            for row in data["rows"]:
                if row["$id"] == CrystalWeaponTypeIDList[i]:
                    CrystalWeaponRoleList.append(row["Role"])
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    for i in range(0, len(CrystalList)):
        if CrystalWeaponRoleList[i] == 1: # Tank
            TankList.append(CrystalList[i])
        elif CrystalWeaponRoleList[i] == 2: # Attacker
            AttackerList.append(CrystalList[i])
        else: # Healer
            HealerList.append(CrystalList[i])
    return TankList, AttackerList, HealerList

def CoreCrystalGroupCreation(NGPlusBladeCrystalIDs, DLCBladeCrystalIDs, TankBladeCrystalIDs, AttackerBladeCrystalIDs, HealerBladeCrystalIDs):
    RenameCrystals(NGPlusBladeCrystalIDs, DLCBladeCrystalIDs, TankBladeCrystalIDs, AttackerBladeCrystalIDs, HealerBladeCrystalIDs)
    global CrystalShopRewardList, CrystalShopCostList, CrystalShopNameList
    CrystalShopRewardList, CrystalShopCostList, CrystalShopNameList = [], [], []
    CurrentReceipt = 0
    for i in range(SetCount): # for each set
        ItemCosts = []
        Item1IDs, Item2IDs, Item3IDs, Item4IDs = [], [], Helper.ExtendListtoLength([], CoreCrystalShop["TradeCount"], "0"), Helper.ExtendListtoLength([], CoreCrystalShop["TradeCount"], "0")
        ItemNames = []
        match i:
            case 0:
                AllowedCrystalPool = TankBladeCrystalIDs + AttackerBladeCrystalIDs + HealerBladeCrystalIDs
            case 3:
                AllowedCrystalPool += DLCBladeCrystalIDs
            case 6:
                AllowedCrystalPool += NGPlusBladeCrystalIDs
            case _:
                pass
        for j in range(CoreCrystalShop["TradeCount"]): # now we choose this many crystals to put in the shop
            ChosenCrystal = random.choice(AllowedCrystalPool)
            if ChosenCrystal in AttackerBladeCrystalIDs:
                ItemNames.append("ATK Core Crystal") # name
                ItemCosts.append(random.randint(4,8)) # cost
            elif ChosenCrystal in TankBladeCrystalIDs:
                ItemNames.append("TNK Core Crystal")
                ItemCosts.append(random.randint(3,7))
            elif ChosenCrystal in HealerBladeCrystalIDs:
                ItemNames.append("HLR Core Crystal")
                ItemCosts.append(random.randint(5,10))
            elif ChosenCrystal in DLCBladeCrystalIDs:
                ItemNames.append("DLC Core Crystal")
                ItemCosts.append(random.randint(15,25))
            else: # must be NG+ Blade
                ItemNames.append("NG+ Core Crystal")
                ItemCosts.append(random.randint(90,120))
            Item1IDs.append(ChosenCrystal)
            Item2IDs.append(CoreCrystalReceiptIDs[CurrentReceipt])
            CurrentReceipt += 1
            AllowedCrystalPool.remove(ChosenCrystal)
        CrystalShopRewardList.append([Item1IDs, Item2IDs, Item3IDs, Item4IDs])
        CrystalShopCostList.append(ItemCosts)
        CrystalShopNameList.append(ItemNames)

def RenameCrystals(NGPlusBladeCrystalIDs, DLCBladeCrystalIDs, TankBladeCrystalIDs, AttackerBladeCrystalIDs, HealerBladeCrystalIDs):    
    AllBladeCrystalIDs = Helper.InclRange(45002,45004) + Helper.InclRange(45006, 45009) + [45016] + Helper.InclRange(45017,45049) + [45056, 45057]
    Helper.ColumnAdjust("./XC2/JsonOutputs/common/ITM_CrystalList.json", ["Condition", "CommonID", "CommonWPN", "CommonAtr", "Price", "RareTableProb", "RareBladeRev", "AssureP"], 0)
    with open("./XC2/JsonOutputs/common_ms/itm_crystal.json", "r+", encoding='utf-8') as file: # Now we want to rename crystals according to their category
        IDNumbers = Helper.InclRange(16, 20)
        CrystalCategoryNames = ["NG+ Core Crystal", "DLC Core Crystal", "TNK Core Crystal", "ATK Core Crystal", "HLR Core Crystal"]
        data = json.load(file)
        for i in range(0, len(IDNumbers)):
            data["rows"].append({"$id": IDNumbers[i], "style": 36, "name": CrystalCategoryNames[i]})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common/ITM_CrystalList.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in NGPlusBladeCrystalIDs:
                row["Name"] = 16
            elif row["$id"] in DLCBladeCrystalIDs:
                row["Name"] = 17
            elif row["$id"] in TankBladeCrystalIDs:
                row["Name"] = 18
            elif row["$id"] in AttackerBladeCrystalIDs:
                row["Name"] = 19
            elif row["$id"] in HealerBladeCrystalIDs:
                row["Name"] = 20
            else:
                row["Name"] = 12
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def WeaponPowerLevel(): # Assigns appropriately powered enhancement and damage value based on rank of weapon
    WeaponStrengthList = Helper.ExtendListtoLength([], 20, "[]")
    WeaponStrengthNameList = Helper.ExtendListtoLength([], 20, "[]")
    WeaponDamageRanges = Helper.ExtendListtoLength([[26, 75]], 20, "[inputlist[i-1][0] + 50, inputlist[i-1][1] + 50]")
    InvalidSkillEnhancements = [ArtCancel,EyeOfJustice, XStartBattle, YStartBattle, BStartBattle, BladeSwapDamage, CatScimPowerUp, EvadeDrainHp, EvadeDriverArt, EtherCannonRange, ArtDamageHeal, DreamOfTheFuture, WPEnemiesBoost, ExpEnemiesBoost, MachineExecute, HumanoidExecute, AquaticExecute, AerialExecute, InsectExecute, BeastExecute, InstaKill, AegisPowerUp, TwinRingPowerUp, DrillShieldPowerUp, MechArmsPowerUp, VarSaberPowerUp, WhipswordPowerUp, BigBangPowerUp, DualScythesPowerUp, GreataxePowerUp, MegalancePowerUp, EtherCannonPowerUp, ShieldHammerPowerUp, ChromaKatanaPowerUp, BitballPowerUp, KnuckleClawsPowerUp]
    ValidSkills = [x for x in EnhanceClassList if x not in InvalidSkillEnhancements]
    Common, Rare, Legendary = 0, 1, 2
    with open("./XC2/JsonOutputs/common/ITM_PcWpnChip.json", 'r+', encoding='utf-8') as file: # Assigns weapons to groups based on category
        data = json.load(file)
        for row in data["rows"]:
            for i in range(1, 37):
                WeaponStrengthList[row["Rank"] - 1].append(row[f"CreateWpn{i}"])
            WeaponStrengthNameList[row["Rank"] - 1].append(row["Name"])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common_ms/itm_pcwpnchip_ms.json", 'r+', encoding='utf-8') as file: # Renames chips according to their rank
        data = json.load(file)
        for row in data["rows"]:
            for rank in range(len(WeaponStrengthNameList)):
                if row["$id"] in WeaponStrengthNameList[rank]:
                    row["name"] = f"{row["name"]} [System:Color name=red]({rank + 1})[/System:Color]"
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common/ITM_PcWpn.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            for i in range(0, len(WeaponStrengthList)):
                if row["$id"] in WeaponStrengthList[i]:
                    row["Damage"] = random.randrange(WeaponDamageRanges[i][0], WeaponDamageRanges[i][1])
                    if row["Rank"] <= 7:
                        curEnh:Enhancement = random.choice(ValidSkills)
                        while curEnh.Caption > 256: # This is needed because the chips descriptions will not load properly they overflow if a caption is above 256. Super annoying the effects work the caption doesnt.
                            curEnh = random.choice(ValidSkills)
                        curEnh.RollEnhancement(Common, 1.1 + 0.05*(row["Rank"]-5))
                        row["Enhance1"] = curEnh.id
                    elif row["Rank"] <= 14:
                        curEnh:Enhancement = random.choice(ValidSkills)
                        while curEnh.Caption > 256: # This is needed because the chips descriptions will not load properly they overflow if a caption is above 256. Super annoying the effects work the caption doesnt.
                            curEnh = random.choice(ValidSkills)
                        curEnh.RollEnhancement(Rare, 1.1 + 0.05*(row["Rank"]-12))
                        row["Enhance1"] = curEnh.id
                    else:
                        curEnh:Enhancement = random.choice(ValidSkills)
                        while curEnh.Caption > 256: # This is needed because the chips descriptions will not load properly they overflow if a caption is above 256. Super annoying the effects work the caption doesnt.
                            curEnh = random.choice(ValidSkills)
                        curEnh.RollEnhancement(Legendary, 1.1 + 0.05*(row["Rank"]- 17))
                        row["Enhance1"] = curEnh.id
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def AddDLCRewards(ChosenAreaOrder):
    BountyCollectionRewards = Helper.InclRange(1, 10)
    StartingDLCItemTextRow = Helper.GetMaxValue("./XC2/JsonOutputs/common_ms/menu_dlc_gift.json", "$id") + 1
    with open("./XC2/JsonOutputs/common/MNU_DlcGift.json", 'r+', encoding='utf-8') as file: #edits DLC items
        data = json.load(file)
        for i in range(0, len(BountyCollectionRewards)):
            for row in data["rows"]:
                if row["$id"] == BountyCollectionRewards[i]:
                    row["releasecount"] = 1
                    row["item_id"] = 25479 + i
                    row["category"] = 1
                    row["value"] = 4
                    row["disp_item_info"] = 0
                    row["condition"] = UMHuntEnableCondListIDs[i]
                    row["title"] = StartingDLCItemTextRow + i
                    break
        if len(ChosenAreaOrder) != len(BountyCollectionRewards):
            for i in range(len(ChosenAreaOrder), len(BountyCollectionRewards)):
                for row in data["rows"]:
                    if row["$id"] == BountyCollectionRewards[i]:
                        row["condition"] = UMHuntDisableCondListID
        del data["rows"][21:]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common_ms/menu_dlc_gift.json", 'r+', encoding='utf-8') as file: #edits DLC items
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 8:
                row["name"] = "[System:Color name=green]Bounty Token[/System:Color] Rewards"
            if row["$id"] == 9:
                row["name"] = "Poppiswap Crafting Materials"
            if row["$id"] == 10:
                row["name"] = "Starting Item Receivals"
        for i in range(0, 10):
            data["rows"].append({"$id": StartingDLCItemTextRow + i, "style": 162, "name": f"[System:Color name=green]Bounty Token[/System:Color] Rewards, Set {i+1}"})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)




# ------ Shop Setup ------




def CustomShopSetup(ChosenAreaOrder): # Sets up the custom shops with loot
    
    # Shop Item Setup
    ReceiptTextChanges()
    WPAdjustments()
    ChipShopRewards() 
    AuxCoreRewards()
    PouchItemRewards()
    AccessoryShopRewards()
    PoppiswapShopRewards()
    GambaShopRewards()
    AddSPManual()

    # List of Shops
    # Sanity Checks: The number of items in InputTaskIDs should always be less than 16
    # The number of SetItem1IDs, RewardIDs, RewardNames, RewardSP, and RewardXP should all be the same, and also equal to the number of non-zero InputTaskIDs
    # Reward IDs, RewardQtys should have same number of values in each list as SetItem1IDs, however, each list should be made up of 4 lists, 1 for each item slot that a reward can be

    MultipleShopList = [CoreCrystalShop, GambaShop, WeaponChipShop, AuxCoreShop, DriverAccessoryShop, PouchItemShop] # these can get duplicated
    ShopList = [TokenExchangeShop, WPManualShop, PoppiswapShop] # these don't get duplicated
    for shop in ShopList:
        shop["Condition"] = UMHuntEnableCondListIDs[0]
    CurMapRowID = Helper.GetMaxValue("./XC2/JsonOutputs/common_gmk/ma02a_FLD_NpcPop.json", "$id") + 1
    CopyUsedShopIDs = UsedShopIDs.copy()
    CopyUnusedBazaarNPCRowIDs = UnusedBazaarNPCRowIDs.copy()
    CopyFullUnusedShopList = FullUnusedShopList.copy()
    for shop in MultipleShopList:
        for i in range(len(ChosenAreaOrder)):
            with open("./XC2/JsonOutputs/common_gmk/ma02a_FLD_NpcPop.json", 'r+', encoding='utf-8') as file:
                data = json.load(file)
                for row in data["rows"]:
                    if row["$id"] == shop["ChosenMapRowID"]:
                        rowtocopy = row.copy()
                        break
                rowtocopy["Condition"] = OneScenarioConditionList[i]
                rowtocopy["$id"] = CurMapRowID
                data["rows"].append(rowtocopy)
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=2, ensure_ascii=False)
            NewShop = ShopLootGeneration(i, shop)
            NewShop["ChosenMapRowID"] = CurMapRowID
            CurMapRowID += 1
            NewShop["Condition"] = OneScenarioConditionList[i]
            CopyUsedShopIDs.append(CopyFullUnusedShopList[0])
            NewShop["ShopIDtoReplace"] = CopyFullUnusedShopList[0]
            CopyFullUnusedShopList.pop(0)
            NewShop["ChosenMapRowID"] = CopyUnusedBazaarNPCRowIDs[0]
            CopyUnusedBazaarNPCRowIDs.pop(0)
            ShopList.append(NewShop.copy())
    ShopCreator(ShopList, True)

def ReceiptTextChanges(): # Changes the test for the Core Crystal Shop Receipts
    ProofofPurchaseNameIDs = Helper.InclRange(617, 632)
    ProofofPurchaseNameTexts = ["ATK 1 Receipt", "ATK 2 Receipt", "ATK 3 Receipt", "ATK 4 Receipt", "TNK 1 Receipt", "TNK 2 Receipt", "TNK 3 Receipt", "HLR 1 Receipt", "HLR 2 Receipt", "HLR 3 Receipt", "DLC 1 Receipt", "DLC 2 Receipt", "DLC 3 Receipt", "NG+ 1 Receipt", "NG+ 2 Receipt", "NG+ 3 Receipt"]
    ProofofPurchaseDescriptionIDs = Helper.InclRange(718, 733)
    ProofofPurchaseDescriptionText = "Proof you purchased this Blade Bundle."
    with open("./XC2/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in ProofofPurchaseIDs: # Proof of Purchases for Core Crystal Bundles
                row["ValueMax"] = 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes name text file
        data = json.load(file)
        for i in range(0, len(ProofofPurchaseIDs)):
            for row in data["rows"]:
                if row["$id"] == ProofofPurchaseNameIDs[i]:
                    row["name"] = ProofofPurchaseNameTexts[i]
                if row["$id"] == ProofofPurchaseDescriptionIDs[i]:
                    row["name"] = ProofofPurchaseDescriptionText
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def WPAdjustments(): # Changes how much a weapon manual gives, and how much is needed to max an art
    Helper.ColumnAdjust("./XC2/JsonOutputs/common/BTL_Arts_Dr.json", ["NeedWP2"], 250) # 250 to upgrade each level
    Helper.ColumnAdjust("./XC2/JsonOutputs/common/BTL_Arts_Dr.json", ["NeedWP3"], 250)
    Helper.ColumnAdjust("./XC2/JsonOutputs/common/BTL_Arts_Dr.json", ["NeedWP4"], 250)
    Helper.ColumnAdjust("./XC2/JsonOutputs/common/BTL_Arts_Dr.json", ["NeedWP5"], 250)
    with open("./XC2/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 25405:
                row["Type"] = 250 # Changed the amount of WP it gives to 250
                continue
            if row["$id"] == 25406:
                row["Type"] = 500
                continue
            if row["$id"] == 25407:
                row["Type"] = 1000
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes names of WP Boosting Items
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 715:
                row["name"] = "250 WP Booster"
                continue
            if row["$id"] == 716:
                row["name"] = "500 WP Booster"
                continue
            if row["$id"] == 717:
                row["name"] = "1000 WP Booster"
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def ChipShopRewards():
    ChipStrengthLists = Helper.ExtendListtoLength([], 20, "[]")
    global ChipBundleNames, ChipShopRewardDistribution, ChipShopCostList
    ChipBundleNames, ChipShopCostList, ChipShopRewardDistribution = [], [], []
    NumTrades = WeaponChipShop["TradeCount"]
    Chips4 = Helper.ExtendListtoLength([], NumTrades, "0")
    with open("./XC2/JsonOutputs/common/ITM_PcWpnChip.json", 'r+', encoding='utf-8') as file: # Assigns weapons to groups based on category
        data = json.load(file)
        for row in data["rows"]:
            ChipStrengthLists[row["Rank"] - 1].append(row["$id"])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    for set in range(SetCount): # Now we put the chips in groups according to strength
        SetCosts, SetNames = [], []
        Chips1, Chips2, Chips3 = Helper.ExtendListtoLength([0], NumTrades, "0"), Helper.ExtendListtoLength([0], NumTrades, "0"), Helper.ExtendListtoLength([0], NumTrades, "0")
        for tradenum in range(NumTrades - 1): # for every trade except the last, we only want to pick from a set pool
            Chips1[tradenum] = random.choice(ChipStrengthLists[min(set + tradenum, 19)])
            Chips2[tradenum] = random.choice(ChipStrengthLists[min(set + tradenum, 19)])
            Chips3[tradenum] = random.choice(ChipStrengthLists[min(set + tradenum, 19)])
            SetNames.append(f"Rank {set + tradenum + 1} Chip Bundle")
            SetCosts.append(random.randint(max(1, round((set + 1) * 10 + (tradenum - 3) * 7 - 5)), max(1, min(200, (set + 1) * 10 + (tradenum - 3) * 7 + 5))))
            if tradenum < 3:
                SetCosts[tradenum] = round(SetCosts[tradenum] * 0.8**(2 - tradenum))
        # for the last trade, we want random chips from a larger pool, and we only want 2 chips, instead of 3
        SetCosts.append(random.randint(max(set * 9, 5), max(set * 15, 10))) # the last trade in the set should always cost in this range
        SetNames.append("Powerful Chips")
        if set >= 7: # only for the last few rounds can we have chips from the highest damage pool in the final reward
            Chips1[NumTrades - 1] = random.choice(ChipStrengthLists[set + 8] + ChipStrengthLists[set + 9] + ChipStrengthLists[set + 10])
            Chips2[NumTrades - 1] = random.choice(ChipStrengthLists[set + 8] + ChipStrengthLists[set + 9] + ChipStrengthLists[set + 10])
            Chips3[NumTrades - 1] = 0
        else:
            Chips1[NumTrades - 1] = random.choice(ChipStrengthLists[random.randint(set + 3, set + 7)])
            Chips2[NumTrades - 1] = random.choice(ChipStrengthLists[random.randint(set + 3, set + 7)])
            Chips3[NumTrades - 1] = 0
        ChipShopRewardDistribution.append([Chips1, Chips2, Chips3, Chips4])
        ChipShopCostList.append(SetCosts)
        ChipBundleNames.append(SetNames)

def AuxCoreRewards(): # Makes the Aux Core Bundles
    global AuxCoreShopRewardDistribution, AuxCoreShopCostDistribution, AuxCoreNameDistribution, SecretAuxCoreIDs
    AuxCoreShopRewardDistribution, AuxCoreShopCostDistribution, AuxCoreNameDistribution, SecretAuxCoreIDs = [], [], [], []
    AuxCoreTypeGroups = {
        "Damage": [TitanDamageUp, MachineDamageUp, HumanoidDamageUp, AquaticDamageUp, AerialDamageUp, InsectDamageUp, BeastDamageUp, BladeComboDamUp, FusionComboDamUp, CritDamageUp, PercentDoubleAuto, FrontDamageUp, SideDamageUp, BackDamageUp, SmashDamageUp, HigherLVEnemyDamageUp, AllyDownDamageUp, BattleDurationDamageUp, LV1Damage, LV2Damage, LV3Damage, LV4Damage, IndoorsDamageUp, OutdoorsDamageUp, DamageUpOnEnemyKill, DoubleHitExtraAutoDamage, ToppleANDLaunchDamageUp, PartyDamageMaxAffinity, PartyCritMaxAffinity, AutoAttackCancelDamageUp, AggroedEnemyDamageUp, Transmigration, OppositeGenderBladeDamageUp, KaiserZone, AffinityMaxAttack, VersusBossUniqueEnemyDamageUp, AutoSpeedArtsSpeed, DamageUpOnCancel, DamageAndCritUpMaxAffinity, FlatCritBoost],
        "Defensive": [HPLowEvasion, HPLowBlockRate, ReduceSpikeDamage, SpecialAndArtsAggroDown, AggroPerSecondANDAggroUp, AffinityMaxBarrier, AffinityMaxEvade, LowHPRegen, AllDebuffRes, BladeArtsTriggerUp, BladeArtDuration, HunterChem, ShoulderToShoulder, WhenDiesHealAllies, SmallHpPotCreate, Twang, Jamming, PotionEffectUp, EtherCounter, PhysCounter, RechargeOnEvade, PartyDamageReducMaxAffinity, PhyAndEthDefenseUp, ReduceEnemyChargeMaxAffinity, GravityPinwheel, RestoreHitDamageToParty, ForeSight, FlatBlockBoost],
        "Playstyle Defining": [SpecialRechargeCancelling, EnemyDropGoldOnHit, DealTakeMore, AwakenPurge, BurstDestroyAnotherOrb, AttackUpGoldUp, DidIDoThat, CritHeal, PartyGaugeCritFill, GlassCannon, CombatMoveSpeed, DestroyOrbOpposingElement, TargetNearbyOrbsChainAttack, PartyGaugeDriverArtFill, RecoverRechargeCrit, DealMoreTakeLessMaxAffinity, HpPotChanceFor2, BladeComboOrbAdder, PotionPickupDamageUp, Vision, DamageUpPerCrit, HealingUpMaxAffinity, TakeDamageHeal, StopThinking, ChainAttackPower, DamagePerEvadeUp]
    }
    Common, Rare, Legendary = 0, 1, 2
    # starting odds, changes
    # common, rare, legendary
    SecretAuxCores = [UMFlatCritBoost, UMSurpriseAttackUp, UMSpecialRecievesAfterImage, UMAutoSpeedArtsSpeed, UMPhyAndEthDefenseUp, UMOnBlockNullDamage, UMFlatBlockBoost]
    NumTrades = DriverAccessoryShop["TradeCount"]
    RarityOdds = [85, 10, 5]
    AllRarities, AllAugments, AllMultipliers, AllSets, AllTypes = [], [], [], [], [] # i really could have just made this a dictionary, but i don't do anything except parse the list, so whatever
    for setnum in range(SetCount):
        ChosenAugments = []
        ChosenTypes = []
        match setnum:
            case setnum if setnum <= 4:
                RarityOdds = [RarityOdds[0] - 12, RarityOdds[1] + 10, RarityOdds[2] + 2]
            case _:
                RarityOdds = [RarityOdds[0] - 4, RarityOdds[1] - 8, RarityOdds[2] + 12]
        ChosenRarities = random.choices([Common, Rare, Legendary], weights = RarityOdds, k = NumTrades)
        ChosenAugments.extend(random.choices(AuxCoreTypeGroups["Damage"], k = NumTrades//3))
        ChosenAugments.extend(random.choices(AuxCoreTypeGroups["Defensive"], k = NumTrades//3))
        ChosenAugments.extend(random.choices(AuxCoreTypeGroups["Playstyle Defining"], k = NumTrades//3))
        ChosenMultipliers = Helper.ExtendListtoLength([0.75 + (setnum + 1) * 0.05], NumTrades, "inputlist[i-1]")
        ChosenTypes = ["Damage", "Damage", "Damage", "Defensive", "Defensive", "Defensive", "Playstyle Defining", "Playstyle Defining", "Playstyle Defining"] # grug smash keyboard and type out by hand
        AllSets.extend(Helper.ExtendListtoLength([setnum], NumTrades, "inputlist[i-1]"))
        AllRarities.extend(ChosenRarities)
        AllAugments.extend(ChosenAugments)
        AllTypes.extend(ChosenTypes)
        AllMultipliers.extend(ChosenMultipliers)

    with open("./XC2/JsonOutputs/common/ITM_OrbEquip.json", 'r+', encoding='utf-8') as file: 
        with open("./XC2/JsonOutputs/common_ms/itm_orb.json", 'r+', encoding='utf-8') as namefile:
    
            namedata = json.load(namefile) 
            data = json.load(file)

            for i in range(len(AllRarities)):
                for row in data["rows"]:
                    if row["$id"] == 17001 + i:
                        curAuxCore:Enhancement = AllAugments[i]
                        curAuxCore.RollEnhancement(AllRarities[i], AllMultipliers[i])
                        row["Enhance"] = curAuxCore.id
                        row["Rarity"] = curAuxCore.Rarity
                        row["EnhanceCategory"] = i
                        CurName = row["Name"]
                        break
                for namerow in namedata["rows"]:  
                    if namerow["$id"] == CurName:    
                        namerow["name"] = f"{curAuxCore.name} Core"
                        break
            for i in range(len(SecretAuxCores)):
                for row in data["rows"]:
                    if row["$id"] == 17000 + len(AllRarities) + i:
                        curAuxCore:UMHuntSecretShopEnhancements = SecretAuxCores[i]
                        curAuxCore.RollEnhancement(2, 1)
                        row["Enhance"] = curAuxCore.id
                        row["Rarity"] = curAuxCore.Rarity
                        row["EnhanceCategory"] = len(AllRarities) + i
                        CurName = row["Name"]
                        SecretAuxCoreIDs.append(row["$id"])
                        break
                for namerow in namedata["rows"]:  
                    if namerow["$id"] == CurName:    
                        namerow["name"] = f"{curAuxCore.name} Core"
                        break
            namefile.seek(0)
            namefile.truncate()
            json.dump(namedata, namefile, indent=2, ensure_ascii=False)

        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    
    # getting the costs
    AllAuxCoreCosts, AllAuxCoreNames = [], []
    for i in range(len(AllRarities)):
        CurRarity = AllRarities[i]
        CurType = AllTypes[i]
        NameString = ""
        match CurRarity:
            case 0: # Common
                AllAuxCoreCosts.append(random.randint(2, 5) + AllSets[i])
                NameString += "Common"
            case 1: # Rare
                AllAuxCoreCosts.append(random.randint(5, 10) + round(AllSets[i]*1.5))
                NameString += "[System:Color name=red]Rare[/System:Color]"
            case 2: # Legendary
                AllAuxCoreCosts.append(random.randint(11, 16) + round(AllSets[i]*2))
                NameString += "[System:Color name=tutorial]Legendary[/System:Color]"
        match CurType:
            case "Damage":
                NameString += " Damage"
            case "Defensive":
                NameString += " Defensive"
            case "Playstyle Defining":
                NameString += " Unique"
        AllAuxCoreNames.append(NameString)
    for setnum in range(SetCount):
        CurAuxCoreNames, CurAuxCoreCosts = [], []
        for i in range(len(AllSets)):
            if AllSets[i] == setnum:
                CurAuxCoreNames.append(AllAuxCoreNames[i])
                CurAuxCoreCosts.append(AllAuxCoreCosts[i])
        AuxCoreNameDistribution.append(CurAuxCoreNames)
        AuxCoreShopCostDistribution.append(CurAuxCoreCosts)
        AuxCoreShopRewardDistribution.append(Helper.ExtendListtoLength([17001 + (setnum * NumTrades)], NumTrades, "inputlist[i-1] + 1"))

def PouchItemRewards():
    global PouchItemShopRewardDistribution, PouchItemShopCostDistribution, PouchItemNameDistribution, SecretPouchItemIDs
    PouchItemShopRewardDistribution, PouchItemShopCostDistribution, PouchItemNameDistribution, SecretPouchItemIDs = [], [], [], []
    global ValidPouchItemsUMHunt
    ValidPouchItemsUMHunt = [x for x in IDs.PouchItems if x not in [40314, 40428]]
    Cheap, Quality, Cuisine, Michelin = 5, 10, 15, 55 # these are the base costs for a given pouch item (Michelin is there for the custom pouch items)
    PouchFoodTypetoCostName = {12: [Quality, "Staple Foods"], 13: [Cheap, "Vegetables"], 14: [Cheap, "Meat"], 15: [Cheap, "Seafood"], 16: [Cuisine, "Desserts"], 17: [Cuisine, "Drinks"], 18: [Cuisine, "Instruments"], 19: [Quality, "Art"], 20: [Quality, "Literature"], 21: [Cuisine, "Board Games"], 22: [Quality, "Cosmetics"], 23: [Cheap, "Textiles"], 24: [Michelin, "Secret"]}
    NumTrades = PouchItemShop["TradeCount"]
    NewPouchItemRow = Helper.GetMaxValue("./XC2/JsonOutputs/common/ITM_FavoriteList.json", "$id") + 1
    NewPouchItemNameRow = Helper.GetMaxValue("./XC2/JsonOutputs/common_ms/itm_favorite.json", "$id") + 1
    NewPouchBuffRow = Helper.GetMaxValue("./XC2/JsonOutputs/common/BTL_PouchBuffSet.json", "$id") + 1
    SecretPouchItemIDs = Helper.InclRange(NewPouchItemRow, NewPouchItemRow + 4)
    PouchItemStatCaps = {1: 50.0, 2: 50.0, 3: 30.0, 4: 30.0, 5: 1.0, 6: 50.0, 7: 300.0, 8: 50.0, 9: 50.0, 10: 8.0, 11: 100.0, 12: 100.0}
    AllItemTypeList = []
    with open("./XC2/JsonOutputs/common/ITM_FavoriteList.json", 'r+', encoding='utf-8') as file: 
        data = json.load(file)
        for i in range(0, 5): # we want to add room for our custom pouch items
            data["rows"].append({"$id": NewPouchItemRow + i, "Name": NewPouchItemNameRow + i, "Caption": 0, "Category": 24, "Zone": 3, "Rarity": 2, "Price": 0, "Type": NewPouchBuffRow + i, "Time": 60, "ValueMax": 10, "TrustPoint": 0, "sortJP": 0, "sortGE": 0, "sortFR": 0, "sortSP": 0, "sortIT": 0, "sortGB": 0, "sortCN": 0, "sortTW": 0, "sortKR": 0})
            ValidPouchItemsUMHunt.append(NewPouchItemRow + i) # we need to add our custom pouch items to the valid ids
        for i in range(12, 25): # this gets the type of each pouch item
            CurrentItemTypeList = []
            for row in data["rows"]:
                if (row["Category"] == i) & (row["$id"] in ValidPouchItemsUMHunt):
                    CurrentItemTypeList.append(row["$id"])
                    if i == 24: # we want to remove the custom category, since we already put it in a bucket correctly, and the game won't recognize the custom category
                        row["Category"] = random.randint(12, 23)
            AllItemTypeList.append(CurrentItemTypeList)
        PouchItem3IDs, PouchItem4IDs = Helper.ExtendListtoLength([0], NumTrades, "0"), Helper.ExtendListtoLength([0], NumTrades, "0")
        for setnum in range(SetCount):
            PouchItem1IDs, PouchItem2IDs = [], []
            PouchItemTypes = random.choices(Helper.InclRange(12, 24), k = NumTrades)
            for trade in range(NumTrades):
                ChosenPouchItems = random.choices(AllItemTypeList[PouchItemTypes[trade] - 12], k = 2)
                PouchItem1IDs.append(ChosenPouchItems[0])
                PouchItem2IDs.append(ChosenPouchItems[1])
            PouchItemShopCostDistribution.append([PouchFoodTypetoCostName[key][0] for key in PouchItemTypes])
            PouchItemNameDistribution.append([PouchFoodTypetoCostName[key][1] for key in PouchItemTypes])
            PouchItemShopRewardDistribution.append([PouchItem1IDs, PouchItem2IDs, PouchItem3IDs, PouchItem4IDs])
        for row in data["rows"]: # Change the duration of all to 60 minutes, and they all give no trust points
            row["Time"] = 60
            row["ValueMax"] = 10
            row["TrustPoint"] = 0
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common_ms/itm_favorite.json", 'r+', encoding='utf-8') as file: # Giving the new pouch items names
        data = json.load(file)
        for i in range(0, len(SecretPouchItemIDs)):
                data["rows"].append({"$id": NewPouchItemNameRow + i, "style": 36, "name": f"[System:Color name=tutorial]Superfood {i+1}[/System:Color]"})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common/BTL_PouchBuffSet.json", 'r+', encoding='utf-8') as file: # Giving the new pouch items their buffs
        data = json.load(file)
        for i in range(0, len(SecretPouchItemIDs)):
            BuffChoices = random.sample(Helper.InclRange(1, 12), 3)
            data["rows"].append({"$id": NewPouchBuffRow + i, "PBuff1": BuffChoices[0], "PBuffParam1": PouchItemStatCaps[BuffChoices[0]], "PBuff2": BuffChoices[1], "PBuffParam2": PouchItemStatCaps[BuffChoices[1]], "PBuff3": BuffChoices[2], "PBuffParam3": PouchItemStatCaps[BuffChoices[2]]})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def AccessoryShopRewards(): # Creates the accessory shop
    global AccessoryShopRewardDistribution, AccessoryShopCostDistribution, AccessoryNameDistribution, SecretAccessoryIDs
    AccessoryShopRewardDistribution, AccessoryShopCostDistribution, AccessoryNameDistribution, SecretAccessoryIDs = [], [], [], []
    AccessoryTypeGroups = {
        "Damage": [TitanDamageUp, MachineDamageUp, HumanoidDamageUp, AquaticDamageUp, AerialDamageUp, InsectDamageUp, BeastDamageUp, CritDamageUp, PercentDoubleAuto, FrontDamageUp, SideDamageUp, BackDamageUp, SmashDamageUp, HigherLVEnemyDamageUp, AllyDownDamageUp, BattleDurationDamageUp,IndoorsDamageUp, OutdoorsDamageUp, DamageUpOnEnemyKill, DoubleHitExtraAutoDamage, ToppleANDLaunchDamageUp, AutoAttackCancelDamageUp, AggroedEnemyDamageUp, Transmigration, OppositeGenderBladeDamageUp, BladeSwitchDamageUp, BreakResDown,KaiserZone, VersusBossUniqueEnemyDamageUp, AutoSpeedArtsSpeed, DamageUpOnCancel, FlatStrengthBoost, FlatEtherBoost],
        "Defensive": [HPLowEvasion, HPLowBlockRate, ReduceSpikeDamage, SpecialAndArtsAggroDown, AggroPerSecondANDAggroUp, LowHPRegen, AllDebuffRes, TastySnack, DoomRes, TauntRes, BladeShackRes, DriverShackRes, WhenDiesHealAllies, SmallHpPotCreate, Twang, Jamming, PotionEffectUp, EtherCounter, PhysCounter, RechargeOnEvade, FlatHPBoost, ArtUseHeal, AgiBoost,GravityPinwheel, RestoreHitDamageToParty, ForeSight, FlatAgiBoost, HPBoost, CritHeal],
        "Playstyle Defining": [SpecialRechargeCancelling, EnemyDropGoldOnHit, DealTakeMore, AwakenPurge, BurstDestroyAnotherOrb, AttackUpGoldUp, DidIDoThat,CritHeal, PartyGaugeCritFill, GlassCannon, CombatMoveSpeed, DestroyOrbOpposingElement, TargetNearbyOrbsChainAttack, PartyGaugeDriverArtFill,RecoverRechargeCrit, HpPotChanceFor2, BladeComboOrbAdder, PotionPickupDamageUp, Vision, DamageUpPerCrit, TakeDamageHeal, DamagePerEvadeUp, PartyHealBladeSwitch, LowHPSpecialUp]
    }
    Common, Rare, Legendary = 0, 1, 2
    # starting odds, changes
    # common, rare, legendary
    SecretAccessories = [UMAllWeaponAttackUp, UMSpecialRechargeCancelling, UMHigherLVEnemyDamageUp, UMVision, UMBreakResDown, UMStrengthBoost, UMEtherBoost]
    NumTrades = DriverAccessoryShop["TradeCount"]
    RarityOdds = [85, 10, 5]
    AllRarities, AllAugments, AllMultipliers, AllSets, AllTypes = [], [], [], [], [] # i really could have just made this a dictionary, but i don't do anything except parse the list, so whatever
    for setnum in range(SetCount):
        ChosenAugments = []
        ChosenTypes = []
        match setnum:
            case setnum if setnum <= 4:
                RarityOdds = [RarityOdds[0] - 12, RarityOdds[1] + 10, RarityOdds[2] + 2]
            case _:
                RarityOdds = [RarityOdds[0] - 4, RarityOdds[1] - 8, RarityOdds[2] + 12]
        ChosenRarities = random.choices([Common, Rare, Legendary], weights = RarityOdds, k = NumTrades)
        ChosenAugments.extend(random.choices(AccessoryTypeGroups["Damage"], k = NumTrades//3))
        ChosenAugments.extend(random.choices(AccessoryTypeGroups["Defensive"], k = NumTrades//3))
        ChosenAugments.extend(random.choices(AccessoryTypeGroups["Playstyle Defining"], k = NumTrades//3))
        ChosenMultipliers = Helper.ExtendListtoLength([0.75 + (setnum + 1) * 0.05], NumTrades, "inputlist[i-1]")
        ChosenTypes = ["Damage", "Damage", "Damage", "Defensive", "Defensive", "Defensive", "Playstyle Defining", "Playstyle Defining", "Playstyle Defining"] # grug smash keyboard and type out by hand
        AllSets.extend(Helper.ExtendListtoLength([setnum], NumTrades, "inputlist[i-1]"))
        AllRarities.extend(ChosenRarities)
        AllAugments.extend(ChosenAugments)
        AllTypes.extend(ChosenTypes)
        AllMultipliers.extend(ChosenMultipliers)

    AccessoryTypesandNames = { # What icon should go with what noun:
        0:["Sandals", "Crocs", "Jordans", "Boots", "Sneakers"], 
        1:["Baseball Cap", "Sweatband", "Beanie", "Earmuffs"], 
        2:["Vest", "Tuxedo", "T-Shirt", "Tank Top", "Jacket"], 
        3:["Choker", "Necklace", "Locket", "Tie"], 
        4:["Belt", "Sash", "Scarf"], 
        5:["Banner", "Loincloth", "Swimsuit", "Thread", "Lamp", "Incense"], 
        6:["Gloves", "Silly Bandz", "Gauntlets", "Bangles", "Watches"],
        7:["Cube", "AirPods", "Headphones", "Hard Drive", "Attachment"],
        8:["Garnet", "Sapphire", "Diamond", "Ruby", "Emerald", "Prismarine"],
        9:["Feather", "Medal", "Bling"]
    }

    with open("./XC2/JsonOutputs/common/ITM_PcEquip.json", 'r+', encoding='utf-8') as file: 
        with open("./XC2/JsonOutputs/common_ms/itm_pcequip.json", 'r+', encoding='utf-8') as namefile:
    
            namedata = json.load(namefile) 
            data = json.load(file)

            for i in range(len(AllRarities)):
                for row in data["rows"]:
                    if row["$id"] == 1 + i:
                        curAccessory:Enhancement = AllAugments[i]
                        curAccessory.RollEnhancement(AllRarities[i], AllMultipliers[i])
                        row["Enhance1"] = curAccessory.id
                        row["Rarity"] = curAccessory.Rarity
                        ItemType = random.randint(0,9)
                        row["Icon"] = ItemType
                        CurName = row["Name"]
                        break
                for namerow in namedata["rows"]:  
                    if namerow["$id"] == CurName:
                        lastWord = random.choice(AccessoryTypesandNames[ItemType])
                        namerow["name"] = f"{curAccessory.name} {lastWord}"
                        break
            for i in range(len(SecretAccessories)):
                for row in data["rows"]:
                    if row["$id"] == 1 + len(AllRarities) + i:
                        curAccessory:UMHuntSecretShopEnhancements = SecretAccessories[i]
                        curAccessory.RollEnhancement(2, 1)
                        row["Enhance1"] = curAccessory.id
                        row["Rarity"] = curAccessory.Rarity
                        ItemType = random.randint(0,9)
                        CurName = row["Name"]
                        row["Icon"] = ItemType
                        SecretAccessoryIDs.append(row["$id"])
                        break
                for namerow in namedata["rows"]:  
                    if namerow["$id"] == CurName:
                        lastWord = random.choice(AccessoryTypesandNames[ItemType])
                        namerow["name"] = f"{curAccessory.name} {lastWord}"
                        break
            namefile.seek(0)
            namefile.truncate()
            json.dump(namedata, namefile, indent=2, ensure_ascii=False)

        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    
    # getting the costs
    AllAccessoryCosts, AllAccessoryNames = [], []
    for i in range(len(AllRarities)):
        CurRarity = AllRarities[i]
        CurType = AllTypes[i]
        NameString = ""
        match CurRarity:
            case 0: # Common
                AllAccessoryCosts.append(random.randint(2, 5) + AllSets[i])
                NameString += "Common"
            case 1: # Rare
                AllAccessoryCosts.append(random.randint(5, 10) + round(AllSets[i]*1.5))
                NameString += "[System:Color name=red]Rare[/System:Color]"
            case 2: # Legendary
                AllAccessoryCosts.append(random.randint(11, 16) + round(AllSets[i]*2))
                NameString += "[System:Color name=tutorial]Legendary[/System:Color]"
        match CurType:
            case "Damage":
                NameString += " Damage"
            case "Defensive":
                NameString += " Defensive"
            case "Playstyle Defining":
                NameString += " Unique"
        AllAccessoryNames.append(NameString)
    for setnum in range(SetCount):
        CurAccessoryNames, CurAccessoryCosts = [], []
        for i in range(len(AllSets)):
            if AllSets[i] == setnum:
                CurAccessoryNames.append(AllAccessoryNames[i])
                CurAccessoryCosts.append(AllAccessoryCosts[i])
        AccessoryNameDistribution.append(CurAccessoryNames)
        AccessoryShopCostDistribution.append(CurAccessoryCosts)
        AccessoryShopRewardDistribution.append(Helper.ExtendListtoLength([1 + (setnum * NumTrades)], NumTrades, "inputlist[i-1] + 1"))

def PoppiswapShopRewards(): # Creates rewards for Poppiswap Shop
    CrystalRows = Helper.InclRange(11, 21)
    StartingCondListRow = Helper.GetMaxValue("./XC2/JsonOutputs/common/FLD_ConditionList.json", "$id") + 1
    StartingItemCondRow = Helper.GetMaxValue("./XC2/JsonOutputs/common/FLD_ConditionItem.json", "$id") + 1
    StartingDLCItemTextRow = Helper.GetMaxValue("./XC2/JsonOutputs/common_ms/menu_dlc_gift.json", "$id") + 1
    CrystalVoucherNameIDs = Helper.InclRange(633, 643)
    CrystalVoucherCaptionIDs = Helper.InclRange(734, 744)
    with open("./XC2/JsonOutputs/common/FLD_ConditionList.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, 11): # ConditionType of 5 is "Item", meaning you need that item listed in FLD_ConditionItem
            data["rows"].append({"$id": StartingCondListRow + i, "Premise": 0, "ConditionType1": 5, "Condition1": StartingItemCondRow + i, "ConditionType2": 0, "Condition2": 0, "ConditionType3": 0, "Condition3": 0, "ConditionType4": 0, "Condition4": 0, "ConditionType5": 0, "Condition5": 0, "ConditionType6": 0, "Condition6": 0, "ConditionType7": 0, "Condition7": 0, "ConditionType8": 0, "Condition8": 0})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common/FLD_ConditionItem.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, 11):
            data["rows"].append({"$id": StartingItemCondRow + i, "ItemCategory": 0, "ItemID": 25322 + i, "Number": 1})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes names of Contracts
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] >= 633:
                for i in range(0, len(CrystalVoucherNameIDs)):
                    if row["$id"] == CrystalVoucherNameIDs[i]:
                        row["name"] = f"Ether Crystal Pack {i+1}"
                    if row["$id"] == CrystalVoucherCaptionIDs[i]:
                        row["name"] = f"Unlocks a DLC {1000*(i+1)}\n Ether Crystal Reward"
            if row["$id"] >= 745:
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common/MNU_DlcGift.json", 'r+', encoding='utf-8') as file: #edits DLC items
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in CrystalRows:
                row["releasecount"] = 2
                row["item_id"] = 0
                row["category"] = 3
                row["value"] = 1000*(row["$id"] - 10)
                row["disp_item_info"] = 0
                row["condition"] = StartingCondListRow + (row["$id"] - 11)
                row["title"] = StartingDLCItemTextRow + (row["$id"] - 11)
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common_ms/menu_dlc_gift.json", 'r+', encoding='utf-8') as file: #edits DLC items
        data = json.load(file)
        for i in range(0, 11):
            data["rows"].append({"$id": StartingDLCItemTextRow + i, "style": 162, "name": f"Poppiswap Crafting Materials Rank {i+1}"})
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def GambaShopRewards(): # Makes the rewards for the gamba shop
    global GambaShopQtyList, GambaShopCostList, GambaShopRewardList
    GambaShopCostList, GambaShopQtyList, GambaShopRewardList = [], [], []
    CopyofGambaShopReceiptIDs = GambaShopReceiptIDs.copy()
    FillerRewardSet = [0,0,0]
    for i in range(0, SetCount):
        RewardSet = []
        Costs = [2 + 2*i, 5 + 3*i, 10 + 6*i] # Small, Medium, Large
        for bet in Costs:
            Reward = random.choices([0.25*bet, 0.5*bet, bet, 1.5*bet, 2*bet, 3*bet, 5*bet], weights=[30, 20, 15, 15, 10, 5, 5], k = 1)[0] # 50% chance to lose tokens, 50% chance to make winnings back + some in theory, but can be better or worse depending on rolled values
            Reward = round(int(Reward))
            if Reward > 255:
                Reward = 255
            if Reward < 1:
                Reward = 1
            RewardSet.append(Reward)
        GambaShopQtyList.append(RewardSet)
        GambaShopRewardList.append([[25489,25489,25489], CopyofGambaShopReceiptIDs[:3], FillerRewardSet, FillerRewardSet])
        del CopyofGambaShopReceiptIDs[:3]
        GambaShopCostList.append(Costs)

def AddSPManual(): # Creates 3 SP Manuals, using ID 25015, 25018, 25033
    SPManualIDs = [25349, 25350, 25351]
    SPManualNameIDs = [660, 661, 662]
    SPManualCaptionIDs = [761, 762, 763]
    SPManualValues = [2500, 5000, 10000]
    with open("./XC2/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file: # Changes max quantity
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in SPManualIDs:
                row["ValueMax"] = 99
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes names of Contracts
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] >= 660:
                for i in range(0, len(SPManualIDs)):
                    if row["$id"] == SPManualNameIDs[i]:
                        row["name"] = f"{SPManualValues[i]} SP Receipt"
                    if row["$id"] == SPManualCaptionIDs[i]:
                        row["name"] = f"Proof that you purchased {SPManualValues[i]} SP\n for the driver skill trees."
            if row["$id"] >= 764:
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def ShopLootGeneration(ShopLevel, Shop): # Makes the loot for the shops, using the existing shop template
    NumTrades = Shop["TradeCount"]
    ShopFillerEmpty = Helper.ExtendListtoLength([], NumTrades, "0")
    ShopFillerFull = Helper.ExtendListtoLength([], NumTrades, "1")
    # These are assumed, if there's an exception for a shop, it gets put in that shop's subsection

    Shop["InputItemIDs"] = [Helper.ExtendListtoLength([], NumTrades, "25489"), ShopFillerEmpty, ShopFillerEmpty, ShopFillerEmpty, ShopFillerEmpty] # MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs
    Shop["RewardSP"] = ShopFillerEmpty #FLD_QuestReward Sp
    Shop["RewardXP"] = ShopFillerEmpty # FLD_QuestReward EXP
    Shop["HideReward"] = ShopFillerEmpty # Whether or not to hide the reward, MNU_ShopChangeTask "HideReward"
    
    if Shop == CoreCrystalShop:
        Shop["InputItemQtys"] = [CrystalShopCostList[ShopLevel], ShopFillerEmpty, ShopFillerEmpty, ShopFillerEmpty, ShopFillerEmpty] # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
        Shop["RewardItemIDs"] = CrystalShopRewardList[ShopLevel] # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
        Shop["RewardQtys"] = [ShopFillerFull, ShopFillerFull, ShopFillerEmpty, ShopFillerEmpty] # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
        Shop["RewardNames"] = CrystalShopNameList[ShopLevel] # names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs
    elif Shop == GambaShop:
        Shop["InputItemQtys"] = [GambaShopCostList[ShopLevel], ShopFillerEmpty, ShopFillerEmpty, ShopFillerEmpty, ShopFillerEmpty] # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
        Shop["RewardItemIDs"] = GambaShopRewardList[ShopLevel] # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
        Shop["RewardQtys"] = [GambaShopQtyList[ShopLevel], ShopFillerFull, ShopFillerEmpty, ShopFillerEmpty] # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
        Shop["RewardNames"] = ["Small Bet Reward", "Medium Bet Reward", "Large Bet Reward"] # names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs
        Shop["HideReward"] = ShopFillerFull # Whether or not to hide the reward, MNU_ShopChangeTask "HideReward"
    elif Shop == WeaponChipShop:
        Shop["InputItemQtys"] = [ChipShopCostList[ShopLevel], ShopFillerEmpty, ShopFillerEmpty, ShopFillerEmpty, ShopFillerEmpty] # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
        Shop["RewardItemIDs"] = ChipShopRewardDistribution[ShopLevel] # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
        Shop["RewardQtys"] = [[2,2,2,2,1], [1,1,1,1,1], [1,1,1,1,0], ShopFillerEmpty] # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
        Shop["RewardNames"] = ChipBundleNames[ShopLevel] # names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs
    elif Shop == AuxCoreShop:
        Shop["InputItemQtys"] = [AuxCoreShopCostDistribution[ShopLevel], ShopFillerEmpty, ShopFillerEmpty, ShopFillerEmpty, ShopFillerEmpty] # MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs
        Shop["RewardItemIDs"] = [AuxCoreShopRewardDistribution[ShopLevel], ShopFillerEmpty, ShopFillerEmpty, ShopFillerEmpty] # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
        Shop["RewardQtys"] = [ShopFillerFull, ShopFillerEmpty, ShopFillerEmpty, ShopFillerEmpty] # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
        Shop["RewardNames"] = AuxCoreNameDistribution[ShopLevel] # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
    elif Shop == DriverAccessoryShop:
        Shop["InputItemQtys"] = [AccessoryShopCostDistribution[ShopLevel], ShopFillerEmpty, ShopFillerEmpty, ShopFillerEmpty, ShopFillerEmpty] # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
        Shop["RewardItemIDs"] = [AccessoryShopRewardDistribution[ShopLevel], ShopFillerEmpty, ShopFillerEmpty, ShopFillerEmpty] # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
        Shop["RewardQtys"] = [ShopFillerFull, ShopFillerEmpty, ShopFillerEmpty, ShopFillerEmpty] # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
        Shop["RewardNames"] = AccessoryNameDistribution[ShopLevel]
    elif Shop == PouchItemShop:
        Shop["InputItemQtys"] = [PouchItemShopCostDistribution[ShopLevel], ShopFillerEmpty, ShopFillerEmpty, ShopFillerEmpty, ShopFillerEmpty] # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
        Shop["RewardItemIDs"] = PouchItemShopRewardDistribution[ShopLevel] # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
        Shop["RewardQtys"] = [ShopFillerFull, ShopFillerFull, ShopFillerEmpty, ShopFillerEmpty] # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
        Shop["RewardNames"] = PouchItemNameDistribution[ShopLevel]
    return Shop

def ShopCreator(ShopList: list, DeleteArgentumShops: bool): # Makes the shops
    # This section cuts down on the number of user inputs:
    StartingTaskID = Helper.GetMaxValue("./XC2/JsonOutputs/common/MNU_ShopChangeTask.json", "$id") + 1
    StartingQuestRewardID = Helper.GetMaxValue("./XC2/JsonOutputs/common/FLD_QuestReward.json", "$id") + 1
    Shoplistnames = []
    ShoplistNPCIDs = []
    ShoplistNPCPositions = []
    for shop in ShopList:
        if shop["ShopIDtoReplace"] in FullShopEventNameDict:
            shop["ShopNametoReplace"] = FullShopEventNameDict[shop["ShopIDtoReplace"]][1] # fld_shopname $id. Can be taken from MNU_ShopList 'Name'
            shop["ShopEventID"] = FullShopEventNameDict[shop["ShopIDtoReplace"]][0] # maXXa_FLD_NpcPop 'EventID'
        shop["InputTaskIDs"] = Helper.InclRange(StartingTaskID, StartingTaskID + shop["TradeCount"] - 1) # MNU_ShopChangeTask $id, feeds into MNU_ShopChange DefTaskSet1->8 and AddTaskSet1->8.
        if shop["TradeCount"] > 8:
            shop["AddTaskConditions"] = Helper.ExtendListtoLength([1], shop["TradeCount"] - 8, "1") # MNU_ShopChange AddCondition1->8 (0 if no task, 1 otherwise) # how many InputTaskIDs you have past 8 determines number of 1s, always 8 items long
        else:
            shop["AddTaskConditions"] = [] # MNU_ShopChange AddCondition1->8 (0 if no task, 1 otherwise) # how many InputTaskIDs you have past 8 determines number of 1s, always 8 items long
        shop["RewardIDs"] = Helper.InclRange(StartingQuestRewardID, StartingQuestRewardID + shop["TradeCount"] - 1) # FLD_QuestReward $id, feeds into MNU_ShopChangeTask Reward
        StartingTaskID += shop["TradeCount"]
        StartingQuestRewardID += shop["TradeCount"]
        Shoplistnames.append(shop["ShopName"])
        ShoplistNPCIDs.append(shop["ChosenMapRowID"])
    with open("./XC2/JsonOutputs/common_gmk/ma02a_FLD_NpcPop.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(len(ShoplistNPCIDs)):
            for row in data["rows"]:
                if row["$id"] == ShoplistNPCIDs[i]:
                    ShoplistNPCPositions.append(row["name"])
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    ShopFullListDict = {}
    ShopNamesList = ['[System:Color name=green]Bounty Token[/System:Color] Bartering', 'Manual Marketplace', 'The Poppishop', 'Core Crystal Cache', 'The [System:Color name=tutorial]Casino[/System:Color]', 'Weapon Warehouse', 'Aux Core Auction', 'Excess Accessories', 'Pouch Item Patisserie']
    for name in ShopNamesList:
        ShopFullListDict[name] = {"ma02a Row": [], "NPC Position": []}
        for i in range(len(Shoplistnames)):
            if Shoplistnames[i] == name:
                ShopFullListDict[name]["ma02a Row"].append(ShoplistNPCIDs[i])
                ShopFullListDict[name]["NPC Position"].append(ShoplistNPCPositions[i])
    DebugSetShop = []
    for i in range(SetCount):
        DebugSetShop = []
        for shop in ShopFullListDict:
            if shop not in ["[System:Color name=green]Bounty Token[/System:Color] Bartering", "Manual Marketplace", "The Poppishop"]:
                if ShopFullListDict[shop]["NPC Position"] != []:
                    if ShopFullListDict[shop]["NPC Position"][i] != "":
                        DebugSetShop.append(ShopFullListDict[shop]["NPC Position"][i])
        #print(DebugSetShop)
    with open("./XC2/JsonOutputs/common/MNU_ShopChange.json", 'r+', encoding='utf-8') as file: # Adds the exchange tasks
        data = json.load(file)
        ShopChangeStartRow = Helper.GetMaxValue("./XC2/JsonOutputs/common/MNU_ShopChange.json", "$id") + 1 # used in MNU_ShopList for "TableID"
        CurrRow = Helper.GetMaxValue("./XC2/JsonOutputs/common/MNU_ShopChange.json", "$id") + 1
        for shop in ShopList:
            ShopChangeRowToAdd = {"$id": CurrRow, "DefTaskSet1": 0, "DefTaskSet2": 0, "DefTaskSet3": 0, "DefTaskSet4": 0, "DefTaskSet5": 0, "DefTaskSet6": 0, "DefTaskSet7": 0, "DefTaskSet8": 0, "AddTaskSet1": 0, "AddCondition1": 0, "AddTaskSet2": 0, "AddCondition2": 0, "AddTaskSet3": 0, "AddCondition3": 0, "AddTaskSet4": 0, "AddCondition4": 0, "AddTaskSet5": 0, "AddCondition5": 0, "AddTaskSet6": 0, "AddCondition6": 0, "AddTaskSet7": 0, "AddCondition7": 0, "AddTaskSet8": 0, "AddCondition8": 0, "LinkQuestTask": 0, "LinkQuestTaskID": 0, "UnitText": 0}
            for i in range(0, len(shop["InputTaskIDs"])):
                if i <= 7:
                    ShopChangeRowToAdd[f"DefTaskSet{i+1}"] = shop["InputTaskIDs"][i]
                else: # once we get past all the regular tasks, we add new ones to addtaskset instead
                    ShopChangeRowToAdd[f"AddTaskSet{i-7}"] = shop["InputTaskIDs"][i]
                    ShopChangeRowToAdd[f"AddCondition{i-7}"] = shop["AddTaskConditions"][i-8]
            data["rows"].append(ShopChangeRowToAdd)
            CurrRow += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common_ms/fld_shopchange.json", 'r+', encoding='utf-8') as file: # Changes the reward name for the token shop
        data = json.load(file)
        CurrRow = Helper.GetMaxValue("./XC2/JsonOutputs/common_ms/fld_shopchange.json", "$id") + 1
        StartingShopChangeNameRow = Helper.GetMaxValue("./XC2/JsonOutputs/common_ms/fld_shopchange.json", "$id") + 1 # Used in MNU_ShopChangeTask for "ShopName"
        for shop in ShopList:
            for reward in shop["RewardNames"]:
                data["rows"].append({"$id": CurrRow, "style": 36, "name": reward})
                CurrRow += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common/MNU_ShopChangeTask.json", 'r+', encoding='utf-8') as file: # Now we define what each task does
        data = json.load(file)
        CurrRow = Helper.GetMaxValue("./XC2/JsonOutputs/common/MNU_ShopChangeTask.json", "$id") + 1
        for shop in ShopList:
            for i in range(0, len(shop["InputItemIDs"][0])):
                data["rows"].append({"$id": CurrRow, "Name": StartingShopChangeNameRow, "SetItem1": shop["InputItemIDs"][0][i], "SetNumber1": shop["InputItemQtys"][0][i], "SetItem2": shop["InputItemIDs"][1][i], "SetNumber2": shop["InputItemQtys"][1][i], "SetItem3": shop["InputItemIDs"][2][i], "SetNumber3": shop["InputItemQtys"][2][i], "SetItem4": shop["InputItemIDs"][3][i], "SetNumber4": shop["InputItemQtys"][3][i], "SetItem5": shop["InputItemIDs"][4][i], "SetNumber5": shop["InputItemQtys"][4][i], "HideReward": shop["HideReward"][i], "Reward": shop["RewardIDs"][i], "HideRewardFlag": 0, "AddFlagValue": 0, "forcequit": 0, "IraCraftIndex": 0})
                CurrRow += 1
                StartingShopChangeNameRow += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common/FLD_QuestReward.json", 'r+', encoding='utf-8') as file: # Sets the reward for each task
        data = json.load(file)
        CurrRow = Helper.GetMaxValue("./XC2/JsonOutputs/common/FLD_QuestReward.json", "$id") + 1
        for shop in ShopList:
            for i in range(0, len(shop["RewardIDs"])):
                data["rows"].append({"$id": CurrRow, "Gold": 0, "EXP": shop["RewardXP"][i], "Sp": shop["RewardSP"][i], "Coin": 0, "DevelopZone": 0, "DevelopPoint": 0, "TrustPoint": 0, "MercenariesPoint": 0, "IdeaCategory": 0, "IdeaValue": 0, "ItemID1": shop["RewardItemIDs"][0][i], "ItemNumber1": shop["RewardQtys"][0][i], "ItemID2": shop["RewardItemIDs"][1][i], "ItemNumber2": shop["RewardQtys"][1][i], "ItemID3": shop["RewardItemIDs"][2][i], "ItemNumber3": shop["RewardQtys"][2][i], "ItemID4": shop["RewardItemIDs"][3][i], "ItemNumber4": shop["RewardQtys"][3][i]})
                CurrRow += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common_ms/fld_shopname.json", 'r+', encoding='utf-8') as file: # Adds new shop name to list 
        data = json.load(file)
        CurrRow = Helper.GetMaxValue("./XC2/JsonOutputs/common_ms/fld_shopname.json", "$id") + 1
        ShopNameStartingRow = Helper.GetMaxValue("./XC2/JsonOutputs/common_ms/fld_shopname.json", "$id") + 1 # used in MNU_ShopList for "Name"
        for i in range(0, len(ShopList)):
            data["rows"].append({"$id": CurrRow, "style": 70, "name": ShopList[i]["ShopName"]})
            CurrRow += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common/MNU_ShopList.json", 'r+', encoding='utf-8') as file: # Changes existing shop to match what we want
        data = json.load(file)
        for i in range(0, len(ShopList)):
            for row in data["rows"]:
                if row["$id"] == ShopList[i]["ShopIDtoReplace"]:
                    row["Name"] = ShopNameStartingRow
                    row["ShopIcon"] = ShopList[i]["ShopIcon"]
                    row["TableID"] = ShopChangeStartRow
                    row["Discount1"] = row["Discount2"] = row["Discount3"] = row["Discount4"] = row["Discount5"] = 0
                    row["ShopType"] = 1
                    ShopChangeStartRow += 1
                    ShopNameStartingRow += 1
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    if DeleteArgentumShops:
        with open("./XC2/JsonOutputs/common_gmk/ma02a_FLD_NpcPop.json", 'r+', encoding='utf-8') as file: # Lets you rest in the Argentum Trade Guild Inn, but removes all other shops (we're adding them back after)
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] != 2096: # keeps only the inn as a shop in Argentum
                    row["ShopID"] = 0
                    row["flag"]["Talkable"] = 0
                    row["EventID"] = 0
                    row["QuestFlag"] = 0
            for i in range(0, len(ShopList)): # gives a specific npc the shop we want
                for row in data["rows"]:
                    if row["$id"] == ShopList[i]["ChosenMapRowID"]:
                        OrigNPCID = row["NpcID"]
                        row["ScenarioFlagMin"] = row["QuestFlag"] = row["QuestFlagMin"] = row["QuestFlagMax"] = row["TimeRange"] = row["Mot"] = row["QuestID"] = 0
                        row["ScenarioFlagMax"] = 10048
                        row["flag"]["Talkable"] = 1
                        row["EventID"] = ShopList[i]["ShopEventID"]
                        row["ShopID"] = ShopList[i]["ShopIDtoReplace"]
                        row["NpcID"] = ShopList[i]["NewNPCModel"]
                        row["Visible_XZ"] = 100
                        row["Visible_Y"] = 10
                        row["Invisible_XZ"] = 105
                        row["Invisible_Y"] = 15
                        row["Condition"] = ShopList[i]["Condition"]
                        break
                for row in data["rows"]: # Need to account for more lines where the original NPC speaks, they overlap bodies and it looks weird
                    if row["NpcID"] == OrigNPCID:
                        row["Condition"] = UMHuntDisableCondListID
                        row["Mot"] = 0
                        row["TimeRange"] = 0
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)



# ------ Shop Setup ------




def InnShopCosts(): # Removes cost to stay at inn
    Helper.ColumnAdjust("./XC2/JsonOutputs/common/MNU_ShopInn.json", ["Price"], 0)

def ReplaceBana(): # I want to use Bana as the exchange shop, so I move rumtumtum into Bana's spots on the map
    with open("./XC2/JsonOutputs/common_gmk/ma02a_FLD_NpcPop.json", 'r+', encoding='utf-8') as file: # Changes name text file
        data = json.load(file)
        for row in data["rows"]:
            if (row["$id"] != 2079) & (row["NpcID"] == 2002):
                row["NpcID"] = 2233
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def SecretShopMaker(ChosenAreaOrder): # Adds some secret shops in the areas of interest
    SecretShopList = []
    CreateSecretShopReceipts()
    SecretShopRewardGeneration(ChosenAreaOrder)
    SecretEmptyFillerList = Helper.ExtendListtoLength([], 5, "0")
    UsableShopIDs = Helper.InclRange(65, 73) + [81] # MNU_ShopList $id, NpcPop ShopID
    Helper.ColumnAdjust("./XC2/JsonOutputs/common_gmk/ma07a_FLD_NpcPop.json", ["FSID1", "FSID2", "FSID3"], 0)
    ShopList = []
    for i in range(0, len(ChosenAreaOrder)):
        MapValidNPCIDs = [x for x in Helper.FindSubOptionValuesList("./XC2/JsonOutputs/common_gmk/" + ContinentInfo[ChosenAreaOrder[i]][2] + "_FLD_NpcPop.json", "flag", "Talkable", 1, "$id") if x not in InvalidMapNPCs]
        ChosenSecretNPCID = random.choice(MapValidNPCIDs)
        OrigNPCID = 0
        with open("./XC2/JsonOutputs/common_gmk/" + ContinentInfo[ChosenAreaOrder[i]][2] + "_FLD_NpcPop.json", 'r+', encoding='utf-8') as file: # Lets you rest in the Argentum Trade Guild Inn, but removes all other shops (we're adding them back after)
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] == ChosenSecretNPCID:
                    if Helper.OddsCheck(50): # 50% chance for a secret shop to exist, and there can be no more than 5 (this is because I'm out space in one of my files?):
                        OrigNPCID = row["NpcID"]
                        row["ScenarioFlagMin"] = row["QuestFlag"] = row["QuestFlagMin"] = row["QuestFlagMax"] = row["TimeRange"] = row["Condition"] = row["Mot"] = row["QuestID"] = row["FSID1"] = row["FSID2"] = row["FSID3"] = 0
                        row["ScenarioFlagMax"] = 10048
                        for type in ShopEventNameDict:
                            if UsableShopIDs[i] in ShopEventNameDict[type]:
                                row["EventID"] = ShopEventNameDict[type][UsableShopIDs[i]][0]
                                break
                        row["ShopID"] = UsableShopIDs[i]
                        row["NpcID"] = 2012 # Klaus
                        row["LookAt"] = 0
                        row["NpcTurn"] = 0
                else:
                    row["EventID"] = 0
                    row["ShopID"] = 0
                    row["QuestID"] = 0
            for row in data["rows"]: # Need to account for more lines where the original NPC speaks, they overlap bodies and it looks weird
                if row["NpcID"] == OrigNPCID:
                    row["Condition"] = UMHuntDisableCondListID
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)
        # defining the shop itself

        SecretShop = {
            "NewNPCModel": 2012,# from RSC_NpcList, goes to ma02a_FLD_NpcPop NpcID. Klaus
            "ChosenMapRowID": ChosenSecretNPCID, # ma02a_FLD_NpcPop $id
            "ShopIcon": 419, # MNU_ShopList ShopIcon
            "ShopIDtoReplace": UsableShopIDs[i], # MNU_ShopList $id
            "ShopName": f"[System:Color name=tutorial]Super-Secret Shop {i+1}[/System:Color]", # fld_shopname name
            "TradeCount": 5, # Number of trades the shop will have
            "InputItemIDs": [SecretEmptyFillerList, SecretEmptyFillerList, SecretEmptyFillerList, SecretEmptyFillerList, SecretEmptyFillerList], # MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs
            "InputItemQtys": [SecretEmptyFillerList, SecretEmptyFillerList, SecretEmptyFillerList, SecretEmptyFillerList, SecretEmptyFillerList], # MNU_ShopChangeTask SetNumber1->5, 1 list for each 
            "RewardItemIDs": [Helper.ExtendListtoLength([SecretReceiptIDs[i]], 5, "inputlist[i-1]"), SecretShopRewardListItem1[i], SecretShopRewardListItem2[i], SecretEmptyFillerList], # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
            "RewardQtys": [SecretShopCostList[i], SecretShopRewardQuantities1[i], SecretShopRewardQuantities2[i], SecretEmptyFillerList], # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
            "RewardNames": ["Secret Trade 1", "Secret Trade 2", "Secret Trade 3", "Secret Trade 4", "Secret Trade 5"], # names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs
            "RewardSP": SecretEmptyFillerList, #FLD_QuestReward Sp
            "RewardXP": SecretEmptyFillerList, # FLD_QuestReward EXP
            "HideReward": SecretEmptyFillerList # Whether or not to hide the reward, MNU_ShopChangeTask "HideReward"
        }

        ShopList.append(SecretShop)

    if len(ShopList) > 0:
        ShopCreator(ShopList, False) # run the function on the whole list at once

def CreateSecretShopReceipts(): # Makes receipts for secret shops, limiting the amount of things a player can buy from a shop.
    global SecretReceiptIDs
    SecretReceiptIDs = Helper.ExtendListtoLength([25352], 10, "inputlist[i-1]+1")
    SecretReceiptNameIDs = Helper.ExtendListtoLength([663], 10, "inputlist[i-1]+1")
    SecretReceiptCaptionIDs = Helper.ExtendListtoLength([764], 10, "inputlist[i-1]+1")
    with open("./XC2/JsonOutputs/common/ITM_PreciousList.json", 'r+', encoding='utf-8') as file: # changes max quantity
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] in SecretReceiptIDs:
                row["ValueMax"] = 5
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common_ms/itm_precious.json", 'r+', encoding='utf-8') as file: # Changes names of Contracts
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] >= 663:
                for i in range(0, len(SecretReceiptIDs)):
                    if row["$id"] == SecretReceiptNameIDs[i]:
                        row["name"] = f"Secret Shop Receipt {i+1}"
                    if row["$id"] == SecretReceiptCaptionIDs[i]:
                        row["name"] = f"Proof that you purchased \nan item set from the Secret Shop {i+1}."
            if row["$id"] >= 773:
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def SecretShopRewardGeneration(ChosenAreaOrder): # Makes the reward sets for the secret shops
    global SecretShopRewardListItem1
    SecretShopRewardListItem1 = []
    global SecretShopRewardListItem2
    SecretShopRewardListItem2 = []
    global SecretShopRewardQuantities1
    SecretShopRewardQuantities1 = [] 
    global SecretShopRewardQuantities2
    SecretShopRewardQuantities2 = []
    global SecretShopCostList
    SecretShopCostList = []

    WeaponRankList = Helper.ExtendListtoLength([], 20, "[]")
    with open("./XC2/JsonOutputs/common/ITM_PcWpnChip.json", 'r+', encoding='utf-8') as file: # Assigns weapons to groups based on category
        data = json.load(file)
        for row in data["rows"]:
            WeaponRankList[row["Rank"] - 1].append(row["$id"])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

    RewardTypes = {
        1: "WP Manual", 
        2: "Pouch Item Set",
        3: "Driver Accessory Set",
        4: "Bounty Tokens",
        5: "Weapon Chips",
        6: "Pouch/Accessory Expander",
        7: "Aux Cores"
    }

    # Now assign rewards
    for j in range(0, len(ChosenAreaOrder)):
        SecretShopChips = []
        SetRewards1 = [0,0,0,0,0]
        SetRewards2 = [0,0,0,0,0]
        SetQuantities1 = [1,1,1,1,1]
        SetQuantities2 = [1,1,1,1,1]
        RewardTypeChoices = random.choices([1, 2, 3, 4, 5, 6, 7], weights = [20, 20, 15, 10, 10, 10, 15], k = 5) # Choose Type of Reward
        ShopCostReceiptList = [0,0,0,0,0]
        for i in range(0, 5): # For each reward,
            match RewardTypeChoices[i]:
                case 1: # WP Manual
                    RandomManuals = random.choices([25405, 25406, 25407], weights = [1, 2, 3], k = 2)
                    SetRewards1[i] = RandomManuals[0]
                    SetRewards2[i] = RandomManuals[1]
                    ShopCostReceiptList[i] = 1
                case 2: # Pouch Item Set
                    RandomPouchItems = random.choices(SecretPouchItemIDs, k = 2)
                    SetRewards1[i] = RandomPouchItems[0]
                    SetRewards2[i] = RandomPouchItems[1]
                    ShopCostReceiptList[i] = 2
                case 3: # Driver Accessory Set
                    RandomAccessories = random.choices(SecretAccessoryIDs, k = 1)
                    SetRewards1[i] = RandomAccessories[0]
                    SetRewards2[i] = 0
                    SetQuantities2[i] = 0
                    ShopCostReceiptList[i] = 2
                case 4: # Bounty Tokens
                    RandomBountyToken = random.choice(Helper.InclRange(25479, 25480 + j))
                    SetRewards1[i] = RandomBountyToken
                    SetRewards2[i] = 0
                    SetQuantities2[i] = 0
                    ShopCostReceiptList[i] = 3
                case 5: # Weapon Chips
                    for k in range(j + 6, j + 11):
                        SecretShopChips.extend(WeaponRankList[k])
                    RandomWeaponChips = random.choices(SecretShopChips, k = 2)
                    SetRewards1[i] = RandomWeaponChips[0]
                    SetRewards2[i] = RandomWeaponChips[1]
                    ShopCostReceiptList[i] = 4
                case 6: # Pouch/Accessory Expander
                    RandomPouchorAccessoryExpander = random.choices([25305, 25450], weights = [66, 34], k = 2)
                    SetRewards1[i] = RandomPouchorAccessoryExpander[0]
                    SetRewards2[i] = RandomPouchorAccessoryExpander[1]
                    ShopCostReceiptList[i] = 3
                case _: # Aux Cores
                    RandomAuxCores = random.choices(SecretAuxCoreIDs, k = 1)
                    SetRewards1[i] = RandomAuxCores[0]
                    SetRewards2[i] = 0
                    SetQuantities2[i] = 0
                    ShopCostReceiptList[i] = 2
        SecretShopCostList.append(ShopCostReceiptList)
        SecretShopRewardListItem1.append(SetRewards1)
        SecretShopRewardListItem2.append(SetRewards2)
        SecretShopRewardQuantities1.append(SetQuantities1)
        SecretShopRewardQuantities2.append(SetQuantities2)

def ReAddInns(): # Need to readd inns to Mor Ardain and Gormott to allow you to change the tide level
    with open("./XC2/JsonOutputs/common_gmk/ma05a_FLD_NpcPop.json", 'r+', encoding='utf-8') as file: # Gormott Inn
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 5487:
                row["EventID"] = 40318
                row["ShopID"] = 31
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common_gmk/ma08a_FLD_NpcPop.json", 'r+', encoding='utf-8') as file: # Mor Ardain Inn
        data = json.load(file)
        for row in data["rows"]:
            if row["$id"] == 8284:
                row["EventID"] = 40660
                row["ShopID"] = 87
                break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def ExportAccessoryAuxCoreMaxIDs(): # outputs the globals to the UMHuntMain file, used to generate enemy drops
    return SecretAccessoryIDs, SecretAuxCoreIDs

class UMHuntSecretShopEnhancements(Enhancement):
    def __init__(self, name, Enhancement, Caption, Param1 = [0,0,0,0], Param2 = [0,0,0,0], ReversePar1 = False, DisTag = "", isRounded = True):
        self.addToList = False 
        self.name = name
        self.EnhanceEffect = Enhancement
        self.Caption = Caption
        self.Param1 = Param1
        self.Param2 = Param2
        self.ReversePar1 = ReversePar1
        self.DisTag = DisTag
        self.isRounded = isRounded

# Accessories
UMAllWeaponAttackUp = UMHuntSecretShopEnhancements("Master",120, 130, Medium)
UMSpecialRechargeCancelling = UMHuntSecretShopEnhancements("Special",92, 100, Large)
UMHigherLVEnemyDamageUp = UMHuntSecretShopEnhancements("Underdog",40,41, Mega)
UMVision = UMHuntSecretShopEnhancements("Monado",242, 298, Small, ReversePar1=True)
UMBreakResDown = UMHuntSecretShopEnhancements("Breaker",180, 192, Medium)
UMStrengthBoost = UMHuntSecretShopEnhancements("Strength", 2,2, Medium)
UMEtherBoost = UMHuntSecretShopEnhancements("Ether", 3,3, Medium)

# Aux Cores
UMFlatCritBoost = UMHuntSecretShopEnhancements("Critical",17,17, Medium)
UMSurpriseAttackUp = UMHuntSecretShopEnhancements("Surprise",36,37, [0, 0, 10000, 20000], DisTag="Surprise!")
UMSpecialRecievesAfterImage = UMHuntSecretShopEnhancements("Afterimage",213, 335, Mini, DisTag="Afterimage")
UMAutoSpeedArtsSpeed= UMHuntSecretShopEnhancements("Lightning",240, 296, High, High)
UMPhyAndEthDefenseUp = UMHuntSecretShopEnhancements("Full Guard",146, 156, [0, 0, 60, 100])
UMOnBlockNullDamage = UMHuntSecretShopEnhancements("Guardian",59, 59, Medium, DisTag="Null Damage")
UMFlatBlockBoost = UMHuntSecretShopEnhancements("Block",20,20, Medium)