from scripts import Helper, JSONParser, PopupDescriptions
import json
import random
import time
from XC2.XC2_Scripts.IDs import *
from scripts import Helper

class TornaSideQuest: # created to allow me to pass these objects easier
    def __init__(self, input, addtolist, rewardnumber):
        self.id = input["Quest Number"]
        self.name = input["Quest Name"]
        self.mainreq = input["Main Story Req"]
        self.sideprereq = input["Sidequest Pre-Req"]
        if self.id == 20:
            pass
        self.itemreqs = Helper.MultiLevelListToSingleLevelList(input["Item Requirements"])
        self.complus = input["Community Gained"]
        self.comreq = input["Community Level Req"]
        self.rewardids = input["Reward Set IDs"]
        self.randomizeditems = Helper.ExtendListtoLength(Helper.ExtendListtoLength([], rewardnumber, "-1"), 4, "0") # holds ids, -1 for progression, 0 for filler spots
        if self.id > 58:
            self.randomizeditems = [-2,-2,-2,-2] # we just throw some invalid items here, the randomizer will know not to give any items to these spots
        self.type = "sidequest"
        if rewardnumber > 0:
            self.hasprogression = True
        else:
            self.hasprogression = False
        self.shopchangeids = input["Shop Change IDs"]
        addtolist.append(self)

class TornaMainQuest:
    def __init__(self, input, addtolist):
        self.fldquesttaskid = input["FLD_QuestTask $id"]
        self.summary = input["Task Summary"]
        self.comreq = input["Community Level Req"]
        self.itemreqs = Helper.MultiLevelListToSingleLevelList(input["Item Requirements"])
        addtolist.append(self)
        self.id = addtolist.index(self) + 1

def SelectRandomPointGoal(): # There are some sidequests that require you to feed items into a shop, any combination of items to get you to the point requirement. This function randomly chooses 1 of the items in that shop, and notes it down as the logical requirement, restricting it to be placed logically accessible before the quest
    # there's probably a much easier way to do this that I'm just not thinking of, but it gets the job done. Probably a dictionary now that I think about it more, but at this point it works, why fix it
    OptionalRows = [91,95,99,100,96,101,102,97,98,103,92] # needs to stay in this order or else the indexes will be wrong!
    TaskLists = []
    CurTaskList = []
    with open("./XC2/JsonOutputs/common/MNU_ShopChange.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for optional in OptionalRows:
            CurTaskList = []
            for row in data["rows"]:
                if row["$id"] == optional:
                    for num in range(1, 9):
                        if row[f"DefTaskSet{num}"] != 0:
                            CurTaskList.append(row[f"DefTaskSet{num}"])
                        if row[f"AddTaskSet{num}"] != 0:
                            CurTaskList.append(row[f"AddTaskSet{num}"])
                    break
            TaskLists.append(CurTaskList)
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    
    TaskIndexes = []
    for tasklist in TaskLists: # choose the index
        TaskIndexes.append(random.choice(Helper.InclRange(0, len(tasklist) - 1)))
    Quest15List = [[30347,30352,30379],[30400,30404,30403],[30407,30438,30408,30411],[30384,30404,30352,30407,30408],[30363,30352,30353],[30406,30404,30408,30407,30403,26146],[30386,30365,30409,30407,26147]]
    Quest28List = [[30353],[30403],[30438],[30356]]
    Quest29List1 = [[30373],[30374],[30375],[30377],[30378]]
    Quest29List2 = [[30425],[30426],[30427],[30428],[30429],[30430]]
    Quest30List = [[30358],[30359],[30360],[30361],[30362],[30409],[30410],[30411],[30412],[30413]]
    Quest34List1 = [[30347,30352,30379],[30400,30404,30403],[30352,30353,30354],[30347,30353,30380],[30384,30404,30352,30407,30408],[30382,30383,30356,30400],[30363,30352,30353],[30400,30363,30406],[30396,30389,30354],[30364,30365,30402],[30365,30358,30355,30385,30396],[30400,30363,30364,30366,30349],[30347,30352,30360],[30380,30358,30353,30363],[30386,30401,30402,30438]]
    Quest34List2 = [[30348,30349,30357,30416],[30345,30354,30364],[30407,30438,30408,30411],[30405,30401,30416,30381],[30356,30357,30400,30385,30405],[30407,30402,30389,30384],[30438,30383,30398,30356,30401]]
    Quest44List1 = [[30363],[30364],[30416],[30366]]
    Quest44List2 = [[30363],[30364],[30366],[30414],[30416],[30417],[30419]]
    Quest47List = [[30343],[30351],[30357],[30371],[30380],[30382],[30384],[30386],[30398],[30421],[30422],[30424],[30439],[30432],[30434],[30436]]
    Quest55List = [[30345],[30349],[30406]]
    AllQuestListTasks = [Quest15List,Quest28List, Quest29List1, Quest29List2, Quest30List, Quest34List1, Quest34List2, Quest44List1, Quest44List2, Quest47List, Quest55List]
    Quest15Optional, Quest28Optional, Quest29Optional1, Quest29Optional2, Quest30Optional, Quest34Optional1, Quest34Optional2, Quest44Optional1, Quest44Optional2, Quest47Optional, Quest55Optional = [],[],[],[],[],[],[],[],[],[],[]
    global AllOptionals
    AllOptionals = [Quest15Optional, Quest28Optional, Quest29Optional1, Quest29Optional2, Quest30Optional, Quest34Optional1, Quest34Optional2, Quest44Optional1, Quest44Optional2, Quest47Optional, Quest55Optional]
    for optional in range(len(AllOptionals)):
        AllOptionals[optional] = AllQuestListTasks[optional][TaskIndexes[optional]]
    
    with open("./XC2/JsonOutputs/common/MNU_ShopChange.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for optional in range(len(OptionalRows)):
            for row in data["rows"]:
                if row["$id"] == OptionalRows[optional]:
                    for num in range(1, 9):
                        row[f"DefTaskSet{num}"], row[f"AddTaskSet{num}"], row[f"AddCondition{num}"] = 0,0,0
                    row["DefTaskSet1"] = TaskLists[optional][TaskIndexes[optional]]
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)
    with open("./XC2/JsonOutputs/common/MNU_ShopChangeTask.json", 'r+', encoding='utf-8') as file:
        data = json.load(file)
        for optional in range(len(TaskLists)):
            for row in data["rows"]:
                if row["$id"] == TaskLists[optional][TaskIndexes[optional]]:
                    row["AddFlagValue"] = 100 # 100 should be enough to instantly clear any flag requirements
                    break
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=2, ensure_ascii=False)

