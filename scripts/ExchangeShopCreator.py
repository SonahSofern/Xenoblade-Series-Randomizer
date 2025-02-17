import json, random, Helper, IDs, EnemyRandoLogic, RaceMode, math, Options, time, FieldSkillAdjustments
from Enhancements import *


# ShopID: EventID
ShopandEventDict = {12: 40057, 16: 40058, 17: 40054, 18: 40045, 21: 40048, 23: 40050, 24: 40051, 26: 40052, 27: 40053, 30: 40002, 31: 20270, 32: 40319, 33: 40320, 36: 40321, 37: 40322, 38: 41172, 39: 40324, 40: 40325, 41: 40326, 42: 40327, 43: 40328, 44: 40329, 45: 40330, 46: 40332, 47: 40331, 48: 41000, 49: 21265, 66: 40441, 70: 40443, 71: 40444, 73: 40446, 87: 40660, 106: 40762, 107: 40949, 108: 40759, 109: 40724, 110: 20592, 113: 40675, 114: 40731, 115: 40758, 116: 40760, 117: 41012, 118: 40723, 119: 40757, 120: 40684, 121: 40756, 122: 40685, 123: 41004, 124: 40840, 125: 40847, 126: 40842, 128: 40835, 129: 40845, 130: 40843, 131: 40844, 132: 40838, 133: 20650, 134: 40846, 135: 40834, 138: 40836, 139: 40839, 140: 40841, 141: 40848, 142: 41006, 143: 41053, 144: 40809, 145: 41040, 146: 41041, 147: 40810, 148: 40806, 149: 40808, 150: 40805, 151: 40981, 152: 40807, 153: 41005, 154: 41039, 156: 40982, 161: 20118, 162: 20119, 174: 20262, 176: 20265, 177: 20268, 186: 40939, 189: 40980, 201: 41556, 203: 21256, 205: 40989, 221: 21453, 222: 21473, 225: 41566, 226: 21623, 227: 21660, 228: 21694, 230: 21727, 231: 21729, 234: 21740, 235: 21741, 237: 21760, 247: 42018, 248: 42017, 249: 42020, 250: 42019, 251: 42022, 252: 42021, 253: 41624, 254: 41675, 255: 42023, 257: 42027}

UsedShopIDs = []
EmptyFillerList = Helper.ExtendListtoLength([], 16, "0") # Empty list of full size
FullFillerList = Helper.ExtendListtoLength([], 16, "1") # Full list of full size

#Pre-Existing Params:
ShopIDtoReplace = 0 # MNU_ShopList $id. Must be a key from ShopandEventDict. Will check if unused. If used already, will automatically assign new unused shop id.
ShopIcon = 0 # MNU_ShopList 'ShopIcon'
RewardItemIDs = [[],[],[],[]] # FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys
RewardQtys = [[],[],[],[]] # FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs
RewardNames = [] # names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs. User determined
RewardSP = [] #FLD_QuestReward Sp
RewardXP = [] # FLD_QuestReward EXP
HideReward = [] # Whether or not to hide the reward, MNU_ShopChangeTask HideReward

#New Params:
MapName = "00" # should be the XX in  './_internal/JsonOutputs/common_gmk/maXXa_FLD_NpcPop.json'
ShopPosition = "" # maXXa_FLD_NpcPop 'name'. Decides where the NPC will stand.
TradeCount = 0 # Number of Trades the shop should have. Determines the InputTaskIDs and AddTaskConditions

#Equivalent Pairs: (renamed for clarity) 

# OLD
# NEW

NPCID = 0 # ma02a_FLD_NpcPop '$id'
ChosenMapRowID = 0 # ma02a_FLD_NpcPop '$id'

Name = "" # fld_shopname 'name'. User Decides
ShopName = "" # fld_shopname 'name'. User Decides

NPCModel = 0 # from RSC_NpcList, goes to ma02a_FLD_NpcPop 'NpcID'.
NewNPCModel = 0 # from RSC_NpcList, goes to ma02a_FLD_NpcPop 'NpcID'.

SetItemIDs = [[],[],[],[],[]] # MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs
InputItemIDs = [[],[],[],[],[]] # MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs

SetItemQtys = [[],[],[],[],[]] # MNU_ShopChangeTask SetNumber1->5, 1 list for each
InputItemQtys = [[],[],[],[],[]] # MNU_ShopChangeTask SetNumber1->5, 1 list for each

