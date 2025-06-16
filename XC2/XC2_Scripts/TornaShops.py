from scripts import Helper, JSONParser, PopupDescriptions
import json
import random
from IDs import *


class TornaShop: # created to allow me to pass these objects easier
    def __init__(self, input, addtolist, rewardnumber):
        self.shoplistid = input["MNU_ShopList $id"]
        self.shopnormalid = input['MNU_ShopNormal $id']
        self.name = input["Name"]
        self.nearloc = input['Location Near']
        self.mainreq = input['Story Pre-Req']
        self.itemreqs = Helper.MultiLevelListToSingleLevelList(input['Required Items'])
        self.talkeventid = input['Talk Event ID']
        self.randomizeditems = Helper.ExtendListtoLength(Helper.ExtendListtoLength([], rewardnumber, "-1"), 15, "0") # holds shop item ids, -1 for progression, 0 for filler spots
        self.type = "shop"
        if rewardnumber > 0:
            self.hasprogression = True
        else:
            self.hasprogression = False
        self.npcid = input['NPC ID']
        addtolist.append(self)

def CreateShopInfo(Mainquests, Areas, ItemsPerShop):
    LaschamWeapons = {
        'MNU_ShopList $id': 248,
        'Talk Event ID': 42017,
        'MNU_ShopNormal $id': 110,
        'Name': 'Lascham Weapons',
        'Location Near': 2401,
        'Story Pre-Req': 12,
        'Required Items': [],
        'NPC ID': 3667
    }
    LaschamAccessories = {
        'MNU_ShopList $id': 247,
        'Talk Event ID': 42018,
        'MNU_ShopNormal $id': 109,
        'Name': 'Lascham Accessories',
        'Location Near': 2401,
        'Story Pre-Req': 12,
        'Required Items': [],
        'NPC ID': 3668
    }
    AlettaWeapons = {
        'MNU_ShopList $id': 250,
        'Talk Event ID': 42019,
        'MNU_ShopNormal $id': 112,
        'Name': 'Aletta Weapons',
        'Location Near': 2305,
        'Story Pre-Req': 25,
        'Required Items': [],
        'NPC ID': 3669
    }
    AlettaAccessories = {
        'MNU_ShopList $id': 249,
        'Talk Event ID': 42020,
        'MNU_ShopNormal $id': 111,
        'Name': 'Aletta Accessories',
        'Location Near': 2305,
        'Story Pre-Req': 25,
        'Required Items': [],
        'NPC ID': 3670
    }
    HyberWeapons = {
        'MNU_ShopList $id': 252,
        'Talk Event ID': 42021,
        'MNU_ShopNormal $id': 114,
        'Name': 'Hyber Weapons',
        'Location Near': 2307,
        'Story Pre-Req': 33,
        'Required Items': [],
        'NPC ID': 3671
    }
    HyberAccessories = {
        'MNU_ShopList $id': 251,
        'Talk Event ID': 42022,
        'MNU_ShopNormal $id': 113,
        'Name': 'Hyber Accessories',
        'Location Near': 2307,
        'Story Pre-Req': 33,
        'Required Items': [],
        'NPC ID': 3672
    }
    GoldenBeastInfo = {
        'MNU_ShopList $id': 255,
        'Talk Event ID': 42023,
        'MNU_ShopNormal $id': 117,
        'Name': 'Golden Beast Info',
        'Location Near': 2368,
        'Story Pre-Req': 53,
        'Required Items': TornaSlatePieceIDs,
        'NPC ID': 3673
    }
    CapitalWeapons = {
        'MNU_ShopList $id': 254,
        'Talk Event ID': 41675,
        'MNU_ShopNormal $id': 116,
        'Name': 'Capital Weapons',
        'Location Near': 2357,
        'Story Pre-Req': 36,
        'Required Items': [],
        'NPC ID': 3376
    }
    CapitalAccessories = {
        'MNU_ShopList $id': 253,
        'Talk Event ID': 41624,
        'MNU_ShopNormal $id': 115,
        'Name': 'Capital Accessories',
        'Location Near': 2357,
        'Story Pre-Req': 36,
        'Required Items': [],
        'NPC ID': 3375
    }
    TravelingBard1 = {
        'MNU_ShopList $id': 67,
        'Talk Event ID': 40339,
        'MNU_ShopNormal $id': 37,
        'Name': 'Traveling Bard 1',
        'Location Near': 2355,
        'Story Pre-Req': 46,
        'Required Items': [],
        'NPC ID': 3704
    }
    TravelingBard2 = {
        'MNU_ShopList $id': 68,
        'Talk Event ID': 40442,
        'MNU_ShopNormal $id': 38,
        'Name': 'Traveling Bard 2',
        'Location Near': 2355,
        'Story Pre-Req': 46,
        'Required Items': [],
        'NPC ID': 3717
    }

    TornaShopDict = [LaschamWeapons, LaschamAccessories, AlettaWeapons, AlettaAccessories, HyberWeapons, HyberAccessories, GoldenBeastInfo, CapitalWeapons, CapitalAccessories, TravelingBard1, TravelingBard2]

    global TornaShops
    TornaShops = []

    for shop in TornaShopDict:
        TornaShop(shop, TornaShops, ItemsPerShop)

    for shop in TornaShops:
        if shop.mainreq != []:
            shop.itemreqs.extend(Mainquests[shop.mainreq - 1].itemreqs) # adds main story req
            shop.itemreqs = Helper.MultiLevelListToSingleLevelList(shop.itemreqs)
            shop.itemreqs = list(set(shop.itemreqs))
            shop.itemreqs.sort()
        for area in Areas: # adds the area reach requirements
            if shop.nearloc == area.id:
                shop.itemreqs.extend(area.itemreqs)
                break
            
    return TornaShops