from scripts import Helper, JSONParser, PopupDescriptions
import json
import random
from IDs import *

TornaChestIDs = Helper.InclRange(2201, 2351)

class TornaChest:
    def __init__(self, input, addtolist, rewardnumber):
        self.id = input["$id"]
        self.name = input["Name"]
        self.nearloc = input['Location Near']
        self.mainreq = input['Story Pre-Req'][0]
        self.itemreqs = Helper.MultiLevelListToSingleLevelList(input['Required Items'])
        self.enemyreqs = input['Must Defeat Enemy IDs']
        self.randomizeditems = Helper.ExtendListtoLength(Helper.ExtendListtoLength([], rewardnumber, "-1"), 7, "0") # holds shop item ids, -1 for progression, 0 for filler spots
        self.type = "chest"
        if rewardnumber > 0:
            self.hasprogression = True
        else:
            self.hasprogression = False
        if self.id in TornaChestIDs:
            self.continent = "Torna"
        else:
            self.continent = "Gormott"
        addtolist.append(self)

def CreateChestInfo(Mainquests, Areas, Enemies, ChestRewardQty):
    TreasureChest2201 = {
		'$id': 2201,
		'Name': 'Treasure Chest 2201',
		'Location Near': 2362,
		'Story Pre-Req': [49],
		'Required Items': [AegaeonKey, SuperstrKey, AegaeonAff[:2], HazeKey, KeenEyeKey, HazeAff[:2]],
		'Must Defeat Enemy IDs': [1467]
	}
    TreasureChest2202 = {
        '$id': 2202,
        'Name': 'Treasure Chest 2202',
        'Location Near': 2362,
        'Story Pre-Req': [49],
        'Required Items': [AegaeonKey, SuperstrKey, AegaeonAff[:2], HazeKey, KeenEyeKey, HazeAff[:2]],
        'Must Defeat Enemy IDs': [1467]
    }
    TreasureChest2203 = {
        '$id': 2203,
        'Name': 'Treasure Chest 2203',
        'Location Near': 2362,
        'Story Pre-Req': [49],
        'Required Items': [AegaeonKey, SuperstrKey, AegaeonAff[:2], HazeKey, KeenEyeKey, HazeAff[:2]],
        'Must Defeat Enemy IDs': [1467]
    }
    TreasureChest2204 = {
        '$id': 2204,
        'Name': 'Treasure Chest 2204',
        'Location Near': 2362,
        'Story Pre-Req': [49],
        'Required Items': [AegaeonKey, SuperstrKey, AegaeonAff[:2], HazeKey, KeenEyeKey, HazeAff[:2]],
        'Must Defeat Enemy IDs': [1467]
    }
    TreasureChest2205 = {
        '$id': 2205,
        'Name': 'Treasure Chest 2205',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]],MinothKey, [MiningKey[0]], [FortitudeKey[0]]],
        'Must Defeat Enemy IDs': []
    }
    TreasureChest2206 = {
        '$id': 2206,
        'Name': 'Treasure Chest 2206',
        'Location Near': 2301,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': []
    }
    TreasureChest2207 = {
        '$id': 2207,
        'Name': 'Treasure Chest 2207',
        'Location Near': 2316,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': []
    }
    TreasureChest2208 = {
        '$id': 2208,
        'Name': 'Treasure Chest 2208',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': []
    }
    TreasureChest2209 = {
        '$id': 2209,
        'Name': 'Treasure Chest 2209',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': []
    }
    TreasureChest2210 = {
        '$id': 2210,
        'Name': 'Treasure Chest 2210',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [HazeKey, [ManipEtherKey[0]], [HazeAff[0]]],
        'Must Defeat Enemy IDs': []
    }
    TreasureChest2211 = {
            '$id': 2211,
            'Name': 'Treasure Chest 2211',
            'Location Near': 2318,
            'Story Pre-Req': [5],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2212 = {
            '$id': 2212,
            'Name': 'Treasure Chest 2212',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2213 = {
            '$id': 2213,
            'Name': 'Treasure Chest 2213',
            'Location Near': 2304,
            'Story Pre-Req': [10],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2214 = {
            '$id': 2214,
            'Name': 'Treasure Chest 2214',
            'Location Near': 2304,
            'Story Pre-Req': [10],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2215 = {
            '$id': 2215,
            'Name': 'Treasure Chest 2215',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [BrighidKey, LockpickKey[:1], [BrighidAff[0]] , HazeKey, KeenEyeKey[:1], [HazeAff[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2216 = {
            '$id': 2216,
            'Name': 'Treasure Chest 2216',
            'Location Near': 2323,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2217 = {
            '$id': 2217,
            'Name': 'Treasure Chest 2217',
            'Location Near': 2308,
            'Story Pre-Req': [25],
            'Required Items': [TornaSlatePieceIDs[:4]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2218 = {
            '$id': 2218,
            'Name': 'Treasure Chest 2218',
            'Location Near': 2308,
            'Story Pre-Req': [25],
            'Required Items': [TornaSlatePieceIDs[:9]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2219 = {
            '$id': 2219,
            'Name': 'Treasure Chest 2219',
            'Location Near': 2368,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2220 = {
            '$id': 2220,
            'Name': 'Treasure Chest 2220',
            'Location Near': 2309,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2221 = {
            '$id': 2221,
            'Name': 'Treasure Chest 2221',
            'Location Near': 2307,
            'Story Pre-Req': [33],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2222 = {
            '$id': 2222,
            'Name': 'Treasure Chest 2222',
            'Location Near': 2329,
            'Story Pre-Req': [35],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2223 = {
            '$id': 2223,
            'Name': 'Treasure Chest 2223',
            'Location Near': 2310,
            'Story Pre-Req': [35],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2224 = {
            '$id': 2224,
            'Name': 'Treasure Chest 2224',
            'Location Near': 2335,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2], HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2225 = {
            '$id': 2225,
            'Name': 'Treasure Chest 2225',
            'Location Near': 2331,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2], HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2226 = {
            '$id': 2226,
            'Name': 'Treasure Chest 2226',
            'Location Near': 2331,
            'Story Pre-Req': [35],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2227 = {
            '$id': 2227,
            'Name': 'Treasure Chest 2227',
            'Location Near': 2333,
            'Story Pre-Req': [35],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2228 = {
            '$id': 2228,
            'Name': 'Treasure Chest 2228',
            'Location Near': 2331,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2229 = {
            '$id': 2229,
            'Name': 'Treasure Chest 2229',
            'Location Near': 2311,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2230 = {
            '$id': 2230,
            'Name': 'Treasure Chest 2230',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2231 = {
            '$id': 2231,
            'Name': 'Treasure Chest 2231',
            'Location Near': 2325,
            'Story Pre-Req': [30], # [25],
            'Required Items': [BrighidKey, LockpickKey[:1], [BrighidAff[0]] , HazeKey, KeenEyeKey[:1], [HazeAff[0]],[25460], [25461]], # LevelUpTokens[:36]],
            'Must Defeat Enemy IDs': [1468]
        }
    TreasureChest2232 = {
            '$id': 2232,
            'Name': 'Treasure Chest 2232',
            'Location Near': 2328,
            'Story Pre-Req': [29],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2233 = {
            '$id': 2233,
            'Name': 'Treasure Chest 2233',
            'Location Near': 2334,
            'Story Pre-Req': [35],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2234 = {
            '$id': 2234,
            'Name': 'Treasure Chest 2234',
            'Location Near': 2317,
            'Story Pre-Req': [5],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2235 = {
            '$id': 2235,
            'Name': 'Treasure Chest 2235',
            'Location Near': 2302,
            'Story Pre-Req': [5],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2236 = {
            '$id': 2236,
            'Name': 'Treasure Chest 2236',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2237 = {
            '$id': 2237,
            'Name': 'Treasure Chest 2237',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2238 = {
            '$id': 2238,
            'Name': 'Treasure Chest 2238',
            'Location Near': 2304,
            'Story Pre-Req': [10],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2239 = {
            '$id': 2239,
            'Name': 'Treasure Chest 2239',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2240 = {
            '$id': 2240,
            'Name': 'Treasure Chest 2240',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2241 = {
            '$id': 2241,
            'Name': 'Treasure Chest 2241',
            'Location Near': 2326,
            'Story Pre-Req': [25],
            'Required Items': [BrighidKey, [LockpickKey[0]] , HazeKey, [KeenEyeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2242 = {
            '$id': 2242,
            'Name': 'Treasure Chest 2242',
            'Location Near': 2324,
            'Story Pre-Req': [25],
            'Required Items': [BrighidKey, LockpickKey[:1], [BrighidAff[0]] , HazeKey, KeenEyeKey[:1], [HazeAff[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2243 = {
            '$id': 2243,
            'Name': 'Treasure Chest 2243',
            'Location Near': 2324,
            'Story Pre-Req': [25],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2244 = {
            '$id': 2244,
            'Name': 'Treasure Chest 2244',
            'Location Near': 2325,
            'Story Pre-Req': [30], # [25],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]],[25460] , [25461]], # LevelUpTokens[:36]],
            'Must Defeat Enemy IDs': [1468]
        }
    TreasureChest2245 = {
            '$id': 2245,
            'Name': 'Treasure Chest 2245',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2246 = {
            '$id': 2246,
            'Name': 'Treasure Chest 2246',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [BrighidKey, LockpickKey[:1], [BrighidAff[0]] , HazeKey, KeenEyeKey[:1], [HazeAff[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2247 = {
            '$id': 2247,
            'Name': 'Treasure Chest 2247',
            'Location Near': 2309,
            'Story Pre-Req': [25],
            'Required Items': [SwordplayKey[:1], [JinAff[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2248 = {
            '$id': 2248,
            'Name': 'Treasure Chest 2248',
            'Location Near': 2326,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2249 = {
            '$id': 2249,
            'Name': 'Treasure Chest 2249',
            'Location Near': 2307,
            'Story Pre-Req': [33],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2250 = {
            '$id': 2250,
            'Name': 'Treasure Chest 2250',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2251 = {
            '$id': 2251,
            'Name': 'Treasure Chest 2251',
            'Location Near': 2310,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': [1661]
        }
    TreasureChest2252 = {
            '$id': 2252,
            'Name': 'Treasure Chest 2252',
            'Location Near': 2332,
            'Story Pre-Req': [35],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2253 = {
            '$id': 2253,
            'Name': 'Treasure Chest 2253',
            'Location Near': 2334,
            'Story Pre-Req': [35],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2254 = {
            '$id': 2254,
            'Name': 'Treasure Chest 2254',
            'Location Near': 2337,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2255 = {
            '$id': 2255,
            'Name': 'Treasure Chest 2255',
            'Location Near': 2334,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2256 = {
            '$id': 2256,
            'Name': 'Treasure Chest 2256',
            'Location Near': 2310,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2257 = {
            '$id': 2257,
            'Name': 'Treasure Chest 2257',
            'Location Near': 2319,
            'Story Pre-Req': [8],
            'Required Items': [MinothKey, MiningKey, MinothAff , FortitudeKey, JinAff],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2258 = {
            '$id': 2258,
            'Name': 'Treasure Chest 2258',
            'Location Near': 2327,
            'Story Pre-Req': [24],
            'Required Items': [[FortitudeKey[0]] , AegaeonKey, [SuperstrKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2259 = {
            '$id': 2259,
            'Name': 'Treasure Chest 2259',
            'Location Near': 2317,
            'Story Pre-Req': [5],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2260 = {
            '$id': 2260,
            'Name': 'Treasure Chest 2260',
            'Location Near': 2332,
            'Story Pre-Req': [35],
            'Required Items': [MinothKey, MiningKey[:1], MinothAff[:1] , FortitudeKey[:1], JinAff[:1]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2261 = {
            '$id': 2261,
            'Name': 'Treasure Chest 2261',
            'Location Near': 2307,
            'Story Pre-Req': [33],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2262 = {
            '$id': 2262,
            'Name': 'Treasure Chest 2262',
            'Location Near': 2329,
            'Story Pre-Req': [35],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2263 = {
            '$id': 2263,
            'Name': 'Treasure Chest 2263',
            'Location Near': 2330,
            'Story Pre-Req': [35],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2264 = {
            '$id': 2264,
            'Name': 'Treasure Chest 2264',
            'Location Near': 2314,
            'Story Pre-Req': [35],
            'Required Items': [MinothKey, MiningKey, MinothAff , FortitudeKey, JinAff],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2265 = {
            '$id': 2265,
            'Name': 'Treasure Chest 2265',
            'Location Near': 2314,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2266 = {
            '$id': 2266,
            'Name': 'Treasure Chest 2266',
            'Location Near': 2312,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2267 = {
            '$id': 2267,
            'Name': 'Treasure Chest 2267',
            'Location Near': 2368,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2268 = {
            '$id': 2268,
            'Name': 'Treasure Chest 2268',
            'Location Near': 2368,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2269 = {
            '$id': 2269,
            'Name': 'Treasure Chest 2269',
            'Location Near': 2368,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2270 = {
            '$id': 2270,
            'Name': 'Treasure Chest 2270',
            'Location Near': 2346,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2271 = {
            '$id': 2271,
            'Name': 'Treasure Chest 2271',
            'Location Near': 2346,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2272 = {
            '$id': 2272,
            'Name': 'Treasure Chest 2272',
            'Location Near': 2347,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2273 = {
            '$id': 2273,
            'Name': 'Treasure Chest 2273',
            'Location Near': 2347,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2274 = {
            '$id': 2274,
            'Name': 'Treasure Chest 2274',
            'Location Near': 2344,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2275 = {
            '$id': 2275,
            'Name': 'Treasure Chest 2275',
            'Location Near': 2341,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2276 = {
            '$id': 2276,
            'Name': 'Treasure Chest 2276',
            'Location Near': 2348,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2277 = {
            '$id': 2277,
            'Name': 'Treasure Chest 2277',
            'Location Near': 2346,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2278 = {
            '$id': 2278,
            'Name': 'Treasure Chest 2278',
            'Location Near': 2341,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2279 = {
            '$id': 2279,
            'Name': 'Treasure Chest 2279',
            'Location Near': 2344,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2280 = {
            '$id': 2280,
            'Name': 'Treasure Chest 2280',
            'Location Near': 2344,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2281 = {
            '$id': 2281,
            'Name': 'Treasure Chest 2281',
            'Location Near': 2350,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2282 = {
            '$id': 2282,
            'Name': 'Treasure Chest 2282',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2283 = {
            '$id': 2283,
            'Name': 'Treasure Chest 2283',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2284 = {
            '$id': 2284,
            'Name': 'Treasure Chest 2284',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2285 = {
            '$id': 2285,
            'Name': 'Treasure Chest 2285',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2286 = {
            '$id': 2286,
            'Name': 'Treasure Chest 2286',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2287 = {
            '$id': 2287,
            'Name': 'Treasure Chest 2287',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2288 = {
            '$id': 2288,
            'Name': 'Treasure Chest 2288',
            'Location Near': 2304,
            'Story Pre-Req': [10],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2289 = {
            '$id': 2289,
            'Name': 'Treasure Chest 2289',
            'Location Near': 2304,
            'Story Pre-Req': [10],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2290 = {
            '$id': 2290,
            'Name': 'Treasure Chest 2290',
            'Location Near': 2304,
            'Story Pre-Req': [10],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2291 = {
            '$id': 2291,
            'Name': 'Treasure Chest 2291',
            'Location Near': 2304,
            'Story Pre-Req': [10],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2292 = {
            '$id': 2292,
            'Name': 'Treasure Chest 2292',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2293 = {
            '$id': 2293,
            'Name': 'Treasure Chest 2293',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2294 = {
            '$id': 2294,
            'Name': 'Treasure Chest 2294',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2295 = {
            '$id': 2295,
            'Name': 'Treasure Chest 2295',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2296 = {
            '$id': 2296,
            'Name': 'Treasure Chest 2296',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2297 = {
            '$id': 2297,
            'Name': 'Treasure Chest 2297',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2298 = {
            '$id': 2298,
            'Name': 'Treasure Chest 2298',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2299 = {
            '$id': 2299,
            'Name': 'Treasure Chest 2299',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2300 = {
            '$id': 2300,
            'Name': 'Treasure Chest 2300',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2301 = {
            '$id': 2301,
            'Name': 'Treasure Chest 2301',
            'Location Near': 2323,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2302 = {
            '$id': 2302,
            'Name': 'Treasure Chest 2302',
            'Location Near': 2323,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2303 = {
            '$id': 2303,
            'Name': 'Treasure Chest 2303',
            'Location Near': 2323,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2304 = {
            '$id': 2304,
            'Name': 'Treasure Chest 2304',
            'Location Near': 2323,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2305 = {
            '$id': 2305,
            'Name': 'Treasure Chest 2305',
            'Location Near': 2323,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2306 = {
            '$id': 2306,
            'Name': 'Treasure Chest 2306',
            'Location Near': 2307,
            'Story Pre-Req': [33],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2307 = {
            '$id': 2307,
            'Name': 'Treasure Chest 2307',
            'Location Near': 2307,
            'Story Pre-Req': [33],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2308 = {
            '$id': 2308,
            'Name': 'Treasure Chest 2308',
            'Location Near': 2307,
            'Story Pre-Req': [33],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2309 = {
            '$id': 2309,
            'Name': 'Treasure Chest 2309',
            'Location Near': 2307,
            'Story Pre-Req': [33],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2310 = {
            '$id': 2310,
            'Name': 'Treasure Chest 2310',
            'Location Near': 2307,
            'Story Pre-Req': [33],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2311 = {
            '$id': 2311,
            'Name': 'Treasure Chest 2311',
            'Location Near': 2310,
            'Story Pre-Req': [35],
            'Required Items': [AegaeonKey, SuperstrKey, AegaeonAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2312 = {
            '$id': 2312,
            'Name': 'Treasure Chest 2312',
            'Location Near': 2323,
            'Story Pre-Req': [25],
            'Required Items': [AegaeonKey, SuperstrKey[:1], AegaeonAff[:1] , HazeKey, KeenEyeKey[:1], [HazeAff[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2313 = {
            '$id': 2313,
            'Name': 'Treasure Chest 2313',
            'Location Near': 2307,
            'Story Pre-Req': [33],
            'Required Items': [AegaeonKey, [SuperstrKey[0]] , HazeKey, [KeenEyeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2314 = {
            '$id': 2314,
            'Name': 'Treasure Chest 2314',
            'Location Near': 2333,
            'Story Pre-Req': [35],
            'Required Items': [AegaeonKey, SuperstrKey, AegaeonAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2315 = {
            '$id': 2315,
            'Name': 'Treasure Chest 2315',
            'Location Near': 2321,
            'Story Pre-Req': [5],
            'Required Items': [],
            'Must Defeat Enemy IDs': [1596, 1608, 1578]
        }
    TreasureChest2316 = {
            '$id': 2316,
            'Name': 'Treasure Chest 2316',
            'Location Near': 2304,
            'Story Pre-Req': [10],
            'Required Items': [SwordplayKey, JinAff[:2] , MythraKey, FocusKey, MythraAff[:2]],
            'Must Defeat Enemy IDs': [1634, 1595, 1653]
        }
    TreasureChest2317 = {
            '$id': 2317,
            'Name': 'Treasure Chest 2317',
            'Location Near': 2313,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': [1575, 1637, 1606]
        }
    TreasureChest2318 = {
            '$id': 2318,
            'Name': 'Treasure Chest 2318',
            'Location Near': 2336,
            'Story Pre-Req': [35],
            'Required Items': [HazeKey, ManipEtherKey, HazeAff[:2] , AegaeonKey, ComWaterKey, AegaeonAff],
            'Must Defeat Enemy IDs': [1594, 1593]
        }
    TreasureChest2319 = {
            '$id': 2319,
            'Name': 'Treasure Chest 2319',
            'Location Near': 2365,
            'Story Pre-Req': [46],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2320 = {
            '$id': 2320,
            'Name': 'Treasure Chest 2320',
            'Location Near': 2356,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2321 = {
            '$id': 2321,
            'Name': 'Treasure Chest 2321',
            'Location Near': 2354,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2322 = {
            '$id': 2322,
            'Name': 'Treasure Chest 2322',
            'Location Near': 2358,
            'Story Pre-Req': [36],
            'Required Items': [FortitudeKey[:1], JinAff[:1] , AegaeonKey, SuperstrKey[:1], AegaeonAff[:1]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2323 = {
            '$id': 2323,
            'Name': 'Treasure Chest 2323',
            'Location Near': 2363,
            'Story Pre-Req': [36],
            'Required Items': [FortitudeKey, JinAff , AegaeonKey, SuperstrKey, AegaeonAff[:2]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2324 = {
            '$id': 2324,
            'Name': 'Treasure Chest 2324',
            'Location Near': 2361,
            'Story Pre-Req': [36],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2325 = {
            '$id': 2325,
            'Name': 'Treasure Chest 2325',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2326 = {
            '$id': 2326,
            'Name': 'Treasure Chest 2326',
            'Location Near': 2361,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2327 = {
            '$id': 2327,
            'Name': 'Treasure Chest 2327',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2328 = {
            '$id': 2328,
            'Name': 'Treasure Chest 2328',
            'Location Near': 2365,
            'Story Pre-Req': [46],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2329 = {
            '$id': 2329,
            'Name': 'Treasure Chest 2329',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2330 = {
            '$id': 2330,
            'Name': 'Treasure Chest 2330',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2331 = {
            '$id': 2331,
            'Name': 'Treasure Chest 2331',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2332 = {
            '$id': 2332,
            'Name': 'Treasure Chest 2332',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2333 = {
            '$id': 2333,
            'Name': 'Treasure Chest 2333',
            'Location Near': 2357,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2334 = {
            '$id': 2334,
            'Name': 'Treasure Chest 2334',
            'Location Near': 2357,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2335 = {
            '$id': 2335,
            'Name': 'Treasure Chest 2335',
            'Location Near': 2365,
            'Story Pre-Req': [46],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2336 = {
            '$id': 2336,
            'Name': 'Treasure Chest 2336',
            'Location Near': 2365,
            'Story Pre-Req': [46],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2337 = {
            '$id': 2337,
            'Name': 'Treasure Chest 2337',
            'Location Near': 2360,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2338 = {
            '$id': 2338,
            'Name': 'Treasure Chest 2338',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2339 = {
            '$id': 2339,
            'Name': 'Treasure Chest 2339',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2340 = {
            '$id': 2340,
            'Name': 'Treasure Chest 2340',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2341 = {
            '$id': 2341,
            'Name': 'Treasure Chest 2341',
            'Location Near': 2361,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2342 = {
            '$id': 2342,
            'Name': 'Treasure Chest 2342',
            'Location Near': 2361,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2343 = {
            '$id': 2343,
            'Name': 'Treasure Chest 2343',
            'Location Near': 2361,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2344 = {
            '$id': 2344,
            'Name': 'Treasure Chest 2344',
            'Location Near': 2361,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2345 = {
            '$id': 2345,
            'Name': 'Treasure Chest 2345',
            'Location Near': 2361,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2346 = {
            '$id': 2346,
            'Name': 'Treasure Chest 2346',
            'Location Near': 2361,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2347 = {
            '$id': 2347,
            'Name': 'Treasure Chest 2347',
            'Location Near': 2363,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2348 = {
            '$id': 2348,
            'Name': 'Treasure Chest 2348',
            'Location Near': 2363,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2349 = {
            '$id': 2349,
            'Name': 'Treasure Chest 2349',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2350 = {
            '$id': 2350,
            'Name': 'Treasure Chest 2350',
            'Location Near': 2368,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2351 = {
            '$id': 2351,
            'Name': 'Treasure Chest 2351',
            'Location Near': 2368,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2501 = {
            '$id': 2501,
            'Name': 'Treasure Chest 2501',
            'Location Near': 2424,
            'Story Pre-Req': [12],
            'Required Items': [MinothKey, MiningKey[:1], MinothAff[:1] , FortitudeKey[:1], JinAff[:1]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2502 = {
            '$id': 2502,
            'Name': 'Treasure Chest 2502',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2503 = {
            '$id': 2503,
            'Name': 'Treasure Chest 2503',
            'Location Near': 2401,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': [1482]
        }
    TreasureChest2504 = {
            '$id': 2504,
            'Name': 'Treasure Chest 2504',
            'Location Near': 2407,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2505 = {
            '$id': 2505,
            'Name': 'Treasure Chest 2505',
            'Location Near': 2401,
            'Story Pre-Req': [16],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2506 = {
            '$id': 2506,
            'Name': 'Treasure Chest 2506',
            'Location Near': 2401,
            'Story Pre-Req': [16],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2507 = {
            '$id': 2507,
            'Name': 'Treasure Chest 2507',
            'Location Near': 2407,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2508 = {
            '$id': 2508,
            'Name': 'Treasure Chest 2508',
            'Location Near': 2413,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2509 = {
            '$id': 2509,
            'Name': 'Treasure Chest 2509',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2510 = {
            '$id': 2510,
            'Name': 'Treasure Chest 2510',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2511 = {
            '$id': 2511,
            'Name': 'Treasure Chest 2511',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2512 = {
            '$id': 2512,
            'Name': 'Treasure Chest 2512',
            'Location Near': 2404,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2513 = {
            '$id': 2513,
            'Name': 'Treasure Chest 2513',
            'Location Near': 2403,
            'Story Pre-Req': [12],
            'Required Items': [BrighidKey, LockpickKey[:1], [BrighidAff[0]] , HazeKey, KeenEyeKey[:1], [HazeAff[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2514 = {
            '$id': 2514,
            'Name': 'Treasure Chest 2514',
            'Location Near': 2413,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2515 = {
            '$id': 2515,
            'Name': 'Treasure Chest 2515',
            'Location Near': 2416,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2516 = {
            '$id': 2516,
            'Name': 'Treasure Chest 2516',
            'Location Near': 2421,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2517 = {
            '$id': 2517,
            'Name': 'Treasure Chest 2517',
            'Location Near': 2413,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2518 = {
            '$id': 2518,
            'Name': 'Treasure Chest 2518',
            'Location Near': 2417,
            'Story Pre-Req': [12],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2519 = {
            '$id': 2519,
            'Name': 'Treasure Chest 2519',
            'Location Near': 2417,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2520 = {
            '$id': 2520,
            'Name': 'Treasure Chest 2520',
            'Location Near': 2422,
            'Story Pre-Req': [12],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': [1564]
        }
    TreasureChest2521 = {
            '$id': 2521,
            'Name': 'Treasure Chest 2521',
            'Location Near': 2421,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2522 = {
            '$id': 2522,
            'Name': 'Treasure Chest 2522',
            'Location Near': 2404,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2523 = {
            '$id': 2523,
            'Name': 'Treasure Chest 2523',
            'Location Near': 2411,
            'Story Pre-Req': [12],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2524 = {
            '$id': 2524,
            'Name': 'Treasure Chest 2524',
            'Location Near': 2412,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2525 = {
            '$id': 2525,
            'Name': 'Treasure Chest 2525',
            'Location Near': 2410,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2526 = {
            '$id': 2526,
            'Name': 'Treasure Chest 2526',
            'Location Near': 2415,
            'Story Pre-Req': [16],
            'Required Items': [MinothKey, MiningKey[:1], MinothAff[:1] , FortitudeKey[:1], JinAff[:1]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2527 = {
            '$id': 2527,
            'Name': 'Treasure Chest 2527',
            'Location Near': 2423,
            'Story Pre-Req': [12],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2528 = {
            '$id': 2528,
            'Name': 'Treasure Chest 2528',
            'Location Near': 2420,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2529 = {
            '$id': 2529,
            'Name': 'Treasure Chest 2529',
            'Location Near': 2410,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2530 = {
            '$id': 2530,
            'Name': 'Treasure Chest 2530',
            'Location Near': 2407,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2531 = {
            '$id': 2531,
            'Name': 'Treasure Chest 2531',
            'Location Near': 2426,
            'Story Pre-Req': [16],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2532 = {
            '$id': 2532,
            'Name': 'Treasure Chest 2532',
            'Location Near': 2422,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': [1564]
        }
    TreasureChest2533 = {
            '$id': 2533,
            'Name': 'Treasure Chest 2533',
            'Location Near': 2416,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2534 = {
            '$id': 2534,
            'Name': 'Treasure Chest 2534',
            'Location Near': 2408,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2535 = {
            '$id': 2535,
            'Name': 'Treasure Chest 2535',
            'Location Near': 2413,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2536 = {
            '$id': 2536,
            'Name': 'Treasure Chest 2536',
            'Location Near': 2408,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2537 = {
            '$id': 2537,
            'Name': 'Treasure Chest 2537',
            'Location Near': 2409,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2538 = {
            '$id': 2538,
            'Name': 'Treasure Chest 2538',
            'Location Near': 2404,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2539 = {
            '$id': 2539,
            'Name': 'Treasure Chest 2539',
            'Location Near': 2408,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2540 = {
            '$id': 2540,
            'Name': 'Treasure Chest 2540',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [MinothKey, MiningKey[:1], MinothAff[:1] , FortitudeKey[:1], JinAff[:1]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2541 = {
            '$id': 2541,
            'Name': 'Treasure Chest 2541',
            'Location Near': 2406,
            'Story Pre-Req': [12],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2542 = {
            '$id': 2542,
            'Name': 'Treasure Chest 2542',
            'Location Near': 2406,
            'Story Pre-Req': [12],
            'Required Items': [MinothKey, MiningKey, MinothAff , FortitudeKey, JinAff],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2543 = {
            '$id': 2543,
            'Name': 'Treasure Chest 2543',
            'Location Near': 2419,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2544 = {
            '$id': 2544,
            'Name': 'Treasure Chest 2544',
            'Location Near': 2419,
            'Story Pre-Req': [12],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2545 = {
            '$id': 2545,
            'Name': 'Treasure Chest 2545',
            'Location Near': 2403,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2546 = {
            '$id': 2546,
            'Name': 'Treasure Chest 2546',
            'Location Near': 2418,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2547 = {
            '$id': 2547,
            'Name': 'Treasure Chest 2547',
            'Location Near': 2403,
            'Story Pre-Req': [12],
            'Required Items': [MinothKey, MiningKey[:1], MinothAff[:1] , FortitudeKey[:1], JinAff[:1]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2548 = {
            '$id': 2548,
            'Name': 'Treasure Chest 2548',
            'Location Near': 2417,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2549 = {
            '$id': 2549,
            'Name': 'Treasure Chest 2549',
            'Location Near': 2417,
            'Story Pre-Req': [12],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': [1563]
        }
    TreasureChest2550 = {
            '$id': 2550,
            'Name': 'Treasure Chest 2550',
            'Location Near': 2423,
            'Story Pre-Req': [12],
            'Required Items': [BrighidKey, LockpickKey[:1], [BrighidAff[0]] , HazeKey, KeenEyeKey[:1], [HazeAff[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2551 = {
            '$id': 2551,
            'Name': 'Treasure Chest 2551',
            'Location Near': 2404,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2552 = {
            '$id': 2552,
            'Name': 'Treasure Chest 2552',
            'Location Near': 2404,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2553 = {
            '$id': 2553,
            'Name': 'Treasure Chest 2553',
            'Location Near': 2428,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2554 = {
            '$id': 2554,
            'Name': 'Treasure Chest 2554',
            'Location Near': 2402,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2555 = {
            '$id': 2555,
            'Name': 'Treasure Chest 2555',
            'Location Near': 2406,
            'Story Pre-Req': [12],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2556 = {
            '$id': 2556,
            'Name': 'Treasure Chest 2556',
            'Location Near': 2416,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2557 = {
            '$id': 2557,
            'Name': 'Treasure Chest 2557',
            'Location Near': 2411,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2558 = {
            '$id': 2558,
            'Name': 'Treasure Chest 2558',
            'Location Near': 2401,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2559 = {
            '$id': 2559,
            'Name': 'Treasure Chest 2559',
            'Location Near': 2401,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2560 = {
            '$id': 2560,
            'Name': 'Treasure Chest 2560',
            'Location Near': 2401,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2561 = {
            '$id': 2561,
            'Name': 'Treasure Chest 2561',
            'Location Near': 2402,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2562 = {
            '$id': 2562,
            'Name': 'Treasure Chest 2562',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2563 = {
            '$id': 2563,
            'Name': 'Treasure Chest 2563',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2564 = {
            '$id': 2564,
            'Name': 'Treasure Chest 2564',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2565 = {
            '$id': 2565,
            'Name': 'Treasure Chest 2565',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2566 = {
            '$id': 2566,
            'Name': 'Treasure Chest 2566',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2567 = {
            '$id': 2567,
            'Name': 'Treasure Chest 2567',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2568 = {
            '$id': 2568,
            'Name': 'Treasure Chest 2568',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2569 = {
            '$id': 2569,
            'Name': 'Treasure Chest 2569',
            'Location Near': 2415,
            'Story Pre-Req': [16],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2570 = {
            '$id': 2570,
            'Name': 'Treasure Chest 2570',
            'Location Near': 2415,
            'Story Pre-Req': [16],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2571 = {
            '$id': 2571,
            'Name': 'Treasure Chest 2571',
            'Location Near': 2428,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2572 = {
            '$id': 2572,
            'Name': 'Treasure Chest 2572',
            'Location Near': 2428,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2573 = {
            '$id': 2573,
            'Name': 'Treasure Chest 2573',
            'Location Near': 2423,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2574 = {
            '$id': 2574,
            'Name': 'Treasure Chest 2574',
            'Location Near': 2423,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2575 = {
            '$id': 2575,
            'Name': 'Treasure Chest 2575',
            'Location Near': 2403,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2576 = {
            '$id': 2576,
            'Name': 'Treasure Chest 2576',
            'Location Near': 2403,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2577 = {
            '$id': 2577,
            'Name': 'Treasure Chest 2577',
            'Location Near': 2403,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2578 = {
            '$id': 2578,
            'Name': 'Treasure Chest 2578',
            'Location Near': 2415,
            'Story Pre-Req': [16],
            'Required Items': [AegaeonKey, SuperstrKey[:1], AegaeonAff[:1] , HazeKey, KeenEyeKey[:1], [HazeAff[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2579 = {
            '$id': 2579,
            'Name': 'Treasure Chest 2579',
            'Location Near': 2422,
            'Story Pre-Req': [12],
            'Required Items': [AegaeonKey, [SuperstrKey[0]] , HazeKey, [KeenEyeKey[0]]],
            'Must Defeat Enemy IDs': [1564]
        }
    TreasureChest2580 = {
            '$id': 2580,
            'Name': 'Treasure Chest 2580',
            'Location Near': 2404,
            'Story Pre-Req': [12],
            'Required Items': [AegaeonKey, SuperstrKey, AegaeonAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2581 = {
            '$id': 2581,
            'Name': 'Treasure Chest 2581',
            'Location Near': 2419,
            'Story Pre-Req': [12],
            'Required Items': [AegaeonKey, SuperstrKey[:1], AegaeonAff[:1] , HazeKey, KeenEyeKey[:1], [HazeAff[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2582 = {
            '$id': 2582,
            'Name': 'Treasure Chest 2582',
            'Location Near': 2421,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2583 = {
            '$id': 2583,
            'Name': 'Treasure Chest 2583',
            'Location Near': 2421,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2584 = {
            '$id': 2584,
            'Name': 'Treasure Chest 2584',
            'Location Near': 2421,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2585 = {
            '$id': 2585,
            'Name': 'Treasure Chest 2585',
            'Location Near': 2412,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2586 = {
            '$id': 2586,
            'Name': 'Treasure Chest 2586',
            'Location Near': 2422,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': [1564]
        }
    TreasureChest2587 = {
            '$id': 2587,
            'Name': 'Treasure Chest 2587',
            'Location Near': 2410,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2588 = {
            '$id': 2588,
            'Name': 'Treasure Chest 2588',
            'Location Near': 2426,
            'Story Pre-Req': [16],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    
    TornaChestDict = [TreasureChest2201, TreasureChest2202, TreasureChest2203, TreasureChest2204, TreasureChest2205, TreasureChest2206, TreasureChest2207, TreasureChest2208, TreasureChest2209, TreasureChest2210, TreasureChest2211, TreasureChest2212, TreasureChest2213, TreasureChest2214, TreasureChest2215, TreasureChest2216, TreasureChest2217, TreasureChest2218, TreasureChest2219, TreasureChest2220, TreasureChest2221, TreasureChest2222, TreasureChest2223, TreasureChest2224, TreasureChest2225, TreasureChest2226, TreasureChest2227, TreasureChest2228, TreasureChest2229, TreasureChest2230, TreasureChest2231, TreasureChest2232, TreasureChest2233, TreasureChest2234, TreasureChest2235, TreasureChest2236, TreasureChest2237, TreasureChest2238, TreasureChest2239, TreasureChest2240, TreasureChest2241, TreasureChest2242, TreasureChest2243, TreasureChest2244, TreasureChest2245, TreasureChest2246, TreasureChest2247, TreasureChest2248, TreasureChest2249, TreasureChest2250, TreasureChest2251, TreasureChest2252, TreasureChest2253, TreasureChest2254, TreasureChest2255, TreasureChest2256, TreasureChest2257, TreasureChest2258, TreasureChest2259, TreasureChest2260, TreasureChest2261, TreasureChest2262, TreasureChest2263, TreasureChest2264, TreasureChest2265, TreasureChest2266, TreasureChest2267, TreasureChest2268, TreasureChest2269, TreasureChest2270, TreasureChest2271, TreasureChest2272, TreasureChest2273, TreasureChest2274, TreasureChest2275, TreasureChest2276, TreasureChest2277, TreasureChest2278, TreasureChest2279, TreasureChest2280, TreasureChest2281, TreasureChest2282, TreasureChest2283, TreasureChest2284, TreasureChest2285, TreasureChest2286, TreasureChest2287, TreasureChest2288, TreasureChest2289, TreasureChest2290, TreasureChest2291, TreasureChest2292, TreasureChest2293, TreasureChest2294, TreasureChest2295, TreasureChest2296, TreasureChest2297, TreasureChest2298, TreasureChest2299, TreasureChest2300, TreasureChest2301, TreasureChest2302, TreasureChest2303, TreasureChest2304, TreasureChest2305, TreasureChest2306, TreasureChest2307, TreasureChest2308, TreasureChest2309, TreasureChest2310, TreasureChest2311, TreasureChest2312, TreasureChest2313, TreasureChest2314, TreasureChest2315, TreasureChest2316, TreasureChest2317, TreasureChest2318, TreasureChest2319, TreasureChest2320, TreasureChest2321, TreasureChest2322, TreasureChest2323, TreasureChest2324, TreasureChest2325, TreasureChest2326, TreasureChest2327, TreasureChest2328, TreasureChest2329, TreasureChest2330, TreasureChest2331, TreasureChest2332, TreasureChest2333, TreasureChest2334, TreasureChest2335, TreasureChest2336, TreasureChest2337, TreasureChest2338, TreasureChest2339, TreasureChest2340, TreasureChest2341, TreasureChest2342, TreasureChest2343, TreasureChest2344, TreasureChest2345, TreasureChest2346, TreasureChest2347, TreasureChest2348, TreasureChest2349, TreasureChest2350, TreasureChest2351, TreasureChest2501, TreasureChest2502, TreasureChest2503, TreasureChest2504, TreasureChest2505, TreasureChest2506, TreasureChest2507, TreasureChest2508, TreasureChest2509, TreasureChest2510, TreasureChest2511, TreasureChest2512, TreasureChest2513, TreasureChest2514, TreasureChest2515, TreasureChest2516, TreasureChest2517, TreasureChest2518, TreasureChest2519, TreasureChest2520, TreasureChest2521, TreasureChest2522, TreasureChest2523, TreasureChest2524, TreasureChest2525, TreasureChest2526, TreasureChest2527, TreasureChest2528, TreasureChest2529, TreasureChest2530, TreasureChest2531, TreasureChest2532, TreasureChest2533, TreasureChest2534, TreasureChest2535, TreasureChest2536, TreasureChest2537, TreasureChest2538, TreasureChest2539, TreasureChest2540, TreasureChest2541, TreasureChest2542, TreasureChest2543, TreasureChest2544, TreasureChest2545, TreasureChest2546, TreasureChest2547, TreasureChest2548, TreasureChest2549, TreasureChest2550, TreasureChest2551, TreasureChest2552, TreasureChest2553, TreasureChest2554, TreasureChest2555, TreasureChest2556, TreasureChest2557, TreasureChest2558, TreasureChest2559, TreasureChest2560, TreasureChest2561, TreasureChest2562, TreasureChest2563, TreasureChest2564, TreasureChest2565, TreasureChest2566, TreasureChest2567, TreasureChest2568, TreasureChest2569, TreasureChest2570, TreasureChest2571, TreasureChest2572, TreasureChest2573, TreasureChest2574, TreasureChest2575, TreasureChest2576, TreasureChest2577, TreasureChest2578, TreasureChest2579, TreasureChest2580, TreasureChest2581, TreasureChest2582, TreasureChest2583, TreasureChest2584, TreasureChest2585, TreasureChest2586, TreasureChest2587, TreasureChest2588]
    
    global TornaChests
    TornaChests = []

    for chest in TornaChestDict:
        TornaChest(chest, TornaChests, ChestRewardQty)

    for chest in TornaChests:
        if chest.mainreq != []:
            chest.itemreqs.extend(Mainquests[chest.mainreq - 1].itemreqs) # adds main story req
            chest.itemreqs = Helper.MultiLevelListToSingleLevelList(chest.itemreqs)
            chest.itemreqs = list(set(chest.itemreqs))
            chest.itemreqs.sort()
        for area in Areas: # adds the area reach requirements
            if chest.nearloc == area.id:
                chest.itemreqs.extend(area.itemreqs)
                break
        if chest.enemyreqs != []:
            for chestenemyreq in chest.enemyreqs:
                for enemy in Enemies:
                    if enemy.id == chestenemyreq:
                        chest.itemreqs.extend(enemy.itemreqs)
                        break
    return TornaChests