#Deleted Params:
ShopEventID = 0 # ma02a_FLD_NpcPop 'EventID'
ShopNametoReplace = 0 # fld_shopname $id. Can be taken from MNU_ShopList 'Name'
InputTaskIDs = [] # MNU_ShopChangeTask $id, Can be determined with max values and TradeCount.
AddTaskConditions = [] # MNU_ShopChange AddCondition1->8 (0 if no task, 1 otherwise). Can be determined with max values and TradeCount
RewardIDs = [] # FLD_QuestReward $id, feeds into MNU_ShopChangeTask Reward. Can be determined with max values and TradeCount

class ExchangeShop:

    def __init__(self, ShopName: str = "", ShopIcon: int = 0, ShopPosition: str = "",
                 ShopIDtoReplace: int = 0, ChosenMapRowID: int = 0, NewNPCModel: int = 0, TradeCount: int = 0,
                 InputItemIDs: list[list[int]] = [[], [], [], [], []], InputItemQtys: list[list[int]] = [[], [], [], [], []],
                 RewardItemIDs: list[list[int]] = [[], [], [], []], RewardQtys: list[list[int]] = [[], [], [], []],
                 RewardNames: list[str] = [], RewardSP: list[int] = [], RewardXP: list[int] = [], RewardHidden: list[bool] = []):
        """
        Overwrites an existing shop with the new shop details, using the following parameters
        :param ShopName (str): fld_shopname 'name'. User Decides.
        :param ShopIcon (int): MNU_ShopList 'ShopIcon'.
        :param ShopPosition (str): maXXa_FLD_NpcPop 'name'. Decides where the NPC will stand.
        :param ShopIDtoReplace (int): MNU_ShopList $id. Must be a key from ShopandEventDict. Will check if unused. If used already, will automatically assign new unused shop id.
        :param ChosenMapRowID (int): ma02a_FLD_NpcPop '$id'.
        :param NewNPCModel (int): from RSC_NpcList, goes to ma02a_FLD_NpcPop 'NpcID'.
        :param TradeCount (int): Number of Trades the shop should have. Determines the InputTaskIDs and AddTaskConditions.
        :param InputItemIDs (list[list[int]]): MNU_ShopChangeTask SetItem1->5, 1 list for each SetItem1->SetItem5, and a number of items in each list equal to the number of InputTaskIDs.
        :param InputItemQtys (list[list[int]]): MNU_ShopChangeTask SetNumber1->5, 1 list for each.
        :param RewardItemIDs (list[list[int]]): FLD_QuestReward ItemID1->4, item ids from ITM files, same number as RewardQtys.
        :param RewardQtys (list[list[int]]): FLD_QuestReward ItemNumber1->4, 1 list for each ItemNumber, and number of items in each list equal to the number of InputTaskIDs.
        :param RewardNames (list[str]): names for items with IDs in FLD_QuestReward, as many items as non-zero InputTaskIDs. User determined.
        :param RewardSP (list[int]): FLD_QuestReward Sp.
        :param RewardXP (list[int]): FLD_QuestReward EXP.
        :param RewardHidden (list[bool]): Whether or not to hide the reward, MNU_ShopChangeTask HideReward.
        """
        self.ShopName = ShopName
        self.ShopIcon = ShopIcon
        self.ShopPosition = ShopPosition
        self.ShopIDtoReplace = ShopIDtoReplace
        self.ChosenMapRowID = ChosenMapRowID
        self.NewNPCModel = NewNPCModel
        self.TradeCount = TradeCount
        self.InputItemIDs = InputItemIDs
        self.InputItemQtys = InputItemQtys
        self.RewardItemIDs = RewardItemIDs
        self.RewardQtys = RewardQtys
        self.RewardNames = RewardNames
        self.RewardSP = RewardSP
        self.RewardXP = RewardXP
        self.RewardHidden = RewardHidden

    def CheckValidity(self): # We want to let the user know if they goofed
        if self.RewardHidden != []:
            objectstocheck = [self.InputItemIDs, self.InputItemQtys, self.RewardItemIDs, self.RewardQtys, self.RewardNames, self.RewardSP, self.RewardXP, self.RewardHidden]
            for singlelist in objectstocheck:
                listname = GetName(singlelist)
                CheckTradeValidity(objectstocheck, self.TradeCount, listname)


def CheckTradeValidity(inputlist: list[list], intendedlength: int, listname: str): # Checks the validity of the trades, used for debugging
    for i in range(0, len(inputlist)):
        match isinstance(inputlist[i], list):
            case True:
                for j in range(0, len(inputlist[i][j])):
                    if len(inputlist[i][j]) != intendedlength:
                        print(f"Number of items in list {listname}, sublist {j} is not the same as the number of Trades!")
            case False:
                if len(inputlist[i]) != intendedlength:
                    print(f"Number of items in list {listname} is not the same as the number of Trades!")

