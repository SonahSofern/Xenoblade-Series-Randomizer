from scripts import Helper, JSONParser, PopupDescriptions
import json
import random
from IDs import *

class TornaEnemyNormalDrops: # created to allow me to pass these objects easier
    def __init__(self, input, addtolist, rewardnumber, EnemyDropCounter):
        self.id = input["$id"]
        self.name = input["Name"]
        self.nearloc = input['Location Near']
        self.level = input["Level"]
        self.mainreq = input['Story Pre-Req'][0]
        self.duringquest = input["During Quest"]
        self.sideprereq = input['Quest Completion Pre-Req']
        self.itemreqs = Helper.MultiLevelListToSingleLevelList(input['Required Items'])
        self.summonedby = input['Summoned By']
        self.droptableids = [EnemyDropCounter]
        self.randomizeditems = Helper.ExtendListtoLength(Helper.ExtendListtoLength([], max(rewardnumber - 1, 0), "-1"), 8, "0") # holds ids, -1 for progression, 0 for filler spots
        if rewardnumber > 0:
            self.hasprogression = True
            self.randomizeditems = Helper.ExtendListtoLength(self.randomizeditems, 9, "-1")
        else:
            self.hasprogression = False
            self.randomizeditems = Helper.ExtendListtoLength(self.randomizeditems, 9, "0")
        addtolist.append(self)

