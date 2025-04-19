from scripts import Helper, JSONParser, PopupDescriptions
import json
import random
import time
from IDs import *

Quest15Optional = []
Quest28Optional = []
Quest29Optional1 = []
Quest29Optional2 = []
Quest30Optional = []
Quest34Optional1 = []
Quest34Optional2 = []
Quest44Optional1 = []
Quest44Optional2 = []
Quest47Optional = []
Quest55Optional = []

TornaSidequest1 = {
    'Quest Name': 'What Bars the Way',
    'Quest Number': 1,
    'Main Story Req': 9,
    'Sidequest Pre-Req': [],
    'Item Requirements': [HazeKey, [ManipEtherKey[0]], [HazeAff[0]], MythraKey, [LightKey[0]] , LevelUpTokens[:11]],
    'Community Gained': 0,
    'Community Level Req': 0
}
TornaSidequest2 = {
    'Quest Name': 'A Simple Errand',
    'Quest Number': 2,
    'Main Story Req': 10,
    'Sidequest Pre-Req': [],
    'Item Requirements': [LevelUpTokens[:11]],
    'Community Gained': 1,
    'Community Level Req': 0
}
TornaSidequest3 = {
    'Quest Name': 'Barmy Tale of Barney',
    'Quest Number': 3,
    'Main Story Req': 10,
    'Sidequest Pre-Req': [],
    'Item Requirements': [[SwordplayKey[0]] , LevelUpTokens[:7]],
    'Community Gained': 1,
    'Community Level Req': 0
}
TornaSidequest4 = {
    'Quest Name': 'Driver Coaching',
    'Quest Number': 4,
    'Main Story Req': 10,
    'Sidequest Pre-Req': [],
    'Item Requirements': [],
    'Community Gained': 0,
    'Community Level Req': 0
}
TornaSidequest5 = {
    'Quest Name': 'A Rare Sense of Justice',
    'Quest Number': 5,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [32, 56],
    'Item Requirements': [AegaeonKey, SuperstrKey, AegaeonAff[:2], HazeKey, KeenEyeKey, HazeAff[:2]],
    'Community Gained': 2,
    'Community Level Req': 5
}
TornaSidequest6 = {
    'Quest Name': 'Punpuns Rival',
    'Quest Number': 6,
    'Main Story Req': 12,
    'Sidequest Pre-Req': [],
    'Item Requirements': [LevelUpTokens[:35]],
    'Community Gained': 1,
    'Community Level Req': 0
}
TornaSidequest7 = {
    'Quest Name': 'Doc, the Miasma Slayer',
    'Quest Number': 7,
    'Main Story Req': 12,
    'Sidequest Pre-Req': [],
    'Item Requirements': [LevelUpTokens[:13]],
    'Community Gained': 1,
    'Community Level Req': 0
}
TornaSidequest8 = {
    'Quest Name': 'Power Unimaginable',
    'Quest Number': 8,
    'Main Story Req': 16,
    'Sidequest Pre-Req': [],
    'Item Requirements': [LevelUpTokens[:17]],
    'Community Gained': 0,
    'Community Level Req': 0
}
TornaSidequest9 = {
    'Quest Name': 'Blade Coaching',
    'Quest Number': 9,
    'Main Story Req': 16,
    'Sidequest Pre-Req': [],
    'Item Requirements': [],
    'Community Gained': 0,
    'Community Level Req': 0
}
TornaSidequest10 = {
    'Quest Name': 'Further Blade Coaching',
    'Quest Number': 10,
    'Main Story Req': 16,
    'Sidequest Pre-Req': [9],
    'Item Requirements': [],
    'Community Gained': 0,
    'Community Level Req': 0
}
TornaSidequest11 = {
    'Quest Name': 'The Ardainian Gunman',
    'Quest Number': 11,
    'Main Story Req': 16,
    'Sidequest Pre-Req': [],
    'Item Requirements': [LevelUpTokens[:20]],
    'Community Gained': 1,
    'Community Level Req': 0
}
TornaSidequest12 = {
    'Quest Name': 'A Taste of Home',
    'Quest Number': 12,
    'Main Story Req': 16,
    'Sidequest Pre-Req': [],
    'Item Requirements': [[30347,30379,30252,30418,26149] , [30400,30379,30252,30418,30029,26191]],
    'Community Gained': 1,
    'Community Level Req': 0
}
TornaSidequest13 = {
    'Quest Name': 'Salvage the Salvager',
    'Quest Number': 13,
    'Main Story Req': 16,
    'Sidequest Pre-Req': [],
    'Item Requirements': [[30426] , [30427] , [25465] , LevelUpTokens[:21]],
    'Community Gained': 1,
    'Community Level Req': 0
}
TornaSidequest14 = {
    'Quest Name': 'Wheres the Boy Gone',
    'Quest Number': 14,
    'Main Story Req': 20,
    'Sidequest Pre-Req': [],
    'Item Requirements': [],
    'Community Gained': 0,
    'Community Level Req': 0
}
TornaSidequest15 = {
    'Quest Name': 'My First Adventure',
    'Quest Number': 15,
    'Main Story Req': 20,
    'Sidequest Pre-Req': [],
    'Item Requirements': [Quest15Optional],
    'Community Gained': 2,
    'Community Level Req': 0
}
TornaSidequest16 = {
    'Quest Name': 'Seeking a Seeker',
    'Quest Number': 16,
    'Main Story Req': 20,
    'Sidequest Pre-Req': [],
    'Item Requirements': [[30019,30411,30041,30360,30444] , [30425] , [30428]],
    'Community Gained': 1,
    'Community Level Req': 0
}
TornaSidequest17 = {
    'Quest Name': 'Feeding an Army',
    'Quest Number': 17,
    'Main Story Req': 25,
    'Sidequest Pre-Req': [],
    'Item Requirements': [[30380] , [30438] , [30347]],
    'Community Gained': 0,
    'Community Level Req': 0
}
TornaSidequest18 = {
    'Quest Name': 'Further Driver Coaching',
    'Quest Number': 18,
    'Main Story Req': 25,
    'Sidequest Pre-Req': [4],
    'Item Requirements': [],
    'Community Gained': 0,
    'Community Level Req': 0
}
TornaSidequest19 = {
    'Quest Name': 'Fusion Coaching',
    'Quest Number': 19,
    'Main Story Req': 37,
    'Sidequest Pre-Req': [10,18],
    'Item Requirements': [],
    'Community Gained': 2,
    'Community Level Req': 2
}
TornaSidequest20 = {
    'Quest Name': 'What Matters Most',
    'Quest Number': 20,
    'Main Story Req': 25,
    'Sidequest Pre-Req': [],
    'Item Requirements': [[25460] , [25461] , LevelUpTokens[:36]],
    'Community Gained': 1,
    'Community Level Req': 0
}
TornaSidequest21 = {
    'Quest Name': 'The Malcontent Doctor',
    'Quest Number': 21,
    'Main Story Req': 26,
    'Sidequest Pre-Req': [],
    'Item Requirements': [[25457]],
    'Community Gained': 1,
    'Community Level Req': 0
}
TornaSidequest22 = {
    'Quest Name': 'Lett Bridge Restoration',
    'Quest Number': 22,
    'Main Story Req': 26,
    'Sidequest Pre-Req': [],
    'Item Requirements': [LevelUpTokens[:25]],
    'Community Gained': 0,
    'Community Level Req': 0
}
TornaSidequest23 = {
    'Quest Name': 'Thicker Than Water',
    'Quest Number': 23,
    'Main Story Req': 37,
    'Sidequest Pre-Req': [],
    'Item Requirements': [HazeKey, KeenEyeKey[:1], [HazeAff[0]], MythraKey, FocusKey, MythraAff[:2]],
    'Community Gained': 3,
    'Community Level Req': 2
}
TornaSidequest24 = {
    'Quest Name': 'The Travails of War',
    'Quest Number': 24,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [],
    'Item Requirements': [LevelUpTokens[:42]],
    'Community Gained': 2,
    'Community Level Req': 4
}
TornaSidequest25 = {
    'Quest Name': 'To Cross a Desert',
    'Quest Number': 25,
    'Main Story Req': 32,
    'Sidequest Pre-Req': [],
    'Item Requirements': [[30355] , [30383]],
    'Community Gained': 0,
    'Community Level Req': 0
}
TornaSidequest26 = {
    'Quest Name': 'For Lack of a Hunter',
    'Quest Number': 26,
    'Main Story Req': 35,
    'Sidequest Pre-Req': [],
    'Item Requirements': [[30380]],
    'Community Gained': 1,
    'Community Level Req': 0
}
TornaSidequest27 = {
    'Quest Name': 'Here Be Treasure',
    'Quest Number': 27,
    'Main Story Req': 35,
    'Sidequest Pre-Req': [],
    'Item Requirements': [MinothKey, [MiningKey[0]], [FortitudeKey[0]]],
    'Community Gained': 1,
    'Community Level Req': 0
}
TornaSidequest28 = {
    'Quest Name': 'The Secret of Dannagh',
    'Quest Number': 28,
    'Main Story Req': 35,
    'Sidequest Pre-Req': [13],
    'Item Requirements': [[30428,30375,30020,30433,26178] , [30428] , [30375] , [30020] , [30433] , Quest28Optional],
    'Community Gained': 1,
    'Community Level Req': 0
}
TornaSidequest29 = {
    'Quest Name': 'The Tornan Inventor',
    'Quest Number': 29,
    'Main Story Req': 36,
    'Sidequest Pre-Req': [],
    'Item Requirements': [Quest29Optional1 , Quest29Optional2],
    'Community Gained': 1,
    'Community Level Req': 0
}
TornaSidequest30 = {
    'Quest Name': 'Nuts about Bugs',
    'Quest Number': 30,
    'Main Story Req': 36,
    'Sidequest Pre-Req': [],
    'Item Requirements': [Quest30Optional],
    'Community Gained': 0,
    'Community Level Req': 0
}
TornaSidequest31 = {
    'Quest Name': 'Lighting the Way',
    'Quest Number': 31,
    'Main Story Req': 37,
    'Sidequest Pre-Req': [],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 0
}
TornaSidequest32 = {
    'Quest Name': 'An Oasis for All',
    'Quest Number': 32,
    'Main Story Req': 37,
    'Sidequest Pre-Req': [],
    'Item Requirements': [LevelUpTokens[:36]],
    'Community Gained': 1,
    'Community Level Req': 0
}
TornaSidequest33 = {
    'Quest Name': 'Armus Gone Astray',
    'Quest Number': 33,
    'Main Story Req': 37,
    'Sidequest Pre-Req': [],
    'Item Requirements': [HazeKey, [KeenEyeKey[0]], MythraKey, [FocusKey[0]] , LevelUpTokens[:32]],
    'Community Gained': 2,
    'Community Level Req': 0
}
TornaSidequest34 = {
    'Quest Name': 'Hungry for More',
    'Quest Number': 34,
    'Main Story Req': 37,
    'Sidequest Pre-Req': [],
    'Item Requirements': [Quest34Optional1 , Quest34Optional2],
    'Community Gained': 1,
    'Community Level Req': 0
}
TornaSidequest35 = {
    'Quest Name': 'Bolstering Sales',
    'Quest Number': 35,
    'Main Story Req': 37,
    'Sidequest Pre-Req': [],
    'Item Requirements': [[30340] , [30348] , [30268] , [30341] , [30024] , [30423]],
    'Community Gained': 2,
    'Community Level Req': 0
}
TornaSidequest36 = {
    'Quest Name': 'Helping the Helper',
    'Quest Number': 36,
    'Main Story Req': 46,
    'Sidequest Pre-Req': [],
    'Item Requirements': [[25458,30342,30368,30429,26164] , [25458]],
    'Community Gained': 1,
    'Community Level Req': 2
}
TornaSidequest37 = {
    'Quest Name': 'Homegrown Inventor',
    'Quest Number': 37,
    'Main Story Req': 46,
    'Sidequest Pre-Req': [30],
    'Item Requirements': [[SwordplayKey[0]] , [30374] , [30378] , [25462] , LevelUpTokens[:40]],
    'Community Gained': 1,
    'Community Level Req': 2
}
TornaSidequest38 = {
    'Quest Name': 'Duplicity',
    'Quest Number': 38,
    'Main Story Req': 46,
    'Sidequest Pre-Req': [],
    'Item Requirements': [LevelUpTokens[:41]],
    'Community Gained': 2,
    'Community Level Req': 2
}
TornaSidequest39 = {
    'Quest Name': 'Sweetest Tidings',
    'Quest Number': 39,
    'Main Story Req': 46,
    'Sidequest Pre-Req': [],
    'Item Requirements': [LevelUpTokens[:42]],
    'Community Gained': 2,
    'Community Level Req': 2
}
TornaSidequest40 = {
    'Quest Name': 'Passing the Torch',
    'Quest Number': 40,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [],
    'Item Requirements': [MinothKey, MiningKey[:1], MinothAff[:1], FortitudeKey[:1], JinAff[:1] , 25455 , LevelUpTokens[:38]],
    'Community Gained': 1,
    'Community Level Req': 2
}
TornaSidequest41 = {
    'Quest Name': 'Trail of Destruction',
    'Quest Number': 41,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [2],
    'Item Requirements': [AegaeonKey, SuperstrKey[:1], AegaeonAff[:1], MythraKey, FocusKey[:1], [MythraAff[0]] , LevelUpTokens[:44]],
    'Community Gained': 2,
    'Community Level Req': 2
}
TornaSidequest42 = {
    'Quest Name': 'Forest Trail Antics',
    'Quest Number': 42,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 2
}
TornaSidequest43 = {
    'Quest Name': 'Making Up the Numbers',
    'Quest Number': 43,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [3, 41, 42],
    'Item Requirements': [],
    'Community Gained': 3,
    'Community Level Req': 2
}
TornaSidequest44 = {
    'Quest Name': 'The Fish That Could Be',
    'Quest Number': 44,
    'Main Story Req': 46,
    'Sidequest Pre-Req': [],
    'Item Requirements': [Quest44Optional1 , Quest44Optional2],
    'Community Gained': 1,
    'Community Level Req': 2
}
TornaSidequest45 = {
    'Quest Name': 'Hubbie Takes a Hike',
    'Quest Number': 45,
    'Main Story Req': 37,
    'Sidequest Pre-Req': [44],
    'Item Requirements': [],
    'Community Gained': 2,
    'Community Level Req': 3
}
TornaSidequest46 = {
    'Quest Name': 'Manning the Gates',
    'Quest Number': 46,
    'Main Story Req': 46,
    'Sidequest Pre-Req': [31, 32],
    'Item Requirements': [MythraKey, FocusKey[:1], [MythraAff[0]], HazeKey, KeenEyeKey[:1], [HazeAff[0]] , LevelUpTokens[:40]],
    'Community Gained': 2,
    'Community Level Req': 3
}
TornaSidequest47 = {
    'Quest Name': '100k in the Red',
    'Quest Number': 47,
    'Main Story Req': 46,
    'Sidequest Pre-Req': [],
    'Item Requirements': [Quest47Optional],
    'Community Gained': 1,
    'Community Level Req': 3
}
TornaSidequest48 = {
    'Quest Name': 'Proof of Love',
    'Quest Number': 48,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [36],
    'Item Requirements': [],
    'Community Gained': 2,
    'Community Level Req': 3
}
TornaSidequest49 = {
    'Quest Name': 'Planning for the Future',
    'Quest Number': 49,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [],
    'Item Requirements': [[30020] , [25464] , LevelUpTokens[:43]],
    'Community Gained': 3,
    'Community Level Req': 3
}
TornaSidequest50 = {
    'Quest Name': 'The Bard Factor',
    'Quest Number': 50,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [48],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 4
}
TornaSidequest51 = {
    'Quest Name': 'Azurda SOS',
    'Quest Number': 51,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [47, 48],
    'Item Requirements': [LevelUpTokens[:51]],
    'Community Gained': 2,
    'Community Level Req': 4
}
TornaSidequest52 = {
    'Quest Name': 'Great Tornan Cook-Off',
    'Quest Number': 52,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [34],
    'Item Requirements': [[30382,30384,30347,30383,30408,26148] , [30033,30400,30347,30027,30438,26150]],
    'Community Gained': 2,
    'Community Level Req': 4
}
TornaSidequest53 = {
    'Quest Name': 'Safety Measures',
    'Quest Number': 53,
    'Main Story Req': 46,
    'Sidequest Pre-Req': [15, 43, 49],
    'Item Requirements': [[30020] , [30372] , [30019] , [30266] , [30427]],
    'Community Gained': 2,
    'Community Level Req': 3
}
TornaSidequest54 = {
    'Quest Name': 'Further Feeding Issues',
    'Quest Number': 54,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [],
    'Item Requirements': [AegaeonKey, ComWaterKey[:1], AegaeonAff[:1] , [25463,30413,30423,30359,26182] , LevelUpTokens[:39]],
    'Community Gained': 1,
    'Community Level Req': 4
}
TornaSidequest55 = {
    'Quest Name': 'Unforgotten Promise',
    'Quest Number': 55,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [],
    'Item Requirements': [MythraKey, FocusKey, MythraAff[:2], HazeKey, KeenEyeKey, HazeAff[:2] , [30344] , [30370] , [25536] , Quest55Optional],
    'Community Gained': 2,
    'Community Level Req': 4
}
TornaSidequest56 = {
    'Quest Name': 'What Goes Around',
    'Quest Number': 56,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [36, 38, 43],
    'Item Requirements': [],
    'Community Gained': 2,
    'Community Level Req': 5
}
TornaSidequest57 = {
    'Quest Name': 'Community Spirit',
    'Quest Number': 57,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [5, 15, 42, 37, 49, 48, 43, 46, 24, 56],
    'Item Requirements': [],
    'Community Gained': 2,
    'Community Level Req': 5
}
TornaSidequest58 = {
    'Quest Name': 'A Small Promise',
    'Quest Number': 58,
    'Main Story Req': 52,
    'Sidequest Pre-Req': [],
    'Item Requirements': [],
    'Community Gained': 2,
    'Community Level Req': 5
}
TornaSidequest59 = {
    'Quest Name': 'Martha',
    'Quest Number': 59,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 5
}
TornaSidequest60 = {
    'Quest Name': 'Benny',
    'Quest Number': 60,
    'Main Story Req': 37,
    'Sidequest Pre-Req': [26],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 2
}
TornaSidequest61 = {
    'Quest Name': 'Dolala',
    'Quest Number': 61,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 2
}
TornaSidequest62 = {
    'Quest Name': 'Clemens',
    'Quest Number': 62,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 2
}
TornaSidequest63 = {
    'Quest Name': 'Nalsaz',
    'Quest Number': 63,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 2
}
TornaSidequest64 = {
    'Quest Name': 'Yrissa',
    'Quest Number': 64,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [42],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 2
}
TornaSidequest65 = {
    'Quest Name': 'Clarke',
    'Quest Number': 65,
    'Main Story Req': 46,
    'Sidequest Pre-Req': [54],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 4
}
TornaSidequest66 = {
    'Quest Name': 'Augustus',
    'Quest Number': 66,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [54],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 4
}
TornaSidequest67 = {
    'Quest Name': 'Lavinia',
    'Quest Number': 67,
    'Main Story Req': 37,
    'Sidequest Pre-Req': [23],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 2
}
TornaSidequest68 = {
    'Quest Name': 'Mini',
    'Quest Number': 68,
    'Main Story Req': 46,
    'Sidequest Pre-Req': [53],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 3
}
TornaSidequest69 = {
    'Quest Name': 'Tranc',
    'Quest Number': 69,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [5],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 5
}
TornaSidequest70 = {
    'Quest Name': 'Vill Ethelmar',
    'Quest Number': 70,
    'Main Story Req': 49,
    'Sidequest Pre-Req': [],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 5
}
TornaSidequest71 = {
    'Quest Name': 'Gedd',
    'Quest Number': 71,
    'Main Story Req': 52,
    'Sidequest Pre-Req': [29],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 5
}
TornaSidequest72 = {
    'Quest Name': 'Piper',
    'Quest Number': 72,
    'Main Story Req': 52,
    'Sidequest Pre-Req': [5],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 5
}
TornaSidequest73 = {
    'Quest Name': 'Mauna',
    'Quest Number': 73,
    'Main Story Req': 52,
    'Sidequest Pre-Req': [5],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 5
}
TornaSidequest74 = {
    'Quest Name': 'Elba',
    'Quest Number': 74,
    'Main Story Req': 52,
    'Sidequest Pre-Req': [],
    'Item Requirements': [],
    'Community Gained': 1,
    'Community Level Req': 5
}

