from scripts import Helper, JSONParser, PopupDescriptions
import json
import random
from XC2.XC2_Scripts.IDs import *

AreaNametoIDDict = {'Lasaria Woodland': 2315, 'Porton Village': 2301, 'Secluded Boneway': 2302, 'Hangnail Crossing': 2316, 'Haradd Hills': 2317, 'Cropwoods of Yorn': 2318, 'Mernes Falls': 2321, 'Feltley Village': 2303, 'Great Crater': 2319, "Uccar's Trail": 2320, 'Yanchik Harbor': 2304, 'Lascham Cove': 2401, 'Lakeshore Campsite': 2402, 'Hidden Hunting Camp': 2403, 'Singbreeze Bough': 2404, 'Torigoth Arch': 2405, "Titan's Roar": 2406, 'Lascham Peninsula': 2407, 'Ordia Great Plains': 2408, 'Serene Springside': 2409, "Duelist's Bridge": 2410, 'Wayside Respite': 2411, 'Outlook Knoll': 2412, 'Lyanne Meadow': 2413, 'Torigoth Village': 2414, 'Torigoth Cemetery': 2415, 'Coolley Lake': 2416, 'Hoary Weald': 2417, 'Seigle Fell': 2418, 'Depths of Ignorance': 2419, "Grandarbor's Embrace": 2420, 'Nebley Wind Cave': 2421, "Saint's Practice Grounds": 2422, 'Hoary Weald Camp': 2423, 'Nox Promontory': 2424, 'Valafum Hill': 2425, 'Strategy Room': 2426, 'Coolley Lake Camp': 2428, 'Aletta Harbor': 2327, 'Aletta: Militia Garrison': 2305, 'Cavern of the Seal': 2308, 'Ossum Magnum': 2309, 'Millennium Grotto': 2313, 'Wrackham Moor': 2322, 'Tirkin Cliff Colony': 2323, 'Lake Sarleigh': 2324, "Behemoth's Roost": 2325, 'Ancient Lakebed': 2326, 'Lett Bridge': 2306, "Olnard's Trail": 2328, 'Hyber Village': 2307, 'The Great Breaksand': 2310, 'Loftin Nature Preserve': 2311, 'Holy Gate of Altana': 2312, 'Turqos Plateau': 2314, 'The Braying Canyon': 2329, 'Dannagh Desert': 2330, 'Streamsand Corridor': 2331, 'Golden Twin Mesa': 2332, 'Verdant Fairylands': 2333, "Peln, Pilgrim's Springland": 2334, 'Lake Wynn': 2335, "Titan's Ulcer": 2336, 'Outriders Forest Trail': 2337, 'Sacred Staircase': 2338, 'Auresco, Main Gate': 2351, 'Spefan Inn': 2352, 'Aureus Palace': 2353, 'Median Gate': 2354, 'Auresco, Rear Gate': 2355, 'Planus Bridge': 2356, 'Formide Shopping Ward': 2357, 'Fabri Industry Ward': 2358, 'Auresco Residential Ward': 2359, 'Acheron Backstreet': 2360, 'Sachsum Gardens': 2361, 'Aquila Watchtower': 2362, 'Orem Storage Ward': 2363, 'Pischator Bridge': 2364, 'Viridian Gate': 2366, "Torna's Womb": 2365, 'Balaur, Dark Zone #1': 2339, 'Fernyiges, Dark Zone #2': 2340, 'Skygate Entrance': 2341, 'Zirnitra, Dark Zone #3': 2342, 'The Soaring Rostrum': 2343, 'Pedestal of Stargazing': 2344, 'Hall of Worship': 2345, 'Crooked Tower': 2346, 'Pantarhei Tower': 2347, 'Pulsating Passage': 2348, "Hermit's Alleyway": 2349, 'Skygate, Endless Road': 2350, 'Tasteless Altar': 2368}

class TornaArea: # created to allow me to pass these objects easier
    def __init__(self, input, addtolist):
        self.id = input["$id"]
        self.name = input["Name"]
        self.prevloc = input['Previous Location Reachable']
        self.mainreq = input['Story Pre-Req'][0]
        self.itemreqs = Helper.MultiLevelListToSingleLevelList(input['Item Reqs'])
        try:
            self.prevlocid = AreaNametoIDDict[self.prevloc]
        except:
            self.prevlocid = 0
        addtolist.append(self)

