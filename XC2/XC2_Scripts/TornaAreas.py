from scripts import Helper, JSONParser, PopupDescriptions
import json
import random
from IDs import *

class TornaArea: # created to allow me to pass these objects easier
    def __init__(self, input, addtolist):
        self.id = input["$id"]
        self.name = input["Name"]
        self.prevloc = input['Previous Location Reachable']
        self.mainreq = input['Story Pre-Req']
        self.itemreqs = Helper.MultiLevelListToSingleLevelList(input['Item Reqs'])
        addtolist.append(self)

def CreateAreaInfo(Sidequests, Mainquests):
    LasariaWoodland = {
        '$id': 2315,
        'Name': 'LasariaWoodland',
        'Previous Location Reachable': '',
        'Story Pre-Req': [1],
        'Item Reqs': []
    }
    PortonVillage = {
        '$id': 2301,
        'Name': 'PortonVillage',
        'Previous Location Reachable': 'Lasaria Woodland',
        'Story Pre-Req': [2],
        'Item Reqs': []
    }
    SecludedBoneway = {
        '$id': 2302,
        'Name': 'SecludedBoneway',
        'Previous Location Reachable': 'Haradd Hills',
        'Story Pre-Req': [5],
        'Item Reqs': []
    }
    HangnailCrossing = {
        '$id': 2316,
        'Name': 'HangnailCrossing',
        'Previous Location Reachable': 'Porton Village',
        'Story Pre-Req': [5],
        'Item Reqs': []
    }
    HaraddHills = {
        '$id': 2317,
        'Name': 'HaraddHills',
        'Previous Location Reachable': 'Hangnail Crossing',
        'Story Pre-Req': [5],
        'Item Reqs': [[SwordplayKey[0]]]
    }
    CropwoodsofYorn = {
        '$id': 2318,
        'Name': 'CropwoodsofYorn',
        'Previous Location Reachable': 'Secluded Boneway',
        'Story Pre-Req': [5],
        'Item Reqs': []
    }
    MernesFalls = {
        '$id': 2321,
        'Name': 'MernesFalls',
        'Previous Location Reachable': 'Haradd Hills',
        'Story Pre-Req': [5],
        'Item Reqs': []
    }
    FeltleyVillage = {
        '$id': 2303,
        'Name': 'FeltleyVillage',
        'Previous Location Reachable': 'Cropwoods of Yorn',
        'Story Pre-Req': [8],
        'Item Reqs': []
    }
    GreatCrater = {
        '$id': 2319,
        'Name': 'GreatCrater',
        'Previous Location Reachable': 'Feltley Village',
        'Story Pre-Req': [8],
        'Item Reqs': []
    }
    UccarsTrail = {
        '$id': 2320,
        'Name': 'UccarsTrail',
        'Previous Location Reachable': 'Feltley Village',
        'Story Pre-Req': [8],
        'Item Reqs': []
    }
    YanchikHarbor = {
        '$id': 2304,
        'Name': 'YanchikHarbor',
        'Previous Location Reachable': 'Uccars Trail',
        'Story Pre-Req': [10],
        'Item Reqs': []
    }
    LaschamCove = {
        '$id': 2401,
        'Name': 'LaschamCove',
        'Previous Location Reachable': 'Yanchik Harbor',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    LakeshoreCampsite = {
        '$id': 2402,
        'Name': 'LakeshoreCampsite',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    HiddenHuntingCamp = {
        '$id': 2403,
        'Name': 'HiddenHuntingCamp',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    SingbreezeBough = {
        '$id': 2404,
        'Name': 'SingbreezeBough',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    TorigothArch = {
        '$id': 2405,
        'Name': 'TorigothArch',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    TitansRoar = {
        '$id': 2406,
        'Name': 'TitansRoar',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    LaschamPeninsula = {
        '$id': 2407,
        'Name': 'LaschamPeninsula',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    OrdiaGreatPlains = {
        '$id': 2408,
        'Name': 'OrdiaGreatPlains',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    SereneSpringside = {
        '$id': 2409,
        'Name': 'SereneSpringside',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    DuelistsBridge = {
        '$id': 2410,
        'Name': 'DuelistsBridge',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    WaysideRespite = {
        '$id': 2411,
        'Name': 'WaysideRespite',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    OutlookKnoll = {
        '$id': 2412,
        'Name': 'OutlookKnoll',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    LyanneMeadow = {
        '$id': 2413,
        'Name': 'LyanneMeadow',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    TorigothVillage = {
        '$id': 2414,
        'Name': 'TorigothVillage',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    TorigothCemetery = {
        '$id': 2415,
        'Name': 'TorigothCemetery',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    CoolleyLake = {
        '$id': 2416,
        'Name': 'CoolleyLake',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    HoaryWeald = {
        '$id': 2417,
        'Name': 'HoaryWeald',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    SeigleFell = {
        '$id': 2418,
        'Name': 'SeigleFell',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    DepthsofIgnorance = {
        '$id': 2419,
        'Name': 'DepthsofIgnorance',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    GrandarborsEmbrace = {
        '$id': 2420,
        'Name': 'GrandarborsEmbrace',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    NebleyWindCave = {
        '$id': 2421,
        'Name': 'NebleyWindCave',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    SaintsPracticeGrounds = {
        '$id': 2422,
        'Name': 'SaintsPracticeGrounds',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    HoaryWealdCamp = {
        '$id': 2423,
        'Name': 'HoaryWealdCamp',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    NoxPromontory = {
        '$id': 2424,
        'Name': 'NoxPromontory',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    ValafumHill = {
        '$id': 2425,
        'Name': 'ValafumHill',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    StrategyRoom = {
        '$id': 2426,
        'Name': 'StrategyRoom',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    CoolleyLakeCamp = {
        '$id': 2428,
        'Name': 'CoolleyLakeCamp',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [12],
        'Item Reqs': []
    }
    AlettaHarbor = {
        '$id': 2327,
        'Name': 'AlettaHarbor',
        'Previous Location Reachable': 'Lascham Cove',
        'Story Pre-Req': [24],
        'Item Reqs': []
    }
    AlettaMilitiaGarrison = {
        '$id': 2305,
        'Name': 'Aletta:MilitiaGarrison',
        'Previous Location Reachable': 'Aletta Harbor',
        'Story Pre-Req': [25],
        'Item Reqs': []
    }
    CavernoftheSeal = {
        '$id': 2308,
        'Name': 'CavernoftheSeal',
        'Previous Location Reachable': 'Aletta: Militia Garrison',
        'Story Pre-Req': [25],
        'Item Reqs': []
    }
    OssumMagnum = {
        '$id': 2309,
        'Name': 'OssumMagnum',
        'Previous Location Reachable': 'Aletta: Militia Garrison',
        'Story Pre-Req': [25],
        'Item Reqs': []
    }
    MillenniumGrotto = {
        '$id': 2313,
        'Name': 'MillenniumGrotto',
        'Previous Location Reachable': 'Aletta: Militia Garrison',
        'Story Pre-Req': [25],
        'Item Reqs': [SwordplayKey[:1], [JinAff[0]] , AegaeonKey, ComWaterKey, AegaeonAff]
    }
    WrackhamMoor = {
        '$id': 2322,
        'Name': 'WrackhamMoor',
        'Previous Location Reachable': 'Aletta: Militia Garrison',
        'Story Pre-Req': [25],
        'Item Reqs': []
    }
    TirkinCliffColony = {
        '$id': 2323,
        'Name': 'TirkinCliffColony',
        'Previous Location Reachable': 'Aletta: Militia Garrison',
        'Story Pre-Req': [25],
        'Item Reqs': []
    }
    LakeSarleigh = {
        '$id': 2324,
        'Name': 'LakeSarleigh',
        'Previous Location Reachable': 'Aletta: Militia Garrison',
        'Story Pre-Req': [25],
        'Item Reqs': []
    }
    BehemothsRoost = {
        '$id': 2325,
        'Name': 'BehemothsRoost',
        'Previous Location Reachable': 'Aletta: Militia Garrison',
        'Story Pre-Req': [25],
        'Item Reqs': []
    }
    AncientLakebed = {
        '$id': 2326,
        'Name': 'AncientLakebed',
        'Previous Location Reachable': 'Aletta: Militia Garrison',
        'Story Pre-Req': [25],
        'Item Reqs': []
    }
    LettBridge = {
        '$id': 2306,
        'Name': 'LettBridge',
        'Previous Location Reachable': 'Aletta: Militia Garrison',
        'Story Pre-Req': [28],
        'Item Reqs': []
    }
    OlnardsTrail = {
        '$id': 2328,
        'Name': 'OlnardsTrail',
        'Previous Location Reachable': 'Lett Bridge',
        'Story Pre-Req': [29],
        'Item Reqs': []
    }
    HyberVillage = {
        '$id': 2307,
        'Name': 'HyberVillage',
        'Previous Location Reachable': 'Olnards Trail',
        'Story Pre-Req': [33],
        'Item Reqs': []
    }
    TheGreatBreaksand = {
        '$id': 2310,
        'Name': 'TheGreatBreaksand',
        'Previous Location Reachable': 'Golden Twin Mesa',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    LoftinNaturePreserve = {
        '$id': 2311,
        'Name': 'LoftinNaturePreserve',
        'Previous Location Reachable': 'Dannagh Desert',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    HolyGateofAltana = {
        '$id': 2312,
        'Name': 'HolyGateofAltana',
        'Previous Location Reachable': 'Sacred Staircase',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    TurqosPlateau = {
        '$id': 2314,
        'Name': 'TurqosPlateau',
        'Previous Location Reachable': 'The Great Breaksand',
        'Story Pre-Req': [35],
        'Item Reqs': [SwordplayKey[:1], [JinAff[0]] , FortitudeKey[:1], JinAff[:1]]
    }
    TheBrayingCanyon = {
        '$id': 2329,
        'Name': 'TheBrayingCanyon',
        'Previous Location Reachable': 'Hyber Village',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    DannaghDesert = {
        '$id': 2330,
        'Name': 'DannaghDesert',
        'Previous Location Reachable': 'The Braying Canyon',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    StreamsandCorridor = {
        '$id': 2331,
        'Name': 'StreamsandCorridor',
        'Previous Location Reachable': 'Dannagh Desert',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    GoldenTwinMesa = {
        '$id': 2332,
        'Name': 'GoldenTwinMesa',
        'Previous Location Reachable': 'Dannagh Desert',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    VerdantFairylands = {
        '$id': 2333,
        'Name': 'VerdantFairylands',
        'Previous Location Reachable': 'Lake Wynn',
        'Story Pre-Req': [35],
        'Item Reqs': [AegaeonKey, ComWaterKey[:1], AegaeonAff[:1]]
    }
    PelnPilgrimsSpringland = {
        '$id': 2334,
        'Name': 'Peln,PilgrimsSpringland',
        'Previous Location Reachable': 'Dannagh Desert',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    LakeWynn = {
        '$id': 2335,
        'Name': 'LakeWynn',
        'Previous Location Reachable': 'Dannagh Desert',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    TitansUlcer = {
        '$id': 2336,
        'Name': 'TitansUlcer',
        'Previous Location Reachable': 'Dannagh Desert',
        'Story Pre-Req': [35],
        'Item Reqs': [HazeKey, ManipEtherKey, HazeAff[:2] , AegaeonKey, ComWaterKey, AegaeonAff]
    }
    OutridersForestTrail = {
        '$id': 2337,
        'Name': 'OutridersForestTrail',
        'Previous Location Reachable': 'Dannagh Desert',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    SacredStaircase = {
        '$id': 2338,
        'Name': 'SacredStaircase',
        'Previous Location Reachable': 'Dannagh Desert',
        'Story Pre-Req': [35],
        'Item Reqs': []
    }
    AurescoMainGate = {
        '$id': 2351,
        'Name': 'Auresco,MainGate',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    SpefanInn = {
        '$id': 2352,
        'Name': 'SpefanInn',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    AureusPalace = {
        '$id': 2353,
        'Name': 'AureusPalace',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    MedianGate = {
        '$id': 2354,
        'Name': 'MedianGate',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    AurescoRearGate = {
        '$id': 2355,
        'Name': 'Auresco,RearGate',
        'Previous Location Reachable': 'Orem Storage Ward',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    PlanusBridge = {
        '$id': 2356,
        'Name': 'PlanusBridge',
        'Previous Location Reachable': 'Outriders Forest Trail',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    FormideShoppingWard = {
        '$id': 2357,
        'Name': 'FormideShoppingWard',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    FabriIndustryWard = {
        '$id': 2358,
        'Name': 'FabriIndustryWard',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    AurescoResidentialWard = {
        '$id': 2359,
        'Name': 'AurescoResidentialWard',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    AcheronBackstreet = {
        '$id': 2360,
        'Name': 'AcheronBackstreet',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    SachsumGardens = {
        '$id': 2361,
        'Name': 'SachsumGardens',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    AquilaWatchtower = {
        '$id': 2362,
        'Name': 'AquilaWatchtower',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    OremStorageWard = {
        '$id': 2363,
        'Name': 'OremStorageWard',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    PischatorBridge = {
        '$id': 2364,
        'Name': 'PischatorBridge',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    ViridianGate = {
        '$id': 2366,
        'Name': 'ViridianGate',
        'Previous Location Reachable': 'Planus Bridge',
        'Story Pre-Req': [36],
        'Item Reqs': []
    }
    TornasWomb = {
        '$id': 2365,
        'Name': 'TornasWomb',
        'Previous Location Reachable': 'Auresco, Rear Gate',
        'Story Pre-Req': [46],
        'Item Reqs': []
    }
    BalaurDarkZone1 = {
        '$id': 2339,
        'Name': 'Balaur,DarkZone#1',
        'Previous Location Reachable': 'Hall of Worship',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    FernyigesDarkZone2 = {
        '$id': 2340,
        'Name': 'Fernyiges,DarkZone#2',
        'Previous Location Reachable': 'Crooked Tower',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    SkygateEntrance = {
        '$id': 2341,
        'Name': 'SkygateEntrance',
        'Previous Location Reachable': 'Pulsating Passage',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    ZirnitraDarkZone3 = {
        '$id': 2342,
        'Name': 'Zirnitra,DarkZone#3',
        'Previous Location Reachable': 'Pantarhei Tower',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    TheSoaringRostrum = {
        '$id': 2343,
        'Name': 'TheSoaringRostrum',
        'Previous Location Reachable': 'Skygate, Endless Road',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    PedestalofStargazing = {
        '$id': 2344,
        'Name': 'PedestalofStargazing',
        'Previous Location Reachable': 'Hermits Alleyway',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    HallofWorship = {
        '$id': 2345,
        'Name': 'HallofWorship',
        'Previous Location Reachable': 'Holy Gate of Altana',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    CrookedTower = {
        '$id': 2346,
        'Name': 'CrookedTower',
        'Previous Location Reachable': 'Balaur, Dark Zone #1',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    PantarheiTower = {
        '$id': 2347,
        'Name': 'PantarheiTower',
        'Previous Location Reachable': 'Fernyiges, Dark Zone #2',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    PulsatingPassage = {
        '$id': 2348,
        'Name': 'PulsatingPassage',
        'Previous Location Reachable': 'Zirnitra, Dark Zone #3',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    HermitsAlleyway = {
        '$id': 2349,
        'Name': 'HermitsAlleyway',
        'Previous Location Reachable': 'Pulsating Passage',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    SkygateEndlessRoad = {
        '$id': 2350,
        'Name': 'Skygate,EndlessRoad',
        'Previous Location Reachable': 'Pulsating Passage',
        'Story Pre-Req': [53],
        'Item Reqs': []
    }
    TastelessAltar = {
        '$id': 2368,
        'Name': 'TastelessAltar',
        'Previous Location Reachable': 'Cavern of the Seal',
        'Story Pre-Req': [25],
        'Item Reqs': TornaSlatePieceIDs
    }
     
    TornaAreaDict = [LasariaWoodland, PortonVillage, SecludedBoneway, HangnailCrossing, HaraddHills, CropwoodsofYorn, MernesFalls, FeltleyVillage, GreatCrater, UccarsTrail, YanchikHarbor, LaschamCove, LakeshoreCampsite, HiddenHuntingCamp, SingbreezeBough, TorigothArch, TitansRoar, LaschamPeninsula, OrdiaGreatPlains, SereneSpringside, DuelistsBridge, WaysideRespite, OutlookKnoll, LyanneMeadow, TorigothVillage, TorigothCemetery, CoolleyLake, HoaryWeald, SeigleFell, DepthsofIgnorance, GrandarborsEmbrace, NebleyWindCave, SaintsPracticeGrounds, HoaryWealdCamp, NoxPromontory, ValafumHill, StrategyRoom, CoolleyLakeCamp, AlettaHarbor, AlettaMilitiaGarrison, CavernoftheSeal, OssumMagnum, MillenniumGrotto, WrackhamMoor, TirkinCliffColony, LakeSarleigh, BehemothsRoost, AncientLakebed, LettBridge, OlnardsTrail, HyberVillage, TheGreatBreaksand, LoftinNaturePreserve, HolyGateofAltana, TurqosPlateau, TheBrayingCanyon, DannaghDesert, StreamsandCorridor, GoldenTwinMesa, VerdantFairylands, PelnPilgrimsSpringland, LakeWynn, TitansUlcer, OutridersForestTrail, SacredStaircase, AurescoMainGate, SpefanInn, AureusPalace, MedianGate, AurescoRearGate, PlanusBridge, FormideShoppingWard, FabriIndustryWard, AurescoResidentialWard, AcheronBackstreet, SachsumGardens, AquilaWatchtower, OremStorageWard, PischatorBridge, ViridianGate, TornasWomb, BalaurDarkZone1, FernyigesDarkZone2, SkygateEntrance, ZirnitraDarkZone3, TheSoaringRostrum, PedestalofStargazing, HallofWorship, CrookedTower, PantarheiTower, PulsatingPassage, HermitsAlleyway, SkygateEndlessRoad, TastelessAltar]
    
    global TornaAreas
    TornaAreas = []

    for area in TornaAreaDict:
        TornaArea(area, TornaAreas)

    for area in TornaAreas:
        if area.mainreq != []:
            area.itemreqs.extend(Mainquests[area.mainreq[0]].itemreqs) # adds main story req
            area.itemreqs = Helper.MultiLevelListToSingleLevelList(area.itemreqs)
            area.itemreqs = list(set(area.itemreqs))
            area.itemreqs.sort()
    return TornaAreas