AllTornaSidequests = [TornaSidequest1, TornaSidequest2, TornaSidequest3, TornaSidequest4, TornaSidequest5, TornaSidequest6, TornaSidequest7, TornaSidequest8, TornaSidequest9, TornaSidequest10, TornaSidequest11, TornaSidequest12, TornaSidequest13, TornaSidequest14, TornaSidequest15, TornaSidequest16, TornaSidequest17, TornaSidequest18, TornaSidequest19, TornaSidequest20, TornaSidequest21, TornaSidequest22, TornaSidequest23, TornaSidequest24, TornaSidequest25, TornaSidequest26, TornaSidequest27, TornaSidequest28, TornaSidequest29, TornaSidequest30, TornaSidequest31, TornaSidequest32, TornaSidequest33, TornaSidequest34, TornaSidequest35, TornaSidequest36, TornaSidequest37, TornaSidequest38, TornaSidequest39, TornaSidequest40, TornaSidequest41, TornaSidequest42, TornaSidequest43, TornaSidequest44, TornaSidequest45, TornaSidequest46, TornaSidequest47, TornaSidequest48, TornaSidequest49, TornaSidequest50, TornaSidequest51, TornaSidequest52, TornaSidequest53, TornaSidequest54, TornaSidequest55, TornaSidequest56, TornaSidequest57, TornaSidequest58, TornaSidequest59, TornaSidequest60, TornaSidequest61, TornaSidequest62, TornaSidequest63, TornaSidequest64, TornaSidequest65, TornaSidequest66, TornaSidequest67, TornaSidequest68, TornaSidequest69, TornaSidequest70, TornaSidequest71, TornaSidequest72, TornaSidequest73, TornaSidequest74]

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