def GetName(var): # gives us the name of the variable we input.
    for name, value in locals().items():
        if value is var:
            return name

def ShopCreator(ShopList: list, DeleteArgentumShops: bool): # Makes the shops
    with open("./_internal/JsonOutputs/common/MNU_ShopChange.json", 'r+', encoding='utf-8') as file: # Adds the exchange tasks
        data = json.load(file)
        ShopChangeStartRow = Helper.GetMaxValue("./_internal/JsonOutputs/common/MNU_ShopChange.json", "$id") + 1 # used in MNU_ShopList for "TableID"
        CurrRow = Helper.GetMaxValue("./_internal/JsonOutputs/common/MNU_ShopChange.json", "$id") + 1
        CurrInputTask = Helper.GetMaxValue("./_internal/JsonOutputs/common/MNU_ShopChange.json", "$id") + 1
        for shop in ShopList:
            ShopChangeRowToAdd = {"$id": CurrRow, "DefTaskSet1": 0, "DefTaskSet2": 0, "DefTaskSet3": 0, "DefTaskSet4": 0, "DefTaskSet5": 0, "DefTaskSet6": 0, "DefTaskSet7": 0, "DefTaskSet8": 0, "AddTaskSet1": 0, "AddCondition1": 0, "AddTaskSet2": 0, "AddCondition2": 0, "AddTaskSet3": 0, "AddCondition3": 0, "AddTaskSet4": 0, "AddCondition4": 0, "AddTaskSet5": 0, "AddCondition5": 0, "AddTaskSet6": 0, "AddCondition6": 0, "AddTaskSet7": 0, "AddCondition7": 0, "AddTaskSet8": 0, "AddCondition8": 0, "LinkQuestTask": 0, "LinkQuestTaskID": 0, "UnitText": 0}
            for i in range(0, len(shop)):
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
    with open("./_internal/JsonOutputs/common_ms/fld_shopchange.json", 'r+', encoding='utf-8') as file: # Changes the reward name for the token shop
        data = json.load(file)
        CurrRow = Helper.GetMaxValue("./_internal/JsonOutputs/common_ms/fld_shopchange.json", "$id") + 1
        StartingShopChangeNameRow = Helper.GetMaxValue("./_internal/JsonOutputs/common_ms/fld_shopchange.json", "$id") + 1 # Used in MNU_ShopChangeTask for "Name"
        for shop in ShopList:
            for reward in shop["RewardNames"]:
                data["rows"].append({"$id": CurrRow, "style": 36, "name": reward})
                CurrRow += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/MNU_ShopChangeTask.json", 'r+', encoding='utf-8') as file: # Now we define what each task does
        data = json.load(file)
        CurrRow = Helper.GetMaxValue("./_internal/JsonOutputs/common/MNU_ShopChangeTask.json", "$id") + 1
        for shop in ShopList:
            for i in range(0, len(shop["SetItemIDs"][0])):
                data["rows"].append({"$id": CurrRow, "Name": StartingShopChangeNameRow, "SetItem1": shop["SetItemIDs"][0][i], "SetNumber1": shop["SetItemQtys"][0][i], "SetItem2": shop["SetItemIDs"][1][i], "SetNumber2": shop["SetItemQtys"][1][i], "SetItem3": shop["SetItemIDs"][2][i], "SetNumber3": shop["SetItemQtys"][2][i], "SetItem4": shop["SetItemIDs"][3][i], "SetNumber4": shop["SetItemQtys"][3][i], "SetItem5": shop["SetItemIDs"][4][i], "SetNumber5": shop["SetItemQtys"][4][i], "HideReward": shop["HideReward"][i], "Reward": shop["RewardIDs"][i], "HideRewardFlag": 0, "AddFlagValue": 0, "forcequit": 0, "IraCraftIndex": 0})
                CurrRow += 1
                StartingShopChangeNameRow += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/FLD_QuestReward.json", 'r+', encoding='utf-8') as file: # Sets the reward for each task
        data = json.load(file)
        CurrRow = Helper.GetMaxValue("./_internal/JsonOutputs/common/FLD_QuestReward.json", "$id") + 1
        for shop in ShopList:
            for i in range(0, len(shop["RewardIDs"])):
                data["rows"].append({"$id": CurrRow, "Gold": 0, "EXP": shop["RewardXP"][i], "Sp": shop["RewardSP"][i], "Coin": 0, "DevelopZone": 0, "DevelopPoint": 0, "TrustPoint": 0, "MercenariesPoint": 0, "IdeaCategory": 0, "IdeaValue": 0, "ItemID1": shop["RewardItemIDs"][0][i], "ItemNumber1": shop["RewardQtys"][0][i], "ItemID2": shop["RewardItemIDs"][1][i], "ItemNumber2": shop["RewardQtys"][1][i], "ItemID3": shop["RewardItemIDs"][2][i], "ItemNumber3": shop["RewardQtys"][2][i], "ItemID4": shop["RewardItemIDs"][3][i], "ItemNumber4": shop["RewardQtys"][3][i]})
                CurrRow += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common_ms/fld_shopname.json", 'r+', encoding='utf-8') as file: # Adds new shop name to list 
        data = json.load(file)
        CurrRow = Helper.GetMaxValue("./_internal/JsonOutputs/common_ms/fld_shopname.json", "$id") + 1
        ShopNameStartingRow = Helper.GetMaxValue("./_internal/JsonOutputs/common_ms/fld_shopname.json", "$id") + 1 # used in MNU_ShopList for "Name"
        for i in range(0, len(ShopList)):
            data["rows"].append({"$id": CurrRow, "style": 70, "name": ShopList[i]["Name"]})
            CurrRow += 1
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./_internal/JsonOutputs/common/MNU_ShopList.json", 'r+', encoding='utf-8') as file: # Changes existing shop to match what we want
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
    # break into new function
    if DeleteArgentumShops:
        with open("./_internal/JsonOutputs/common_gmk/ma02a_FLD_NpcPop.json", 'r+', encoding='utf-8') as file: # Lets you rest in the Argentum Trade Guild Inn, but removes all other shops (we're adding them back after)
            data = json.load(file)
            for row in data["rows"]:
                if row["$id"] != 2096: # keeps only the inn as a shop in Argentum
                    row["ShopID"] = 0
                    row["flag"]["Talkable"] = 0
                    row["EventID"] = 0
                    row["QuestFlag"] = 0
            for i in range(0, len(ShopList)): # gives a specific npc the shop we want
                for row in data["rows"]:
                    if row["$id"] == ShopList[i]["NPCID"]:
                        row["ScenarioFlagMin"] = row["QuestFlag"] = row["QuestFlagMin"] = row["QuestFlagMax"] = row["TimeRange"] = row["Condition"] = row["Mot"] = row["QuestID"] = 0
                        row["ScenarioFlagMax"] = 10048
                        row["flag"]["Talkable"] = 1
                        row["EventID"] = ShopList[i]["ShopEventID"]
                        row["ShopID"] = ShopList[i]["ShopIDtoReplace"]
                        row["NpcID"] = ShopList[i]["NPCModel"]
                        row["Visible_XZ"] = 100 # lets us see them from a bit further
                        row["Visible_Y"] = 10
                        row["Invisible_XZ"] = 105
                        row["Invisible_Y"] = 15
                        break
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=2, ensure_ascii=False)

