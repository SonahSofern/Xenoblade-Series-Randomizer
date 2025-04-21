from scripts import Helper, JSONParser, PopupDescriptions
import json
import random
from IDs import *

class TornaRedBag: # created to allow me to pass these objects easier
    def __init__(self, input, addtolist, rewardnumber):
        self.id = input['ma40a PreciousPop $id']
        self.name = input["Name"]
        self.nearloc = input['Location Near']
        self.mainreq = input['Story Pre-Req']
        self.itemreqs = Helper.MultiLevelListToSingleLevelList(input['Required Items'])
        self.randomizeditems = Helper.ExtendListtoLength([], rewardnumber, "0") # holds enemy drop ids
        addtolist.append(self)

def CreateRedBagInfo(Mainquests, Areas, RedBagsOn):
    VaultKeyBag = {
        'ma40a PreciousPop $id': 1101,
        'Name': 'VaultKeyBag',
        'Location Near': 2325,
        'Story Pre-Req': [25],
        'Required Items': []
    }
    IndigoSlatePieceBag = {
        'ma40a PreciousPop $id': 1102,
        'Name': 'IndigoSlatePieceBag',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': []
    }
    DawningSlatePieceBag = {
        'ma40a PreciousPop $id': 1103,
        'Name': 'DawningSlatePieceBag',
        'Location Near': 2321,
        'Story Pre-Req': [5],
        'Required Items': []
    }
    CrimsonSlatePieceBag = {
        'ma40a PreciousPop $id': 1104,
        'Name': 'CrimsonSlatePieceBag',
        'Location Near': 2303,
        'Story Pre-Req': [8],
        'Required Items': []
    }
    RustySlatePieceBag = {
        'ma40a PreciousPop $id': 1105,
        'Name': 'RustySlatePieceBag',
        'Location Near': 2304,
        'Story Pre-Req': [10],
        'Required Items': []
    }
    PurpleSlatePieceBag = {
        'ma40a PreciousPop $id': 1106,
        'Name': 'PurpleSlatePieceBag',
        'Location Near': 2305,
        'Story Pre-Req': [25],
        'Required Items': []
    }
    ChestnutSlatePieceBag = {
        'ma40a PreciousPop $id': 1107,
        'Name': 'ChestnutSlatePieceBag',
        'Location Near': 2323,
        'Story Pre-Req': [25],
        'Required Items': []
    }
    CinnabarSlatePieceBag = {
        'ma40a PreciousPop $id': 1108,
        'Name': 'CinnabarSlatePieceBag',
        'Location Near': 2326,
        'Story Pre-Req': [25],
        'Required Items': []
    }
    ScarletSlatePieceBag = {
        'ma40a PreciousPop $id': 1109,
        'Name': 'ScarletSlatePieceBag',
        'Location Near': 2313,
        'Story Pre-Req': [25],
        'Required Items': []
    }
    NavyBlueSlatePieceBag = {
        'ma40a PreciousPop $id': 1110,
        'Name': 'Navy-BlueSlatePieceBag',
        'Location Near': 2307,
        'Story Pre-Req': [33],
        'Required Items': []
    }
    InkySlatePieceBag = {
        'ma40a PreciousPop $id': 1111,
        'Name': 'InkySlatePieceBag',
        'Location Near': 2342,
        'Story Pre-Req': [53],
        'Required Items': []
    }
    CherrySlatePieceBag = {
        'ma40a PreciousPop $id': 1112,
        'Name': 'CherrySlatePieceBag',
        'Location Near': 2333,
        'Story Pre-Req': [35],
        'Required Items': []
    }
    PeachSlatePieceBag = {
        'ma40a PreciousPop $id': 1113,
        'Name': 'PeachSlatePieceBag',
        'Location Near': 2311,
        'Story Pre-Req': [35],
        'Required Items': []
    }
    DarkGraySlatePieceBag = {
        'ma40a PreciousPop $id': 1114,
        'Name': 'Dark-GraySlatePieceBag',
        'Location Near': 2361,
        'Story Pre-Req': [36],
        'Required Items': []
    }
    MossGreenSlatePieceBag = {
        'ma40a PreciousPop $id': 1116,
        'Name': 'Moss-GreenSlatePieceBag',
        'Location Near': 2355,
        'Story Pre-Req': [46],
        'Required Items': []
    }
    HollyhockSlatePieceBag = {
        'ma40a PreciousPop $id': 1117,
        'Name': 'HollyhockSlatePieceBag',
        'Location Near': 2306,
        'Story Pre-Req': [29],
        'Required Items': []
    }
    LeadenSlatePieceBag = {
        'ma40a PreciousPop $id': 1118,
        'Name': 'LeadenSlatePieceBag',
        'Location Near': 2347,
        'Story Pre-Req': [53],
        'Required Items': []
    }

    TornaRedBagDict = [VaultKeyBag,IndigoSlatePieceBag,DawningSlatePieceBag,CrimsonSlatePieceBag,RustySlatePieceBag,PurpleSlatePieceBag,ChestnutSlatePieceBag,CinnabarSlatePieceBag,ScarletSlatePieceBag,NavyBlueSlatePieceBag,InkySlatePieceBag,CherrySlatePieceBag,PeachSlatePieceBag,DarkGraySlatePieceBag,MossGreenSlatePieceBag,HollyhockSlatePieceBag,LeadenSlatePieceBag]
    
    global TornaRedBags
    TornaRedBags = []

    for bag in TornaRedBagDict:
        TornaRedBag(bag, TornaRedBags, RedBagsOn)

    for bag in TornaRedBags:
        if bag.mainreq != []:
            bag.itemreqs.extend(Mainquests[bag.mainreq[0]].itemreqs) # adds main story req
            bag.itemreqs = Helper.MultiLevelListToSingleLevelList(bag.itemreqs)
            bag.itemreqs = list(set(bag.itemreqs))
            bag.itemreqs.sort()
        for area in Areas: # adds the area reach requirements
            if bag.nearloc == area.id:
                bag.itemreqs.extend(area.itemreqs)
                break
    return TornaRedBags