def CreateAreaInfo(Sidequests, Mainquests):
    LasariaWoodland = {
        '$id': 2315,
        'Name': 'Lasaria Woodland',
        'Previous Location Reachable': '',
        'Story Pre-Req': [1],
        'Item Reqs': []
    }
    PortonVillage = {
        '$id': 2301,
        'Name': 'Porton Village',
        'Previous Location Reachable': 'Lasaria Woodland',
        'Story Pre-Req': [2],
        'Item Reqs': []
    }
    SecludedBoneway = {
        '$id': 2302,
        'Name': 'Secluded Boneway',
        'Previous Location Reachable': 'Haradd Hills',
        'Story Pre-Req': [5],
        'Item Reqs': []
    }
    HangnailCrossing = {
        '$id': 2316,
        'Name': 'Hangnail Crossing',
        'Previous Location Reachable': 'Porton Village',
        'Story Pre-Req': [5],
        'Item Reqs': []
    }
    HaraddHills = {
        '$id': 2317,
        'Name': 'Haradd Hills',
        'Previous Location Reachable': 'Hangnail Crossing',
        'Story Pre-Req': [5],
        'Item Reqs': [[SwordplayKey[0]]]
    }
    CropwoodsofYorn = {
        '$id': 2318,
        'Name': 'Cropwoods of Yorn',
        'Previous Location Reachable': 'Secluded Boneway',
        'Story Pre-Req': [5],
        'Item Reqs': []
    }
    MernesFalls = {
        '$id': 2321,
        'Name': 'Mernes Falls',
        'Previous Location Reachable': 'Haradd Hills',
        'Story Pre-Req': [5],
        'Item Reqs': []
    }
    FeltleyVillage = {
        '$id': 2303,
        'Name': 'Feltley Village',
        'Previous Location Reachable': 'Cropwoods of Yorn',
        'Story Pre-Req': [8],
        'Item Reqs': []
    }
    GreatCrater = {
        '$id': 2319,
        'Name': 'Great Crater',
        'Previous Location Reachable': 'Feltley Village',
        'Story Pre-Req': [8],
        'Item Reqs': []
    }
    UccarsTrail = {
        '$id': 2320,
        'Name': 'Uccar\'s Trail',
        'Previous Location Reachable': 'Feltley Village',
        'Story Pre-Req': [8],
        'Item Reqs': []
    }
    YanchikHarbor = {
        '$id': 2304,
        'Name': 'Yanchik Harbor',
        'Previous Location Reachable': 'Uccar\'s Trail',
        'Story Pre-Req': [10],
        'Item Reqs': []
    }
    LaschamCove = {
        '$id': 2401,
        'Name': 'Lascham Cove',
        'Previous Location Reachable': 'Yanchik Harbor',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    LakeshoreCampsite = {
        '$id': 2402,
        'Name': 'Lakeshore Campsite',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    HiddenHuntingCamp = {
        '$id': 2403,
        'Name': 'Hidden Hunting Camp',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    SingbreezeBough = {
        '$id': 2404,
        'Name': 'Singbreeze Bough',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    TorigothArch = {
        '$id': 2405,
        'Name': 'Torigoth Arch',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    TitansRoar = {
        '$id': 2406,
        'Name': 'Titan\'s Roar',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    LaschamPeninsula = {
        '$id': 2407,
        'Name': 'Lascham Peninsula',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    OrdiaGreatPlains = {
        '$id': 2408,
        'Name': 'Ordia Great Plains',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    SereneSpringside = {
        '$id': 2409,
        'Name': 'Serene Springside',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    DuelistsBridge = {
        '$id': 2410,
        'Name': 'Duelist\'s Bridge',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    WaysideRespite = {
        '$id': 2411,
        'Name': 'Wayside Respite',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    OutlookKnoll = {
        '$id': 2412,
        'Name': 'Outlook Knoll',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    LyanneMeadow = {
        '$id': 2413,
        'Name': 'Lyanne Meadow',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    TorigothVillage = {
        '$id': 2414,
        'Name': 'Torigoth Village',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    TorigothCemetery = {
        '$id': 2415,
        'Name': 'Torigoth Cemetery',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    CoolleyLake = {
        '$id': 2416,
        'Name': 'Coolley Lake',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    HoaryWeald = {
        '$id': 2417,
        'Name': 'Hoary Weald',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    SeigleFell = {
        '$id': 2418,
        'Name': 'Seigle Fell',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    DepthsofIgnorance = {
        '$id': 2419,
        'Name': 'Depths of Ignorance',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    GrandarborsEmbrace = {
        '$id': 2420,
        'Name': 'Grandarbor\'s Embrace',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    NebleyWindCave = {
        '$id': 2421,
        'Name': 'Nebley Wind Cave',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    SaintsPracticeGrounds = {
        '$id': 2422,
        'Name': 'Saint\'s Practice Grounds',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    HoaryWealdCamp = {
        '$id': 2423,
        'Name': 'Hoary Weald Camp',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    NoxPromontory = {
        '$id': 2424,
        'Name': 'Nox Promontory',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    ValafumHill = {
        '$id': 2425,
        'Name': 'Valafum Hill',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    StrategyRoom = {
        '$id': 2426,
        'Name': 'Strategy Room',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    CoolleyLakeCamp = {
        '$id': 2428,
        'Name': 'Coolley Lake Camp',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    AlettaHarbor = {
        '$id': 2327,
        'Name': 'Aletta Harbor',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [24],
        'Item Reqs': []
    }
    AlettaMilitiaGarrison = {
        '$id': 2305,
        'Name': 'Aletta: Militia Garrison',
        'Previous Location Reachable': 'Aletta Harbor',
        'Story Pre-Req': [25],
        'Item Reqs': []
    }
    CavernoftheSeal = {
        '$id': 2308,
        'Name': 'Cavern of the Seal',
        'Previous Location Reachable': 'Aletta: Militia Garrison',
        'Story Pre-Req': [25],
        'Item Reqs': []
    }
    OssumMagnum = {
        '$id': 2309,
        'Name': 'Ossum Magnum',
        'Previous Location Reachable': 'Aletta: Militia Garrison',
        'Story Pre-Req': [25],
        'Item Reqs': []
    }
    MillenniumGrotto = {
        '$id': 2313,
        'Name': 'Millennium Grotto',
        'Previous Location Reachable': 'Aletta: Militia Garrison',
        'Story Pre-Req': [25],
        'Item Reqs': [SwordplayKey[:2], [JinAff[0]] , AegaeonKey, ComWaterKey, AegaeonAff]
    }
    WrackhamMoor = {
        '$id': 2322,
        'Name': 'Wrackham Moor',
        'Previous Location Reachable': 'Aletta: Militia Garrison',
        'Story Pre-Req': [25],
        'Item Reqs': []
    }
    TirkinCliffColony = {
        '$id': 2323,
        'Name': 'Tirkin Cliff Colony',
        'Previous Location Reachable': 'Aletta: Militia Garrison',
        'Story Pre-Req': [25],
        'Item Reqs': []
    }
    LakeSarleigh = {
        '$id': 2324,
        'Name': 'Lake Sarleigh',
        'Previous Location Reachable': 'Aletta: Militia Garrison',
        'Story Pre-Req': [25],
        'Item Reqs': []
    }
    BehemothsRoost = {
        '$id': 2325,
        'Name': 'Behemoth\'s Roost',
        'Previous Location Reachable': 'Aletta: Militia Garrison',
        'Story Pre-Req': [25],
        'Item Reqs': []
    }
    AncientLakebed = {
        '$id': 2326,
        'Name': 'Ancient Lakebed',
        'Previous Location Reachable': 'Aletta: Militia Garrison',
        'Story Pre-Req': [25],
        'Item Reqs': []
    }
    LettBridge = {
        '$id': 2306,
        'Name': 'Lett Bridge',
        'Previous Location Reachable': 'Aletta: Militia Garrison',
        'Story Pre-Req': [28],
        'Item Reqs': []
    }
    OlnardsTrail = {
        '$id': 2328,
        'Name': 'Olnard\'s Trail',
        'Previous Location Reachable': 'Lett Bridge',
        'Story Pre-Req': [29],
        'Item Reqs': []
    }
    HyberVillage = {
        '$id': 2307,
        'Name': 'Hyber Village',
        'Previous Location Reachable': 'Olnard\'s Trail',
        'Story Pre-Req': [33],
        'Item Reqs': []
    }
    TheGreatBreaksand = {
        '$id': 2310,
        'Name': 'The Great Breaksand',
        'Previous Location Reachable': 'Golden Twin Mesa',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    LoftinNaturePreserve = {
        '$id': 2311,
        'Name': 'Loftin Nature Preserve',
        'Previous Location Reachable': 'Dannagh Desert',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    HolyGateofAltana = {
        '$id': 2312,
        'Name': 'Holy Gate of Altana',
        'Previous Location Reachable': 'Sacred Staircase',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    TurqosPlateau = {
        '$id': 2314,
        'Name': 'Turqos Plateau',
        'Previous Location Reachable': 'The Great Breaksand',
        'Story Pre-Req': [35],
        'Item Reqs': [SwordplayKey[:2], [JinAff[0]] , FortitudeKey[:2], JinAff[:2]]
    }
    TheBrayingCanyon = {
        '$id': 2329,
        'Name': 'The Braying Canyon',
        'Previous Location Reachable': 'Hyber Village',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    DannaghDesert = {
        '$id': 2330,
        'Name': 'Dannagh Desert',
        'Previous Location Reachable': 'The Braying Canyon',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    StreamsandCorridor = {
        '$id': 2331,
        'Name': 'Streamsand Corridor',
        'Previous Location Reachable': 'Dannagh Desert',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    GoldenTwinMesa = {
        '$id': 2332,
        'Name': 'Golden Twin Mesa',
        'Previous Location Reachable': 'Dannagh Desert',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    VerdantFairylands = {
        '$id': 2333,
        'Name': 'Verdant Fairylands',
        'Previous Location Reachable': 'Lake Wynn',
        'Story Pre-Req': [35],
        'Item Reqs': [AegaeonKey, ComWaterKey[:2], AegaeonAff[:2]]
    }
    PelnPilgrimsSpringland = {
        '$id': 2334,
        'Name': 'Peln, Pilgrim\'s Springland',
        'Previous Location Reachable': 'Dannagh Desert',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    LakeWynn = {
        '$id': 2335,
        'Name': 'Lake Wynn',
        'Previous Location Reachable': 'Dannagh Desert',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    TitansUlcer = {
        '$id': 2336,
        'Name': 'Titan\'s Ulcer',
        'Previous Location Reachable': 'Dannagh Desert',
        'Story Pre-Req': [35],
        'Item Reqs': [HazeKey, ManipEtherKey, HazeAff[:3] , AegaeonKey, ComWaterKey, AegaeonAff]
    }
    OutridersForestTrail = {
        '$id': 2337,
        'Name': 'Outriders Forest Trail',
        'Previous Location Reachable': 'Dannagh Desert',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    SacredStaircase = {
        '$id': 2338,
        'Name': 'Sacred Staircase',
        'Previous Location Reachable': 'Dannagh Desert',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    AurescoMainGate = {
        '$id': 2351,
        'Name': 'Auresco, Main Gate',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    SpefanInn = {
        '$id': 2352,
        'Name': 'Spefan Inn',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    AureusPalace = {
        '$id': 2353,
        'Name': 'Aureus Palace',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    MedianGate = {
        '$id': 2354,
        'Name': 'Median Gate',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    AurescoRearGate = {
        '$id': 2355,
        'Name': 'Auresco, Rear Gate',
        'Previous Location Reachable': 'Orem Storage Ward',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    PlanusBridge = {
        '$id': 2356,
        'Name': 'Planus Bridge',
        'Previous Location Reachable': 'Outrider\'s Forest Trail',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    FormideShoppingWard = {
        '$id': 2357,
        'Name': 'Formide Shopping Ward',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    FabriIndustryWard = {
        '$id': 2358,
        'Name': 'Fabri Industry Ward',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    AurescoResidentialWard = {
        '$id': 2359,
        'Name': 'Auresco Residential Ward',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    AcheronBackstreet = {
        '$id': 2360,
        'Name': 'Acheron Backstreet',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    SachsumGardens = {
        '$id': 2361,
        'Name': 'Sachsum Gardens',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    AquilaWatchtower = {
        '$id': 2362,
        'Name': 'Aquila Watchtower',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    OremStorageWard = {
        '$id': 2363,
        'Name': 'Orem Storage Ward',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    PischatorBridge = {
        '$id': 2364,
        'Name': 'Pischator Bridge',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    ViridianGate = {
        '$id': 2366,
        'Name': 'Viridian Gate',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    TornasWomb = {
        '$id': 2365,
        'Name': 'Torna\'s Womb',
        'Previous Location Reachable': 'Auresco, Rear Gate',
        'Story Pre-Req': [46],
        'Item Reqs': []
    }
    BalaurDarkZone1 = {
        '$id': 2339,
        'Name': 'Balaur, Dark Zone #1',
        'Previous Location Reachable': 'Hall of Worship',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    FernyigesDarkZone2 = {
        '$id': 2340,
        'Name': 'Fernyiges, Dark Zone #2',
        'Previous Location Reachable': 'Crooked Tower',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    SkygateEntrance = {
        '$id': 2341,
        'Name': 'Skygate Entrance',
        'Previous Location Reachable': 'Pulsating Passage',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    ZirnitraDarkZone3 = {
        '$id': 2342,
        'Name': 'Zirnitra, Dark Zone #3',
        'Previous Location Reachable': 'Pantarhei Tower',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    TheSoaringRostrum = {
        '$id': 2343,
        'Name': 'The Soaring Rostrum',
        'Previous Location Reachable': 'Skygate, Endless Road',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    PedestalofStargazing = {
        '$id': 2344,
        'Name': 'Pedestal of Stargazing',
        'Previous Location Reachable': 'Hermit\'s Alleyway',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    HallofWorship = {
        '$id': 2345,
        'Name': 'Hall of Worship',
        'Previous Location Reachable': 'Holy Gate of Altana',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    CrookedTower = {
        '$id': 2346,
        'Name': 'Crooked Tower',
        'Previous Location Reachable': 'Balaur, Dark Zone #1',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    PantarheiTower = {
        '$id': 2347,
        'Name': 'Pantarhei Tower',
        'Previous Location Reachable': 'Fernyiges, Dark Zone #2',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    PulsatingPassage = {
        '$id': 2348,
        'Name': 'Pulsating Passage',
        'Previous Location Reachable': 'Zirnitra, Dark Zone #3',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    HermitsAlleyway = {
        '$id': 2349,
        'Name': 'Hermit\'s Alleyway',
        'Previous Location Reachable': 'Pulsating Passage',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    SkygateEndlessRoad = {
        '$id': 2350,
        'Name': 'Skygate, Endless Road',
        'Previous Location Reachable': 'Pulsating Passage',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    TastelessAltar = {
        '$id': 2368,
        'Name': 'Tasteless Altar',
        'Previous Location Reachable': 'Cavern of the Seal',
        'Story Pre-Req': [25],
        'Item Reqs': TornaSlatePieceIDs
    }
     
    TornaAreaDict = [LasariaWoodland, PortonVillage, SecludedBoneway, HangnailCrossing, HaraddHills, CropwoodsofYorn, MernesFalls, FeltleyVillage, GreatCrater, UccarsTrail, YanchikHarbor, LaschamCove, LakeshoreCampsite, HiddenHuntingCamp, SingbreezeBough, TorigothArch, TitansRoar, LaschamPeninsula, OrdiaGreatPlains, SereneSpringside, DuelistsBridge, WaysideRespite, OutlookKnoll, LyanneMeadow, TorigothVillage, TorigothCemetery, CoolleyLake, HoaryWeald, SeigleFell, DepthsofIgnorance, GrandarborsEmbrace, NebleyWindCave, SaintsPracticeGrounds, HoaryWealdCamp, NoxPromontory, ValafumHill, StrategyRoom, CoolleyLakeCamp, AlettaHarbor, AlettaMilitiaGarrison, CavernoftheSeal, OssumMagnum, MillenniumGrotto, WrackhamMoor, TirkinCliffColony, LakeSarleigh, BehemothsRoost, AncientLakebed, LettBridge, OlnardsTrail, HyberVillage, TheGreatBreaksand, LoftinNaturePreserve, HolyGateofAltana, TurqosPlateau, TheBrayingCanyon, DannaghDesert, StreamsandCorridor, GoldenTwinMesa, VerdantFairylands, PelnPilgrimsSpringland, LakeWynn, TitansUlcer, OutridersForestTrail, SacredStaircase, AurescoMainGate, SpefanInn, AureusPalace, MedianGate, AurescoRearGate, PlanusBridge, FormideShoppingWard, FabriIndustryWard, AurescoResidentialWard, AcheronBackstreet, SachsumGardens, AquilaWatchtower, OremStorageWard, PischatorBridge, ViridianGate, TornasWomb, BalaurDarkZone1, FernyigesDarkZone2, SkygateEntrance, ZirnitraDarkZone3, TheSoaringRostrum, PedestalofStargazing, HallofWorship, CrookedTower, PantarheiTower, PulsatingPassage, HermitsAlleyway, SkygateEndlessRoad, TastelessAltar]
    
    global TornaAreas
    TornaAreas = []

    for area in TornaAreaDict:
        TornaArea(area, TornaAreas)

    TornaAreaIDtoNameDict = {}
    for area in TornaAreas:
        TornaAreaIDtoNameDict[area.id] = area

    for area in TornaAreas:
        if area.mainreq != []:
            area.itemreqs.extend(Mainquests[area.mainreq - 1].itemreqs) # adds main story req
        if area.prevlocid != 0:
            area.itemreqs.extend(TornaAreaIDtoNameDict[area.prevlocid].itemreqs)
        area.itemreqs = Helper.MultiLevelListToSingleLevelList(area.itemreqs)
        area.itemreqs = list(set(area.itemreqs))
        area.itemreqs.sort()

    return TornaAreas, TornaAreaIDtoNameDict