def AdjustEnemyRequirements(Sidequests, Mainquests, Areas, DropQty): # the enemy requirements may change depending on the logic of which quests get rolled
    
    RagingVolff = {
		'$id': 1428,
		'Name': 'Raging Volff',
		'Location Near': 2315,
		'Level': 1,
		'Story Pre-Req': [1],
		'During Quest': [],
		'Quest Completion Pre-Req': [],
		'Summoned By': [],
		'Required Items': [],
		'Enemy Drop Table IDs': []
	}
    JubelFeris = {
        '$id': 1429,
        'Name': 'Jubel Feris',
        'Location Near': 2315,
        'Level': 2,
        'Story Pre-Req': [1],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    CursedBuloofoA = {
        '$id': 1430,
        'Name': 'Cursed Buloofo A',
        'Location Near': 2315,
        'Level': 2,
        'Story Pre-Req': [1],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    GargoyleA = {
        '$id': 1431,
        'Name': 'Gargoyle A',
        'Location Near': 2318,
        'Level': 8,
        'Story Pre-Req': [7],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    Addam = {
        '$id': 1432,
        'Name': 'Addam',
        'Location Near': 2318,
        'Level': 10,
        'Story Pre-Req': [8],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    Mythra = {
        '$id': 1433,
        'Name': 'Mythra',
        'Location Near': 2318,
        'Level': 10,
        'Story Pre-Req': [8],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [],
    }
    Brighid = {
        '$id': 1434,
        'Name': 'Brighid',
        'Location Near': 2415,
        'Level': 14,
        'Story Pre-Req': [16],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    ArdainianScoutA = {
        '$id': 1435,
        'Name': 'Ardainian Scout A',
        'Location Near': 2415,
        'Level': 10,
        'Story Pre-Req': [16],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    ArdainianScoutB = {
        '$id': 1436,
        'Name': 'Ardainian Scout B',
        'Location Near': 2415,
        'Level': 11,
        'Story Pre-Req': [16],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    GortA = {
        '$id': 1437,
        'Name': 'Gort A',
        'Location Near': 2415,
        'Level': 20,
        'Story Pre-Req': [19],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    AntipatheticArchibald = {
        '$id': 1438,
        'Name': 'Antipathetic Archibald',
        'Location Near': 2415,
        'Level': 16,
        'Story Pre-Req': [19],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    ScurvyCurtis = {
        '$id': 1439,
        'Name': 'Scurvy Curtis',
        'Location Near': 2415,
        'Level': 17,
        'Story Pre-Req': [19],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    InsufferableUlysses = {
        '$id': 1440,
        'Name': 'Insufferable Ulysses',
        'Location Near': 2415,
        'Level': 18,
        'Story Pre-Req': [19],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    #SlitheJagronA = { # this enemy technically can't be killed, the loot table can get smashed out of it I think. regardless, removing it from the pool
    #    '$id': 1441,
    #    'Name': 'Slithe Jagron A',
    #    'Location Near': 2328,
    #    'Level': 29,
    #    'Story Pre-Req': [30],
    #    'During Quest': [],
    #    'Quest Completion Pre-Req': [],
    #    'Summoned By': [],
    #    'Required Items': [],
    #    'Enemy Drop Table IDs': []
    #}
    SlitheJagronB = {
        '$id': 1442,
        'Name': 'Slithe Jagron B',
        'Location Near': 2328,
        'Level': 29,
        'Story Pre-Req': [31],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    MalosA = {
        '$id': 1443,
        'Name': 'Malos A',
        'Location Near': 2353,
        'Level': 40,
        'Story Pre-Req': [44],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    GargoyleD = {
        '$id': 1444,
        'Name': 'Gargoyle D',
        'Location Near': 2353,
        'Level': 38,
        'Story Pre-Req': [44],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    ArtificeColossus = {
        '$id': 1445,
        'Name': 'Artifice Colossus',
        'Location Near': 2343,
        'Level': 48,
        'Story Pre-Req': [55],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    MalosB = {
        '$id': 1446,
        'Name': 'Malos B',
        'Location Near': 2343,
        'Level': 50,
        'Story Pre-Req': [55],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    MalosC = {
        '$id': 1447,
        'Name': 'Malos C',
        'Location Near': 2343,
        'Level': 50,
        'Story Pre-Req': [56],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    GortB = {
        '$id': 1448,
        'Name': 'Gort B',
        'Location Near': 2343,
        'Level': 53,
        'Story Pre-Req': [57],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    ArtificeSirenA = {
        '$id': 1449,
        'Name': 'Artifice Siren A',
        'Location Near': 2343,
        'Level': 50,
        'Story Pre-Req': [55],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    ArtificeSirenB = {
        '$id': 1450,
        'Name': 'Artifice Siren B',
        'Location Near': 2343,
        'Level': 50,
        'Story Pre-Req': [56],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    CursedBuloofoB = {
        '$id': 1454,
        'Name': 'Cursed Buloofo B',
        'Location Near': 2315,
        'Level': 3,
        'Story Pre-Req': [1],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    VanadiumTirkin = {
        '$id': 1455,
        'Name': 'Vanadium Tirkin',
        'Location Near': 2332,
        'Level': 31,
        'Story Pre-Req': [0],
        'During Quest': [33],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    SorgusTirkin = {
        '$id': 1456,
        'Name': 'Sorgus Tirkin',
        'Location Near': 2332,
        'Level': 30,
        'Story Pre-Req': [0],
        'During Quest': [33],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    LeractGogol = {
        '$id': 1457,
        'Name': 'Leract Gogol',
        'Location Near': 2334,
        'Level': 32,
        'Story Pre-Req': [0],
        'During Quest': [32],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    HewliGogol = {
        '$id': 1458,
        'Name': 'Hewli Gogol',
        'Location Near': 2330,
        'Level': 35,
        'Story Pre-Req': [0],
        'During Quest': [32],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    MarrithAntol = {
        '$id': 1459,
        'Name': 'Marrith Antol',
        'Location Near': 2317,
        'Level': 38,
        'Story Pre-Req': [0],
        'During Quest': [37],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    IncubFlier = {
        '$id': 1460,
        'Name': 'Incub Flier',
        'Location Near': 2317,
        'Level': 39,
        'Story Pre-Req': [0],
        'During Quest': [37],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    PradoCaterpile = {
        '$id': 1461,
        'Name': 'Prado Caterpile',
        'Location Near': 2317,
        'Level': 39,
        'Story Pre-Req': [0],
        'During Quest': [37],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    AppetBrog = {
        '$id': 1462,
        'Name': 'Appet Brog',
        'Location Near': 2428,
        'Level': 35,
        'Story Pre-Req': [0],
        'During Quest': [53],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    DurallBuloofo = {
        '$id': 1463,
        'Name': 'Durall Buloofo',
        'Location Near': 2410,
        'Level': 37,
        'Story Pre-Req': [0],
        'During Quest': [40],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    InnocentVolff = {
        '$id': 1464,
        'Name': 'Innocent Volff',
        'Location Near': 2410,
        'Level': 36,
        'Story Pre-Req': [0],
        'During Quest': [40],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    LoweBlant = {
        '$id': 1465,
        'Name': 'Lowe Blant',
        'Location Near': 2314,
        'Level': 42,
        'Story Pre-Req': [0],
        'During Quest': [48],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    TizzaParisax = {
        '$id': 1466,
        'Name': 'Tizza Parisax',
        'Location Near': 2329,
        'Level': 38,
        'Story Pre-Req': [0],
        'During Quest': [54],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    IndignantJerry = {
        '$id': 1467,
        'Name': 'Indignant Jerry',
        'Location Near': 2357,
        'Level': 46,
        'Story Pre-Req': [0],
        'During Quest': [56],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    GraftonFeris = {
        '$id': 1468,
        'Name': 'Grafton Feris',
        'Location Near': 2325,
        'Level': 35,
        'Story Pre-Req': [0],
        'During Quest': [20],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    ConspiratorMacNeth = {
        '$id': 1469,
        'Name': 'Conspirator MacNeth',
        'Location Near': 2307,
        'Level': 40,
        'Story Pre-Req': [0],
        'During Quest': [38],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    WanderingUrchon = {
        '$id': 1470,
        'Name': 'Wandering Urchon',
        'Location Near': 2327,
        'Level': 37,
        'Story Pre-Req': [0],
        'During Quest': [24],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    WanderingRopl = {
        '$id': 1471,
        'Name': 'Wandering Ropl',
        'Location Near': 2327,
        'Level': 39,
        'Story Pre-Req': [0],
        'During Quest': [24],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    WanderingLaia = {
        '$id': 1472,
        'Name': 'Wandering Laia',
        'Location Near': 2327,
        'Level': 41,
        'Story Pre-Req': [0],
        'During Quest': [24],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    TimidVolff = {
        '$id': 1473,
        'Name': 'Timid Volff',
        'Location Near': 2318,
        'Level': 9,
        'Story Pre-Req': [0],
        'During Quest': [2],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    PickerBuloofo = {
        '$id': 1474,
        'Name': 'Picker Buloofo',
        'Location Near': 2318,
        'Level': 10,
        'Story Pre-Req': [0],
        'During Quest': [2],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    ElegiacMercenary = {
        '$id': 1476,
        'Name': 'Elegiac Mercenary',
        'Location Near': 2358,
        'Level': 52,
        'Story Pre-Req': [0],
        'During Quest': [5],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    HalcyonMercenary = {
        '$id': 1477,
        'Name': 'Halcyon Mercenary',
        'Location Near': 2358,
        'Level': 52,
        'Story Pre-Req': [0],
        'During Quest': [5],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    ChatteringSkeeter = {
        '$id': 1479,
        'Name': 'Chattering Skeeter',
        'Location Near': 2423,
        'Level': 41,
        'Story Pre-Req': [0],
        'During Quest': [39],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    TacitusUrchon = {
        '$id': 1482,
        'Name': 'Tacitus Urchon',
        'Location Near': 2401,
        'Level': 20,
        'Story Pre-Req': [0],
        'During Quest': [13],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    GloomyAspar = {
        '$id': 1483,
        'Name': 'Gloomy Aspar',
        'Location Near': 2409,
        'Level': 18,
        'Story Pre-Req': [0],
        'During Quest': [15],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    WhistlingBathein = {
        '$id': 1484,
        'Name': 'Whistling Bathein',
        'Location Near': 2401,
        'Level': 19,
        'Story Pre-Req': [0],
        'During Quest': [11],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    PreoccupiedGogol = {
        '$id': 1485,
        'Name': 'Preoccupied Gogol',
        'Location Near': 2306,
        'Level': 24,
        'Story Pre-Req': [0],
        'During Quest': [22],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    TenaxEkidno = {
        '$id': 1486,
        'Name': 'Tenax Ekidno',
        'Location Near': 2365,
        'Level': 50,
        'Story Pre-Req': [0],
        'During Quest': [51],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    CalculatingGogol = {
        '$id': 1487,
        'Name': 'Calculating Gogol',
        'Location Near': 2356,
        'Level': 37,
        'Story Pre-Req': [0],
        'During Quest': [46],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    ElectGogol = {
        '$id': 1488,
        'Name': 'Elect Gogol',
        'Location Near': 2356,
        'Level': 39,
        'Story Pre-Req': [0],
        'During Quest': [46],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    CloudArachno = {
        '$id': 1489,
        'Name': 'Cloud Arachno',
        'Location Near': 2320,
        'Level': 10,
        'Story Pre-Req': [0],
        'During Quest': [1],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    DispareRopl = {
        '$id': 1490,
        'Name': 'Dispare Ropl',
        'Location Near': 2425,
        'Level': 16,
        'Story Pre-Req': [0],
        'During Quest': [8],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    CreefGriffox = {
        '$id': 1491,
        'Name': 'Creef Griffox',
        'Location Near': 2315,
        'Level': 43,
        'Story Pre-Req': [0],
        'During Quest': [41],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    EvokeBunnit = {
        '$id': 1496,
        'Name': 'Evoke Bunnit',
        'Location Near': 2417,
        'Level': 38,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [372, 492]
    }
    ForayBunnit = {
        '$id': 1497,
        'Name': 'Foray Bunnit',
        'Location Near': 2417,
        'Level': 40,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [373, 492]
    }
    NoggleBunnit = {
        '$id': 1498,
        'Name': 'Noggle Bunnit',
        'Location Near': 2408,
        'Level': 12,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [310, 492]
    }
    PinchBunnit = {
        '$id': 1499,
        'Name': 'Pinch Bunnit',
        'Location Near': 2408,
        'Level': 14,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [315, 492]
    }
    FirmVolff = {
        '$id': 1500,
        'Name': 'Firm Volff',
        'Location Near': 2425,
        'Level': 16,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [313, 485]
    }
    GeminiVolff = {
        '$id': 1501,
        'Name': 'Gemini Volff',
        'Location Near': 2425,
        'Level': 10,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [304, 485]
    }
    EspinaFeris = {
        '$id': 1502,
        'Name': 'Espina Feris',
        'Location Near': 2408,
        'Level': 12,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [312, 486]
    }
    LekutFeris = {
        '$id': 1503,
        'Name': 'Lekut Feris',
        'Location Near': 2408,
        'Level': 8,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [300, 486]
    }
    RinkerEks = {
        '$id': 1507,
        'Name': 'Rinker Eks',
        'Location Near': 2408,
        'Level': 11,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [305, 499]
    }
    DominalFlamii = {
        '$id': 1512,
        'Name': 'Dominal Flamii',
        'Location Near': 2413,
        'Level': 15,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [310, 494]
    }
    IngleCamill = {
        '$id': 1515,
        'Name': 'Ingle Camill',
        'Location Near': 2408,
        'Level': 11,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [306, 500]
    }
    GrayBuloofo = {
        '$id': 1516,
        'Name': 'Gray Buloofo',
        'Location Near': 2417,
        'Level': 41,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [387, 488]
    }
    ImbaLizard = {
        '$id': 1518,
        'Name': 'Imba Lizard',
        'Location Near': 2416,
        'Level': 32,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [347]
    }
    CelsarsTaos = {
        '$id': 1519,
        'Name': 'Celsars Taos',
        'Location Near': 2413,
        'Level': 15,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [318]
    }
    DreadCaterpileSummon = {
        '$id': 1521,
        'Name': 'Dread Caterpile (Summon)',
        'Location Near': 2417,
        'Level': 36,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [1516],
        'Required Items': [],
        'Enemy Drop Table IDs': []
    }
    KanooSkwaror = {
        '$id': 1522,
        'Name': 'Kanoo Skwaror',
        'Location Near': 2413,
        'Level': 12,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [311]
    }
    DreadCaterpileNormal = {
        '$id': 1526,
        'Name': 'Dread Caterpile (Normal)',
        'Location Near': 2425,
        'Level': 26,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [337]
    }
    MyrrhesCrustip = {
        '$id': 1527,
        'Name': 'Myrrhes Crustip',
        'Location Near': 2409,
        'Level': 34,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [353]
    }
    ArrahRhogul = {
        '$id': 1528,
        'Name': 'Arrah Rhogul',
        'Location Near': 2413,
        'Level': 14,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [312, 490]
    }
    BohnQuadwing = {
        '$id': 1529,
        'Name': 'Bohn Quadwing',
        'Location Near': 2404,
        'Level': 11,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [307]
    }
    HighbohnQuadwing = {
        '$id': 1530,
        'Name': 'Highbohn Quadwing',
        'Location Near': 2404,
        'Level': 15,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [314]
    }
    LapisVang = {
        '$id': 1531,
        'Name': 'Lapis Vang',
        'Location Near': 2410,
        'Level': 36,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [380]
    }
    ErsSkeeter = {
        '$id': 1532,
        'Name': 'Ers Skeeter',
        'Location Near': 2408,
        'Level': 12,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [310]
    }
    AstorFlier = {
        '$id': 1533,
        'Name': 'Astor Flier',
        'Location Near': 2425,
        'Level': 34,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [1547],
        'Required Items': [],
        'Enemy Drop Table IDs': [382, 495]
    }
    CascadeKrabble = {
        '$id': 1534,
        'Name': 'Cascade Krabble',
        'Location Near': 2407,
        'Level': 12,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [311, 501]
    }
    KastKrabble = {
        '$id': 1535,
        'Name': 'Kast Krabble',
        'Location Near': 2416,
        'Level': 30,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [354, 501]
    }
    ReedPiranhax = {
        '$id': 1536,
        'Name': 'Reed Piranhax',
        'Location Near': 2409,
        'Level': 13,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [312, 487]
    }
    MaramalPiranhax = {
        '$id': 1537,
        'Name': 'Maramal Piranhax',
        'Location Near': 2416,
        'Level': 32,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [348, 487]
    }
    KeatTirkin = {
        '$id': 1539,
        'Name': 'Keat Tirkin',
        'Location Near': 2422,
        'Level': 38,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [360, 496]
    }
    GradsTirkin = {
        '$id': 1540,
        'Name': 'Grads Tirkin',
        'Location Near': 2422,
        'Level': 37,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [361]
    }
    VabraTirkin = {
        '$id': 1542,
        'Name': 'Vabra Tirkin',
        'Location Near': 2422,
        'Level': 38,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [364, 497]
    }
    EpistoTirkin = {
        '$id': 1544,
        'Name': 'Episto Tirkin',
        'Location Near': 2422,
        'Level': 36,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [366, 497]
    }
    DerrahTirkin = {
        '$id': 1545,
        'Name': 'Derrah Tirkin',
        'Location Near': 2422,
        'Level': 35,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [367]
    }
    XanePippito = {
        '$id': 1546,
        'Name': 'Xane Pippito',
        'Location Near': 2418,
        'Level': 38,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [368]
    }
    CooraNest = {
        '$id': 1547,
        'Name': 'Coora Nest',
        'Location Near': 2425,
        'Level': 36,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [355, 489]
    }
    GneoRopl = {
        '$id': 1548,
        'Name': 'Gneo Ropl',
        'Location Near': 2425,
        'Level': 33,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [355]
    }
    FersGrebel = {
        '$id': 1549,
        'Name': 'Fers Grebel',
        'Location Near': 2408,
        'Level': 9,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [302]
    }
    HighscreebQuadwing = {
        '$id': 1550,
        'Name': 'Highscreeb Quadwing',
        'Location Near': 2417,
        'Level': 39,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [381]
    }
    ScriboQuadwing = {
        '$id': 1551,
        'Name': 'Scribo Quadwing',
        'Location Near': 2417,
        'Level': 40,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [383]
    }
    HerculeanGibson = {
        '$id': 1559,
        'Name': 'Herculean Gibson',
        'Location Near': 2322,
        'Level': 75,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [26192],
        'Enemy Drop Table IDs': [481]
    }
    HurricaneAnise = {
        '$id': 1560,
        'Name': 'Hurricane Anise',
        'Location Near': 2344,
        'Level': 100,
        'Story Pre-Req': [53],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [26193],
        'Enemy Drop Table IDs': [482]
    }
    MesmerTlaloc = {
        '$id': 1561,
        'Name': 'Mesmer Tlaloc',
        'Location Near': 2331,
        'Level': 85,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [26194],
        'Enemy Drop Table IDs': [483]
    }
    SentinelCarpathia = {
        '$id': 1562,
        'Name': 'Sentinel Carpathia',
        'Location Near': 2319,
        'Level': 65,
        'Story Pre-Req': [8],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [26195],
        'Enemy Drop Table IDs': [484]
    }
    RavineBunnit = {
        '$id': 1563,
        'Name': 'Ravine Bunnit',
        'Location Near': 2417,
        'Level': 50,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [465]
    }
    ErraticGoliante = {
        '$id': 1564,
        'Name': 'Erratic Goliante',
        'Location Near': 2422,
        'Level': 45,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [466]
    }
    HandwringingBigelow = {
        '$id': 1566,
        'Name': 'Handwringing Bigelow',
        'Location Near': 2409,
        'Level': 25,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [467]
    }
    OveraffectionateMurph = {
        '$id': 1567,
        'Name': 'Overaffectionate Murph',
        'Location Near': 2408,
        'Level': 18,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [468]
    }
    SpillitUrchon = {
        '$id': 1568,
        'Name': 'Spillit Urchon',
        'Location Near': 2319,
        'Level': 60,
        'Story Pre-Req': [8],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [1562],
        'Required Items': [26195],
        'Enemy Drop Table IDs': []
    }
    ApostleRhogul = {
        '$id': 1569,
        'Name': 'Apostle Rhogul',
        'Location Near': 2344,
        'Level': 99,
        'Story Pre-Req': [53],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [1560],
        'Required Items': [26193],
        'Enemy Drop Table IDs': []
    }
    SteekyHox = {
        '$id': 1570,
        'Name': 'Steeky Hox',
        'Location Near': 2317,
        'Level': 4,
        'Story Pre-Req': [5],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [303]
    }
    RalshVolff = {
        '$id': 1571,
        'Name': 'Ralsh Volff',
        'Location Near': 2315,
        'Level': 3,
        'Story Pre-Req': [1],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [298, 485]
    }
    SowlFeris = {
        '$id': 1573,
        'Name': 'Sowl Feris',
        'Location Near': 2322,
        'Level': 21,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [329, 486]
    }
    UrbsArmuA = {
        '$id': 1574,
        'Name': 'Urbs Armu A',
        'Location Near': 2322,
        'Level': 18,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [319, 23]
    }
    AureaArdun = {
        '$id': 1575,
        'Name': 'Aurea Ardun',
        'Location Near': 2322,
        'Level': 20,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [323]
    }
    SladeEks = {
        '$id': 1576,
        'Name': 'Slade Eks',
        'Location Near': 2322,
        'Level': 18,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [320, 499]
    }
    LibelteFlamii = {
        '$id': 1577,
        'Name': 'Libelte Flamii',
        'Location Near': 2326,
        'Level': 26,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [338, 494]
    }
    LefthFlamii = {
        '$id': 1578,
        'Name': 'Lefth Flamii',
        'Location Near': 2317,
        'Level': 4,
        'Story Pre-Req': [5],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [299, 494]
    }
    MarnaGaraffa = {
        '$id': 1579,
        'Name': 'Marna Garaffa',
        'Location Near': 2311,
        'Level': 40,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [375]
    }
    NemusCamill = {
        '$id': 1580,
        'Name': 'Nemus Camill',
        'Location Near': 2318,
        'Level': 6,
        'Story Pre-Req': [5],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [300, 500]
    }
    AstleEllook = {
        '$id': 1581,
        'Name': 'Astle Ellook',
        'Location Near': 2311,
        'Level': 40,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [376]
    }
    FaneBuloofo = {
        '$id': 1582,
        'Name': 'Fane Buloofo',
        'Location Near': 2315,
        'Level': 4,
        'Story Pre-Req': [1],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [301, 488]
    }
    VokkonGriffox = {
        '$id': 1583,
        'Name': 'Vokkon Griffox',
        'Location Near': 2330,
        'Level': 32,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [349]
    }
    TelahRiik = {
        '$id': 1585,
        'Name': 'Telah Riik',
        'Location Near': 2328,
        'Level': 23,
        'Story Pre-Req': [29],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [332]
    }
    WhispUpa = {
        '$id': 1587,
        'Name': 'Whisp Upa',
        'Location Near': 2301,
        'Level': 3,
        'Story Pre-Req': [2],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [302]
    }
    BebthUpa = {
        '$id': 1588,
        'Name': 'Bebth Upa',
        'Location Near': 2321,
        'Level': 9,
        'Story Pre-Req': [5],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [303]
    }
    OoneEkidno = {
        '$id': 1589,
        'Name': 'Oone Ekidno',
        'Location Near': 2335,
        'Level': 43,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [389]
    }
    ClocheRapchor = {
        '$id': 1590,
        'Name': 'Cloche Rapchor',
        'Location Near': 2322,
        'Level': 19,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [324]
    }
    NobleAspar = {
        '$id': 1591,
        'Name': 'Noble Aspar',
        'Location Near': 2408,
        'Level': 13,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [310, 493]
    }
    TretsAspar = {
        '$id': 1592,
        'Name': 'Trets Aspar',
        'Location Near': 2330,
        'Level': 38,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [364, 493]
    }
    SurveeAntol = {
        '$id': 1593,
        'Name': 'Survee Antol',
        'Location Near': 2310,
        'Level': 32,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [1635],
        'Required Items': [],
        'Enemy Drop Table IDs': [350]
    }
    GreetzAntol = {
        '$id': 1594,
        'Name': 'Greetz Antol',
        'Location Near': 2310,
        'Level': 36,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [358]
    }
    CheltaCaterpileLasaria = {
        '$id': 1595,
        'Name': 'Chelta Caterpile (Lasaria)',
        'Location Near': 2317,
        'Level': 5,
        'Story Pre-Req': [5],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [298]
    }
    CaliberScorpox = {
        '$id': 1596,
        'Name': 'Caliber Scorpox',
        'Location Near': 2317,
        'Level': 6,
        'Story Pre-Req': [5],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [299]
    }
    ZafirahCrustip = {
        '$id': 1598,
        'Name': 'Zafirah Crustip',
        'Location Near': 2331,
        'Level': 38,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [365]
    }
    YouseParisax = {
        '$id': 1599,
        'Name': 'Youse Parisax',
        'Location Near': 2347,
        'Level': 39,
        'Story Pre-Req': [53],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [1630],
        'Required Items': [],
        'Enemy Drop Table IDs': [384]
    }
    UisParisax = {
        '$id': 1600,
        'Name': 'Uis Parisax',
        'Location Near': 2347,
        'Level': 43,
        'Story Pre-Req': [53],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [390]
    }
    LegginParisax = {
        '$id': 1601,
        'Name': 'Leggin Parisax',
        'Location Near': 2347,
        'Level': 45,
        'Story Pre-Req': [53],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [391]
    }
    BurranGyanna = {
        '$id': 1602,
        'Name': 'Burran Gyanna',
        'Location Near': 2326,
        'Level': 23,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [333]
    }
    SalshRhogul = {
        '$id': 1604,
        'Name': 'Salsh Rhogul',
        'Location Near': 2317,
        'Level': 5,
        'Story Pre-Req': [5],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [301, 490]
    }
    TonbreRhogul = {
        '$id': 1605,
        'Name': 'Tonbre Rhogul',
        'Location Near': 2329,
        'Level': 28,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [341, 490]
    }
    AnbuVang = {
        '$id': 1607,
        'Name': 'Anbu Vang',
        'Location Near': 2309,
        'Level': 21,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [330]
    }
    LapseFlier = {
        '$id': 1608,
        'Name': 'Lapse Flier',
        'Location Near': 2301,
        'Level': 4,
        'Story Pre-Req': [2],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [302, 495]
    }
    KlaretWisp = {
        '$id': 1609,
        'Name': 'Klaret Wisp',
        'Location Near': 2330,
        'Level': 33,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [356]
    }
    RegusMoramora = {
        '$id': 1610,
        'Name': 'Regus Moramora',
        'Location Near': 2326,
        'Level': 32,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [351, 498]
    }
    TwondusAspid = {
        '$id': 1611,
        'Name': 'Twondus Aspid',
        'Location Near': 2347,
        'Level': 48,
        'Story Pre-Req': [53],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [392]
    }
    PhantomMedooz = {
        '$id': 1612,
        'Name': 'Phantom Medooz',
        'Location Near': 2347,
        'Level': 40,
        'Story Pre-Req': [53],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [378]
    }
    BiblisPuffot = {
        '$id': 1613,
        'Name': 'Biblis Puffot',
        'Location Near': 2322,
        'Level': 20,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [325]
    }
    RobalKrabble = {
        '$id': 1614,
        'Name': 'Robal Krabble',
        'Location Near': 2326,
        'Level': 23,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [334, 501]
    }
    RibageGrady = {
        '$id': 1616,
        'Name': 'Ribage Grady',
        'Location Near': 2317,
        'Level': 30,
        'Story Pre-Req': [5],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [347, 487]
    }
    SarchessGrady = {
        '$id': 1617,
        'Name': 'Sarchess Grady',
        'Location Near': 2321,
        'Level': 10,
        'Story Pre-Req': [5],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [306, 487]
    }
    LegarreMarrin = {
        '$id': 1618,
        'Name': 'Legarre Marrin',
        'Location Near': 2310,
        'Level': 42,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [379, 491]
    }
    ArloKapiba = {
        '$id': 1619,
        'Name': 'Arlo Kapiba',
        'Location Near': 2316,
        'Level': 3,
        'Story Pre-Req': [5],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [303]
    }
    RooseBlant = {
        '$id': 1621,
        'Name': 'Roose Blant',
        'Location Near': 2314,
        'Level': 38,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [367]
    }
    DrothUrchon = {
        '$id': 1622,
        'Name': 'Droth Urchon',
        'Location Near': 2314,
        'Level': 36,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [359]
    }
    TeppusPippito = {
        '$id': 1623,
        'Name': 'Teppus Pippito',
        'Location Near': 2331,
        'Level': 25,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [346]
    }
    ArcahPippito = {
        '$id': 1624,
        'Name': 'Arcah Pippito',
        'Location Near': 2343,
        'Level': 51,
        'Story Pre-Req': [53],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [385, 401]
    }
    TyphonTirkin = {
        '$id': 1625,
        'Name': 'Typhon Tirkin',
        'Location Near': 2323,
        'Level': 21,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [331, 496]
    }
    GratTirkin = {
        '$id': 1626,
        'Name': 'Grat Tirkin',
        'Location Near': 2323,
        'Level': 20,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [326]
    }
    CardineTirkin = {
        '$id': 1627,
        'Name': 'Cardine Tirkin',
        'Location Near': 2323,
        'Level': 19,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [327, 497]
    }
    ParoleTirkin = {
        '$id': 1628,
        'Name': 'Parole Tirkin',
        'Location Near': 2323,
        'Level': 19,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [322]
    }
    SomeliaNest = {
        '$id': 1629,
        'Name': 'Somelia Nest',
        'Location Near': 2328,
        'Level': 21,
        'Story Pre-Req': [29],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [329, 489]
    }
    PsitEgg = {
        '$id': 1630,
        'Name': 'Psit Egg',
        'Location Near': 2347,
        'Level': 43,
        'Story Pre-Req': [53],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [386]
    }
    VictorTotem = {
        '$id': 1631,
        'Name': 'Victor Totem',
        'Location Near': 2323,
        'Level': 20,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [335]
    }
    GargoyleB = {
        '$id': 1632,
        'Name': 'Gargoyle B',
        'Location Near': 2351,
        'Level': 32,
        'Story Pre-Req': [40],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [352]
    }
    GargoyleC = {
        '$id': 1633,
        'Name': 'Gargoyle C',
        'Location Near': 2357,
        'Level': 32,
        'Story Pre-Req': [40],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [353]
    }
    VenttsRopl = {
        '$id': 1634,
        'Name': 'Ventts Ropl',
        'Location Near': 2331,
        'Level': 38,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [364]
    }
    KnooberPod = {
        '$id': 1635,
        'Name': 'Knoober Pod',
        'Location Near': 2310,
        'Level': 33,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [354]
    }
    AveroTirkin = {
        '$id': 1636,
        'Name': 'Avero Tirkin',
        'Location Near': 2322,
        'Level': 20,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [323, 497]
    }
    SorolleArmu = {
        '$id': 1637,
        'Name': 'Sorolle Armu',
        'Location Near': 2322,
        'Level': 11,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [308]
    }
    MagraQuadwing = {
        '$id': 1639,
        'Name': 'Magra Quadwing',
        'Location Near': 2315,
        'Level': 2,
        'Story Pre-Req': [1],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [298]
    }
    NightMagraQuadwing = {
        '$id': 1640,
        'Name': 'Night Magra Quadwing',
        'Location Near': 2315,
        'Level': 4,
        'Story Pre-Req': [1],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [299]
    }
    LegiaFlier = {
        '$id': 1641,
        'Name': 'Legia Flier',
        'Location Near': 2328,
        'Level': 21,
        'Story Pre-Req': [29],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [1629],
        'Required Items': [],
        'Enemy Drop Table IDs': [330, 495]
    }
    SordisRhogul = {
        '$id': 1643,
        'Name': 'Sordis Rhogul',
        'Location Near': 2322,
        'Level': 22,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [331, 490]
    }
    TalesRapchor = {
        '$id': 1644,
        'Name': 'Tales Rapchor',
        'Location Near': 2335,
        'Level': 40,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [377]
    }
    AwarthScorpox = {
        '$id': 1645,
        'Name': 'Awarth Scorpox',
        'Location Near': 2330,
        'Level': 27,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [342]
    }
    DakhimTirkin = {
        '$id': 1646,
        'Name': 'Dakhim Tirkin',
        'Location Near': 2335,
        'Level': 39,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [369, 496]
    }
    TsorridTirkin = {
        '$id': 1647,
        'Name': 'Tsorrid Tirkin',
        'Location Near': 2335,
        'Level': 39,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [370, 497]
    }
    PallovTirkin = {
        '$id': 1648,
        'Name': 'Pallov Tirkin',
        'Location Near': 2333,
        'Level': 39,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [371]
    }
    GlorrTotem = {
        '$id': 1649,
        'Name': 'Glorr Totem',
        'Location Near': 2333,
        'Level': 39,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [372]
    }
    NereusQuadwing = {
        '$id': 1650,
        'Name': 'Nereus Quadwing',
        'Location Near': 2322,
        'Level': 21,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [329]
    }
    SableVolff = {
        '$id': 1651,
        'Name': 'Sable Volff',
        'Location Near': 2330,
        'Level': 25,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [339, 485]
    }
    GobeenGogol = {
        '$id': 1652,
        'Name': 'Gobeen Gogol',
        'Location Near': 2330,
        'Level': 28,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [343]
    }
    DormineBrog = {
        '$id': 1653,
        'Name': 'Dormine Brog',
        'Location Near': 2326,
        'Level': 28,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [344]
    }
    GrohlPlambus = {
        '$id': 1655,
        'Name': 'Grohl Plambus',
        'Location Near': 2413,
        'Level': 38,
        'Story Pre-Req': [12],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [321]
    }
    CheltaCaterpileDannagh = {
        '$id': 1656,
        'Name': 'Chelta Caterpile (Dannagh)',
        'Location Near': 2330,
        'Level': 30,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [341]
    }
    LunarAmaruq = {
        '$id': 1657,
        'Name': 'Lunar Amaruq',
        'Location Near': 2307,
        'Level': 34,
        'Story Pre-Req': [33],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [469]
    }
    BeatificOphelia = {
        '$id': 1658,
        'Name': 'Beatific Ophelia',
        'Location Near': 2311,
        'Level': 48,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [470]
    }
    NomadicRusholme = {
        '$id': 1659,
        'Name': 'Nomadic Rusholme',
        'Location Near': 2325,
        'Level': 44,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [20],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [471]
    }
    IonosphericMitchell = {
        '$id': 1660,
        'Name': 'Ionospheric Mitchell',
        'Location Near': 2320,
        'Level': 50,
        'Story Pre-Req': [8],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [472]
    }
    InterceptorGrace = {
        '$id': 1661,
        'Name': 'Interceptor Grace',
        'Location Near': 2310,
        'Level': 40,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [473]
    }
    GourmandGalgan = {
        '$id': 1662,
        'Name': 'Gourmand Galgan',
        'Location Near': 2322,
        'Level': 38,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [474]
    }
    SleepwalkerMork = {
        '$id': 1663,
        'Name': 'Sleepwalker Mork',
        'Location Near': 2334,
        'Level': 33,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [475]
    }
    HarbingerCavill = {
        '$id': 1664,
        'Name': 'Harbinger Cavill',
        'Location Near': 2317,
        'Level': 23,
        'Story Pre-Req': [5],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [476]
    }
    SequesteredLudd = {
        '$id': 1665,
        'Name': 'Sequestered Ludd',
        'Location Near': 2348,
        'Level': 48,
        'Story Pre-Req': [53],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [477]
    }
    EverdarkErg = {
        '$id': 1666,
        'Name': 'Everdark Erg',
        'Location Near': 2315,
        'Level': 36,
        'Story Pre-Req': [24],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [478]
    }
    FlyingFortressDesmor = {
        '$id': 1667,
        'Name': 'Flying Fortress Desmor',
        'Location Near': 2314,
        'Level': 55,
        'Story Pre-Req': [35],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [479]
    }
    ScowlingQuincy = {
        '$id': 1670,
        'Name': 'Scowling Quincy',
        'Location Near': 2323,
        'Level': 25,
        'Story Pre-Req': [25],
        'During Quest': [],
        'Quest Completion Pre-Req': [],
        'Summoned By': [],
        'Required Items': [],
        'Enemy Drop Table IDs': [480]
    }

    EnemyDropCounter = 1

    TornaEnemyDict = [RagingVolff, JubelFeris, CursedBuloofoA, GargoyleA, Addam, Mythra, Brighid, ArdainianScoutA, ArdainianScoutB, GortA, AntipatheticArchibald, ScurvyCurtis, InsufferableUlysses, SlitheJagronB, MalosA, GargoyleD, ArtificeColossus, MalosB, MalosC, GortB, ArtificeSirenA, ArtificeSirenB, CursedBuloofoB, VanadiumTirkin, SorgusTirkin, LeractGogol, HewliGogol, MarrithAntol, IncubFlier, PradoCaterpile, AppetBrog, DurallBuloofo, InnocentVolff, LoweBlant, TizzaParisax, IndignantJerry, GraftonFeris, ConspiratorMacNeth, WanderingUrchon, WanderingRopl, WanderingLaia, TimidVolff, PickerBuloofo, ElegiacMercenary, HalcyonMercenary, ChatteringSkeeter, TacitusUrchon, GloomyAspar, WhistlingBathein, PreoccupiedGogol, TenaxEkidno, CalculatingGogol, ElectGogol, CloudArachno, DispareRopl, CreefGriffox, EvokeBunnit, ForayBunnit, NoggleBunnit, PinchBunnit, FirmVolff, GeminiVolff, EspinaFeris, LekutFeris, RinkerEks, DominalFlamii, IngleCamill, GrayBuloofo, ImbaLizard, CelsarsTaos, DreadCaterpileSummon, KanooSkwaror, DreadCaterpileNormal, MyrrhesCrustip, ArrahRhogul, BohnQuadwing, HighbohnQuadwing, LapisVang, ErsSkeeter, AstorFlier, CascadeKrabble, KastKrabble, ReedPiranhax, MaramalPiranhax, KeatTirkin, GradsTirkin, VabraTirkin, EpistoTirkin, DerrahTirkin, XanePippito, CooraNest, GneoRopl, FersGrebel, HighscreebQuadwing, ScriboQuadwing, HerculeanGibson, HurricaneAnise, MesmerTlaloc, SentinelCarpathia, RavineBunnit, ErraticGoliante, HandwringingBigelow, OveraffectionateMurph, SpillitUrchon, ApostleRhogul, SteekyHox, RalshVolff, SowlFeris, UrbsArmuA, AureaArdun, SladeEks, LibelteFlamii, LefthFlamii, MarnaGaraffa, NemusCamill, AstleEllook, FaneBuloofo, VokkonGriffox, TelahRiik, WhispUpa, BebthUpa, OoneEkidno, ClocheRapchor, NobleAspar, TretsAspar, SurveeAntol, GreetzAntol, CheltaCaterpileLasaria, CaliberScorpox, ZafirahCrustip, YouseParisax, UisParisax, LegginParisax, BurranGyanna, SalshRhogul, TonbreRhogul, AnbuVang, LapseFlier, KlaretWisp, RegusMoramora, TwondusAspid, PhantomMedooz, BiblisPuffot, RobalKrabble, RibageGrady, SarchessGrady, LegarreMarrin, ArloKapiba, RooseBlant, DrothUrchon, TeppusPippito, ArcahPippito, TyphonTirkin, GratTirkin, CardineTirkin, ParoleTirkin, SomeliaNest, PsitEgg, VictorTotem, GargoyleB, GargoyleC, VenttsRopl, KnooberPod, AveroTirkin, SorolleArmu, MagraQuadwing, NightMagraQuadwing, LegiaFlier, SordisRhogul, TalesRapchor, AwarthScorpox, DakhimTirkin, TsorridTirkin, PallovTirkin, GlorrTotem, NereusQuadwing, SableVolff, GobeenGogol, DormineBrog, GrohlPlambus, CheltaCaterpileDannagh, LunarAmaruq, BeatificOphelia, NomadicRusholme, IonosphericMitchell, InterceptorGrace, GourmandGalgan, SleepwalkerMork, HarbingerCavill, SequesteredLudd, EverdarkErg, FlyingFortressDesmor, ScowlingQuincy] # SlitheJagronA
    
    global TornaEnemies
    TornaEnemies = []

    for enemy in TornaEnemyDict:
        TornaEnemyNormalDrops(enemy, TornaEnemies, DropQty, EnemyDropCounter)
        EnemyDropCounter += 1

    # adding back other requirements

    SummonedList = []

    for enemy in TornaEnemies:
        TurnEnemyLevelIntoMainStoryReq(enemy)
        if enemy.mainreq != 0:
            enemy.itemreqs.extend(Mainquests[enemy.mainreq - 1].itemreqs) # adds the main story requirement to the enemy of choice
        if enemy.duringquest != []:
            enemy.itemreqs.extend(Sidequests[enemy.duringquest[0] - 1].itemreqs) # adds the current sidequest item requirements to the enemy of choice
        if enemy.sideprereq != []:
            enemy.itemreqs.extend(Sidequests[enemy.sideprereq[0] - 1].itemreqs) # adds the pre-req sidequest items to the enemy of choice (used for one enemy that isn't directly part of a quest, but spawns after a sidequest is finished)
        if enemy.id in TornaUMIDs:
            enemy.type = "uniquemonster"
        elif enemy.id in TornaBossIDs:
            enemy.type = "boss"
        elif enemy.id in TornaQuestEnemyIDs:
            enemy.type = "questenemy"
        elif enemy.id in TornaNormalEnemyIDs:
            enemy.type = "normalenemy"
        for area in Areas: # adds the area reach requirements
            if enemy.nearloc == area.id:
                enemy.itemreqs.extend(area.itemreqs)
                break
        if enemy.summonedby != []: # need to write down which enemies are summoned by who, so if the enemy's id is later in the list, we just copy the requirements from the original enemy. You shouldn't have to fight a level 50 enemy to get a crack at them spawning a level 10 enemy, i.e.
            SummonedList.append(enemy)
        enemy.itemreqs = Helper.MultiLevelListToSingleLevelList(enemy.itemreqs)
        enemy.itemreqs = list(set(enemy.itemreqs))
        enemy.itemreqs.sort()

    for enemy in SummonedList:
        for summoningenemy in TornaEnemies:
            if enemy.summonedby[0] == summoningenemy.id:
                enemy.itemreqs.extend(summoningenemy.itemreqs)
                break
        enemy.itemreqs = Helper.MultiLevelListToSingleLevelList(enemy.itemreqs)
        enemy.itemreqs = list(set(enemy.itemreqs))
        enemy.itemreqs.sort()

    return TornaEnemies, EnemyDropCounter

def TurnEnemyLevelIntoMainStoryReq(enemy): # decided not to go with the enemy level token system and instead use a level cap based system.
    match enemy.level: # these should be 3 levels under the level cap
        case _ if enemy.level > 8 and enemy.level <= 14:
           enemy.mainreq = max(enemy.mainreq, 8)
        case _ if enemy.level > 14 and enemy.level <= 21:
            enemy.mainreq = max(enemy.mainreq, 16)
        case _ if enemy.level > 21 and enemy.level <= 30:
            enemy.mainreq = max(enemy.mainreq, 19)
        case _ if enemy.level > 30 and enemy.level <= 34:
            enemy.mainreq = max(enemy.mainreq, 30)
        case _ if enemy.level > 34 and enemy.level <= 42:
            enemy.mainreq = max(enemy.mainreq, 40)
        case _ if enemy.level > 42:
            enemy.mainreq = max(enemy.mainreq, 44)

    