def SelectCommunityQuests(CommunityReqs: list): # Selects the community quests that logically unlock Story Events 38 and 50 (lv 2 and lv 4 community)
    Community2Quests, Community4Quests = [], []
    for sidequest in AllTornaSidequests:
        if sidequest["Main Story Req"] < 38 and sidequest["Community Level Req"] < 2:
            Community2Quests.append(sidequest)
        if sidequest['Main Story Req'] < 50 and sidequest["Community Level Req"] < 4:
            Community4Quests.append(sidequest)

    ChosenLevel2Quests, ChosenLevel4Quests = [], []
    AlteredLevel2Quests, AlteredLevel4Quests = Community2Quests.copy(), Community4Quests.copy()
    ChosenPeopleGained = 0

    while ChosenPeopleGained < CommunityReqs[1]:
        CurrentQuest = random.choice(AlteredLevel2Quests)
        ChosenLevel2Quests.append(CurrentQuest)
        ChosenLevel4Quests.append(CurrentQuest)
        ChosenPeopleGained += CurrentQuest["Community Gained"]
        AlteredLevel2Quests.remove(CurrentQuest)
        AlteredLevel4Quests.remove(CurrentQuest)
        if CurrentQuest["Sidequest Pre-Req"] != []:
            for i in range(10): # should be enough to get dependency chains
                for quest in ChosenLevel2Quests:
                    if quest["Sidequest Pre-Req"] != []:
                        for prereq in quest["Sidequest Pre-Req"]:
                            if AllTornaSidequests[prereq - 1] not in ChosenLevel2Quests:
                                ChosenLevel2Quests.append(AllTornaSidequests[prereq - 1])
                                ChosenLevel4Quests.append(AllTornaSidequests[prereq - 1])
                                ChosenPeopleGained += AllTornaSidequests[prereq - 1]["Community Gained"]
                                AlteredLevel2Quests.remove(AllTornaSidequests[prereq - 1])
                                AlteredLevel4Quests.remove(AllTornaSidequests[prereq - 1])

    while ChosenPeopleGained < CommunityReqs[3]:
        CurrentQuest = random.choice(AlteredLevel4Quests)
        ChosenLevel4Quests.append(CurrentQuest)
        ChosenPeopleGained += CurrentQuest["Community Gained"]
        AlteredLevel4Quests.remove(CurrentQuest)
        if CurrentQuest["Sidequest Pre-Req"] != []:
            for i in range(10): # should be enough to get dependency chains
                for quest in ChosenLevel4Quests:
                    if quest["Sidequest Pre-Req"] != []:
                        for prereq in quest["Sidequest Pre-Req"]:
                            if AllTornaSidequests[prereq - 1] not in ChosenLevel4Quests:
                                ChosenLevel4Quests.append(AllTornaSidequests[prereq - 1])
                                ChosenPeopleGained += AllTornaSidequests[prereq - 1]["Community Gained"]
                                AlteredLevel4Quests.remove(AllTornaSidequests[prereq - 1])

    
    print(ChosenLevel2Quests)
    print(ChosenLevel4Quests)
    print(ChosenPeopleGained)