def ShopDictToClass(ShopList):
    ShopClassList = {}
    for shop in ShopList:
        ShopName = GetName(shop)
        tempshop = ExchangeShop(shop["Name"])
        tempshop.ShopIcon = shop["ShopIcon"]
        if len(str(shop["NPCID"])) == 4:
            mapidentifier = "0" + str(shop["NPCID"])[0]
        else:
            mapidentifier = str(shop["NPCID"])[:2]
        tempshop.ShopPosition = Helper.FindValues(f"./_internal/JsonOutputs/common_gmk/ma{mapidentifier}a_FLD_NpcPop.json", ["$id"], [shop["NPCID"]], "name")
        tempshop.ShopIDtoReplace = shop["ShopIDtoReplace"]
        tempshop.ChosenMapRowID = shop["NPCID"]
        tempshop.NewNPCModel = shop["NPCModel"]
        tempshop.TradeCount = len(shop["SetItemIDs"][0])
        tempshop.InputItemIDs = shop["SetItemIDs"]
        tempshop.InputItemQtys = shop["SetItemQtys"]
        tempshop.RewardItemIDs = shop["RewardItemIDs"]
        tempshop.RewardQtys = shop["RewardQtys"]
        tempshop.RewardNames = shop["RewardNames"]
        tempshop.RewardSP = shop["RewardSP"]
        tempshop.RewardXP = shop["RewardXP"]
        tempshop.RewardHidden = shop["HideReward"]
        ShopClassList[ShopName] = tempshop
    print(ShopClassList)