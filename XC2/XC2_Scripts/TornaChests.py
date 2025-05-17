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
		'Name': 'TreasureChest2201',
		'Location Near': 2362,
		'Story Pre-Req': [49],
		'Required Items': [AegaeonKey, SuperstrKey, AegaeonAff[:2], HazeKey, KeenEyeKey, HazeAff[:2]],
		'Must Defeat Enemy IDs': [1467]
	}
    TreasureChest2202 = {
        '$id': 2202,
        'Name': 'TreasureChest2202',
        'Location Near': 2362,
        'Story Pre-Req': [49],
        'Required Items': [AegaeonKey, SuperstrKey, AegaeonAff[:2], HazeKey, KeenEyeKey, HazeAff[:2]],
        'Must Defeat Enemy IDs': [1467]
    }
    TreasureChest2203 = {
        '$id': 2203,
        'Name': 'TreasureChest2203',
        'Location Near': 2362,
        'Story Pre-Req': [49],
        'Required Items': [AegaeonKey, SuperstrKey, AegaeonAff[:2], HazeKey, KeenEyeKey, HazeAff[:2]],
        'Must Defeat Enemy IDs': [1467]
    }
    TreasureChest2204 = {
        '$id': 2204,
        'Name': 'TreasureChest2204',
        'Location Near': 2362,
        'Story Pre-Req': [49],
        'Required Items': [AegaeonKey, SuperstrKey, AegaeonAff[:2], HazeKey, KeenEyeKey, HazeAff[:2]],
        'Must Defeat Enemy IDs': [1467]
    }
    TreasureChest2205 = {
        '$id': 2205,
        'Name': 'TreasureChest2205',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]],MinothKey, [MiningKey[0]], [FortitudeKey[0]]],
        'Must Defeat Enemy IDs': []
    }
    TreasureChest2206 = {
        '$id': 2206,
        'Name': 'TreasureChest2206',
        'Location Near': 2301,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': []
    }
    TreasureChest2207 = {
        '$id': 2207,
        'Name': 'TreasureChest2207',
        'Location Near': 2316,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': []
    }
    TreasureChest2208 = {
        '$id': 2208,
        'Name': 'TreasureChest2208',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': []
    }
    TreasureChest2209 = {
        '$id': 2209,
        'Name': 'TreasureChest2209',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': []
    }
    TreasureChest2210 = {
        '$id': 2210,
        'Name': 'TreasureChest2210',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [HazeKey, [ManipEtherKey[0]], [HazeAff[0]]],
        'Must Defeat Enemy IDs': []
    }
    TreasureChest2211 = {
            '$id': 2211,
            'Name': 'TreasureChest2211',
            'Location Near': 2318,
            'Story Pre-Req': [5],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2212 = {
            '$id': 2212,
            'Name': 'TreasureChest2212',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2213 = {
            '$id': 2213,
            'Name': 'TreasureChest2213',
            'Location Near': 2304,
            'Story Pre-Req': [10],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2214 = {
            '$id': 2214,
            'Name': 'TreasureChest2214',
            'Location Near': 2304,
            'Story Pre-Req': [10],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2215 = {
            '$id': 2215,
            'Name': 'TreasureChest2215',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [BrighidKey, LockpickKey[:1], [BrighidAff[0]] , HazeKey, KeenEyeKey[:1], [HazeAff[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2216 = {
            '$id': 2216,
            'Name': 'TreasureChest2216',
            'Location Near': 2323,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2217 = {
            '$id': 2217,
            'Name': 'TreasureChest2217',
            'Location Near': 2308,
            'Story Pre-Req': [25],
            'Required Items': [TornaSlatePieceIDs[:4]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2218 = {
            '$id': 2218,
            'Name': 'TreasureChest2218',
            'Location Near': 2308,
            'Story Pre-Req': [25],
            'Required Items': [TornaSlatePieceIDs[:9]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2219 = {
            '$id': 2219,
            'Name': 'TreasureChest2219',
            'Location Near': 2368,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2220 = {
            '$id': 2220,
            'Name': 'TreasureChest2220',
            'Location Near': 2309,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2221 = {
            '$id': 2221,
            'Name': 'TreasureChest2221',
            'Location Near': 2307,
            'Story Pre-Req': [33],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2222 = {
            '$id': 2222,
            'Name': 'TreasureChest2222',
            'Location Near': 2329,
            'Story Pre-Req': [35],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2223 = {
            '$id': 2223,
            'Name': 'TreasureChest2223',
            'Location Near': 2310,
            'Story Pre-Req': [35],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2224 = {
            '$id': 2224,
            'Name': 'TreasureChest2224',
            'Location Near': 2335,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2], HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2225 = {
            '$id': 2225,
            'Name': 'TreasureChest2225',
            'Location Near': 2331,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2], HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2226 = {
            '$id': 2226,
            'Name': 'TreasureChest2226',
            'Location Near': 2331,
            'Story Pre-Req': [35],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2227 = {
            '$id': 2227,
            'Name': 'TreasureChest2227',
            'Location Near': 2333,
            'Story Pre-Req': [35],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2228 = {
            '$id': 2228,
            'Name': 'TreasureChest2228',
            'Location Near': 2331,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2229 = {
            '$id': 2229,
            'Name': 'TreasureChest2229',
            'Location Near': 2311,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2230 = {
            '$id': 2230,
            'Name': 'TreasureChest2230',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2231 = {
            '$id': 2231,
            'Name': 'TreasureChest2231',
            'Location Near': 2325,
            'Story Pre-Req': [30], # [25],
            'Required Items': [BrighidKey, LockpickKey[:1], [BrighidAff[0]] , HazeKey, KeenEyeKey[:1], [HazeAff[0]],[25460], [25461]], # LevelUpTokens[:36]],
            'Must Defeat Enemy IDs': [1468]
        }
    TreasureChest2232 = {
            '$id': 2232,
            'Name': 'TreasureChest2232',
            'Location Near': 2328,
            'Story Pre-Req': [29],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2233 = {
            '$id': 2233,
            'Name': 'TreasureChest2233',
            'Location Near': 2334,
            'Story Pre-Req': [35],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2234 = {
            '$id': 2234,
            'Name': 'TreasureChest2234',
            'Location Near': 2317,
            'Story Pre-Req': [5],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2235 = {
            '$id': 2235,
            'Name': 'TreasureChest2235',
            'Location Near': 2302,
            'Story Pre-Req': [5],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2236 = {
            '$id': 2236,
            'Name': 'TreasureChest2236',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2237 = {
            '$id': 2237,
            'Name': 'TreasureChest2237',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2238 = {
            '$id': 2238,
            'Name': 'TreasureChest2238',
            'Location Near': 2304,
            'Story Pre-Req': [10],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2239 = {
            '$id': 2239,
            'Name': 'TreasureChest2239',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2240 = {
            '$id': 2240,
            'Name': 'TreasureChest2240',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2241 = {
            '$id': 2241,
            'Name': 'TreasureChest2241',
            'Location Near': 2326,
            'Story Pre-Req': [25],
            'Required Items': [BrighidKey, [LockpickKey[0]] , HazeKey, [KeenEyeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2242 = {
            '$id': 2242,
            'Name': 'TreasureChest2242',
            'Location Near': 2324,
            'Story Pre-Req': [25],
            'Required Items': [BrighidKey, LockpickKey[:1], [BrighidAff[0]] , HazeKey, KeenEyeKey[:1], [HazeAff[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2243 = {
            '$id': 2243,
            'Name': 'TreasureChest2243',
            'Location Near': 2324,
            'Story Pre-Req': [25],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2244 = {
            '$id': 2244,
            'Name': 'TreasureChest2244',
            'Location Near': 2325,
            'Story Pre-Req': [30], # [25],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]],[25460] , [25461]], # LevelUpTokens[:36]],
            'Must Defeat Enemy IDs': [1468]
        }
    TreasureChest2245 = {
            '$id': 2245,
            'Name': 'TreasureChest2245',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2246 = {
            '$id': 2246,
            'Name': 'TreasureChest2246',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [BrighidKey, LockpickKey[:1], [BrighidAff[0]] , HazeKey, KeenEyeKey[:1], [HazeAff[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2247 = {
            '$id': 2247,
            'Name': 'TreasureChest2247',
            'Location Near': 2309,
            'Story Pre-Req': [25],
            'Required Items': [SwordplayKey[:1], [JinAff[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2248 = {
            '$id': 2248,
            'Name': 'TreasureChest2248',
            'Location Near': 2326,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2249 = {
            '$id': 2249,
            'Name': 'TreasureChest2249',
            'Location Near': 2307,
            'Story Pre-Req': [33],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2250 = {
            '$id': 2250,
            'Name': 'TreasureChest2250',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2251 = {
            '$id': 2251,
            'Name': 'TreasureChest2251',
            'Location Near': 2310,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': [1661]
        }
    TreasureChest2252 = {
            '$id': 2252,
            'Name': 'TreasureChest2252',
            'Location Near': 2332,
            'Story Pre-Req': [35],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2253 = {
            '$id': 2253,
            'Name': 'TreasureChest2253',
            'Location Near': 2334,
            'Story Pre-Req': [35],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2254 = {
            '$id': 2254,
            'Name': 'TreasureChest2254',
            'Location Near': 2337,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2255 = {
            '$id': 2255,
            'Name': 'TreasureChest2255',
            'Location Near': 2334,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2256 = {
            '$id': 2256,
            'Name': 'TreasureChest2256',
            'Location Near': 2310,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2257 = {
            '$id': 2257,
            'Name': 'TreasureChest2257',
            'Location Near': 2319,
            'Story Pre-Req': [8],
            'Required Items': [MinothKey, MiningKey, MinothAff , FortitudeKey, JinAff],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2258 = {
            '$id': 2258,
            'Name': 'TreasureChest2258',
            'Location Near': 2327,
            'Story Pre-Req': [24],
            'Required Items': [[FortitudeKey[0]] , AegaeonKey, [SuperstrKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2259 = {
            '$id': 2259,
            'Name': 'TreasureChest2259',
            'Location Near': 2317,
            'Story Pre-Req': [5],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2260 = {
            '$id': 2260,
            'Name': 'TreasureChest2260',
            'Location Near': 2332,
            'Story Pre-Req': [35],
            'Required Items': [MinothKey, MiningKey[:1], MinothAff[:1] , FortitudeKey[:1], JinAff[:1]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2261 = {
            '$id': 2261,
            'Name': 'TreasureChest2261',
            'Location Near': 2307,
            'Story Pre-Req': [33],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2262 = {
            '$id': 2262,
            'Name': 'TreasureChest2262',
            'Location Near': 2329,
            'Story Pre-Req': [35],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2263 = {
            '$id': 2263,
            'Name': 'TreasureChest2263',
            'Location Near': 2330,
            'Story Pre-Req': [35],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2264 = {
            '$id': 2264,
            'Name': 'TreasureChest2264',
            'Location Near': 2314,
            'Story Pre-Req': [35],
            'Required Items': [MinothKey, MiningKey, MinothAff , FortitudeKey, JinAff],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2265 = {
            '$id': 2265,
            'Name': 'TreasureChest2265',
            'Location Near': 2314,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2266 = {
            '$id': 2266,
            'Name': 'TreasureChest2266',
            'Location Near': 2312,
            'Story Pre-Req': [35],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2267 = {
            '$id': 2267,
            'Name': 'TreasureChest2267',
            'Location Near': 2368,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2268 = {
            '$id': 2268,
            'Name': 'TreasureChest2268',
            'Location Near': 2368,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2269 = {
            '$id': 2269,
            'Name': 'TreasureChest2269',
            'Location Near': 2368,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2270 = {
            '$id': 2270,
            'Name': 'TreasureChest2270',
            'Location Near': 2346,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2271 = {
            '$id': 2271,
            'Name': 'TreasureChest2271',
            'Location Near': 2346,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2272 = {
            '$id': 2272,
            'Name': 'TreasureChest2272',
            'Location Near': 2347,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2273 = {
            '$id': 2273,
            'Name': 'TreasureChest2273',
            'Location Near': 2347,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2274 = {
            '$id': 2274,
            'Name': 'TreasureChest2274',
            'Location Near': 2344,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2275 = {
            '$id': 2275,
            'Name': 'TreasureChest2275',
            'Location Near': 2341,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2276 = {
            '$id': 2276,
            'Name': 'TreasureChest2276',
            'Location Near': 2348,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2277 = {
            '$id': 2277,
            'Name': 'TreasureChest2277',
            'Location Near': 2346,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2278 = {
            '$id': 2278,
            'Name': 'TreasureChest2278',
            'Location Near': 2341,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2279 = {
            '$id': 2279,
            'Name': 'TreasureChest2279',
            'Location Near': 2344,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2280 = {
            '$id': 2280,
            'Name': 'TreasureChest2280',
            'Location Near': 2344,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2281 = {
            '$id': 2281,
            'Name': 'TreasureChest2281',
            'Location Near': 2350,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2282 = {
            '$id': 2282,
            'Name': 'TreasureChest2282',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2283 = {
            '$id': 2283,
            'Name': 'TreasureChest2283',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2284 = {
            '$id': 2284,
            'Name': 'TreasureChest2284',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2285 = {
            '$id': 2285,
            'Name': 'TreasureChest2285',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2286 = {
            '$id': 2286,
            'Name': 'TreasureChest2286',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2287 = {
            '$id': 2287,
            'Name': 'TreasureChest2287',
            'Location Near': 2303,
            'Story Pre-Req': [8],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2288 = {
            '$id': 2288,
            'Name': 'TreasureChest2288',
            'Location Near': 2304,
            'Story Pre-Req': [10],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2289 = {
            '$id': 2289,
            'Name': 'TreasureChest2289',
            'Location Near': 2304,
            'Story Pre-Req': [10],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2290 = {
            '$id': 2290,
            'Name': 'TreasureChest2290',
            'Location Near': 2304,
            'Story Pre-Req': [10],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2291 = {
            '$id': 2291,
            'Name': 'TreasureChest2291',
            'Location Near': 2304,
            'Story Pre-Req': [10],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2292 = {
            '$id': 2292,
            'Name': 'TreasureChest2292',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2293 = {
            '$id': 2293,
            'Name': 'TreasureChest2293',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2294 = {
            '$id': 2294,
            'Name': 'TreasureChest2294',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2295 = {
            '$id': 2295,
            'Name': 'TreasureChest2295',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2296 = {
            '$id': 2296,
            'Name': 'TreasureChest2296',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2297 = {
            '$id': 2297,
            'Name': 'TreasureChest2297',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2298 = {
            '$id': 2298,
            'Name': 'TreasureChest2298',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2299 = {
            '$id': 2299,
            'Name': 'TreasureChest2299',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2300 = {
            '$id': 2300,
            'Name': 'TreasureChest2300',
            'Location Near': 2305,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2301 = {
            '$id': 2301,
            'Name': 'TreasureChest2301',
            'Location Near': 2323,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2302 = {
            '$id': 2302,
            'Name': 'TreasureChest2302',
            'Location Near': 2323,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2303 = {
            '$id': 2303,
            'Name': 'TreasureChest2303',
            'Location Near': 2323,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2304 = {
            '$id': 2304,
            'Name': 'TreasureChest2304',
            'Location Near': 2323,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2305 = {
            '$id': 2305,
            'Name': 'TreasureChest2305',
            'Location Near': 2323,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2306 = {
            '$id': 2306,
            'Name': 'TreasureChest2306',
            'Location Near': 2307,
            'Story Pre-Req': [33],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2307 = {
            '$id': 2307,
            'Name': 'TreasureChest2307',
            'Location Near': 2307,
            'Story Pre-Req': [33],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2308 = {
            '$id': 2308,
            'Name': 'TreasureChest2308',
            'Location Near': 2307,
            'Story Pre-Req': [33],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2309 = {
            '$id': 2309,
            'Name': 'TreasureChest2309',
            'Location Near': 2307,
            'Story Pre-Req': [33],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2310 = {
            '$id': 2310,
            'Name': 'TreasureChest2310',
            'Location Near': 2307,
            'Story Pre-Req': [33],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2311 = {
            '$id': 2311,
            'Name': 'TreasureChest2311',
            'Location Near': 2310,
            'Story Pre-Req': [35],
            'Required Items': [AegaeonKey, SuperstrKey, AegaeonAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2312 = {
            '$id': 2312,
            'Name': 'TreasureChest2312',
            'Location Near': 2323,
            'Story Pre-Req': [25],
            'Required Items': [AegaeonKey, SuperstrKey[:1], AegaeonAff[:1] , HazeKey, KeenEyeKey[:1], [HazeAff[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2313 = {
            '$id': 2313,
            'Name': 'TreasureChest2313',
            'Location Near': 2307,
            'Story Pre-Req': [33],
            'Required Items': [AegaeonKey, [SuperstrKey[0]] , HazeKey, [KeenEyeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2314 = {
            '$id': 2314,
            'Name': 'TreasureChest2314',
            'Location Near': 2333,
            'Story Pre-Req': [35],
            'Required Items': [AegaeonKey, SuperstrKey, AegaeonAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2315 = {
            '$id': 2315,
            'Name': 'TreasureChest2315',
            'Location Near': 2321,
            'Story Pre-Req': [5],
            'Required Items': [],
            'Must Defeat Enemy IDs': [1596, 1608, 1578]
        }
    TreasureChest2316 = {
            '$id': 2316,
            'Name': 'TreasureChest2316',
            'Location Near': 2304,
            'Story Pre-Req': [10],
            'Required Items': [SwordplayKey, JinAff[:2] , MythraKey, FocusKey, MythraAff[:2]],
            'Must Defeat Enemy IDs': [1634, 1595, 1653]
        }
    TreasureChest2317 = {
            '$id': 2317,
            'Name': 'TreasureChest2317',
            'Location Near': 2313,
            'Story Pre-Req': [25],
            'Required Items': [],
            'Must Defeat Enemy IDs': [1575, 1637, 1606]
        }
    TreasureChest2318 = {
            '$id': 2318,
            'Name': 'TreasureChest2318',
            'Location Near': 2336,
            'Story Pre-Req': [35],
            'Required Items': [HazeKey, ManipEtherKey, HazeAff[:2] , AegaeonKey, ComWaterKey, AegaeonAff],
            'Must Defeat Enemy IDs': [1594, 1593]
        }
    TreasureChest2319 = {
            '$id': 2319,
            'Name': 'TreasureChest2319',
            'Location Near': 2365,
            'Story Pre-Req': [46],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2320 = {
            '$id': 2320,
            'Name': 'TreasureChest2320',
            'Location Near': 2356,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2321 = {
            '$id': 2321,
            'Name': 'TreasureChest2321',
            'Location Near': 2354,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2322 = {
            '$id': 2322,
            'Name': 'TreasureChest2322',
            'Location Near': 2358,
            'Story Pre-Req': [36],
            'Required Items': [FortitudeKey[:1], JinAff[:1] , AegaeonKey, SuperstrKey[:1], AegaeonAff[:1]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2323 = {
            '$id': 2323,
            'Name': 'TreasureChest2323',
            'Location Near': 2363,
            'Story Pre-Req': [36],
            'Required Items': [FortitudeKey, JinAff , AegaeonKey, SuperstrKey, AegaeonAff[:2]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2324 = {
            '$id': 2324,
            'Name': 'TreasureChest2324',
            'Location Near': 2361,
            'Story Pre-Req': [36],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2325 = {
            '$id': 2325,
            'Name': 'TreasureChest2325',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2326 = {
            '$id': 2326,
            'Name': 'TreasureChest2326',
            'Location Near': 2361,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2327 = {
            '$id': 2327,
            'Name': 'TreasureChest2327',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2328 = {
            '$id': 2328,
            'Name': 'TreasureChest2328',
            'Location Near': 2365,
            'Story Pre-Req': [46],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2329 = {
            '$id': 2329,
            'Name': 'TreasureChest2329',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2330 = {
            '$id': 2330,
            'Name': 'TreasureChest2330',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2331 = {
            '$id': 2331,
            'Name': 'TreasureChest2331',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2332 = {
            '$id': 2332,
            'Name': 'TreasureChest2332',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2333 = {
            '$id': 2333,
            'Name': 'TreasureChest2333',
            'Location Near': 2357,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2334 = {
            '$id': 2334,
            'Name': 'TreasureChest2334',
            'Location Near': 2357,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2335 = {
            '$id': 2335,
            'Name': 'TreasureChest2335',
            'Location Near': 2365,
            'Story Pre-Req': [46],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2336 = {
            '$id': 2336,
            'Name': 'TreasureChest2336',
            'Location Near': 2365,
            'Story Pre-Req': [46],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2337 = {
            '$id': 2337,
            'Name': 'TreasureChest2337',
            'Location Near': 2360,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2338 = {
            '$id': 2338,
            'Name': 'TreasureChest2338',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2339 = {
            '$id': 2339,
            'Name': 'TreasureChest2339',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2340 = {
            '$id': 2340,
            'Name': 'TreasureChest2340',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2341 = {
            '$id': 2341,
            'Name': 'TreasureChest2341',
            'Location Near': 2361,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2342 = {
            '$id': 2342,
            'Name': 'TreasureChest2342',
            'Location Near': 2361,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2343 = {
            '$id': 2343,
            'Name': 'TreasureChest2343',
            'Location Near': 2361,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2344 = {
            '$id': 2344,
            'Name': 'TreasureChest2344',
            'Location Near': 2361,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2345 = {
            '$id': 2345,
            'Name': 'TreasureChest2345',
            'Location Near': 2361,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2346 = {
            '$id': 2346,
            'Name': 'TreasureChest2346',
            'Location Near': 2361,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2347 = {
            '$id': 2347,
            'Name': 'TreasureChest2347',
            'Location Near': 2363,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2348 = {
            '$id': 2348,
            'Name': 'TreasureChest2348',
            'Location Near': 2363,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2349 = {
            '$id': 2349,
            'Name': 'TreasureChest2349',
            'Location Near': 2362,
            'Story Pre-Req': [36],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2350 = {
            '$id': 2350,
            'Name': 'TreasureChest2350',
            'Location Near': 2368,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2351 = {
            '$id': 2351,
            'Name': 'TreasureChest2351',
            'Location Near': 2368,
            'Story Pre-Req': [53],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2501 = {
            '$id': 2501,
            'Name': 'TreasureChest2501',
            'Location Near': 2424,
            'Story Pre-Req': [12],
            'Required Items': [MinothKey, MiningKey[:1], MinothAff[:1] , FortitudeKey[:1], JinAff[:1]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2502 = {
            '$id': 2502,
            'Name': 'TreasureChest2502',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2503 = {
            '$id': 2503,
            'Name': 'TreasureChest2503',
            'Location Near': 2401,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': [1482]
        }
    TreasureChest2504 = {
            '$id': 2504,
            'Name': 'TreasureChest2504',
            'Location Near': 2407,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2505 = {
            '$id': 2505,
            'Name': 'TreasureChest2505',
            'Location Near': 2401,
            'Story Pre-Req': [16],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2506 = {
            '$id': 2506,
            'Name': 'TreasureChest2506',
            'Location Near': 2401,
            'Story Pre-Req': [16],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2507 = {
            '$id': 2507,
            'Name': 'TreasureChest2507',
            'Location Near': 2407,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2508 = {
            '$id': 2508,
            'Name': 'TreasureChest2508',
            'Location Near': 2413,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2509 = {
            '$id': 2509,
            'Name': 'TreasureChest2509',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2510 = {
            '$id': 2510,
            'Name': 'TreasureChest2510',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2511 = {
            '$id': 2511,
            'Name': 'TreasureChest2511',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2512 = {
            '$id': 2512,
            'Name': 'TreasureChest2512',
            'Location Near': 2404,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2513 = {
            '$id': 2513,
            'Name': 'TreasureChest2513',
            'Location Near': 2403,
            'Story Pre-Req': [12],
            'Required Items': [BrighidKey, LockpickKey[:1], [BrighidAff[0]] , HazeKey, KeenEyeKey[:1], [HazeAff[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2514 = {
            '$id': 2514,
            'Name': 'TreasureChest2514',
            'Location Near': 2413,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2515 = {
            '$id': 2515,
            'Name': 'TreasureChest2515',
            'Location Near': 2416,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2516 = {
            '$id': 2516,
            'Name': 'TreasureChest2516',
            'Location Near': 2421,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2517 = {
            '$id': 2517,
            'Name': 'TreasureChest2517',
            'Location Near': 2413,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2518 = {
            '$id': 2518,
            'Name': 'TreasureChest2518',
            'Location Near': 2417,
            'Story Pre-Req': [12],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2519 = {
            '$id': 2519,
            'Name': 'TreasureChest2519',
            'Location Near': 2417,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2520 = {
            '$id': 2520,
            'Name': 'TreasureChest2520',
            'Location Near': 2422,
            'Story Pre-Req': [12],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': [1564]
        }
    TreasureChest2521 = {
            '$id': 2521,
            'Name': 'TreasureChest2521',
            'Location Near': 2421,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2522 = {
            '$id': 2522,
            'Name': 'TreasureChest2522',
            'Location Near': 2404,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2523 = {
            '$id': 2523,
            'Name': 'TreasureChest2523',
            'Location Near': 2411,
            'Story Pre-Req': [12],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2524 = {
            '$id': 2524,
            'Name': 'TreasureChest2524',
            'Location Near': 2412,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2525 = {
            '$id': 2525,
            'Name': 'TreasureChest2525',
            'Location Near': 2410,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2526 = {
            '$id': 2526,
            'Name': 'TreasureChest2526',
            'Location Near': 2415,
            'Story Pre-Req': [16],
            'Required Items': [MinothKey, MiningKey[:1], MinothAff[:1] , FortitudeKey[:1], JinAff[:1]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2527 = {
            '$id': 2527,
            'Name': 'TreasureChest2527',
            'Location Near': 2423,
            'Story Pre-Req': [12],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2528 = {
            '$id': 2528,
            'Name': 'TreasureChest2528',
            'Location Near': 2420,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2529 = {
            '$id': 2529,
            'Name': 'TreasureChest2529',
            'Location Near': 2410,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2530 = {
            '$id': 2530,
            'Name': 'TreasureChest2530',
            'Location Near': 2407,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2531 = {
            '$id': 2531,
            'Name': 'TreasureChest2531',
            'Location Near': 2426,
            'Story Pre-Req': [16],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2532 = {
            '$id': 2532,
            'Name': 'TreasureChest2532',
            'Location Near': 2422,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': [1564]
        }
    TreasureChest2533 = {
            '$id': 2533,
            'Name': 'TreasureChest2533',
            'Location Near': 2416,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2534 = {
            '$id': 2534,
            'Name': 'TreasureChest2534',
            'Location Near': 2408,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2535 = {
            '$id': 2535,
            'Name': 'TreasureChest2535',
            'Location Near': 2413,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2536 = {
            '$id': 2536,
            'Name': 'TreasureChest2536',
            'Location Near': 2408,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2537 = {
            '$id': 2537,
            'Name': 'TreasureChest2537',
            'Location Near': 2409,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2538 = {
            '$id': 2538,
            'Name': 'TreasureChest2538',
            'Location Near': 2404,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2539 = {
            '$id': 2539,
            'Name': 'TreasureChest2539',
            'Location Near': 2408,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2540 = {
            '$id': 2540,
            'Name': 'TreasureChest2540',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [MinothKey, MiningKey[:1], MinothAff[:1] , FortitudeKey[:1], JinAff[:1]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2541 = {
            '$id': 2541,
            'Name': 'TreasureChest2541',
            'Location Near': 2406,
            'Story Pre-Req': [12],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2542 = {
            '$id': 2542,
            'Name': 'TreasureChest2542',
            'Location Near': 2406,
            'Story Pre-Req': [12],
            'Required Items': [MinothKey, MiningKey, MinothAff , FortitudeKey, JinAff],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2543 = {
            '$id': 2543,
            'Name': 'TreasureChest2543',
            'Location Near': 2419,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2544 = {
            '$id': 2544,
            'Name': 'TreasureChest2544',
            'Location Near': 2419,
            'Story Pre-Req': [12],
            'Required Items': [MinothKey, [MiningKey[0]] , [FortitudeKey[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2545 = {
            '$id': 2545,
            'Name': 'TreasureChest2545',
            'Location Near': 2403,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2546 = {
            '$id': 2546,
            'Name': 'TreasureChest2546',
            'Location Near': 2418,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2547 = {
            '$id': 2547,
            'Name': 'TreasureChest2547',
            'Location Near': 2403,
            'Story Pre-Req': [12],
            'Required Items': [MinothKey, MiningKey[:1], MinothAff[:1] , FortitudeKey[:1], JinAff[:1]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2548 = {
            '$id': 2548,
            'Name': 'TreasureChest2548',
            'Location Near': 2417,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2549 = {
            '$id': 2549,
            'Name': 'TreasureChest2549',
            'Location Near': 2417,
            'Story Pre-Req': [12],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': [1563]
        }
    TreasureChest2550 = {
            '$id': 2550,
            'Name': 'TreasureChest2550',
            'Location Near': 2423,
            'Story Pre-Req': [12],
            'Required Items': [BrighidKey, LockpickKey[:1], [BrighidAff[0]] , HazeKey, KeenEyeKey[:1], [HazeAff[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2551 = {
            '$id': 2551,
            'Name': 'TreasureChest2551',
            'Location Near': 2404,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2552 = {
            '$id': 2552,
            'Name': 'TreasureChest2552',
            'Location Near': 2404,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2553 = {
            '$id': 2553,
            'Name': 'TreasureChest2553',
            'Location Near': 2428,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2554 = {
            '$id': 2554,
            'Name': 'TreasureChest2554',
            'Location Near': 2402,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2555 = {
            '$id': 2555,
            'Name': 'TreasureChest2555',
            'Location Near': 2406,
            'Story Pre-Req': [12],
            'Required Items': [BrighidKey, LockpickKey, BrighidAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2556 = {
            '$id': 2556,
            'Name': 'TreasureChest2556',
            'Location Near': 2416,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2557 = {
            '$id': 2557,
            'Name': 'TreasureChest2557',
            'Location Near': 2411,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2558 = {
            '$id': 2558,
            'Name': 'TreasureChest2558',
            'Location Near': 2401,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2559 = {
            '$id': 2559,
            'Name': 'TreasureChest2559',
            'Location Near': 2401,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2560 = {
            '$id': 2560,
            'Name': 'TreasureChest2560',
            'Location Near': 2401,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2561 = {
            '$id': 2561,
            'Name': 'TreasureChest2561',
            'Location Near': 2402,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2562 = {
            '$id': 2562,
            'Name': 'TreasureChest2562',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2563 = {
            '$id': 2563,
            'Name': 'TreasureChest2563',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2564 = {
            '$id': 2564,
            'Name': 'TreasureChest2564',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2565 = {
            '$id': 2565,
            'Name': 'TreasureChest2565',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2566 = {
            '$id': 2566,
            'Name': 'TreasureChest2566',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2567 = {
            '$id': 2567,
            'Name': 'TreasureChest2567',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2568 = {
            '$id': 2568,
            'Name': 'TreasureChest2568',
            'Location Near': 2414,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2569 = {
            '$id': 2569,
            'Name': 'TreasureChest2569',
            'Location Near': 2415,
            'Story Pre-Req': [16],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2570 = {
            '$id': 2570,
            'Name': 'TreasureChest2570',
            'Location Near': 2415,
            'Story Pre-Req': [16],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2571 = {
            '$id': 2571,
            'Name': 'TreasureChest2571',
            'Location Near': 2428,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2572 = {
            '$id': 2572,
            'Name': 'TreasureChest2572',
            'Location Near': 2428,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2573 = {
            '$id': 2573,
            'Name': 'TreasureChest2573',
            'Location Near': 2423,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2574 = {
            '$id': 2574,
            'Name': 'TreasureChest2574',
            'Location Near': 2423,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2575 = {
            '$id': 2575,
            'Name': 'TreasureChest2575',
            'Location Near': 2403,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2576 = {
            '$id': 2576,
            'Name': 'TreasureChest2576',
            'Location Near': 2403,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2577 = {
            '$id': 2577,
            'Name': 'TreasureChest2577',
            'Location Near': 2403,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2578 = {
            '$id': 2578,
            'Name': 'TreasureChest2578',
            'Location Near': 2415,
            'Story Pre-Req': [16],
            'Required Items': [AegaeonKey, SuperstrKey[:1], AegaeonAff[:1] , HazeKey, KeenEyeKey[:1], [HazeAff[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2579 = {
            '$id': 2579,
            'Name': 'TreasureChest2579',
            'Location Near': 2422,
            'Story Pre-Req': [12],
            'Required Items': [AegaeonKey, [SuperstrKey[0]] , HazeKey, [KeenEyeKey[0]]],
            'Must Defeat Enemy IDs': [1564]
        }
    TreasureChest2580 = {
            '$id': 2580,
            'Name': 'TreasureChest2580',
            'Location Near': 2404,
            'Story Pre-Req': [12],
            'Required Items': [AegaeonKey, SuperstrKey, AegaeonAff[:2] , HazeKey, KeenEyeKey, [HazeAff[:2]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2581 = {
            '$id': 2581,
            'Name': 'TreasureChest2581',
            'Location Near': 2419,
            'Story Pre-Req': [12],
            'Required Items': [AegaeonKey, SuperstrKey[:1], AegaeonAff[:1] , HazeKey, KeenEyeKey[:1], [HazeAff[0]]],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2582 = {
            '$id': 2582,
            'Name': 'TreasureChest2582',
            'Location Near': 2421,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2583 = {
            '$id': 2583,
            'Name': 'TreasureChest2583',
            'Location Near': 2421,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2584 = {
            '$id': 2584,
            'Name': 'TreasureChest2584',
            'Location Near': 2421,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2585 = {
            '$id': 2585,
            'Name': 'TreasureChest2585',
            'Location Near': 2412,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2586 = {
            '$id': 2586,
            'Name': 'TreasureChest2586',
            'Location Near': 2422,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': [1564]
        }
    TreasureChest2587 = {
            '$id': 2587,
            'Name': 'TreasureChest2587',
            'Location Near': 2410,
            'Story Pre-Req': [12],
            'Required Items': [],
            'Must Defeat Enemy IDs': []
        }
    TreasureChest2588 = {
            '$id': 2588,
            'Name': 'TreasureChest2588',
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