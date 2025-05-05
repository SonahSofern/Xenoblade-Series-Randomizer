from scripts import Helper, JSONParser, PopupDescriptions
import json
import random
import time
from IDs import *

# if a quest has 2 rewardids, they need to equal each other so you can't miss out on progression.
# need to make the sidequest that require a certain number of points only require 1 point, and remove all other alternate sources, so you need that exact item.
# need to make the quest Unforgotten Promise only require 1 eternity loam, not 4, they're key items with the same id, so you can't make them a one-time reward, like from a boss drop, you need 4 in logic

class TornaSideQuest: # created to allow me to pass these objects easier
    def __init__(self, input, addtolist, rewardnumber):
        self.id = input["Quest Number"]
        self.name = input["Quest Name"]
        self.mainreq = input["Main Story Req"]
        self.sideprereq = input["Sidequest Pre-Req"]
        self.itemreqs = Helper.MultiLevelListToSingleLevelList(input["Item Requirements"])
        self.complus = input["Community Gained"]
        self.comreq = input["Community Level Req"]
        self.rewardids = input["Reward Set IDs"]
        self.randomizeditems = Helper.ExtendListtoLength(Helper.ExtendListtoLength([], rewardnumber, "-1"), 4, "0") # holds ids, -1 for progression, 0 for filler spots
        self.type = "sidequest"
        if rewardnumber > 0:
            self.hasprogression = True
        else:
            self.hasprogression = False
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
    global Quest15Optional, Quest28Optional, Quest29Optional1, Quest29Optional2, Quest30Optional, Quest34Optional1, Quest34Optional2, Quest44Optional1, Quest44Optional2, Quest47Optional, Quest55Optional
    Quest15Optional = random.choice([[30347,30352,30379],[30400,30032,30030],[30407,30438,30408,30411],[30384,30032,30352,30407,30408],[30363,30352,30353],[30252,30032,30408,30407,30030,26146],[30386,30365,30409,30407,26147]])
    Quest28Optional = random.choice([[30353],[30030],[30438],[30356]])
    Quest29Optional1 = random.choice([[30373],[30374],[30375],[30377],[30378]])
    Quest29Optional2 = random.choice([[30425],[30426],[30427],[30428],[30429],[30430]])
    Quest30Optional = random.choice([[30358],[30359],[30360],[30361],[30362],[30409],[30410],[30411],[30412],[30413]])
    Quest34Optional1 = random.choice([[30347,30352,30379],[30400,30032,30030],[30352,30353,30354],[30347,30353,30380],[30384,30032,30352,30407,30408],[30382,30383,30356,30400],[30363,30352,30353],[30400,30363,30252],[30025,30021,30354],[30364,30365,30029],[30365,30358,30355,30385,30025],[30400,30363,30364,30366,30349],[30347,30352,30360],[30380,30358,30353,30363],[30386,30028,30029,30438]])
    Quest34Optional2 = random.choice([[30348,30349,30357,30039],[30345,30354,30364],[30407,30438,30408,30411],[30033,30028,30039,30381],[30356,30357,30400,30385,30033],[30407,30029,30021,30384],[30438,30383,30027,30356,30028]])
    Quest44Optional1 = random.choice([[30363],[30364],[30039],[30366]])
    Quest44Optional2 = random.choice([[30363],[30364],[30366],[30037],[30039],[30417],[30419]])
    Quest47Optional = random.choice([[30343],[30351],[30357],[30371],[30380],[30382],[30384],[30386],[30027],[30041],[30042],[30424],[30439],[30432],[30434],[30436]])
    Quest55Optional = random.choice([[30345],[30349],[30252]])