def SelectCommunityQuests(CommunityReqs: list, QuestRewardQty, Community1Gate, Community2Gate): # Selects the community quests that logically unlock Story Events 38 and 50 (lv 2 and lv 4 community)
    TornaSidequest1 = {
        'Quest Name': 'What Bars the Way',
        'Quest Number': 1,
        'Main Story Req': 9,
        'Sidequest Pre-Req': [],
        'Item Requirements': [HazeKey, [ManipEtherKey[0]], [HazeAff[0]], MythraKey, [LightKey[0]]], # LevelUpTokens[:11]],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1082],
        'Shop Change IDs': []
    }
    TornaSidequest2 = {
        'Quest Name': 'A Simple Errand',
        'Quest Number': 2,
        'Main Story Req': 10,
        'Sidequest Pre-Req': [],
        'Item Requirements': [], # LevelUpTokens[:11]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1060],
        'Shop Change IDs': []
    }
    TornaSidequest3 = {
        'Quest Name': 'Barmy Tale of Barney',
        'Quest Number': 3,
        'Main Story Req': 10,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[SwordplayKey[0]]], #LevelUpTokens[:7]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1076],
        'Shop Change IDs': []
    }
    TornaSidequest4 = {
        'Quest Name': 'Driver Coaching',
        'Quest Number': 4,
        'Main Story Req': 10,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1206],
        'Shop Change IDs': []
    }
    TornaSidequest5 = {
        'Quest Name': 'A Rare Sense of Justice',
        'Quest Number': 5,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [32, 56],
        'Item Requirements': [AegaeonKey, SuperstrKey, AegaeonAff[:3], HazeKey, KeenEyeKey, HazeAff[:3]],
        'Community Gained': 2,
        'Community Level Req': 5,
        'Reward Set IDs': [1061],
        'Shop Change IDs': []
    }
    TornaSidequest6 = {
        'Quest Name': 'Punpun\'s Rival',
        'Quest Number': 6,
        'Main Story Req': 30, # used to be 12, when LevelUpTokens were going to be included
        'Sidequest Pre-Req': [],
        'Item Requirements': [], # LevelUpTokens[:35]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1081],
        'Shop Change IDs': []
    }
    TornaSidequest7 = {
        'Quest Name': 'Doc, the Miasma Slayer',
        'Quest Number': 7,
        'Main Story Req': 12,
        'Sidequest Pre-Req': [],
        'Item Requirements': [], # LevelUpTokens[:13]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1080],
        'Shop Change IDs': []
    }
    TornaSidequest8 = {
        'Quest Name': 'Power Unimaginable',
        'Quest Number': 8,
        'Main Story Req': 16,
        'Sidequest Pre-Req': [],
        'Item Requirements': [], # LevelUpTokens[:17]],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1083],
        'Shop Change IDs': []
    }
    TornaSidequest9 = {
        'Quest Name': 'Blade Coaching',
        'Quest Number': 9,
        'Main Story Req': 16,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1208],
        'Shop Change IDs': []
    }
    TornaSidequest10 = {
        'Quest Name': 'Further Blade Coaching',
        'Quest Number': 10,
        'Main Story Req': 16,
        'Sidequest Pre-Req': [9],
        'Item Requirements': [],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1209],
        'Shop Change IDs': []
    }
    TornaSidequest11 = {
        'Quest Name': 'The Ardainian Gunman',
        'Quest Number': 11,
        'Main Story Req': 16,
        'Sidequest Pre-Req': [],
        'Item Requirements': [], # LevelUpTokens[:20]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1074],
        'Shop Change IDs': []
    }
    TornaSidequest12 = {
        'Quest Name': 'A Taste of Home',
        'Quest Number': 12,
        'Main Story Req': 16,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[30347,30379,30406,30418,26149] , [30400,30379,30406,30418,30402,26191]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1075],
        'Shop Change IDs': []
    }
    TornaSidequest13 = {
        'Quest Name': 'Salvage the Salvager',
        'Quest Number': 13,
        'Main Story Req': 16,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[30426] , [30427] , [25465]], # LevelUpTokens[:21]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1063],
        'Shop Change IDs': []
    }
    TornaSidequest14 = {
        'Quest Name': 'Where\'s the Boy Gone?',
        'Quest Number': 14,
        'Main Story Req': 20,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1084],
        'Shop Change IDs': []
    }
    TornaSidequest15 = {
        'Quest Name': 'My First Adventure',
        'Quest Number': 15,
        'Main Story Req': 20,
        'Sidequest Pre-Req': [],
        'Item Requirements': [AllOptionals[0]],
        'Community Gained': 2,
        'Community Level Req': 0,
        'Reward Set IDs': [1064],
        'Shop Change IDs': [91]
    }
    TornaSidequest16 = {
        'Quest Name': 'Seeking a Seeker',
        'Quest Number': 16,
        'Main Story Req': 20,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[30387,30411,30421,30360,30444] , [30425] , [30428]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1079],
        'Shop Change IDs': []
    }
    TornaSidequest17 = {
        'Quest Name': 'Feeding an Army',
        'Quest Number': 17,
        'Main Story Req': 25,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[30380] , [30438] , [30347]],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1085],
        'Shop Change IDs': []
    }
    TornaSidequest18 = {
        'Quest Name': 'Further Driver Coaching',
        'Quest Number': 18,
        'Main Story Req': 25,
        'Sidequest Pre-Req': [4],
        'Item Requirements': [],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1207],
        'Shop Change IDs': []
    }
    TornaSidequest19 = {
        'Quest Name': 'Fusion Coaching',
        'Quest Number': 19,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [10,18],
        'Item Requirements': [],
        'Community Gained': 2,
        'Community Level Req': 2,
        'Reward Set IDs': [1210],
        'Shop Change IDs': []
    }
    TornaSidequest20 = {
        'Quest Name': 'What Matters Most',
        'Quest Number': 20,
        'Main Story Req': 30, # used to be 25, changed when I removed the level up token item 
        'Sidequest Pre-Req': [],
        'Item Requirements': [[25460] , [25461]], # LevelUpTokens[:36]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1054],
        'Shop Change IDs': []
    }
    TornaSidequest21 = {
        'Quest Name': 'The Malcontent Doctor',
        'Quest Number': 21,
        'Main Story Req': 26,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[25457]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1053],
        'Shop Change IDs': []
    }
    TornaSidequest22 = {
        'Quest Name': 'Lett Bridge Restoration',
        'Quest Number': 22,
        'Main Story Req': 26,
        'Sidequest Pre-Req': [],
        'Item Requirements': [], # LevelUpTokens[:25]],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1086],
        'Shop Change IDs': []
    }
    TornaSidequest23 = {
        'Quest Name': 'Thicker Than Water',
        'Quest Number': 23,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [],
        'Item Requirements': [HazeKey, KeenEyeKey[:2], [HazeAff[0]], MythraKey, FocusKey, MythraAff[:3]],
        'Community Gained': 3,
        'Community Level Req': 2,
        'Reward Set IDs': [1052],
        'Shop Change IDs': []
    }
    TornaSidequest24 = {
        'Quest Name': 'The Travails of War',
        'Quest Number': 24,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [], # LevelUpTokens[:42]],
        'Community Gained': 2,
        'Community Level Req': 4,
        'Reward Set IDs': [1057],
        'Shop Change IDs': []
    }
    TornaSidequest25 = {
        'Quest Name': 'To Cross a Desert',
        'Quest Number': 25,
        'Main Story Req': 32,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[30355] , [30383]],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1087],
        'Shop Change IDs': []
    }
    TornaSidequest26 = {
        'Quest Name': 'For Lack of a Hunter',
        'Quest Number': 26,
        'Main Story Req': 35,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[30380]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1078],
        'Shop Change IDs': []
    }
    TornaSidequest27 = {
        'Quest Name': 'Here Be Treasure',
        'Quest Number': 27,
        'Main Story Req': 35,
        'Sidequest Pre-Req': [],
        'Item Requirements': [MinothKey, [MiningKey[0]], [FortitudeKey[0]]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1077],
        'Shop Change IDs': []
    }
    TornaSidequest28 = {
        'Quest Name': 'The Secret of Dannagh',
        'Quest Number': 28,
        'Main Story Req': 35,
        'Sidequest Pre-Req': [13],
        'Item Requirements': [[30428,30375,30388,30433,30428,30375,30388,30433] , [30428] , [30375] , [30388] , [30433] , AllOptionals[1]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1058, 1059],
        'Shop Change IDs': [95]
    }
    TornaSidequest29 = {
        'Quest Name': 'The Tornan Inventor',
        'Quest Number': 29,
        'Main Story Req': 36,
        'Sidequest Pre-Req': [],
        'Item Requirements': [AllOptionals[2] , AllOptionals[3]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1068],
        'Shop Change IDs': [99,100]
    }
    TornaSidequest30 = {
        'Quest Name': 'Nuts about Bugs',
        'Quest Number': 30,
        'Main Story Req': 36,
        'Sidequest Pre-Req': [],
        'Item Requirements': [AllOptionals[4]],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1066],
        'Shop Change IDs': [96]
    }
    TornaSidequest31 = {
        'Quest Name': 'Lighting the Way',
        'Quest Number': 31,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1034],
        'Shop Change IDs': []
    }
    TornaSidequest32 = {
        'Quest Name': 'An Oasis for All',
        'Quest Number': 32,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [],
        'Item Requirements': [], #LevelUpTokens[:36]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1035],
        'Shop Change IDs': []
    }
    TornaSidequest33 = {
        'Quest Name': 'Armus Gone Astray',
        'Quest Number': 33,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [],
        'Item Requirements': [HazeKey, [KeenEyeKey[0]], MythraKey, [FocusKey[0]]], # LevelUpTokens[:32]],
        'Community Gained': 2,
        'Community Level Req': 0,
        'Reward Set IDs': [1032],
        'Shop Change IDs': []
    }
    TornaSidequest34 = {
        'Quest Name': 'Hungry for More',
        'Quest Number': 34,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [],
        'Item Requirements': [AllOptionals[5] , AllOptionals[6]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1071],
        'Shop Change IDs': [101,102]
    }
    TornaSidequest35 = {
        'Quest Name': 'Bolstering Sales',
        'Quest Number': 35,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[30340] , [30348] , [30399] , [30341] , [30395] , [30423]],
        'Community Gained': 2,
        'Community Level Req': 0,
        'Reward Set IDs': [1033],
        'Shop Change IDs': []
    }
    TornaSidequest36 = {
        'Quest Name': 'Helping the Helper',
        'Quest Number': 36,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[25458,30342,30368,30429,26164] , [25458]],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': [1036],
        'Shop Change IDs': []
    }
    TornaSidequest37 = {
        'Quest Name': 'Homegrown Inventor',
        'Quest Number': 37,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [30],
        'Item Requirements': [[SwordplayKey[0]] , [30374] , [30378] , [25462]], #LevelUpTokens[:40]],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': [1037],
        'Shop Change IDs': []
    }
    TornaSidequest38 = {
        'Quest Name': 'Duplicity',
        'Quest Number': 38,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [],
        'Item Requirements': [], #LevelUpTokens[:41]],
        'Community Gained': 2,
        'Community Level Req': 2,
        'Reward Set IDs': [1055],
        'Shop Change IDs': []
    }
    TornaSidequest39 = {
        'Quest Name': 'Sweetest Tidings',
        'Quest Number': 39,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [],
        'Item Requirements': [], #LevelUpTokens[:42]],
        'Community Gained': 2,
        'Community Level Req': 2,
        'Reward Set IDs': [1062],
        'Shop Change IDs': []
    }
    TornaSidequest40 = {
        'Quest Name': 'Passing the Torch',
        'Quest Number': 40,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [MinothKey, MiningKey[:2], MinothAff[:2], FortitudeKey[:2], JinAff[:2] , 25455], # LevelUpTokens[:38]],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': [1043],
        'Shop Change IDs': []
    }
    TornaSidequest41 = {
        'Quest Name': 'Trail of Destruction',
        'Quest Number': 41,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [2],
        'Item Requirements': [AegaeonKey, SuperstrKey[:2], AegaeonAff[:2], MythraKey, FocusKey[:2], [MythraAff[0]]], # LevelUpTokens[:44]],
        'Community Gained': 2,
        'Community Level Req': 2,
        'Reward Set IDs': [1038],
        'Shop Change IDs': []
    }
    TornaSidequest42 = {
        'Quest Name': 'Forest Trail Antics',
        'Quest Number': 42,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': [1039],
        'Shop Change IDs': []
    }
    TornaSidequest43 = {
        'Quest Name': 'Making Up the Numbers',
        'Quest Number': 43,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [3, 41, 42],
        'Item Requirements': [],
        'Community Gained': 3,
        'Community Level Req': 2,
        'Reward Set IDs': [1056],
        'Shop Change IDs': []
    }
    TornaSidequest44 = {
        'Quest Name': 'The Fish That Could Be',
        'Quest Number': 44,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [],
        'Item Requirements': [AllOptionals[7] , AllOptionals[8]],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': [1067],
        'Shop Change IDs': [97,98]
    }
    TornaSidequest45 = {
        'Quest Name': 'Hubbie Takes a Hike',
        'Quest Number': 45,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [44],
        'Item Requirements': [],
        'Community Gained': 2,
        'Community Level Req': 3,
        'Reward Set IDs': [1073],
        'Shop Change IDs': []
    }
    TornaSidequest46 = {
        'Quest Name': 'Manning the Gates',
        'Quest Number': 46,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [31, 32],
        'Item Requirements': [MythraKey, FocusKey[:2], [MythraAff[0]], HazeKey, KeenEyeKey[:2], [HazeAff[0]]], #  LevelUpTokens[:40]],
        'Community Gained': 2,
        'Community Level Req': 3,
        'Reward Set IDs': [1040],
        'Shop Change IDs': []
    }
    TornaSidequest47 = {
        'Quest Name': '100k in the Red',
        'Quest Number': 47,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [],
        'Item Requirements': [AllOptionals[9]],
        'Community Gained': 1,
        'Community Level Req': 3,
        'Reward Set IDs': [1072],
        'Shop Change IDs': [103]
    }
    TornaSidequest48 = {
        'Quest Name': 'Proof of Love',
        'Quest Number': 48,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [36],
        'Item Requirements': [],
        'Community Gained': 2,
        'Community Level Req': 3,
        'Reward Set IDs': [1044],
        'Shop Change IDs': []
    }
    TornaSidequest49 = {
        'Quest Name': 'Planning for the Future',
        'Quest Number': 49,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[30388] , [25464]], # LevelUpTokens[:43]],
        'Community Gained': 3,
        'Community Level Req': 3,
        'Reward Set IDs': [1042],
        'Shop Change IDs': []
    }
    TornaSidequest50 = {
        'Quest Name': 'The Bard Factor',
        'Quest Number': 50,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [48],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 4,
        'Reward Set IDs': [1069],
        'Shop Change IDs': []
    }
    TornaSidequest51 = {
        'Quest Name': 'Azurda SOS',
        'Quest Number': 51,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [47, 48],
        'Item Requirements': [], #LevelUpTokens[:51]],
        'Community Gained': 2,
        'Community Level Req': 4,
        'Reward Set IDs': [1065],
        'Shop Change IDs': []
    }
    TornaSidequest52 = {
        'Quest Name': 'Great Tornan Cook-Off',
        'Quest Number': 52,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [34],
        'Item Requirements': [[30382,30384,30347,30383,30408,26148] , [30405,30400,30347,30398,30438,26150]],
        'Community Gained': 2,
        'Community Level Req': 4,
        'Reward Set IDs': [1047, 1048],
        'Shop Change IDs': []
    }
    TornaSidequest53 = {
        'Quest Name': 'Safety Measures',
        'Quest Number': 53,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [15, 43, 49],
        'Item Requirements': [[30388] , [30372] , [30387] , [30392] , [30427]],
        'Community Gained': 2,
        'Community Level Req': 3,
        'Reward Set IDs': [1041],
        'Shop Change IDs': []
    }
    TornaSidequest54 = {
        'Quest Name': 'Further Feeding Issues',
        'Quest Number': 54,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [AegaeonKey, ComWaterKey[:2], AegaeonAff[:2] , [25463,30413,30423,30359,26182]], # LevelUpTokens[:39]],
        'Community Gained': 1,
        'Community Level Req': 4,
        'Reward Set IDs': [1045],
        'Shop Change IDs': []
    }
    TornaSidequest55 = {
        'Quest Name': 'Unforgotten Promise',
        'Quest Number': 55,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [MythraKey, FocusKey, MythraAff[:3], HazeKey, KeenEyeKey, HazeAff[:3] , [30344] , [30370] , [25536] , AllOptionals[10]],
        'Community Gained': 2,
        'Community Level Req': 4,
        'Reward Set IDs': [1046],
        'Shop Change IDs': [92]
    }
    TornaSidequest56 = {
        'Quest Name': 'What Goes Around',
        'Quest Number': 56,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [36, 38, 43],
        'Item Requirements': [],
        'Community Gained': 2,
        'Community Level Req': 5,
        'Reward Set IDs': [1049],
        'Shop Change IDs': []
    }
    TornaSidequest57 = {
        'Quest Name': 'Community Spirit',
        'Quest Number': 57,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [5, 15, 42, 37, 49, 48, 43, 46, 24, 56],
        'Item Requirements': [],
        'Community Gained': 2,
        'Community Level Req': 5,
        'Reward Set IDs': [1051],
        'Shop Change IDs': []
    }
    TornaSidequest58 = {
        'Quest Name': 'A Small Promise',
        'Quest Number': 58,
        'Main Story Req': 52,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 2,
        'Community Level Req': 5,
        'Reward Set IDs': [1050],
        'Shop Change IDs': []
    }
    TornaSidequest59 = {
        'Quest Name': 'Martha',
        'Quest Number': 59,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 5,
        'Reward Set IDs': [],
        'Shop Change IDs': []
    }
    TornaSidequest60 = {
        'Quest Name': 'Benny',
        'Quest Number': 60,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [26],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': [],
        'Shop Change IDs': []
    }
    TornaSidequest61 = {
        'Quest Name': 'Dolala',
        'Quest Number': 61,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': [],
        'Shop Change IDs': []
    }
    TornaSidequest62 = {
        'Quest Name': 'Clemens',
        'Quest Number': 62,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': [],
        'Shop Change IDs': []
    }
    TornaSidequest63 = {
        'Quest Name': 'Nalsaz',
        'Quest Number': 63,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': [],
        'Shop Change IDs': []
    }
    TornaSidequest64 = {
        'Quest Name': 'Yrissa',
        'Quest Number': 64,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [42],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': [],
        'Shop Change IDs': []
    }
    TornaSidequest65 = {
        'Quest Name': 'Clarke',
        'Quest Number': 65,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [54],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 4,
        'Reward Set IDs': [],
        'Shop Change IDs': []
    }
    TornaSidequest66 = {
        'Quest Name': 'Augustus',
        'Quest Number': 66,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [54],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 4,
        'Reward Set IDs': [],
        'Shop Change IDs': []
    }
    TornaSidequest67 = {
        'Quest Name': 'Lavinia',
        'Quest Number': 67,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [23],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 4,
        'Reward Set IDs': [],
        'Shop Change IDs': []
    }
    TornaSidequest68 = {
        'Quest Name': 'Mini',
        'Quest Number': 68,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [53],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 3,
        'Reward Set IDs': [],
        'Shop Change IDs': []
    }
    TornaSidequest69 = {
        'Quest Name': 'Tranc',
        'Quest Number': 69,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [5],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 5,
        'Reward Set IDs': [],
        'Shop Change IDs': []
    }
    TornaSidequest70 = {
        'Quest Name': 'Vill Ethelmar',
        'Quest Number': 70,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 5,
        'Reward Set IDs': [],
        'Shop Change IDs': []
    }
    TornaSidequest71 = {
        'Quest Name': 'Gedd',
        'Quest Number': 71,
        'Main Story Req': 52,
        'Sidequest Pre-Req': [29],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 5,
        'Reward Set IDs': [],
        'Shop Change IDs': []
    }
    TornaSidequest72 = {
        'Quest Name': 'Piper',
        'Quest Number': 72,
        'Main Story Req': 52,
        'Sidequest Pre-Req': [5],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 5,
        'Reward Set IDs': [],
        'Shop Change IDs': []
    }
    TornaSidequest73 = {
        'Quest Name': 'Mauna',
        'Quest Number': 73,
        'Main Story Req': 52,
        'Sidequest Pre-Req': [5],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 5,
        'Reward Set IDs': [],
        'Shop Change IDs': []
    }
    TornaSidequest74 = {
        'Quest Name': 'Elba',
        'Quest Number': 74,
        'Main Story Req': 52,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 5,
        'Reward Set IDs': [],
        'Shop Change IDs': []
    }

    TornaSidequestDict = [TornaSidequest1, TornaSidequest2, TornaSidequest3, TornaSidequest4, TornaSidequest5, TornaSidequest6, TornaSidequest7, TornaSidequest8, TornaSidequest9, TornaSidequest10, TornaSidequest11, TornaSidequest12, TornaSidequest13, TornaSidequest14, TornaSidequest15, TornaSidequest16, TornaSidequest17, TornaSidequest18, TornaSidequest19, TornaSidequest20, TornaSidequest21, TornaSidequest22, TornaSidequest23, TornaSidequest24, TornaSidequest25, TornaSidequest26, TornaSidequest27, TornaSidequest28, TornaSidequest29, TornaSidequest30, TornaSidequest31, TornaSidequest32, TornaSidequest33, TornaSidequest34, TornaSidequest35, TornaSidequest36, TornaSidequest37, TornaSidequest38, TornaSidequest39, TornaSidequest40, TornaSidequest41, TornaSidequest42, TornaSidequest43, TornaSidequest44, TornaSidequest45, TornaSidequest46, TornaSidequest47, TornaSidequest48, TornaSidequest49, TornaSidequest50, TornaSidequest51, TornaSidequest52, TornaSidequest53, TornaSidequest54, TornaSidequest55, TornaSidequest56, TornaSidequest57, TornaSidequest58, TornaSidequest59, TornaSidequest60, TornaSidequest61, TornaSidequest62, TornaSidequest63, TornaSidequest64, TornaSidequest65, TornaSidequest66, TornaSidequest67, TornaSidequest68, TornaSidequest69, TornaSidequest70, TornaSidequest71, TornaSidequest72, TornaSidequest73, TornaSidequest74]
    global TornaSidequests
    TornaSidequests = [] # holds the TornaSideQuest class objects

    for sidequest in TornaSidequestDict:
        TornaSideQuest(sidequest, TornaSidequests, QuestRewardQty)

    TornaMainQuest1 = {
        'FLD_QuestTask $id': 1,
        'Task Summary': 'Defeat the Tutorial Fight',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest2 = {
        'FLD_QuestTask $id': 2,
        'Task Summary': 'Leave Lasaria Woodland',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest3 = {
        'FLD_QuestTask $id': 49,
        'Task Summary': 'Collect Food',
        'Community Level Req': 0,
        'Item Requirements': [[30363] , [30352] , [30353] , PVC_Key]
    }
    TornaMainQuest4 = {
        'FLD_QuestTask $id': 50,
        'Task Summary': 'Open the Camp Menu',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest5 = {
        'FLD_QuestTask $id': 51,
        'Task Summary': 'Make Dinner',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest6 = {
        'FLD_QuestTask $id': 3,
        'Task Summary': 'Reach Feltley Village',
        'Community Level Req': 0,
        'Item Requirements': [[SwordplayKey[0]]]
    }
    TornaMainQuest7 = {
        'FLD_QuestTask $id': 4,
        'Task Summary': 'Defeat the Gargoyle in the Crater',
        'Community Level Req': 0,
        'Item Requirements': Helper.FindValues("./XC2/JsonOutputs/common/ITM_PcWpnChip.json", ["Rank"], [3], "$id")[:2] # [LevelUpTokens[:12]]
    }
    TornaMainQuest8 = {
        'FLD_QuestTask $id': 5,
        'Task Summary': 'Defeat Addam and Mythra',
        'Community Level Req': 0,
        'Item Requirements': [AddamKey, MythraKey, HazeKey] #,LevelUpTokens[:14]]
    }
    TornaMainQuest9 = {
        'FLD_QuestTask $id': 6,
        'Task Summary': 'Reach Yanchik Harbor',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest10 = {
        'FLD_QuestTask $id': 7,
        'Task Summary': 'Complete \"What Bars the Way\"',
        'Community Level Req': 0,
        'Item Requirements': [[ManipEtherKey[0]], [HazeAff[0]], [LightKey[0]]]
    }
    TornaMainQuest11 = {
        'FLD_QuestTask $id': 55,
        'Task Summary': 'Head for Yanchik Harbor',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest12 = {
        'FLD_QuestTask $id': 8,
        'Task Summary': 'Head out to Gormott',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest13 = {
        'FLD_QuestTask $id': 9,
        'Task Summary': 'Head for Torigoth Village',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest14 = {
        'FLD_QuestTask $id': 10,
        'Task Summary': 'Search Torigoth',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest15 = {
        'FLD_QuestTask $id': 11,
        'Task Summary': 'Go to the Torigoth Cemetary',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest16 = {
        'FLD_QuestTask $id': 12,
        'Task Summary': 'Defeat Brighid',
        'Community Level Req': 0,
        'Item Requirements': [HugoKey, BrighidKey, AegaeonKey, Helper.FindValues("./XC2/JsonOutputs/common/ITM_PcWpnChip.json", ["Rank"], [4], "$id")[:2]] #, LevelUpTokens[:18]]
    }
    TornaMainQuest17 = {
        'FLD_QuestTask $id': 13,
        'Task Summary': 'Complete \"Power Unimaginable\"',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest18 = {
        'FLD_QuestTask $id': 14,
        'Task Summary': 'Head for Lascham Cove',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest19 = {
        'FLD_QuestTask $id': 15,
        'Task Summary': 'Defeat Gort',
        'Community Level Req': 0,
        'Item Requirements': Helper.FindValues("./XC2/JsonOutputs/common/ITM_PcWpnChip.json", ["Rank"], [6], "$id")[:2] #LevelUpTokens[:24]]
    }
    TornaMainQuest20 = {
        'FLD_QuestTask $id': 16,
        'Task Summary': 'Head for Lascham Cove',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest21 = {
        'FLD_QuestTask $id': 17,
        'Task Summary': "Complete \"Where's the Boy Gone?\"",
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest22 = {
        'FLD_QuestTask $id': 18,
        'Task Summary': 'Head to the Strategy Room',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest23 = {
        'FLD_QuestTask $id': 19,
        'Task Summary': 'Speak to Addam',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest24 = {
        'FLD_QuestTask $id': 20,
        'Task Summary': 'Set out for Torna',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest25 = {
        'FLD_QuestTask $id': 21,
        'Task Summary': 'Reach the Militia Garrison',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest26 = {
        'FLD_QuestTask $id': 22,
        'Task Summary': 'Complete \"Feeding an Army\"',
        'Community Level Req': 0,
        'Item Requirements': [[30380], [30438], [30347], [30365]]
    }
    TornaMainQuest27 = {
        'FLD_QuestTask $id': 23,
        'Task Summary': 'Complete \"Lett Bridge Restoration\"',
        'Community Level Req': 0,
        'Item Requirements': [] # LevelUpTokens[:25]]
    }
    TornaMainQuest28 = {
        'FLD_QuestTask $id': 57,
        'Task Summary': 'Return to Aletta\'s Military Garrison',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest29 = {
        'FLD_QuestTask $id': 24,
        'Task Summary': 'Cross Lett Bridge',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest30 = {
        'FLD_QuestTask $id': 25,
        'Task Summary': 'Defeat Slithe Jagron',
        'Community Level Req': 0,
        'Item Requirements': Helper.FindValues("./XC2/JsonOutputs/common/ITM_PcWpnChip.json", ["Rank"], [9], "$id")[:2] # LevelUpTokens[:33]]
    }
    TornaMainQuest31 = {
        'FLD_QuestTask $id': 26,
        'Task Summary': 'Defeat Slithe Jagron Pt. 2',
        'Community Level Req': 0,
        'Item Requirements': [MinothKey]
    }
    TornaMainQuest32 = {
        'FLD_QuestTask $id': 27,
        'Task Summary': 'Rest at Olnard\'s Trail Campsite',
        'Community Level Req': 0,
        'Item Requirements': [OTC_Key]
    }
    TornaMainQuest33 = {
        'FLD_QuestTask $id': 28,
        'Task Summary': 'Complete \"To Cross a Desert\"',
        'Community Level Req': 0,
        'Item Requirements': [[30355] , [30383]]
    }
    TornaMainQuest34 = {
        'FLD_QuestTask $id': 29,
        'Task Summary': 'Head past Olnard\'s Trail',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest35 = {
        'FLD_QuestTask $id': 30,
        'Task Summary': 'Talk with residents of Hyber Village',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest36 = {
        'FLD_QuestTask $id': 31,
        'Task Summary': 'Cross Dannagh Desert',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest37 = {
        'FLD_QuestTask $id': 32,
        'Task Summary': 'Speak with Palace Guard Clemens',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest38 = {
        'FLD_QuestTask $id': 33,
        'Task Summary': f"Raise Community to Level {Community1Gate}",
        'Community Level Req': Community1Gate,
        'Item Requirements': []
    }
    TornaMainQuest39 = {
        'FLD_QuestTask $id': 34,
        'Task Summary': 'Head to Sachsum Gardens',
        'Community Level Req': Community1Gate,
        'Item Requirements': []
    }
    TornaMainQuest40 = {
        'FLD_QuestTask $id': 35,
        'Task Summary': 'Defeat Gargoyles Pt. 1',
        'Community Level Req': Community1Gate,
        'Item Requirements': Helper.FindValues("./XC2/JsonOutputs/common/ITM_PcWpnChip.json", ["Rank"], [11], "$id")[:2] # LevelUpTokens[:36]]
    }
    TornaMainQuest41 = {
        'FLD_QuestTask $id': 52,
        'Task Summary': 'Defeat Gargoyles Pt. 2',
        'Community Level Req': Community1Gate,
        'Item Requirements': []
    }
    TornaMainQuest42 = {
        'FLD_QuestTask $id': 53,
        'Task Summary': 'Defeat Gargoyles Pt. 3',
        'Community Level Req': Community1Gate,
        'Item Requirements': []
    }
    TornaMainQuest43 = {
        'FLD_QuestTask $id': 36,
        'Task Summary': 'Return to Sachsum Gardens',
        'Community Level Req': Community1Gate,
        'Item Requirements': []
    }
    TornaMainQuest44 = {
        'FLD_QuestTask $id': 37,
        'Task Summary': 'Defeat Malos',
        'Community Level Req': Community1Gate,
        'Item Requirements': Helper.FindValues("./XC2/JsonOutputs/common/ITM_PcWpnChip.json", ["Rank"], [13], "$id")[:2] # LevelUpTokens[:44]]
    }
    TornaMainQuest45 = {
        'FLD_QuestTask $id': 38,
        'Task Summary': 'Defeat Gargoyles Pt. 4',
        'Community Level Req': Community1Gate,
        'Item Requirements': []
    }
    TornaMainQuest46 = {
        'FLD_QuestTask $id': 39,
        'Task Summary': 'Speak with Palace Guard Clemens',
        'Community Level Req': Community1Gate,
        'Item Requirements': []
    }
    TornaMainQuest47 = {
        'FLD_QuestTask $id': 40,
        'Task Summary': 'Head to Torna\'s Womb',
        'Community Level Req': Community1Gate,
        'Item Requirements': []
    }
    TornaMainQuest48 = {
        'FLD_QuestTask $id': 56,
        'Task Summary': 'Head to Torna\'s Womb Pt. 2',
        'Community Level Req': Community1Gate,
        'Item Requirements': []
    }
    TornaMainQuest49 = {
        'FLD_QuestTask $id': 41,
        'Task Summary': 'Head to Spefan Inn',
        'Community Level Req': Community1Gate,
        'Item Requirements': []
    }
    TornaMainQuest50 = {
        'FLD_QuestTask $id': 42,
        'Task Summary': f"Raise Community to Level {Community2Gate}",
        'Community Level Req': Community2Gate,
        'Item Requirements': []
    }
    TornaMainQuest51 = {
        'FLD_QuestTask $id': 54,
        'Task Summary': 'Return to Main Auresco Gate',
        'Community Level Req': Community2Gate,
        'Item Requirements': []
    }
    TornaMainQuest52 = {
        'FLD_QuestTask $id': 43,
        'Task Summary': 'Return to Spefan Inn',
        'Community Level Req': Community2Gate,
        'Item Requirements': []
    }
    TornaMainQuest53 = {
        'FLD_QuestTask $id': 44,
        'Task Summary': 'Cross Dannagh Desert',
        'Community Level Req': Community2Gate,
        'Item Requirements': []
    }
    TornaMainQuest54 = {
        'FLD_QuestTask $id': 45,
        'Task Summary': 'Reach Malos',
        'Community Level Req': Community2Gate,
        'Item Requirements': []
    }
    TornaMainQuest55 = {
        'FLD_QuestTask $id': 46,
        'Task Summary': 'Defeat Malos Pt. 1',
        'Community Level Req': Community2Gate,
        'Item Requirements': Helper.FindValues("./XC2/JsonOutputs/common/ITM_PcWpnChip.json", ["Rank"], [20], "$id")[:2] # LevelUpTokens[:54]]
    }
    TornaMainQuest56 = {
        'FLD_QuestTask $id': 47,
        'Task Summary': 'Defeat Malos Pt. 2',
        'Community Level Req': Community2Gate,
        'Item Requirements': []
    }
    TornaMainQuest57 = {
        'FLD_QuestTask $id': 48,
        'Task Summary': 'Defeat Gort',
        'Community Level Req': Community2Gate,
        'Item Requirements': [] # LevelUpTokens[:57]]
    }

    global TornaMainquests # holds the TornaMainQuest class objects
    TornaMainquests = []
    TornaMainQuestDict = [TornaMainQuest1, TornaMainQuest2, TornaMainQuest3, TornaMainQuest4, TornaMainQuest5, TornaMainQuest6, TornaMainQuest7, TornaMainQuest8, TornaMainQuest9, TornaMainQuest10, TornaMainQuest11, TornaMainQuest12, TornaMainQuest13, TornaMainQuest14, TornaMainQuest15, TornaMainQuest16, TornaMainQuest17, TornaMainQuest18, TornaMainQuest19, TornaMainQuest20, TornaMainQuest21, TornaMainQuest22, TornaMainQuest23, TornaMainQuest24, TornaMainQuest25, TornaMainQuest26, TornaMainQuest27, TornaMainQuest28, TornaMainQuest29, TornaMainQuest30, TornaMainQuest31, TornaMainQuest32, TornaMainQuest33, TornaMainQuest34, TornaMainQuest35, TornaMainQuest36, TornaMainQuest37, TornaMainQuest38, TornaMainQuest39, TornaMainQuest40, TornaMainQuest41, TornaMainQuest42, TornaMainQuest43, TornaMainQuest44, TornaMainQuest45, TornaMainQuest46, TornaMainQuest47, TornaMainQuest48, TornaMainQuest49, TornaMainQuest50, TornaMainQuest51, TornaMainQuest52, TornaMainQuest53, TornaMainQuest54, TornaMainQuest55, TornaMainQuest56, TornaMainQuest57]

    for mainquest in TornaMainQuestDict:
        TornaMainQuest(mainquest, TornaMainquests)

    CommunityGate1Quests, CommunityGate2Quests = [], []

    for sidequest in TornaSidequests:
        if sidequest.mainreq < 38 and sidequest.comreq < Community1Gate:
            CommunityGate1Quests.append(sidequest)
        if sidequest.mainreq < 50 and sidequest.comreq < max(Community1Gate, Community2Gate):
            CommunityGate2Quests.append(sidequest)

    for sq in range(len(TornaSidequests)):
        if sq == 19:
            pass
        if TornaSidequests[sq].sideprereq != []:
            for prereq in TornaSidequests[sq].sideprereq:
                TornaSidequests[sq].itemreqs.extend(TornaSidequests[prereq - 1].itemreqs)
        TornaSidequests[sq].itemreqs = sorted(list(set(TornaSidequests[sq].itemreqs)))
        if TornaSidequests[sq].itemreqs == None:
            TornaSidequests[sq].itemreqs = []

    AllSidequestItemReqs = []
    for sidequest in TornaSidequests:
        AllSidequestItemReqs.append(Helper.MultiLevelListToSingleLevelList(sidequest.itemreqs))
    NewAllSidequestItemReqs = list(set(Helper.MultiLevelListToSingleLevelList(AllSidequestItemReqs)))

    ChosenGate1Quests, ChosenGate2Quests = [], []
    AlteredGate1Quests, AlteredGate2Quests = CommunityGate1Quests.copy(), CommunityGate2Quests.copy()
    ChosenPeopleGained = 0
    TotalGate1QuestRequirements, TotalGate2QuestRequirements = [], []

    if Community1Gate != 0:
        while ChosenPeopleGained < CommunityReqs[Community1Gate - 1]:
            CurrentQuest = random.choice(AlteredGate1Quests)
            ChosenGate1Quests.append(CurrentQuest)
            ChosenGate2Quests.append(CurrentQuest)
            ChosenPeopleGained += CurrentQuest.complus
            AlteredGate1Quests.remove(CurrentQuest)
            AlteredGate2Quests.remove(CurrentQuest)
            if CurrentQuest.sideprereq != []:
                for i in range(10): # should be enough to get dependency chains
                    for quest in ChosenGate1Quests:
                        if quest.sideprereq != []:
                            for prereq in quest.sideprereq:
                                if TornaSidequests[prereq - 1] not in ChosenGate1Quests:
                                    ChosenGate1Quests.append(TornaSidequests[prereq - 1])
                                    ChosenGate2Quests.append(TornaSidequests[prereq - 1])
                                    ChosenPeopleGained += TornaSidequests[prereq - 1].complus
                                    AlteredGate1Quests.remove(TornaSidequests[prereq - 1])
                                    AlteredGate2Quests.remove(TornaSidequests[prereq - 1])
    if Community2Gate != 0:
        while ChosenPeopleGained < CommunityReqs[Community2Gate - 1]:
            CurrentQuest = random.choice(AlteredGate2Quests)
            ChosenGate2Quests.append(CurrentQuest)
            ChosenPeopleGained += CurrentQuest.complus
            AlteredGate2Quests.remove(CurrentQuest)
            if CurrentQuest.sideprereq != []:
                for i in range(10): # should be enough to get dependency chains
                    for quest in ChosenGate2Quests:
                        if quest.sideprereq != []:
                            for prereq in quest.sideprereq:
                                if TornaSidequests[prereq - 1] not in ChosenGate2Quests:
                                    ChosenGate2Quests.append(TornaSidequests[prereq - 1])
                                    ChosenPeopleGained += TornaSidequests[prereq - 1].complus
                                    AlteredGate2Quests.remove(TornaSidequests[prereq - 1])
    for quest in ChosenGate1Quests:
        TotalGate1QuestRequirements.extend(quest.itemreqs)
    for quest in ChosenGate2Quests:
        TotalGate2QuestRequirements.extend(quest.itemreqs)
    TotalGate1QuestRequirements = Helper.MultiLevelListToSingleLevelList(TotalGate1QuestRequirements)
    TotalGate2QuestRequirements = Helper.MultiLevelListToSingleLevelList(TotalGate2QuestRequirements)
    TotalGate1QuestRequirements = list(set(TotalGate1QuestRequirements))
    TotalGate2QuestRequirements = list(set(TotalGate2QuestRequirements))
    TotalGate1QuestRequirements.sort()
    TotalGate2QuestRequirements.sort()

    StackStoryRequirements(TotalGate1QuestRequirements, TotalGate2QuestRequirements)
    #ChangeQuestShops()
    return ChosenGate1Quests, ChosenGate2Quests, TornaSidequests, TornaMainquests, NewAllSidequestItemReqs

def StackStoryRequirements(Gate1QuestReqs, Gate2QuestReqs): # This adds the previous story requirements to the current story step's requirements. I wanted to keep the original requirements clear in case someone makes a tracker from the dictionary above
    for storystep in range(1, len(TornaMainquests)):
        TornaMainquests[storystep].itemreqs.extend(TornaMainquests[storystep - 1].itemreqs) # adds the previous step's requirements
        TornaMainquests[storystep].itemreqs = Helper.MultiLevelListToSingleLevelList(TornaMainquests[storystep].itemreqs) # turns nested lists into one list
        if TornaMainquests[storystep].id == 38:
            TornaMainquests[storystep].itemreqs.extend(Gate1QuestReqs)
        elif TornaMainquests[storystep].id == 50:
            TornaMainquests[storystep].itemreqs.extend(Gate2QuestReqs)
        TornaMainquests[storystep].itemreqs = list(set(TornaMainquests[storystep].itemreqs))
        TornaMainquests[storystep].itemreqs.sort()