def SelectCommunityQuests(CommunityReqs: list, QuestRewardQty): # Selects the community quests that logically unlock Story Events 38 and 50 (lv 2 and lv 4 community)
    TornaSidequest1 = {
        'Quest Name': 'What Bars the Way',
        'Quest Number': 1,
        'Main Story Req': 9,
        'Sidequest Pre-Req': [],
        'Item Requirements': [HazeKey, [ManipEtherKey[0]], [HazeAff[0]], MythraKey, [LightKey[0]] , LevelUpTokens[:11]],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1082]
    }
    TornaSidequest2 = {
        'Quest Name': 'A Simple Errand',
        'Quest Number': 2,
        'Main Story Req': 10,
        'Sidequest Pre-Req': [],
        'Item Requirements': [LevelUpTokens[:11]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1060]
    }
    TornaSidequest3 = {
        'Quest Name': 'Barmy Tale of Barney',
        'Quest Number': 3,
        'Main Story Req': 10,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[SwordplayKey[0]] , LevelUpTokens[:7]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1076]
    }
    TornaSidequest4 = {
        'Quest Name': 'Driver Coaching',
        'Quest Number': 4,
        'Main Story Req': 10,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1206]
    }
    TornaSidequest5 = {
        'Quest Name': 'A Rare Sense of Justice',
        'Quest Number': 5,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [32, 56],
        'Item Requirements': [AegaeonKey, SuperstrKey, AegaeonAff[:2], HazeKey, KeenEyeKey, HazeAff[:2]],
        'Community Gained': 2,
        'Community Level Req': 5,
        'Reward Set IDs': [1061]
    }
    TornaSidequest6 = {
        'Quest Name': 'Punpuns Rival',
        'Quest Number': 6,
        'Main Story Req': 12,
        'Sidequest Pre-Req': [],
        'Item Requirements': [LevelUpTokens[:35]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1081]
    }
    TornaSidequest7 = {
        'Quest Name': 'Doc, the Miasma Slayer',
        'Quest Number': 7,
        'Main Story Req': 12,
        'Sidequest Pre-Req': [],
        'Item Requirements': [LevelUpTokens[:13]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1080]
    }
    TornaSidequest8 = {
        'Quest Name': 'Power Unimaginable',
        'Quest Number': 8,
        'Main Story Req': 16,
        'Sidequest Pre-Req': [],
        'Item Requirements': [LevelUpTokens[:17]],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1083]
    }
    TornaSidequest9 = {
        'Quest Name': 'Blade Coaching',
        'Quest Number': 9,
        'Main Story Req': 16,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1208]
    }
    TornaSidequest10 = {
        'Quest Name': 'Further Blade Coaching',
        'Quest Number': 10,
        'Main Story Req': 16,
        'Sidequest Pre-Req': [9],
        'Item Requirements': [],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1209]
    }
    TornaSidequest11 = {
        'Quest Name': 'The Ardainian Gunman',
        'Quest Number': 11,
        'Main Story Req': 16,
        'Sidequest Pre-Req': [],
        'Item Requirements': [LevelUpTokens[:20]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1074]
    }
    TornaSidequest12 = {
        'Quest Name': 'A Taste of Home',
        'Quest Number': 12,
        'Main Story Req': 16,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[30347,30379,30252,30418,26149] , [30400,30379,30252,30418,30029,26191]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1075]
    }
    TornaSidequest13 = {
        'Quest Name': 'Salvage the Salvager',
        'Quest Number': 13,
        'Main Story Req': 16,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[30426] , [30427] , [25465] , LevelUpTokens[:21]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1063]
    }
    TornaSidequest14 = {
        'Quest Name': 'Wheres the Boy Gone',
        'Quest Number': 14,
        'Main Story Req': 20,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1084]
    }
    TornaSidequest15 = {
        'Quest Name': 'My First Adventure',
        'Quest Number': 15,
        'Main Story Req': 20,
        'Sidequest Pre-Req': [],
        'Item Requirements': [Quest15Optional],
        'Community Gained': 2,
        'Community Level Req': 0,
        'Reward Set IDs': [1064]
    }
    TornaSidequest16 = {
        'Quest Name': 'Seeking a Seeker',
        'Quest Number': 16,
        'Main Story Req': 20,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[30019,30411,30041,30360,30444] , [30425] , [30428]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1079]
    }
    TornaSidequest17 = {
        'Quest Name': 'Feeding an Army',
        'Quest Number': 17,
        'Main Story Req': 25,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[30380] , [30438] , [30347]],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1085]
    }
    TornaSidequest18 = {
        'Quest Name': 'Further Driver Coaching',
        'Quest Number': 18,
        'Main Story Req': 25,
        'Sidequest Pre-Req': [4],
        'Item Requirements': [],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1207]
    }
    TornaSidequest19 = {
        'Quest Name': 'Fusion Coaching',
        'Quest Number': 19,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [10,18],
        'Item Requirements': [],
        'Community Gained': 2,
        'Community Level Req': 2,
        'Reward Set IDs': [1210]
    }
    TornaSidequest20 = {
        'Quest Name': 'What Matters Most',
        'Quest Number': 20,
        'Main Story Req': 25,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[25460] , [25461] , LevelUpTokens[:36]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1054]
    }
    TornaSidequest21 = {
        'Quest Name': 'The Malcontent Doctor',
        'Quest Number': 21,
        'Main Story Req': 26,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[25457]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1053]
    }
    TornaSidequest22 = {
        'Quest Name': 'Lett Bridge Restoration',
        'Quest Number': 22,
        'Main Story Req': 26,
        'Sidequest Pre-Req': [],
        'Item Requirements': [LevelUpTokens[:25]],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1086]
    }
    TornaSidequest23 = {
        'Quest Name': 'Thicker Than Water',
        'Quest Number': 23,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [],
        'Item Requirements': [HazeKey, KeenEyeKey[:1], [HazeAff[0]], MythraKey, FocusKey, MythraAff[:2]],
        'Community Gained': 3,
        'Community Level Req': 2,
        'Reward Set IDs': [1052]
    }
    TornaSidequest24 = {
        'Quest Name': 'The Travails of War',
        'Quest Number': 24,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [LevelUpTokens[:42]],
        'Community Gained': 2,
        'Community Level Req': 4,
        'Reward Set IDs': [1057]
    }
    TornaSidequest25 = {
        'Quest Name': 'To Cross a Desert',
        'Quest Number': 25,
        'Main Story Req': 32,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[30355] , [30383]],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1087]
    }
    TornaSidequest26 = {
        'Quest Name': 'For Lack of a Hunter',
        'Quest Number': 26,
        'Main Story Req': 35,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[30380]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1078]
    }
    TornaSidequest27 = {
        'Quest Name': 'Here Be Treasure',
        'Quest Number': 27,
        'Main Story Req': 35,
        'Sidequest Pre-Req': [],
        'Item Requirements': [MinothKey, [MiningKey[0]], [FortitudeKey[0]]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1077]
    }
    TornaSidequest28 = {
        'Quest Name': 'The Secret of Dannagh',
        'Quest Number': 28,
        'Main Story Req': 35,
        'Sidequest Pre-Req': [13],
        'Item Requirements': [[30428,30375,30020,30433,30428,30375,30020,30433] , [30428] , [30375] , [30020] , [30433] , Quest28Optional],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1058, 1059]
    }
    TornaSidequest29 = {
        'Quest Name': 'The Tornan Inventor',
        'Quest Number': 29,
        'Main Story Req': 36,
        'Sidequest Pre-Req': [],
        'Item Requirements': [Quest29Optional1 , Quest29Optional2],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1068]
    }
    TornaSidequest30 = {
        'Quest Name': 'Nuts about Bugs',
        'Quest Number': 30,
        'Main Story Req': 36,
        'Sidequest Pre-Req': [],
        'Item Requirements': [Quest30Optional],
        'Community Gained': 0,
        'Community Level Req': 0,
        'Reward Set IDs': [1066]
    }
    TornaSidequest31 = {
        'Quest Name': 'Lighting the Way',
        'Quest Number': 31,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1034]
    }
    TornaSidequest32 = {
        'Quest Name': 'An Oasis for All',
        'Quest Number': 32,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [],
        'Item Requirements': [LevelUpTokens[:36]],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1035]
    }
    TornaSidequest33 = {
        'Quest Name': 'Armus Gone Astray',
        'Quest Number': 33,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [],
        'Item Requirements': [HazeKey, [KeenEyeKey[0]], MythraKey, [FocusKey[0]] , LevelUpTokens[:32]],
        'Community Gained': 2,
        'Community Level Req': 0,
        'Reward Set IDs': [1032]
    }
    TornaSidequest34 = {
        'Quest Name': 'Hungry for More',
        'Quest Number': 34,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [],
        'Item Requirements': [Quest34Optional1 , Quest34Optional2],
        'Community Gained': 1,
        'Community Level Req': 0,
        'Reward Set IDs': [1071]
    }
    TornaSidequest35 = {
        'Quest Name': 'Bolstering Sales',
        'Quest Number': 35,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[30340] , [30348] , [30268] , [30341] , [30024] , [30423]],
        'Community Gained': 2,
        'Community Level Req': 0,
        'Reward Set IDs': [1033]
    }
    TornaSidequest36 = {
        'Quest Name': 'Helping the Helper',
        'Quest Number': 36,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[25458,30342,30368,30429,26164] , [25458]],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': [1036]
    }
    TornaSidequest37 = {
        'Quest Name': 'Homegrown Inventor',
        'Quest Number': 37,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [30],
        'Item Requirements': [[SwordplayKey[0]] , [30374] , [30378] , [25462] , LevelUpTokens[:40]],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': [1037]
    }
    TornaSidequest38 = {
        'Quest Name': 'Duplicity',
        'Quest Number': 38,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [],
        'Item Requirements': [LevelUpTokens[:41]],
        'Community Gained': 2,
        'Community Level Req': 2,
        'Reward Set IDs': [1055]
    }
    TornaSidequest39 = {
        'Quest Name': 'Sweetest Tidings',
        'Quest Number': 39,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [],
        'Item Requirements': [LevelUpTokens[:42]],
        'Community Gained': 2,
        'Community Level Req': 2,
        'Reward Set IDs': [1062]
    }
    TornaSidequest40 = {
        'Quest Name': 'Passing the Torch',
        'Quest Number': 40,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [MinothKey, MiningKey[:1], MinothAff[:1], FortitudeKey[:1], JinAff[:1] , 25455 , LevelUpTokens[:38]],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': [1043]
    }
    TornaSidequest41 = {
        'Quest Name': 'Trail of Destruction',
        'Quest Number': 41,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [2],
        'Item Requirements': [AegaeonKey, SuperstrKey[:1], AegaeonAff[:1], MythraKey, FocusKey[:1], [MythraAff[0]] , LevelUpTokens[:44]],
        'Community Gained': 2,
        'Community Level Req': 2,
        'Reward Set IDs': [1038]
    }
    TornaSidequest42 = {
        'Quest Name': 'Forest Trail Antics',
        'Quest Number': 42,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': [1039]
    }
    TornaSidequest43 = {
        'Quest Name': 'Making Up the Numbers',
        'Quest Number': 43,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [3, 41, 42],
        'Item Requirements': [],
        'Community Gained': 3,
        'Community Level Req': 2,
        'Reward Set IDs': [1056]
    }
    TornaSidequest44 = {
        'Quest Name': 'The Fish That Could Be',
        'Quest Number': 44,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [],
        'Item Requirements': [Quest44Optional1 , Quest44Optional2],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': [1067]
    }
    TornaSidequest45 = {
        'Quest Name': 'Hubbie Takes a Hike',
        'Quest Number': 45,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [44],
        'Item Requirements': [],
        'Community Gained': 2,
        'Community Level Req': 3,
        'Reward Set IDs': [1073]
    }
    TornaSidequest46 = {
        'Quest Name': 'Manning the Gates',
        'Quest Number': 46,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [31, 32],
        'Item Requirements': [MythraKey, FocusKey[:1], [MythraAff[0]], HazeKey, KeenEyeKey[:1], [HazeAff[0]] , LevelUpTokens[:40]],
        'Community Gained': 2,
        'Community Level Req': 3,
        'Reward Set IDs': [1040]
    }
    TornaSidequest47 = {
        'Quest Name': '100k in the Red',
        'Quest Number': 47,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [],
        'Item Requirements': [Quest47Optional],
        'Community Gained': 1,
        'Community Level Req': 3,
        'Reward Set IDs': [1072]
    }
    TornaSidequest48 = {
        'Quest Name': 'Proof of Love',
        'Quest Number': 48,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [36],
        'Item Requirements': [],
        'Community Gained': 2,
        'Community Level Req': 3,
        'Reward Set IDs': [1044]
    }
    TornaSidequest49 = {
        'Quest Name': 'Planning for the Future',
        'Quest Number': 49,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [[30020] , [25464] , LevelUpTokens[:43]],
        'Community Gained': 3,
        'Community Level Req': 3,
        'Reward Set IDs': [1042]
    }
    TornaSidequest50 = {
        'Quest Name': 'The Bard Factor',
        'Quest Number': 50,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [48],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 4,
        'Reward Set IDs': [1069]
    }
    TornaSidequest51 = {
        'Quest Name': 'Azurda SOS',
        'Quest Number': 51,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [47, 48],
        'Item Requirements': [LevelUpTokens[:51]],
        'Community Gained': 2,
        'Community Level Req': 4,
        'Reward Set IDs': [1065]
    }
    TornaSidequest52 = {
        'Quest Name': 'Great Tornan Cook-Off',
        'Quest Number': 52,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [34],
        'Item Requirements': [[30382,30384,30347,30383,30408,26148] , [30033,30400,30347,30027,30438,26150]],
        'Community Gained': 2,
        'Community Level Req': 4,
        'Reward Set IDs': [1047, 1048]
    }
    TornaSidequest53 = {
        'Quest Name': 'Safety Measures',
        'Quest Number': 53,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [15, 43, 49],
        'Item Requirements': [[30020] , [30372] , [30019] , [30266] , [30427]],
        'Community Gained': 2,
        'Community Level Req': 3,
        'Reward Set IDs': [1041]
    }
    TornaSidequest54 = {
        'Quest Name': 'Further Feeding Issues',
        'Quest Number': 54,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [AegaeonKey, ComWaterKey[:1], AegaeonAff[:1] , [25463,30413,30423,30359,26182] , LevelUpTokens[:39]],
        'Community Gained': 1,
        'Community Level Req': 4,
        'Reward Set IDs': [1045]
    }
    TornaSidequest55 = {
        'Quest Name': 'Unforgotten Promise',
        'Quest Number': 55,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [MythraKey, FocusKey, MythraAff[:2], HazeKey, KeenEyeKey, HazeAff[:2] , [30344] , [30370] , [25536] , Quest55Optional],
        'Community Gained': 2,
        'Community Level Req': 4,
        'Reward Set IDs': [1046]
    }
    TornaSidequest56 = {
        'Quest Name': 'What Goes Around',
        'Quest Number': 56,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [36, 38, 43],
        'Item Requirements': [],
        'Community Gained': 2,
        'Community Level Req': 5,
        'Reward Set IDs': [1049]
    }
    TornaSidequest57 = {
        'Quest Name': 'Community Spirit',
        'Quest Number': 57,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [5, 15, 42, 37, 49, 48, 43, 46, 24, 56],
        'Item Requirements': [],
        'Community Gained': 2,
        'Community Level Req': 5,
        'Reward Set IDs': [1051]
    }
    TornaSidequest58 = {
        'Quest Name': 'A Small Promise',
        'Quest Number': 58,
        'Main Story Req': 52,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 2,
        'Community Level Req': 5,
        'Reward Set IDs': [1050]
    }
    TornaSidequest59 = {
        'Quest Name': 'Martha',
        'Quest Number': 59,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 5,
        'Reward Set IDs': []
    }
    TornaSidequest60 = {
        'Quest Name': 'Benny',
        'Quest Number': 60,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [26],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': []
    }
    TornaSidequest61 = {
        'Quest Name': 'Dolala',
        'Quest Number': 61,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': []
    }
    TornaSidequest62 = {
        'Quest Name': 'Clemens',
        'Quest Number': 62,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': []
    }
    TornaSidequest63 = {
        'Quest Name': 'Nalsaz',
        'Quest Number': 63,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': []
    }
    TornaSidequest64 = {
        'Quest Name': 'Yrissa',
        'Quest Number': 64,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [42],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 2,
        'Reward Set IDs': []
    }
    TornaSidequest65 = {
        'Quest Name': 'Clarke',
        'Quest Number': 65,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [54],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 4,
        'Reward Set IDs': []
    }
    TornaSidequest66 = {
        'Quest Name': 'Augustus',
        'Quest Number': 66,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [54],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 4,
        'Reward Set IDs': []
    }
    TornaSidequest67 = {
        'Quest Name': 'Lavinia',
        'Quest Number': 67,
        'Main Story Req': 37,
        'Sidequest Pre-Req': [23],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 4,
        'Reward Set IDs': []
    }
    TornaSidequest68 = {
        'Quest Name': 'Mini',
        'Quest Number': 68,
        'Main Story Req': 46,
        'Sidequest Pre-Req': [53],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 3,
        'Reward Set IDs': []
    }
    TornaSidequest69 = {
        'Quest Name': 'Tranc',
        'Quest Number': 69,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [5],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 5,
        'Reward Set IDs': []
    }
    TornaSidequest70 = {
        'Quest Name': 'Vill Ethelmar',
        'Quest Number': 70,
        'Main Story Req': 49,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 5,
        'Reward Set IDs': []
    }
    TornaSidequest71 = {
        'Quest Name': 'Gedd',
        'Quest Number': 71,
        'Main Story Req': 52,
        'Sidequest Pre-Req': [29],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 5,
        'Reward Set IDs': []
    }
    TornaSidequest72 = {
        'Quest Name': 'Piper',
        'Quest Number': 72,
        'Main Story Req': 52,
        'Sidequest Pre-Req': [5],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 5,
        'Reward Set IDs': []
    }
    TornaSidequest73 = {
        'Quest Name': 'Mauna',
        'Quest Number': 73,
        'Main Story Req': 52,
        'Sidequest Pre-Req': [5],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 5,
        'Reward Set IDs': []
    }
    TornaSidequest74 = {
        'Quest Name': 'Elba',
        'Quest Number': 74,
        'Main Story Req': 52,
        'Sidequest Pre-Req': [],
        'Item Requirements': [],
        'Community Gained': 1,
        'Community Level Req': 5,
        'Reward Set IDs': []
    }

    TornaSidequestDict = [TornaSidequest1, TornaSidequest2, TornaSidequest3, TornaSidequest4, TornaSidequest5, TornaSidequest6, TornaSidequest7, TornaSidequest8, TornaSidequest9, TornaSidequest10, TornaSidequest11, TornaSidequest12, TornaSidequest13, TornaSidequest14, TornaSidequest15, TornaSidequest16, TornaSidequest17, TornaSidequest18, TornaSidequest19, TornaSidequest20, TornaSidequest21, TornaSidequest22, TornaSidequest23, TornaSidequest24, TornaSidequest25, TornaSidequest26, TornaSidequest27, TornaSidequest28, TornaSidequest29, TornaSidequest30, TornaSidequest31, TornaSidequest32, TornaSidequest33, TornaSidequest34, TornaSidequest35, TornaSidequest36, TornaSidequest37, TornaSidequest38, TornaSidequest39, TornaSidequest40, TornaSidequest41, TornaSidequest42, TornaSidequest43, TornaSidequest44, TornaSidequest45, TornaSidequest46, TornaSidequest47, TornaSidequest48, TornaSidequest49, TornaSidequest50, TornaSidequest51, TornaSidequest52, TornaSidequest53, TornaSidequest54, TornaSidequest55, TornaSidequest56, TornaSidequest57, TornaSidequest58, TornaSidequest59, TornaSidequest60, TornaSidequest61, TornaSidequest62, TornaSidequest63, TornaSidequest64, TornaSidequest65, TornaSidequest66, TornaSidequest67, TornaSidequest68, TornaSidequest69, TornaSidequest70, TornaSidequest71, TornaSidequest72, TornaSidequest73, TornaSidequest74]
    global TornaSidequests
    TornaSidequests = [] # holds the TornaSideQuest class objects

    for sidequest in TornaSidequestDict:
        TornaSideQuest(sidequest, TornaSidequests, QuestRewardQty)

    TornaMainQuest1 = {
        'FLD_QuestTask $id': 1,
        'Task Summary': 'Defeat Tutorial Fight',
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
        'Task Summary': 'Defeat Gargoyle in Crater',
        'Community Level Req': 0,
        'Item Requirements': [LevelUpTokens[:12]]
    }
    TornaMainQuest8 = {
        'FLD_QuestTask $id': 5,
        'Task Summary': 'Defeat Addam and Mythra',
        'Community Level Req': 0,
        'Item Requirements': [AddamKey, MythraKey, HazeKey, LevelUpTokens[:14]]
    }
    TornaMainQuest9 = {
        'FLD_QuestTask $id': 6,
        'Task Summary': 'Reach Yanchik Harbor',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest10 = {
        'FLD_QuestTask $id': 7,
        'Task Summary': 'Complete What Bars the Way',
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
        'Task Summary': 'Go to Torigoth graves',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest16 = {
        'FLD_QuestTask $id': 12,
        'Task Summary': 'Defeat Brighid',
        'Community Level Req': 0,
        'Item Requirements': [HugoKey, BrighidKey, AegaeonKey, LevelUpTokens[:18]]
    }
    TornaMainQuest17 = {
        'FLD_QuestTask $id': 13,
        'Task Summary': 'Complete Power Unimaginable',
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
        'Item Requirements': [LevelUpTokens[:24]]
    }
    TornaMainQuest20 = {
        'FLD_QuestTask $id': 16,
        'Task Summary': 'Head for Lascham Cove',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest21 = {
        'FLD_QuestTask $id': 17,
        'Task Summary': 'Compete Wheres the Boy Gone?',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest22 = {
        'FLD_QuestTask $id': 18,
        'Task Summary': 'Head to Strategy Room',
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
        'Task Summary': 'Reach Militia Garrison',
        'Community Level Req': 0,
        'Item Requirements': []
    }
    TornaMainQuest26 = {
        'FLD_QuestTask $id': 22,
        'Task Summary': 'Complete Feeding an Army',
        'Community Level Req': 0,
        'Item Requirements': [[30380], [30438], [30347], [30365]]
    }
    TornaMainQuest27 = {
        'FLD_QuestTask $id': 23,
        'Task Summary': 'Complete Lett Bridge Restoration',
        'Community Level Req': 0,
        'Item Requirements': [LevelUpTokens[:25]]
    }
    TornaMainQuest28 = {
        'FLD_QuestTask $id': 57,
        'Task Summary': 'Return to Alettas Military Garrison',
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
        'Item Requirements': [LevelUpTokens[:33]]
    }
    TornaMainQuest31 = {
        'FLD_QuestTask $id': 26,
        'Task Summary': 'Defeat Slithe Jagron Pt. 2',
        'Community Level Req': 0,
        'Item Requirements': [MinothKey]
    }
    TornaMainQuest32 = {
        'FLD_QuestTask $id': 27,
        'Task Summary': 'Rest at Campsite',
        'Community Level Req': 0,
        'Item Requirements': [OTC_Key]
    }
    TornaMainQuest33 = {
        'FLD_QuestTask $id': 28,
        'Task Summary': 'Complete To Cross a Desert',
        'Community Level Req': 0,
        'Item Requirements': [[30355] , [30383]]
    }
    TornaMainQuest34 = {
        'FLD_QuestTask $id': 29,
        'Task Summary': 'Head past Olnards Trail',
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
        'Task Summary': 'Raise Community to Level 2',
        'Community Level Req': 2,
        'Item Requirements': []
    }
    TornaMainQuest39 = {
        'FLD_QuestTask $id': 34,
        'Task Summary': 'Head to Sachsum Gardens',
        'Community Level Req': 2,
        'Item Requirements': []
    }
    TornaMainQuest40 = {
        'FLD_QuestTask $id': 35,
        'Task Summary': 'Defeat Gargoyles Pt 1',
        'Community Level Req': 2,
        'Item Requirements': [LevelUpTokens[:36]]
    }
    TornaMainQuest41 = {
        'FLD_QuestTask $id': 52,
        'Task Summary': 'Defeat Gargoyles Pt 2',
        'Community Level Req': 2,
        'Item Requirements': []
    }
    TornaMainQuest42 = {
        'FLD_QuestTask $id': 53,
        'Task Summary': 'Defeat Gargoyles Pt 3',
        'Community Level Req': 2,
        'Item Requirements': []
    }
    TornaMainQuest43 = {
        'FLD_QuestTask $id': 36,
        'Task Summary': 'Return to Sachsum Gardens',
        'Community Level Req': 2,
        'Item Requirements': []
    }
    TornaMainQuest44 = {
        'FLD_QuestTask $id': 37,
        'Task Summary': 'Defeat Malos',
        'Community Level Req': 2,
        'Item Requirements': [LevelUpTokens[:44]]
    }
    TornaMainQuest45 = {
        'FLD_QuestTask $id': 38,
        'Task Summary': 'Defeat Gargoyles Pt 4',
        'Community Level Req': 2,
        'Item Requirements': []
    }
    TornaMainQuest46 = {
        'FLD_QuestTask $id': 39,
        'Task Summary': 'Speak with Palace Guard Clemens',
        'Community Level Req': 2,
        'Item Requirements': []
    }
    TornaMainQuest47 = {
        'FLD_QuestTask $id': 40,
        'Task Summary': 'Head to Tornas Womb',
        'Community Level Req': 2,
        'Item Requirements': []
    }
    TornaMainQuest48 = {
        'FLD_QuestTask $id': 56,
        'Task Summary': 'Head to Tornas Womb Pt 2',
        'Community Level Req': 2,
        'Item Requirements': []
    }
    TornaMainQuest49 = {
        'FLD_QuestTask $id': 41,
        'Task Summary': 'Head to Spefan Inn',
        'Community Level Req': 2,
        'Item Requirements': []
    }
    TornaMainQuest50 = {
        'FLD_QuestTask $id': 42,
        'Task Summary': 'Raise Community to Level 4',
        'Community Level Req': 4,
        'Item Requirements': []
    }
    TornaMainQuest51 = {
        'FLD_QuestTask $id': 54,
        'Task Summary': 'Return to Main Auresco Gate',
        'Community Level Req': 4,
        'Item Requirements': []
    }
    TornaMainQuest52 = {
        'FLD_QuestTask $id': 43,
        'Task Summary': 'Return to Spefan Inn',
        'Community Level Req': 4,
        'Item Requirements': []
    }
    TornaMainQuest53 = {
        'FLD_QuestTask $id': 44,
        'Task Summary': 'Cross Dannagh Desert',
        'Community Level Req': 4,
        'Item Requirements': []
    }
    TornaMainQuest54 = {
        'FLD_QuestTask $id': 45,
        'Task Summary': 'Reach Malos',
        'Community Level Req': 4,
        'Item Requirements': []
    }
    TornaMainQuest55 = {
        'FLD_QuestTask $id': 46,
        'Task Summary': 'Defeat Malos Pt 1',
        'Community Level Req': 4,
        'Item Requirements': [LevelUpTokens[:54]]
    }
    TornaMainQuest56 = {
        'FLD_QuestTask $id': 47,
        'Task Summary': 'Defeat Malos Pt 2',
        'Community Level Req': 4,
        'Item Requirements': []
    }
    TornaMainQuest57 = {
        'FLD_QuestTask $id': 48,
        'Task Summary': 'Defeat Gort',
        'Community Level Req': 4,
        'Item Requirements': [LevelUpTokens[:57]]
    }

    global TornaMainquests # holds the TornaMainQuest class objects
    TornaMainquests = []
    TornaMainQuestDict = [TornaMainQuest1, TornaMainQuest2, TornaMainQuest3, TornaMainQuest4, TornaMainQuest5, TornaMainQuest6, TornaMainQuest7, TornaMainQuest8, TornaMainQuest9, TornaMainQuest10, TornaMainQuest11, TornaMainQuest12, TornaMainQuest13, TornaMainQuest14, TornaMainQuest15, TornaMainQuest16, TornaMainQuest17, TornaMainQuest18, TornaMainQuest19, TornaMainQuest20, TornaMainQuest21, TornaMainQuest22, TornaMainQuest23, TornaMainQuest24, TornaMainQuest25, TornaMainQuest26, TornaMainQuest27, TornaMainQuest28, TornaMainQuest29, TornaMainQuest30, TornaMainQuest31, TornaMainQuest32, TornaMainQuest33, TornaMainQuest34, TornaMainQuest35, TornaMainQuest36, TornaMainQuest37, TornaMainQuest38, TornaMainQuest39, TornaMainQuest40, TornaMainQuest41, TornaMainQuest42, TornaMainQuest43, TornaMainQuest44, TornaMainQuest45, TornaMainQuest46, TornaMainQuest47, TornaMainQuest48, TornaMainQuest49, TornaMainQuest50, TornaMainQuest51, TornaMainQuest52, TornaMainQuest53, TornaMainQuest54, TornaMainQuest55, TornaMainQuest56, TornaMainQuest57]

    for mainquest in TornaMainQuestDict:
        TornaMainQuest(mainquest, TornaMainquests)

    Community2Quests, Community4Quests = [], []

    for sidequest in TornaSidequests:
        if sidequest.mainreq < 38 and sidequest.comreq < 2:
            Community2Quests.append(sidequest)
        if sidequest.mainreq < 50 and sidequest.comreq < 4:
            Community4Quests.append(sidequest)

    ChosenLevel2Quests, ChosenLevel4Quests = [], []
    AlteredLevel2Quests, AlteredLevel4Quests = Community2Quests.copy(), Community4Quests.copy()
    ChosenPeopleGained = 0
    TotalLevel2QuestRequirements, TotalLevel4QuestRequirements = [], []

    while ChosenPeopleGained < CommunityReqs[1]:
        CurrentQuest = random.choice(AlteredLevel2Quests)
        ChosenLevel2Quests.append(CurrentQuest)
        ChosenLevel4Quests.append(CurrentQuest)
        ChosenPeopleGained += CurrentQuest.complus
        AlteredLevel2Quests.remove(CurrentQuest)
        AlteredLevel4Quests.remove(CurrentQuest)
        if CurrentQuest.sideprereq != []:
            for i in range(10): # should be enough to get dependency chains
                for quest in ChosenLevel2Quests:
                    if quest.sideprereq != []:
                        for prereq in quest.sideprereq:
                            if TornaSidequests[prereq - 1] not in ChosenLevel2Quests:
                                ChosenLevel2Quests.append(TornaSidequests[prereq - 1])
                                ChosenLevel4Quests.append(TornaSidequests[prereq - 1])
                                ChosenPeopleGained += TornaSidequests[prereq - 1].complus
                                AlteredLevel2Quests.remove(TornaSidequests[prereq - 1])
                                AlteredLevel4Quests.remove(TornaSidequests[prereq - 1])

    while ChosenPeopleGained < CommunityReqs[3]:
        CurrentQuest = random.choice(AlteredLevel4Quests)
        ChosenLevel4Quests.append(CurrentQuest)
        ChosenPeopleGained += CurrentQuest.complus
        AlteredLevel4Quests.remove(CurrentQuest)
        if CurrentQuest.sideprereq != []:
            for i in range(10): # should be enough to get dependency chains
                for quest in ChosenLevel4Quests:
                    if quest.sideprereq != []:
                        for prereq in quest.sideprereq:
                            if TornaSidequests[prereq - 1] not in ChosenLevel4Quests:
                                ChosenLevel4Quests.append(TornaSidequests[prereq - 1])
                                ChosenPeopleGained += TornaSidequests[prereq - 1].complus
                                AlteredLevel4Quests.remove(TornaSidequests[prereq - 1])
    
    for quest in ChosenLevel2Quests:
        TotalLevel2QuestRequirements.extend(quest.itemreqs)
    for quest in ChosenLevel4Quests:
        TotalLevel4QuestRequirements.extend(quest.itemreqs)
    TotalLevel2QuestRequirements = Helper.MultiLevelListToSingleLevelList(TotalLevel2QuestRequirements)
    TotalLevel4QuestRequirements = Helper.MultiLevelListToSingleLevelList(TotalLevel4QuestRequirements)
    TotalLevel2QuestRequirements = list(set(TotalLevel2QuestRequirements))
    TotalLevel4QuestRequirements = list(set(TotalLevel4QuestRequirements))
    TotalLevel2QuestRequirements.sort()
    TotalLevel4QuestRequirements.sort()

    StackStoryRequirements(TotalLevel2QuestRequirements, TotalLevel4QuestRequirements)

    return ChosenLevel2Quests, ChosenLevel4Quests, TornaSidequests, TornaMainquests

def StackStoryRequirements(Level2QuestReqs, Level4QuestReqs): # This adds the previous story requirements to the current story step's requirements. I wanted to keep the original requirements clear in case someone makes a tracker from the dictionary above
    for storystep in range(1, len(TornaMainquests)):
        TornaMainquests[storystep].itemreqs.extend(TornaMainquests[storystep - 1].itemreqs) # adds the previous step's requirements
        TornaMainquests[storystep].itemreqs = Helper.MultiLevelListToSingleLevelList(TornaMainquests[storystep].itemreqs) # turns nested lists into one list
        if TornaMainquests[storystep].id == 33:
            TornaMainquests[storystep].itemreqs.extend(Level2QuestReqs)
        elif TornaMainquests[storystep].comreq == 42:
            TornaMainquests[storystep].itemreqs.extend(Level4QuestReqs)
        TornaMainquests[storystep].itemreqs = list(set(TornaMainquests[storystep].itemreqs))
        TornaMainquests[storystep].itemreqs.sort()