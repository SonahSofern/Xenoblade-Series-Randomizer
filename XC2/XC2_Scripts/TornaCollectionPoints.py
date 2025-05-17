from scripts import Helper, JSONParser, PopupDescriptions
import json
import random
import time
from IDs import *

class TornaCollectionPoint: # created to allow me to pass these objects easier
    def __init__(self, input, addtolist, rewardnumber):
        self.id = input['$id'][:4]
        self.uuid = input['$id']
        self.name = input['Name']
        self.mainreq = input['Story Pre-Req'][0]
        self.itemreqs = Helper.MultiLevelListToSingleLevelList(input['Required Items'])
        self.enemyreqs = input['Must Defeat Enemy IDs']
        self.nearloc = input['Location Near']
        self.rarity = input['Rarity']
        self.collectiontableid = input['CollectionTableID']
        self.randomizeditems = Helper.ExtendListtoLength(Helper.ExtendListtoLength([], rewardnumber, "-1"), 4, "0") # holds ids, -1 for progression, 0 for filler spots
        if rewardnumber > 0:
            self.hasprogression = True
        else:
            self.hasprogression = False
        addtolist.append(self)

def CreateCollectionPointInfo(Mainquests, Areas, Enemies, CollectionRewardQty):
    ma40aCollectionPoint4401 = {
        '$id': '4401colle_ma40a_qst7014_001',
        'Name': 'ma40aCollectionPoint4401',
        'Location Near': 2333,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 1
        }
    ma40aCollectionPoint4402 = {
        '$id': '4402colle_ma40a_qst7014_002',
        'Name': 'ma40aCollectionPoint4402',
        'Location Near': 2333,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 2
        }
    ma40aCollectionPoint4403 = {
        '$id': '4403colle_ma40a_qst7014_003',
        'Name': 'ma40aCollectionPoint4403',
        'Location Near': 2333,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 3
        }
    ma40aCollectionPoint4404 = {
        '$id': '4404colle_ma40a_qst7014_004',
        'Name': 'ma40aCollectionPoint4404',
        'Location Near': 2333,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 4
        }
    ma40aCollectionPoint4405 = {
        '$id': '4405colle_ma40a_qst7014_005',
        'Name': 'ma40aCollectionPoint4405',
        'Location Near': 2333,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 5
        }
    ma40aCollectionPoint4406 = {
        '$id': '4406colle_ma40a_qst7005_001',
        'Name': 'ma40aCollectionPoint4406',
        'Location Near': 2316,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 6
        }
    ma40aCollectionPoint4407 = {
        '$id': '4407colle_ma40a_qst7026_001',
        'Name': 'ma40aCollectionPoint4407',
        'Location Near': 2332,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 7
        }
    ma40aCollectionPoint4408 = {
        '$id': '4408colle_ma40a_qst7026_002',
        'Name': 'ma40aCollectionPoint4408',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 8
        }
    ma40aCollectionPoint4409 = {
        '$id': '4409colle_ma40a_qst7021_001',
        'Name': 'ma40aCollectionPoint4409',
        'Location Near': 2323,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 9
        }
    ma40aCollectionPoint4410 = {
        '$id': '4410colle_ma40a_qst7021_002',
        'Name': 'ma40aCollectionPoint4410',
        'Location Near': 2323,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 10
        }
    ma40aCollectionPoint4411 = {
        '$id': '4411colle_ma40a_qst7021_003',
        'Name': 'ma40aCollectionPoint4411',
        'Location Near': 2322,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 11
        }
    ma40aCollectionPoint4413 = {
        '$id': '4413colle_ma40a_11_050_100_01',
        'Name': 'ma40aCollectionPoint4413',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 13
        }
    ma40aCollectionPoint4414 = {
        '$id': '4414colle_ma40a_11_050_100_02',
        'Name': 'ma40aCollectionPoint4414',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 14
        }
    ma40aCollectionPoint4415 = {
        '$id': '4415colle_ma40a_11_050_100_03',
        'Name': 'ma40aCollectionPoint4415',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 15
        }
    ma40aCollectionPoint4416 = {
        '$id': '4416colle_ma40a_11_050_100_04',
        'Name': 'ma40aCollectionPoint4416',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 16
        }
    ma40aCollectionPoint4417 = {
        '$id': '4417colle_ma40a_m_n_1',
        'Name': 'ma40aCollectionPoint4417',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [30387,30411,30421,30360,30444],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 17
        }
    ma40aCollectionPoint4418 = {
        '$id': '4418colle_ma40a_m_n_2',
        'Name': 'ma40aCollectionPoint4418',
        'Location Near': 2304,
        'Story Pre-Req': [10],
        'Required Items': [30387,30411,30421,30360,30444],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 18
        }
    ma40aCollectionPoint4419 = {
        '$id': '4419colle_ma40a_m_n_3',
        'Name': 'ma40aCollectionPoint4419',
        'Location Near': 2305,
        'Story Pre-Req': [25],
        'Required Items': [30387,30411,30421,30360,30444],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 19
        }
    ma40aCollectionPoint4420 = {
        '$id': '4420colle_ma40a_m_n_4',
        'Name': 'ma40aCollectionPoint4420',
        'Location Near': 2307,
        'Story Pre-Req': [33],
        'Required Items': [30387,30411,30421,30360,30444],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 20
        }
    ma40aCollectionPoint4421 = {
        '$id': '4421colle_ma40a_m_n_5',
        'Name': 'ma40aCollectionPoint4421',
        'Location Near': 2334,
        'Story Pre-Req': [35],
        'Required Items': [30387,30411,30421,30360,30444],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 21
        }
    ma40aCollectionPoint4422 = {
        '$id': '4422colle_ma40a_m_n_6',
        'Name': 'ma40aCollectionPoint4422',
        'Location Near': 2351,
        'Story Pre-Req': [36],
        'Required Items': [30387,30411,30421,30360,30444],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 22
        }
    ma40aCollectionPoint4423 = {
        '$id': '4423colle_ma40a_m_r_1',
        'Name': 'ma40aCollectionPoint4423',
        'Location Near': 2303,
        'Story Pre-Req': [8],
        'Required Items': [30378,30428,30372,30388,30436],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 23
        }
    ma40aCollectionPoint4424 = {
        '$id': '4424colle_ma40a_m_r_2',
        'Name': 'ma40aCollectionPoint4424',
        'Location Near': 2322,
        'Story Pre-Req': [25],
        'Required Items': [30378,30428,30372,30388,30436],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 24
        }
    ma40aCollectionPoint4425 = {
        '$id': '4425colle_ma40a_m_r_3',
        'Name': 'ma40aCollectionPoint4425',
        'Location Near': 2333,
        'Story Pre-Req': [35],
        'Required Items': [30378,30428,30372,30388,30436],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 25
        }
    ma40aCollectionPoint4426 = {
        '$id': '4426colle_ma40a_shouki_sq7201',
        'Name': 'ma40aCollectionPoint4426',
        'Location Near': 2320,
        'Story Pre-Req': [10],
        'Required Items': [HazeKey, [ManipEtherKey[0]], [HazeAff[0]]],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 26
        }
    ma40aCollectionPoint4427 = {
        '$id': '4427colle_ma40a_shouki_1',
        'Name': 'ma40aCollectionPoint4427',
        'Location Near': 2322,
        'Story Pre-Req': [25],
        'Required Items': [HazeKey, [ManipEtherKey[0]], [HazeAff[0]] , MythraKey, [LightKey[0]]],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 27
        }
    ma40aCollectionPoint4428 = {
        '$id': '4428colle_ma40a_shouki_2',
        'Name': 'ma40aCollectionPoint4428',
        'Location Near': 2328,
        'Story Pre-Req': [29],
        'Required Items': [HazeKey, ManipEtherKey[:1], HazeAff[:1] , MythraKey, LightKey[:1], MythraAff[:1]],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 28
        }
    ma40aCollectionPoint4429 = {
        '$id': '4429colle_ma40a_shouki_3',
        'Name': 'ma40aCollectionPoint4429',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [HazeKey, ManipEtherKey, HazeAff[:2] , MythraKey, LightKey, MythraAff],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 29
        }
    ma40aCollectionPoint4430 = {
        '$id': '4430colle_ma40a_shouki_4',
        'Name': 'ma40aCollectionPoint4430',
        'Location Near': 2310,
        'Story Pre-Req': [35],
        'Required Items': [HazeKey, ManipEtherKey, HazeAff[:2] , MythraKey, LightKey, MythraAff],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 30
        }
    ma40aCollectionPoint4431 = {
        '$id': '4431colle_ma40a_rock_n_2',
        'Name': 'ma40aCollectionPoint4431',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 31
        }
    ma40aCollectionPoint4432 = {
        '$id': '4432colle_ma40a_rock_n_4',
        'Name': 'ma40aCollectionPoint4432',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 32
        }
    ma40aCollectionPoint4433 = {
        '$id': '4433colle_ma40a_rock_n_5',
        'Name': 'ma40aCollectionPoint4433',
        'Location Near': 2318,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 33
        }
    ma40aCollectionPoint4434 = {
        '$id': '4434colle_ma40a_rock_n_6',
        'Name': 'ma40aCollectionPoint4434',
        'Location Near': 2302,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 34
        }
    ma40aCollectionPoint4435 = {
        '$id': '4435colle_ma40a_rock_n_7',
        'Name': 'ma40aCollectionPoint4435',
        'Location Near': 2320,
        'Story Pre-Req': [10],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 35
        }
    ma40aCollectionPoint4436 = {
        '$id': '4436colle_ma40a_rock_n_9',
        'Name': 'ma40aCollectionPoint4436',
        'Location Near': 2304,
        'Story Pre-Req': [10],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 36
        }
    ma40aCollectionPoint4437 = {
        '$id': '4437colle_ma40a_rock_n_13',
        'Name': 'ma40aCollectionPoint4437',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 37
        }
    ma40aCollectionPoint4438 = {
        '$id': '4438colle_ma40a_rock_n_14',
        'Name': 'ma40aCollectionPoint4438',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 38
        }
    ma40aCollectionPoint4439 = {
        '$id': '4439colle_ma40a_rock_r_1',
        'Name': 'ma40aCollectionPoint4439',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 39
        }
    ma40aCollectionPoint4440 = {
        '$id': '4440colle_ma40a_rock_r_2',
        'Name': 'ma40aCollectionPoint4440',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 40
        }
    ma40aCollectionPoint4441 = {
        '$id': '4441colle_ma40a_rock_r_3',
        'Name': 'ma40aCollectionPoint4441',
        'Location Near': 2318,
        'Story Pre-Req': [5],
        'Required Items': [[SwordplayKey[0]] , MythraKey, [FocusKey[0]]],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 41
        }
    ma40aCollectionPoint4442 = {
        '$id': '4442colle_ma40a_rock_r_4',
        'Name': 'ma40aCollectionPoint4442',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 42
        }
    ma40aCollectionPoint4443 = {
        '$id': '4443colle_ma40a_rock_r_5',
        'Name': 'ma40aCollectionPoint4443',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 43
        }
    ma40aCollectionPoint4444 = {
        '$id': '4444colle_ma40a_rock_r_6',
        'Name': 'ma40aCollectionPoint4444',
        'Location Near': 2315,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 44
        }
    ma40aCollectionPoint4445 = {
        '$id': '4445colle_ma40a_rock2_n_1',
        'Name': 'ma40aCollectionPoint4445',
        'Location Near': 2305,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 45
        }
    ma40aCollectionPoint4446 = {
        '$id': '4446colle_ma40a_rock2_n_2',
        'Name': 'ma40aCollectionPoint4446',
        'Location Near': 2326,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 46
        }
    ma40aCollectionPoint4447 = {
        '$id': '4447colle_ma40a_rock2_n_3',
        'Name': 'ma40aCollectionPoint4447',
        'Location Near': 2322,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 47
        }
    ma40aCollectionPoint4448 = {
        '$id': '4448colle_ma40a_rock2_n_4',
        'Name': 'ma40aCollectionPoint4448',
        'Location Near': 2323,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 48
        }
    ma40aCollectionPoint4449 = {
        '$id': '4449colle_ma40a_rock2_n_5',
        'Name': 'ma40aCollectionPoint4449',
        'Location Near': 2325,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 49
        }
    ma40aCollectionPoint4450 = {
        '$id': '4450colle_ma40a_rock2_n_6',
        'Name': 'ma40aCollectionPoint4450',
        'Location Near': 2324,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 50
        }
    ma40aCollectionPoint4451 = {
        '$id': '4451colle_ma40a_rock2_n_7',
        'Name': 'ma40aCollectionPoint4451',
        'Location Near': 2306,
        'Story Pre-Req': [29],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 51
        }
    ma40aCollectionPoint4452 = {
        '$id': '4452colle_ma40a_rock2_n_8',
        'Name': 'ma40aCollectionPoint4452',
        'Location Near': 2328,
        'Story Pre-Req': [29],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 52
        }
    ma40aCollectionPoint4453 = {
        '$id': '4453colle_ma40a_rock2_n_9',
        'Name': 'ma40aCollectionPoint4453',
        'Location Near': 2307,
        'Story Pre-Req': [33],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 53
        }
    ma40aCollectionPoint4454 = {
        '$id': '4454colle_ma40a_rock2_r_1',
        'Name': 'ma40aCollectionPoint4454',
        'Location Near': 2326,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 54
        }
    ma40aCollectionPoint4455 = {
        '$id': '4455colle_ma40a_rock2_r_2',
        'Name': 'ma40aCollectionPoint4455',
        'Location Near': 2328,
        'Story Pre-Req': [29],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 55
        }
    ma40aCollectionPoint4456 = {
        '$id': '4456colle_ma40a_rock2_r_3',
        'Name': 'ma40aCollectionPoint4456',
        'Location Near': 2322,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 56
        }
    ma40aCollectionPoint4457 = {
        '$id': '4457colle_ma40a_rock3_n_1',
        'Name': 'ma40aCollectionPoint4457',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 57
        }
    ma40aCollectionPoint4458 = {
        '$id': '4458colle_ma40a_rock3_n_2',
        'Name': 'ma40aCollectionPoint4458',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 58
        }
    ma40aCollectionPoint4459 = {
        '$id': '4459colle_ma40a_rock3_n_3',
        'Name': 'ma40aCollectionPoint4459',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 59
        }
    ma40aCollectionPoint4460 = {
        '$id': '4460colle_ma40a_rock3_n_4',
        'Name': 'ma40aCollectionPoint4460',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 60
        }
    ma40aCollectionPoint4461 = {
        '$id': '4461colle_ma40a_rock3_n_5',
        'Name': 'ma40aCollectionPoint4461',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 61
        }
    ma40aCollectionPoint4462 = {
        '$id': '4462colle_ma40a_rock3_n_6',
        'Name': 'ma40aCollectionPoint4462',
        'Location Near': 2334,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 62
        }
    ma40aCollectionPoint4463 = {
        '$id': '4463colle_ma40a_rock3_n_7',
        'Name': 'ma40aCollectionPoint4463',
        'Location Near': 2335,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 63
        }
    ma40aCollectionPoint4464 = {
        '$id': '4464colle_ma40a_rock3_n_8',
        'Name': 'ma40aCollectionPoint4464',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 64
        }
    ma40aCollectionPoint4465 = {
        '$id': '4465colle_ma40a_rock3_n_9',
        'Name': 'ma40aCollectionPoint4465',
        'Location Near': 2311,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 65
        }
    ma40aCollectionPoint4466 = {
        '$id': '4466colle_ma40a_rock3_n_10',
        'Name': 'ma40aCollectionPoint4466',
        'Location Near': 2311,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 66
        }
    ma40aCollectionPoint4467 = {
        '$id': '4467colle_ma40a_rock3_n_11',
        'Name': 'ma40aCollectionPoint4467',
        'Location Near': 2310,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 67
        }
    ma40aCollectionPoint4468 = {
        '$id': '4468colle_ma40a_rock3_n_12',
        'Name': 'ma40aCollectionPoint4468',
        'Location Near': 2338,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 68
        }
    ma40aCollectionPoint4469 = {
        '$id': '4469colle_ma40a_rock3_n_13',
        'Name': 'ma40aCollectionPoint4469',
        'Location Near': 2337,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 69
        }
    ma40aCollectionPoint4470 = {
        '$id': '4470colle_ma40a_rock3_n_14',
        'Name': 'ma40aCollectionPoint4470',
        'Location Near': 2361,
        'Story Pre-Req': [36],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 70
        }
    ma40aCollectionPoint4471 = {
        '$id': '4471colle_ma40a_rock3_r_1',
        'Name': 'ma40aCollectionPoint4471',
        'Location Near': 2314,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 71
        }
    ma40aCollectionPoint4472 = {
        '$id': '4472colle_ma40a_rock3_r_2',
        'Name': 'ma40aCollectionPoint4472',
        'Location Near': 2314,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 72
        }
    ma40aCollectionPoint4473 = {
        '$id': '4473colle_ma40a_rock3_r_3',
        'Name': 'ma40aCollectionPoint4473',
        'Location Near': 2310,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [1661],
        'Rarity': 1,
        'CollectionTableID': 73
        }
    ma40aCollectionPoint4474 = {
        '$id': '4474colle_ma40a_rock3_r_4',
        'Name': 'ma40aCollectionPoint4474',
        'Location Near': 2355,
        'Story Pre-Req': [46],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 74
        }
    ma40aCollectionPoint4475 = {
        '$id': '4475colle_ma40a_rock3_r_5',
        'Name': 'ma40aCollectionPoint4475',
        'Location Near': 2308,
        'Story Pre-Req': [25],
        'Required Items': [TornaSlatePieceIDs[:4]],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 75
        }
    ma40aCollectionPoint4476 = {
        '$id': '4476colle_ma40a_hana_n_2',
        'Name': 'ma40aCollectionPoint4476',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 76
        }
    ma40aCollectionPoint4477 = {
        '$id': '4477colle_ma40a_hana_n_3',
        'Name': 'ma40aCollectionPoint4477',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 77
        }
    ma40aCollectionPoint4478 = {
        '$id': '4478colle_ma40a_hana_n_4',
        'Name': 'ma40aCollectionPoint4478',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 78
        }
    ma40aCollectionPoint4479 = {
        '$id': '4479colle_ma40a_hana_n_5',
        'Name': 'ma40aCollectionPoint4479',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 79
        }
    ma40aCollectionPoint4480 = {
        '$id': '4480colle_ma40a_hana_n_7',
        'Name': 'ma40aCollectionPoint4480',
        'Location Near': 2301,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 80
        }
    ma40aCollectionPoint4481 = {
        '$id': '4481colle_ma40a_hana_n_12',
        'Name': 'ma40aCollectionPoint4481',
        'Location Near': 2303,
        'Story Pre-Req': [8],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 81
        }
    ma40aCollectionPoint4482 = {
        '$id': '4482colle_ma40a_hana_r_1',
        'Name': 'ma40aCollectionPoint4482',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 82
        }
    ma40aCollectionPoint4483 = {
        '$id': '4483colle_ma40a_hana_r_2',
        'Name': 'ma40aCollectionPoint4483',
        'Location Near': 2303,
        'Story Pre-Req': [8],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 83
        }
    ma40aCollectionPoint4484 = {
        '$id': '4484colle_ma40a_hana_r_4',
        'Name': 'ma40aCollectionPoint4484',
        'Location Near': 2304,
        'Story Pre-Req': [10],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 84
        }
    ma40aCollectionPoint4485 = {
        '$id': '4485colle_ma40a_hana_r_5',
        'Name': 'ma40aCollectionPoint4485',
        'Location Near': 2318,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 85
        }
    ma40aCollectionPoint4486 = {
        '$id': '4486colle_ma40a_hana2_n_1',
        'Name': 'ma40aCollectionPoint4486',
        'Location Near': 2322,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 86
        }
    ma40aCollectionPoint4487 = {
        '$id': '4487colle_ma40a_hana2_n_2',
        'Name': 'ma40aCollectionPoint4487',
        'Location Near': 2305,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 87
        }
    ma40aCollectionPoint4488 = {
        '$id': '4488colle_ma40a_hana2_n_3',
        'Name': 'ma40aCollectionPoint4488',
        'Location Near': 2322,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 88
        }
    ma40aCollectionPoint4489 = {
        '$id': '4489colle_ma40a_hana2_n_4',
        'Name': 'ma40aCollectionPoint4489',
        'Location Near': 2325,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 89
        }
    ma40aCollectionPoint4490 = {
        '$id': '4490colle_ma40a_hana2_n_5',
        'Name': 'ma40aCollectionPoint4490',
        'Location Near': 2325,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 90
        }
    ma40aCollectionPoint4491 = {
        '$id': '4491colle_ma40a_hana2_n_6',
        'Name': 'ma40aCollectionPoint4491',
        'Location Near': 2323,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 91
        }
    ma40aCollectionPoint4492 = {
        '$id': '4492colle_ma40a_hana2_n_7',
        'Name': 'ma40aCollectionPoint4492',
        'Location Near': 2322,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 92
        }
    ma40aCollectionPoint4493 = {
        '$id': '4493colle_ma40a_hana2_n_8',
        'Name': 'ma40aCollectionPoint4493',
        'Location Near': 2328,
        'Story Pre-Req': [33],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 93
        }
    ma40aCollectionPoint4494 = {
        '$id': '4494colle_ma40a_hana2_n_9',
        'Name': 'ma40aCollectionPoint4494',
        'Location Near': 2307,
        'Story Pre-Req': [33],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 94
        }
    ma40aCollectionPoint4495 = {
        '$id': '4495colle_ma40a_hana2_n_10',
        'Name': 'ma40aCollectionPoint4495',
        'Location Near': 2307,
        'Story Pre-Req': [33],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 95
        }
    ma40aCollectionPoint4496 = {
        '$id': '4496colle_ma40a_hana2_r_1',
        'Name': 'ma40aCollectionPoint4496',
        'Location Near': 2325,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 96
        }
    ma40aCollectionPoint4497 = {
        '$id': '4497colle_ma40a_hana2_r_2',
        'Name': 'ma40aCollectionPoint4497',
        'Location Near': 2328,
        'Story Pre-Req': [29],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 97
        }
    ma40aCollectionPoint4498 = {
        '$id': '4498colle_ma40a_hana2_r_3',
        'Name': 'ma40aCollectionPoint4498',
        'Location Near': 2326,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 98
        }
    ma40aCollectionPoint4499 = {
        '$id': '4499colle_ma40a_hana2_r_4',
        'Name': 'ma40aCollectionPoint4499',
        'Location Near': 2307,
        'Story Pre-Req': [33],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 99
        }
    ma40aCollectionPoint4500 = {
        '$id': '4500colle_ma40a_hana3_n_1',
        'Name': 'ma40aCollectionPoint4500',
        'Location Near': 2334,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 100
        }
    ma40aCollectionPoint4501 = {
        '$id': '4501colle_ma40a_hana3_n_2',
        'Name': 'ma40aCollectionPoint4501',
        'Location Near': 2314,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 101
        }
    ma40aCollectionPoint4502 = {
        '$id': '4502colle_ma40a_hana3_n_3',
        'Name': 'ma40aCollectionPoint4502',
        'Location Near': 2333,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 102
        }
    ma40aCollectionPoint4503 = {
        '$id': '4503colle_ma40a_hana3_n_4',
        'Name': 'ma40aCollectionPoint4503',
        'Location Near': 2334,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 103
        }
    ma40aCollectionPoint4504 = {
        '$id': '4504colle_ma40a_hana3_n_5',
        'Name': 'ma40aCollectionPoint4504',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 104
        }
    ma40aCollectionPoint4505 = {
        '$id': '4505colle_ma40a_hana3_n_6',
        'Name': 'ma40aCollectionPoint4505',
        'Location Near': 2310,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 105
        }
    ma40aCollectionPoint4506 = {
        '$id': '4506colle_ma40a_hana3_n_7',
        'Name': 'ma40aCollectionPoint4506',
        'Location Near': 2332,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 106
        }
    ma40aCollectionPoint4507 = {
        '$id': '4507colle_ma40a_hana3_n_9',
        'Name': 'ma40aCollectionPoint4507',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 107
        }
    ma40aCollectionPoint4508 = {
        '$id': '4508colle_ma40a_hana3_n_10',
        'Name': 'ma40aCollectionPoint4508',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 108
        }
    ma40aCollectionPoint4509 = {
        '$id': '4509colle_ma40a_hana3_n_11',
        'Name': 'ma40aCollectionPoint4509',
        'Location Near': 2337,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 109
        }
    ma40aCollectionPoint4510 = {
        '$id': '4510colle_ma40a_hana3_r_1',
        'Name': 'ma40aCollectionPoint4510',
        'Location Near': 2314,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 110
        }
    ma40aCollectionPoint4511 = {
        '$id': '4511colle_ma40a_hana3_r_2',
        'Name': 'ma40aCollectionPoint4511',
        'Location Near': 2311,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 111
        }
    ma40aCollectionPoint4512 = {
        '$id': '4512colle_ma40a_hana3_r_3',
        'Name': 'ma40aCollectionPoint4512',
        'Location Near': 2334,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 112
        }
    ma40aCollectionPoint4513 = {
        '$id': '4513colle_ma40a_hana3_r_4',
        'Name': 'ma40aCollectionPoint4513',
        'Location Near': 2311,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 113
        }
    ma40aCollectionPoint4514 = {
        '$id': '4514colle_ma40a_hana3_r_5',
        'Name': 'ma40aCollectionPoint4514',
        'Location Near': 2334,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 114
        }
    ma40aCollectionPoint4515 = {
        '$id': '4515colle_ma40a_hana3_r_6',
        'Name': 'ma40aCollectionPoint4515',
        'Location Near': 2335,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 115
        }
    ma40aCollectionPoint4516 = {
        '$id': '4516colle_ma40a_yasai_n_1',
        'Name': 'ma40aCollectionPoint4516',
        'Location Near': 2303,
        'Story Pre-Req': [8],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 116
        }
    ma40aCollectionPoint4517 = {
        '$id': '4517colle_ma40a_yasai_n_2',
        'Name': 'ma40aCollectionPoint4517',
        'Location Near': 2303,
        'Story Pre-Req': [8],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 117
        }
    ma40aCollectionPoint4518 = {
        '$id': '4518colle_ma40a_yasai_n_3',
        'Name': 'ma40aCollectionPoint4518',
        'Location Near': 2320,
        'Story Pre-Req': [10],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 118
        }
    ma40aCollectionPoint4519 = {
        '$id': '4519colle_ma40a_yasai_n_4',
        'Name': 'ma40aCollectionPoint4519',
        'Location Near': 2301,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 119
        }
    ma40aCollectionPoint4520 = {
        '$id': '4520colle_ma40a_yasai_n_5',
        'Name': 'ma40aCollectionPoint4520',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 120
        }
    ma40aCollectionPoint4521 = {
        '$id': '4521colle_ma40a_yasai_r_1',
        'Name': 'ma40aCollectionPoint4521',
        'Location Near': 2303,
        'Story Pre-Req': [8],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 121
        }
    ma40aCollectionPoint4522 = {
        '$id': '4522colle_ma40a_yasai_r_2',
        'Name': 'ma40aCollectionPoint4522',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 122
        }
    ma40aCollectionPoint4523 = {
        '$id': '4523colle_ma40a_yasai_r_3',
        'Name': 'ma40aCollectionPoint4523',
        'Location Near': 2320,
        'Story Pre-Req': [10],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 123
        }
    ma40aCollectionPoint4525 = {
        '$id': '4525colle_ma40a_yasai2_n_1',
        'Name': 'ma40aCollectionPoint4525',
        'Location Near': 2326,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 125
        }
    ma40aCollectionPoint4526 = {
        '$id': '4526colle_ma40a_yasai2_n_2',
        'Name': 'ma40aCollectionPoint4526',
        'Location Near': 2322,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 126
        }
    ma40aCollectionPoint4527 = {
        '$id': '4527colle_ma40a_yasai2_n_3',
        'Name': 'ma40aCollectionPoint4527',
        'Location Near': 2322,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 127
        }
    ma40aCollectionPoint4528 = {
        '$id': '4528colle_ma40a_yasai2_n_4',
        'Name': 'ma40aCollectionPoint4528',
        'Location Near': 2307,
        'Story Pre-Req': [33],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 128
        }
    ma40aCollectionPoint4529 = {
        '$id': '4529colle_ma40a_yasai2_n_5',
        'Name': 'ma40aCollectionPoint4529',
        'Location Near': 2307,
        'Story Pre-Req': [33],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 129
        }
    ma40aCollectionPoint4530 = {
        '$id': '4530colle_ma40a_yasai2_n_6',
        'Name': 'ma40aCollectionPoint4530',
        'Location Near': 2322,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 130
        }
    ma40aCollectionPoint4531 = {
        '$id': '4531colle_ma40a_yasai2_n_7',
        'Name': 'ma40aCollectionPoint4531',
        'Location Near': 2325,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 131
        }
    ma40aCollectionPoint4532 = {
        '$id': '4532colle_ma40a_yasai2_n_8',
        'Name': 'ma40aCollectionPoint4532',
        'Location Near': 2323,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 132
        }
    ma40aCollectionPoint4533 = {
        '$id': '4533colle_ma40a_yasai2_n_9',
        'Name': 'ma40aCollectionPoint4533',
        'Location Near': 2328,
        'Story Pre-Req': [29],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 133
        }
    ma40aCollectionPoint4534 = {
        '$id': '4534colle_ma40a_yasai2_r_1',
        'Name': 'ma40aCollectionPoint4534',
        'Location Near': 2323,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 134
        }
    ma40aCollectionPoint4535 = {
        '$id': '4535colle_ma40a_yasai2_r_2',
        'Name': 'ma40aCollectionPoint4535',
        'Location Near': 2307,
        'Story Pre-Req': [33],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 135
        }
    ma40aCollectionPoint4536 = {
        '$id': '4536colle_ma40a_yasai2_r_3',
        'Name': 'ma40aCollectionPoint4536',
        'Location Near': 2323,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 136
        }
    ma40aCollectionPoint4537 = {
        '$id': '4537colle_ma40a_yasai3_n_1',
        'Name': 'ma40aCollectionPoint4537',
        'Location Near': 2337,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 137
        }
    ma40aCollectionPoint4538 = {
        '$id': '4538colle_ma40a_yasai3_n_2',
        'Name': 'ma40aCollectionPoint4538',
        'Location Near': 2357,
        'Story Pre-Req': [36],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 138
        }
    ma40aCollectionPoint4539 = {
        '$id': '4539colle_ma40a_yasai3_n_3',
        'Name': 'ma40aCollectionPoint4539',
        'Location Near': 2332,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 139
        }
    ma40aCollectionPoint4540 = {
        '$id': '4540colle_ma40a_yasai3_n_4',
        'Name': 'ma40aCollectionPoint4540',
        'Location Near': 2355,
        'Story Pre-Req': [46],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 140
        }
    ma40aCollectionPoint4541 = {
        '$id': '4541colle_ma40a_yasai3_n_5',
        'Name': 'ma40aCollectionPoint4541',
        'Location Near': 2337,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 141
        }
    ma40aCollectionPoint4542 = {
        '$id': '4542colle_ma40a_yasai3_n_6',
        'Name': 'ma40aCollectionPoint4542',
        'Location Near': 2311,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 142
        }
    ma40aCollectionPoint4543 = {
        '$id': '4543colle_ma40a_yasai3_n_7',
        'Name': 'ma40aCollectionPoint4543',
        'Location Near': 2332,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 143
        }
    ma40aCollectionPoint4544 = {
        '$id': '4544colle_ma40a_yasai3_n_8',
        'Name': 'ma40aCollectionPoint4544',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 144
        }
    ma40aCollectionPoint4545 = {
        '$id': '4545colle_ma40a_yasai3_r_1',
        'Name': 'ma40aCollectionPoint4545',
        'Location Near': 2333,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 145
        }
    ma40aCollectionPoint4546 = {
        '$id': '4546colle_ma40a_yasai3_r_2',
        'Name': 'ma40aCollectionPoint4546',
        'Location Near': 2333,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 146
        }
    ma40aCollectionPoint4547 = {
        '$id': '4547colle_ma40a_yasai3_r_3',
        'Name': 'ma40aCollectionPoint4547',
        'Location Near': 2311,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 147
        }
    ma40aCollectionPoint4548 = {
        '$id': '4548colle_ma40a_yasai3_r_4',
        'Name': 'ma40aCollectionPoint4548',
        'Location Near': 2331,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 148
        }
    ma40aCollectionPoint4549 = {
        '$id': '4549colle_ma40a_ki_n_1',
        'Name': 'ma40aCollectionPoint4549',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 149
        }
    ma40aCollectionPoint4550 = {
        '$id': '4550colle_ma40a_ki_n_2',
        'Name': 'ma40aCollectionPoint4550',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 150
        }
    ma40aCollectionPoint4551 = {
        '$id': '4551colle_ma40a_ki_n_3',
        'Name': 'ma40aCollectionPoint4551',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 151
        }
    ma40aCollectionPoint4552 = {
        '$id': '4552colle_ma40a_ki_n_4',
        'Name': 'ma40aCollectionPoint4552',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 152
        }
    ma40aCollectionPoint4553 = {
        '$id': '4553colle_ma40a_ki_n_5',
        'Name': 'ma40aCollectionPoint4553',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 153
        }
    ma40aCollectionPoint4554 = {
        '$id': '4554colle_ma40a_ki_n_7',
        'Name': 'ma40aCollectionPoint4554',
        'Location Near': 2318,
        'Story Pre-Req': [8],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 154
        }
    ma40aCollectionPoint4555 = {
        '$id': '4555colle_ma40a_ki_n_8',
        'Name': 'ma40aCollectionPoint4555',
        'Location Near': 2318,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 155
        }
    ma40aCollectionPoint4556 = {
        '$id': '4556colle_ma40a_ki_n_9',
        'Name': 'ma40aCollectionPoint4556',
        'Location Near': 2303,
        'Story Pre-Req': [8],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 156
        }
    ma40aCollectionPoint4557 = {
        '$id': '4557colle_ma40a_ki_r_1',
        'Name': 'ma40aCollectionPoint4557',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 157
        }
    ma40aCollectionPoint4558 = {
        '$id': '4558colle_ma40a_ki_r_2',
        'Name': 'ma40aCollectionPoint4558',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 158
        }
    ma40aCollectionPoint4559 = {
        '$id': '4559colle_ma40a_ki_r_3',
        'Name': 'ma40aCollectionPoint4559',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 159
        }
    ma40aCollectionPoint4560 = {
        '$id': '4560colle_ma40a_ki2_n_1',
        'Name': 'ma40aCollectionPoint4560',
        'Location Near': 2305,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 160
        }
    ma40aCollectionPoint4561 = {
        '$id': '4561colle_ma40a_ki2_n_2',
        'Name': 'ma40aCollectionPoint4561',
        'Location Near': 2305,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 161
        }
    ma40aCollectionPoint4562 = {
        '$id': '4562colle_ma40a_ki2_n_3',
        'Name': 'ma40aCollectionPoint4562',
        'Location Near': 2322,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 162
        }
    ma40aCollectionPoint4563 = {
        '$id': '4563colle_ma40a_ki2_n_4',
        'Name': 'ma40aCollectionPoint4563',
        'Location Near': 2307,
        'Story Pre-Req': [33],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 163
        }
    ma40aCollectionPoint4564 = {
        '$id': '4564colle_ma40a_ki2_n_5',
        'Name': 'ma40aCollectionPoint4564',
        'Location Near': 2305,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 164
        }
    ma40aCollectionPoint4565 = {
        '$id': '4565colle_ma40a_ki2_n_6',
        'Name': 'ma40aCollectionPoint4565',
        'Location Near': 2305,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 165
        }
    ma40aCollectionPoint4566 = {
        '$id': '4566colle_ma40a_ki2_n_7',
        'Name': 'ma40aCollectionPoint4566',
        'Location Near': 2327,
        'Story Pre-Req': [24],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 166
        }
    ma40aCollectionPoint4567 = {
        '$id': '4567colle_ma40a_ki2_r_1',
        'Name': 'ma40aCollectionPoint4567',
        'Location Near': 2322,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 167
        }
    ma40aCollectionPoint4568 = {
        '$id': '4568colle_ma40a_ki2_r_2',
        'Name': 'ma40aCollectionPoint4568',
        'Location Near': 2309,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 168
        }
    ma40aCollectionPoint4569 = {
        '$id': '4569colle_ma40a_ki2_r_3',
        'Name': 'ma40aCollectionPoint4569',
        'Location Near': 2305,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 169
        }
    ma40aCollectionPoint4570 = {
        '$id': '4570colle_ma40a_ki3_n_1',
        'Name': 'ma40aCollectionPoint4570',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 170
        }
    ma40aCollectionPoint4571 = {
        '$id': '4571colle_ma40a_ki3_n_2',
        'Name': 'ma40aCollectionPoint4571',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 171
        }
    ma40aCollectionPoint4572 = {
        '$id': '4572colle_ma40a_ki3_n_3',
        'Name': 'ma40aCollectionPoint4572',
        'Location Near': 2337,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 172
        }
    ma40aCollectionPoint4573 = {
        '$id': '4573colle_ma40a_ki3_n_4',
        'Name': 'ma40aCollectionPoint4573',
        'Location Near': 2337,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 173
        }
    ma40aCollectionPoint4574 = {
        '$id': '4574colle_ma40a_ki3_n_5',
        'Name': 'ma40aCollectionPoint4574',
        'Location Near': 2357,
        'Story Pre-Req': [36],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 174
        }
    ma40aCollectionPoint4575 = {
        '$id': '4575colle_ma40a_ki3_n_6',
        'Name': 'ma40aCollectionPoint4575',
        'Location Near': 2337,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 175
        }
    ma40aCollectionPoint4576 = {
        '$id': '4576colle_ma40a_ki3_n_7',
        'Name': 'ma40aCollectionPoint4576',
        'Location Near': 2337,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 176
        }
    ma40aCollectionPoint4577 = {
        '$id': '4577colle_ma40a_ki3_n_8',
        'Name': 'ma40aCollectionPoint4577',
        'Location Near': 2335,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 177
        }
    ma40aCollectionPoint4578 = {
        '$id': '4578colle_ma40a_ki3_r_1',
        'Name': 'ma40aCollectionPoint4578',
        'Location Near': 2337,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 178
        }
    ma40aCollectionPoint4579 = {
        '$id': '4579colle_ma40a_ki3_r_2',
        'Name': 'ma40aCollectionPoint4579',
        'Location Near': 2314,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 179
        }
    ma40aCollectionPoint4580 = {
        '$id': '4580colle_ma40a_ki3_r_3',
        'Name': 'ma40aCollectionPoint4580',
        'Location Near': 2311,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 180
        }
    ma40aCollectionPoint4581 = {
        '$id': '4581colle_ma40a_ki3_r_4',
        'Name': 'ma40aCollectionPoint4581',
        'Location Near': 2311,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 181
        }
    ma40aCollectionPoint4582 = {
        '$id': '4582colle_ma40a_musi_n_1',
        'Name': 'ma40aCollectionPoint4582',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 182
        }
    ma40aCollectionPoint4583 = {
        '$id': '4583colle_ma40a_musi_n_2',
        'Name': 'ma40aCollectionPoint4583',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 183
        }
    ma40aCollectionPoint4584 = {
        '$id': '4584colle_ma40a_musi_n_3',
        'Name': 'ma40aCollectionPoint4584',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 184
        }
    ma40aCollectionPoint4585 = {
        '$id': '4585colle_ma40a_musi_n_4',
        'Name': 'ma40aCollectionPoint4585',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 185
        }
    ma40aCollectionPoint4586 = {
        '$id': '4586colle_ma40a_musi_n_5',
        'Name': 'ma40aCollectionPoint4586',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 186
        }
    ma40aCollectionPoint4587 = {
        '$id': '4587colle_ma40a_musi_n_6',
        'Name': 'ma40aCollectionPoint4587',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 187
        }
    ma40aCollectionPoint4588 = {
        '$id': '4588colle_ma40a_musi_n_7',
        'Name': 'ma40aCollectionPoint4588',
        'Location Near': 2302,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 188
        }
    ma40aCollectionPoint4589 = {
        '$id': '4589colle_ma40a_musi_n_8',
        'Name': 'ma40aCollectionPoint4589',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 189
        }
    ma40aCollectionPoint4590 = {
        '$id': '4590colle_ma40a_musi_r_1',
        'Name': 'ma40aCollectionPoint4590',
        'Location Near': 2303,
        'Story Pre-Req': [8],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 190
        }
    ma40aCollectionPoint4591 = {
        '$id': '4591colle_ma40a_musi_r_2',
        'Name': 'ma40aCollectionPoint4591',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 191
        }
    ma40aCollectionPoint4592 = {
        '$id': '4592colle_ma40a_musi2_n_1',
        'Name': 'ma40aCollectionPoint4592',
        'Location Near': 2326,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 192
        }
    ma40aCollectionPoint4593 = {
        '$id': '4593colle_ma40a_musi2_n_2',
        'Name': 'ma40aCollectionPoint4593',
        'Location Near': 2323,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 193
        }
    ma40aCollectionPoint4594 = {
        '$id': '4594colle_ma40a_musi2_n_3',
        'Name': 'ma40aCollectionPoint4594',
        'Location Near': 2324,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 194
        }
    ma40aCollectionPoint4595 = {
        '$id': '4595colle_ma40a_musi2_n_4',
        'Name': 'ma40aCollectionPoint4595',
        'Location Near': 2325,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 195
        }
    ma40aCollectionPoint4596 = {
        '$id': '4596colle_ma40a_musi2_n_5',
        'Name': 'ma40aCollectionPoint4596',
        'Location Near': 2326,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 196
        }
    ma40aCollectionPoint4597 = {
        '$id': '4597colle_ma40a_musi2_n_6',
        'Name': 'ma40aCollectionPoint4597',
        'Location Near': 2309,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 197
        }
    ma40aCollectionPoint4598 = {
        '$id': '4598colle_ma40a_musi2_n_7',
        'Name': 'ma40aCollectionPoint4598',
        'Location Near': 2307,
        'Story Pre-Req': [33],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 198
        }
    ma40aCollectionPoint4599 = {
        '$id': '4599colle_ma40a_musi2_n_8',
        'Name': 'ma40aCollectionPoint4599',
        'Location Near': 2329,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 199
        }
    ma40aCollectionPoint4601 = {
        '$id': '4601colle_ma40a_musi2_r_1',
        'Name': 'ma40aCollectionPoint4601',
        'Location Near': 2325,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 201
        }
    ma40aCollectionPoint4602 = {
        '$id': '4602colle_ma40a_musi2_r_2',
        'Name': 'ma40aCollectionPoint4602',
        'Location Near': 2307,
        'Story Pre-Req': [33],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 202
        }
    ma40aCollectionPoint4603 = {
        '$id': '4603colle_ma40a_musi2_r_3',
        'Name': 'ma40aCollectionPoint4603',
        'Location Near': 2308,
        'Story Pre-Req': [25],
        'Required Items': [TornaSlatePieceIDs[:9]],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 203
        }
    ma40aCollectionPoint4604 = {
        '$id': '4604colle_ma40a_musi3_n_1',
        'Name': 'ma40aCollectionPoint4604',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 204
        }
    ma40aCollectionPoint4605 = {
        '$id': '4605colle_ma40a_musi3_n_2',
        'Name': 'ma40aCollectionPoint4605',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 205
        }
    ma40aCollectionPoint4606 = {
        '$id': '4606colle_ma40a_musi3_n_3',
        'Name': 'ma40aCollectionPoint4606',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 206
        }
    ma40aCollectionPoint4607 = {
        '$id': '4607colle_ma40a_musi3_n_4',
        'Name': 'ma40aCollectionPoint4607',
        'Location Near': 2335,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 207
        }
    ma40aCollectionPoint4608 = {
        '$id': '4608colle_ma40a_musi3_n_5',
        'Name': 'ma40aCollectionPoint4608',
        'Location Near': 2331,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 208
        }
    ma40aCollectionPoint4609 = {
        '$id': '4609colle_ma40a_musi3_n_6',
        'Name': 'ma40aCollectionPoint4609',
        'Location Near': 2310,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [1661],
        'Rarity': 0,
        'CollectionTableID': 209
        }
    ma40aCollectionPoint4610 = {
        '$id': '4610colle_ma40a_musi3_n_7',
        'Name': 'ma40aCollectionPoint4610',
        'Location Near': 2361,
        'Story Pre-Req': [36],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 210
        }
    ma40aCollectionPoint4611 = {
        '$id': '4611colle_ma40a_musi3_r_1',
        'Name': 'ma40aCollectionPoint4611',
        'Location Near': 2331,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 211
        }
    ma40aCollectionPoint4612 = {
        '$id': '4612colle_ma40a_musi3_r_2',
        'Name': 'ma40aCollectionPoint4612',
        'Location Near': 2314,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 212
        }
    ma40aCollectionPoint4613 = {
        '$id': '4613colle_ma40a_musi3_r_3',
        'Name': 'ma40aCollectionPoint4613',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [HazeKey, ManipEtherKey, HazeAff[:2] , AegaeonKey, ComWaterKey, AegaeonAff],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 213
        }
    ma40aCollectionPoint4614 = {
        '$id': '4614colle_ma40a_musi3_r_4',
        'Name': 'ma40aCollectionPoint4614',
        'Location Near': 2368,
        'Story Pre-Req': [53],
        'Required Items': [TornaSlatePieceIDs],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 214
        }
    ma40aCollectionPoint4615 = {
        '$id': '4615colle_ma40a_musi3_r_5',
        'Name': 'ma40aCollectionPoint4615',
        'Location Near': 2310,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 215
        }
    ma40aCollectionPoint4616 = {
        '$id': '4616colle_ma40a_sakana_n_1',
        'Name': 'ma40aCollectionPoint4616',
        'Location Near': 2301,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 216
        }
    ma40aCollectionPoint4617 = {
        '$id': '4617colle_ma40a_sakana_n_3',
        'Name': 'ma40aCollectionPoint4617',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 217
        }
    ma40aCollectionPoint4618 = {
        '$id': '4618colle_ma40a_sakana_n_4',
        'Name': 'ma40aCollectionPoint4618',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 218
        }
    ma40aCollectionPoint4619 = {
        '$id': '4619colle_ma40a_sakana_n_5',
        'Name': 'ma40aCollectionPoint4619',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 219
        }
    ma40aCollectionPoint4620 = {
        '$id': '4620colle_ma40a_sakana_n_6',
        'Name': 'ma40aCollectionPoint4620',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 220
        }
    ma40aCollectionPoint4621 = {
        '$id': '4621colle_ma40a_sakana_n_8',
        'Name': 'ma40aCollectionPoint4621',
        'Location Near': 2303,
        'Story Pre-Req': [8],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 221
        }
    ma40aCollectionPoint4622 = {
        '$id': '4622colle_ma40a_sakana_r_1',
        'Name': 'ma40aCollectionPoint4622',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 222
        }
    ma40aCollectionPoint4623 = {
        '$id': '4623colle_ma40a_sakana_r_2',
        'Name': 'ma40aCollectionPoint4623',
        'Location Near': 2317,
        'Story Pre-Req': [5],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 223
        }
    ma40aCollectionPoint4624 = {
        '$id': '4624colle_ma40a_sakana2_n_2',
        'Name': 'ma40aCollectionPoint4624',
        'Location Near': 2326,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 224
        }
    ma40aCollectionPoint4625 = {
        '$id': '4625colle_ma40a_sakana2_n_3',
        'Name': 'ma40aCollectionPoint4625',
        'Location Near': 2326,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 225
        }
    ma40aCollectionPoint4626 = {
        '$id': '4626colle_ma40a_sakana2_n_4',
        'Name': 'ma40aCollectionPoint4626',
        'Location Near': 2324,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 226
        }
    ma40aCollectionPoint4627 = {
        '$id': '4627colle_ma40a_sakana2_n_5',
        'Name': 'ma40aCollectionPoint4627',
        'Location Near': 2309,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 227
        }
    ma40aCollectionPoint4628 = {
        '$id': '4628colle_ma40a_sakana2_n_6',
        'Name': 'ma40aCollectionPoint4628',
        'Location Near': 2322,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 228
        }
    ma40aCollectionPoint4629 = {
        '$id': '4629colle_ma40a_sakana2_n_7',
        'Name': 'ma40aCollectionPoint4629',
        'Location Near': 2322,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 229
        }
    ma40aCollectionPoint4630 = {
        '$id': '4630colle_ma40a_sakana2_r_1',
        'Name': 'ma40aCollectionPoint4630',
        'Location Near': 2313,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 230
        }
    ma40aCollectionPoint4631 = {
        '$id': '4631colle_ma40a_sakana2_r_2',
        'Name': 'ma40aCollectionPoint4631',
        'Location Near': 2324,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 231
        }
    ma40aCollectionPoint4632 = {
        '$id': '4632colle_ma40a_sakana3_n_1',
        'Name': 'ma40aCollectionPoint4632',
        'Location Near': 2335,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 232
        }
    ma40aCollectionPoint4633 = {
        '$id': '4633colle_ma40a_sakana3_n_2',
        'Name': 'ma40aCollectionPoint4633',
        'Location Near': 2335,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 233
        }
    ma40aCollectionPoint4634 = {
        '$id': '4634colle_ma40a_sakana3_n_3',
        'Name': 'ma40aCollectionPoint4634',
        'Location Near': 2334,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 234
        }
    ma40aCollectionPoint4635 = {
        '$id': '4635colle_ma40a_sakana3_n_4',
        'Name': 'ma40aCollectionPoint4635',
        'Location Near': 2334,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 235
        }
    ma40aCollectionPoint4636 = {
        '$id': '4636colle_ma40a_sakana3_n_5',
        'Name': 'ma40aCollectionPoint4636',
        'Location Near': 2334,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 236
        }
    ma40aCollectionPoint4637 = {
        '$id': '4637colle_ma40a_sakana3_n_6',
        'Name': 'ma40aCollectionPoint4637',
        'Location Near': 2351,
        'Story Pre-Req': [36],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 237
        }
    ma40aCollectionPoint4638 = {
        '$id': '4638colle_ma40a_sakana3_n_7',
        'Name': 'ma40aCollectionPoint4638',
        'Location Near': 2363,
        'Story Pre-Req': [36],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 238
        }
    ma40aCollectionPoint4640 = {
        '$id': '4640colle_ma40a_sakana3_r_2',
        'Name': 'ma40aCollectionPoint4640',
        'Location Near': 2335,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 240
        }
    ma40aCollectionPoint4641 = {
        '$id': '4641colle_ma40a_sakana3_r_3',
        'Name': 'ma40aCollectionPoint4641',
        'Location Near': 2314,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 241
        }
    ma40aCollectionPoint4642 = {
        '$id': '4642colle_ma40a_sakana3_r_4',
        'Name': 'ma40aCollectionPoint4642',
        'Location Near': 2310,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 242
        }
    ma40aCollectionPoint4643 = {
        '$id': '4643colle_ma40a_sabaku_ex_1',
        'Name': 'ma40aCollectionPoint4643',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 243
        }
    ma40aCollectionPoint4644 = {
        '$id': '4644colle_ma40a_sabaku_ex_2',
        'Name': 'ma40aCollectionPoint4644',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 244
        }
    ma40aCollectionPoint4646 = {
        '$id': '4646colle_ma40a_sabaku_ex_4',
        'Name': 'ma40aCollectionPoint4646',
        'Location Near': 2335,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 246
        }
    ma40aCollectionPoint4647 = {
        '$id': '4647colle_ma40a_sabaku_ex_5',
        'Name': 'ma40aCollectionPoint4647',
        'Location Near': 2331,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 247
        }
    ma40aCollectionPoint4648 = {
        '$id': '4648colle_ma40a_sabaku_ex_6',
        'Name': 'ma40aCollectionPoint4648',
        'Location Near': 2334,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 248
        }
    ma40aCollectionPoint4649 = {
        '$id': '4649colle_ma40a_sabaku_ex_7',
        'Name': 'ma40aCollectionPoint4649',
        'Location Near': 2334,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 249
        }
    ma40aCollectionPoint4650 = {
        '$id': '4650colle_ma40a_sabaku_ex_8',
        'Name': 'ma40aCollectionPoint4650',
        'Location Near': 2330,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 250
        }
    ma40aCollectionPoint4651 = {
        '$id': '4651colle_ma40a_sabaku_ex_9',
        'Name': 'ma40aCollectionPoint4651',
        'Location Near': 2337,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 251
        }
    ma40aCollectionPoint4652 = {
        '$id': '4652colle_ma40a_rain_ex_1',
        'Name': 'ma40aCollectionPoint4652',
        'Location Near': 2337,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 252
        }
    ma40aCollectionPoint4653 = {
        '$id': '4653colle_ma40a_rain_ex_2',
        'Name': 'ma40aCollectionPoint4653',
        'Location Near': 2337,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 253
        }
    ma40aCollectionPoint4654 = {
        '$id': '4654colle_ma40a_rain_ex_3',
        'Name': 'ma40aCollectionPoint4654',
        'Location Near': 2337,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 254
        }
    ma40aCollectionPoint4655 = {
        '$id': '4655colle_ma40a_rain_ex_4',
        'Name': 'ma40aCollectionPoint4655',
        'Location Near': 2311,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 255
        }
    ma40aCollectionPoint4656 = {
        '$id': '4656colle_ma40a_rain_ex_5',
        'Name': 'ma40aCollectionPoint4656',
        'Location Near': 2311,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 256
        }
    ma40aCollectionPoint4657 = {
        '$id': '4657colle_ma40a_rain_ex_6',
        'Name': 'ma40aCollectionPoint4657',
        'Location Near': 2311,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 257
        }
    ma40aCollectionPoint4658 = {
        '$id': '4658colle_ma40a_rain_ex_7',
        'Name': 'ma40aCollectionPoint4658',
        'Location Near': 2311,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 258
        }
    ma40aCollectionPoint4659 = {
        '$id': '4659colle_ma40a_rain2_ex_1',
        'Name': 'ma40aCollectionPoint4659',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 259
        }
    ma40aCollectionPoint4660 = {
        '$id': '4660colle_ma40a_rain2_ex_2',
        'Name': 'ma40aCollectionPoint4660',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 260
        }
    ma40aCollectionPoint4661 = {
        '$id': '4661colle_ma40a_rain2_ex_3',
        'Name': 'ma40aCollectionPoint4661',
        'Location Near': 2301,
        'Story Pre-Req': [2],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 261
        }
    ma40aCollectionPoint4662 = {
        '$id': '4662colle_ma40a_rain3_ex_1',
        'Name': 'ma40aCollectionPoint4662',
        'Location Near': 2324,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 262
        }
    ma40aCollectionPoint4663 = {
        '$id': '4663colle_ma40a_rain3_ex_2',
        'Name': 'ma40aCollectionPoint4663',
        'Location Near': 2306,
        'Story Pre-Req': [29],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 263
        }
    ma40aCollectionPoint4664 = {
        '$id': '4664colle_ma40a_rain3_ex_3',
        'Name': 'ma40aCollectionPoint4664',
        'Location Near': 2306,
        'Story Pre-Req': [25],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 264
        }
    ma40aCollectionPoint4666 = {
        '$id': '4666colle_ma40a_qst7015_001',
        'Name': 'ma40aCollectionPoint4666',
        'Location Near': 2311,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 266
        }
    ma40aCollectionPoint4667 = {
        '$id': '4667colle_ma40a_qst7015_002',
        'Name': 'ma40aCollectionPoint4667',
        'Location Near': 2311,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 267
        }
    ma40aCollectionPoint4668 = {
        '$id': '4668colle_ma40a_qst7015_003',
        'Name': 'ma40aCollectionPoint4668',
        'Location Near': 2311,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 268
        }
    ma40aCollectionPoint4669 = {
        '$id': '4669colle_ma40a_qst7015_004',
        'Name': 'ma40aCollectionPoint4669',
        'Location Near': 2311,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 269
        }
    ma40aCollectionPoint4670 = {
        '$id': '4670colle_ma40a_qst7018_001',
        'Name': 'ma40aCollectionPoint4670',
        'Location Near': 2331,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 270
        }
    ma40aCollectionPoint4671 = {
        '$id': '4671colle_ma40a_qst7018_002',
        'Name': 'ma40aCollectionPoint4671',
        'Location Near': 2331,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 271
        }
    ma40aCollectionPoint4672 = {
        '$id': '4672colle_ma40a_qst7018_003',
        'Name': 'ma40aCollectionPoint4672',
        'Location Near': 2331,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 272
        }
    ma40aCollectionPoint4673 = {
        '$id': '4673colle_ma40a_qst7014_006',
        'Name': 'ma40aCollectionPoint4673',
        'Location Near': 2333,
        'Story Pre-Req': [35],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 273
        }
    ma41aCollectionPoint4651 = {
	'$id': '4651colle_ma41a_f004',
	'Name': 'ma40aCollectionPoint4651',
	'Location Near': 2412,
	'Story Pre-Req': [12],
	'Required Items': [],
	'Must Defeat Enemy IDs': [],
	'Rarity': 1,
	'CollectionTableID': 279
    }
    ma41aCollectionPoint4652 = {
        '$id': '4652colle_ma41a_f005',
        'Name': 'ma40aCollectionPoint4652',
        'Location Near': 2416,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 280
    }
    ma41aCollectionPoint4653 = {
        '$id': '4653colle_ma41a_f006',
        'Name': 'ma40aCollectionPoint4653',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 281
    }
    ma41aCollectionPoint4654 = {
        '$id': '4654colle_ma41a_f007',
        'Name': 'ma40aCollectionPoint4654',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 282
    }
    ma41aCollectionPoint4655 = {
        '$id': '4655colle_ma41a_f008',
        'Name': 'ma40aCollectionPoint4655',
        'Location Near': 2406,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 283
    }
    ma41aCollectionPoint4656 = {
        '$id': '4656colle_ma41a_f009',
        'Name': 'ma40aCollectionPoint4656',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 284
    }
    ma41aCollectionPoint4657 = {
        '$id': '4657colle_ma41a_f010',
        'Name': 'ma40aCollectionPoint4657',
        'Location Near': 2416,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 285
    }
    ma41aCollectionPoint4658 = {
        '$id': '4658colle_ma41a_f011',
        'Name': 'ma40aCollectionPoint4658',
        'Location Near': 2428,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 286
    }
    ma41aCollectionPoint4659 = {
        '$id': '4659colle_ma41a_f012',
        'Name': 'ma40aCollectionPoint4659',
        'Location Near': 2416,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 287
    }
    ma41aCollectionPoint4660 = {
        '$id': '4660colle_ma41a_f015',
        'Name': 'ma40aCollectionPoint4660',
        'Location Near': 2416,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 288
    }
    ma41aCollectionPoint4661 = {
        '$id': '4661colle_ma41a_f016',
        'Name': 'ma40aCollectionPoint4661',
        'Location Near': 2402,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 289
    }
    ma41aCollectionPoint4662 = {
        '$id': '4662colle_ma41a_f017',
        'Name': 'ma40aCollectionPoint4662',
        'Location Near': 2428,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 290
    }
    ma41aCollectionPoint4663 = {
        '$id': '4663colle_ma41a_f018',
        'Name': 'ma40aCollectionPoint4663',
        'Location Near': 2416,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 291
    }
    ma41aCollectionPoint4664 = {
        '$id': '4664colle_ma41a_f019',
        'Name': 'ma40aCollectionPoint4664',
        'Location Near': 2418,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 292
    }
    ma41aCollectionPoint4665 = {
        '$id': '4665colle_ma41a_f020',
        'Name': 'ma40aCollectionPoint4665',
        'Location Near': 2425,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 293
    }
    ma41aCollectionPoint4666 = {
        '$id': '4666colle_ma41a_f021',
        'Name': 'ma40aCollectionPoint4666',
        'Location Near': 2416,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 294
    }
    ma41aCollectionPoint4667 = {
        '$id': '4667colle_ma41a_f022',
        'Name': 'ma40aCollectionPoint4667',
        'Location Near': 2416,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 295
    }
    ma41aCollectionPoint4668 = {
        '$id': '4668colle_ma41a_f023',
        'Name': 'ma40aCollectionPoint4668',
        'Location Near': 2402,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 296
    }
    ma41aCollectionPoint4669 = {
        '$id': '4669colle_ma41a_f024',
        'Name': 'ma40aCollectionPoint4669',
        'Location Near': 2417,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 297
    }
    ma41aCollectionPoint4670 = {
        '$id': '4670colle_ma41a_f026',
        'Name': 'ma40aCollectionPoint4670',
        'Location Near': 2420,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 298
    }
    ma41aCollectionPoint4671 = {
        '$id': '4671colle_ma41a_f027',
        'Name': 'ma40aCollectionPoint4671',
        'Location Near': 2428,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 299
    }
    ma41aCollectionPoint4672 = {
        '$id': '4672colle_ma41a_f028',
        'Name': 'ma40aCollectionPoint4672',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 300
    }
    ma41aCollectionPoint4673 = {
        '$id': '4673colle_ma41a_f029',
        'Name': 'ma40aCollectionPoint4673',
        'Location Near': 2422,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [1564],
        'Rarity': 1,
        'CollectionTableID': 301
    }
    ma41aCollectionPoint4674 = {
        '$id': '4674colle_ma41a_f030',
        'Name': 'ma40aCollectionPoint4674',
        'Location Near': 2417,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 302
    }
    ma41aCollectionPoint4675 = {
        '$id': '4675colle_ma41a_f032',
        'Name': 'ma40aCollectionPoint4675',
        'Location Near': 2414,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 303
    }
    ma41aCollectionPoint4676 = {
        '$id': '4676colle_ma41a_f033',
        'Name': 'ma40aCollectionPoint4676',
        'Location Near': 2420,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 304
    }
    ma41aCollectionPoint4677 = {
        '$id': '4677colle_ma41a_f034',
        'Name': 'ma40aCollectionPoint4677',
        'Location Near': 2425,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 305
    }
    ma41aCollectionPoint4678 = {
        '$id': '4678colle_ma41a_f035',
        'Name': 'ma40aCollectionPoint4678',
        'Location Near': 2408,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 306
    }
    ma41aCollectionPoint4679 = {
        '$id': '4679colle_ma41a_f036',
        'Name': 'ma40aCollectionPoint4679',
        'Location Near': 2422,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 307
    }
    ma41aCollectionPoint4680 = {
        '$id': '4680colle_ma41a_f037',
        'Name': 'ma40aCollectionPoint4680',
        'Location Near': 2402,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 308
    }
    ma41aCollectionPoint4681 = {
        '$id': '4681colle_ma41a_f038',
        'Name': 'ma40aCollectionPoint4681',
        'Location Near': 2401,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 309
    }
    ma41aCollectionPoint4682 = {
        '$id': '4682colle_ma41a_f039',
        'Name': 'ma40aCollectionPoint4682',
        'Location Near': 2408,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 310
    }
    ma41aCollectionPoint4683 = {
        '$id': '4683colle_ma41a_f040',
        'Name': 'ma40aCollectionPoint4683',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 311
    }
    ma41aCollectionPoint4684 = {
        '$id': '4684colle_ma41a_f041',
        'Name': 'ma40aCollectionPoint4684',
        'Location Near': 2401,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 312
    }
    ma41aCollectionPoint4685 = {
        '$id': '4685colle_ma41a_f043',
        'Name': 'ma40aCollectionPoint4685',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 313
    }
    ma41aCollectionPoint4686 = {
        '$id': '4686colle_ma41a_f044',
        'Name': 'ma40aCollectionPoint4686',
        'Location Near': 2425,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 314
    }
    ma41aCollectionPoint4687 = {
        '$id': '4687colle_ma41a_f045',
        'Name': 'ma40aCollectionPoint4687',
        'Location Near': 2428,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 315
    }
    ma41aCollectionPoint4688 = {
        '$id': '4688colle_ma41a_f047',
        'Name': 'ma40aCollectionPoint4688',
        'Location Near': 2416,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 316
    }
    ma41aCollectionPoint4689 = {
        '$id': '4689colle_ma41a_f048',
        'Name': 'ma40aCollectionPoint4689',
        'Location Near': 2408,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 317
    }
    ma41aCollectionPoint4690 = {
        '$id': '4690colle_ma41a_f051',
        'Name': 'ma40aCollectionPoint4690',
        'Location Near': 2401,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 318
    }
    ma41aCollectionPoint4691 = {
        '$id': '4691colle_ma41a_f052',
        'Name': 'ma40aCollectionPoint4691',
        'Location Near': 2417,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 319
    }
    ma41aCollectionPoint4692 = {
        '$id': '4692colle_ma41a_f055',
        'Name': 'ma40aCollectionPoint4692',
        'Location Near': 2425,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 320
    }
    ma41aCollectionPoint4693 = {
        '$id': '4693colle_ma41a_f056',
        'Name': 'ma40aCollectionPoint4693',
        'Location Near': 2408,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 321
    }
    ma41aCollectionPoint4694 = {
        '$id': '4694colle_ma41a_f058',
        'Name': 'ma40aCollectionPoint4694',
        'Location Near': 2409,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 322
    }
    ma41aCollectionPoint4695 = {
        '$id': '4695colle_ma41a_f059',
        'Name': 'ma40aCollectionPoint4695',
        'Location Near': 2428,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 323
    }
    ma41aCollectionPoint4696 = {
        '$id': '4696colle_ma41a_f060',
        'Name': 'ma40aCollectionPoint4696',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 324
    }
    ma41aCollectionPoint4697 = {
        '$id': '4697colle_ma41a_f061',
        'Name': 'ma40aCollectionPoint4697',
        'Location Near': 2422,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 325
    }
    ma41aCollectionPoint4698 = {
        '$id': '4698colle_ma41a_f062',
        'Name': 'ma40aCollectionPoint4698',
        'Location Near': 2424,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 326
    }
    ma41aCollectionPoint4699 = {
        '$id': '4699colle_ma41a_f063',
        'Name': 'ma40aCollectionPoint4699',
        'Location Near': 2417,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 327
    }
    ma41aCollectionPoint4700 = {
        '$id': '4700colle_ma41a_f064',
        'Name': 'ma40aCollectionPoint4700',
        'Location Near': 2416,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 328
    }
    ma41aCollectionPoint4701 = {
        '$id': '4701colle_ma41a_f065',
        'Name': 'ma40aCollectionPoint4701',
        'Location Near': 2415,
        'Story Pre-Req': [16],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 329
    }
    ma41aCollectionPoint4702 = {
        '$id': '4702colle_ma41a_f066',
        'Name': 'ma40aCollectionPoint4702',
        'Location Near': 2419,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 330
    }
    ma41aCollectionPoint4703 = {
        '$id': '4703colle_ma41a_f067',
        'Name': 'ma40aCollectionPoint4703',
        'Location Near': 2408,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 331
    }
    ma41aCollectionPoint4704 = {
        '$id': '4704colle_ma41a_f069',
        'Name': 'ma40aCollectionPoint4704',
        'Location Near': 2415,
        'Story Pre-Req': [16],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 332
    }
    ma41aCollectionPoint4705 = {
        '$id': '4705colle_ma41a_f070',
        'Name': 'ma40aCollectionPoint4705',
        'Location Near': 2414,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 333
    }
    ma41aCollectionPoint4706 = {
        '$id': '4706colle_ma41a_f071',
        'Name': 'ma40aCollectionPoint4706',
        'Location Near': 2408,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 334
    }
    ma41aCollectionPoint4707 = {
        '$id': '4707colle_ma41a_f072',
        'Name': 'ma40aCollectionPoint4707',
        'Location Near': 2428,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 335
    }
    ma41aCollectionPoint4708 = {
        '$id': '4708colle_ma41a_f073',
        'Name': 'ma40aCollectionPoint4708',
        'Location Near': 2401,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 336
    }
    ma41aCollectionPoint4709 = {
        '$id': '4709colle_ma41a_f076',
        'Name': 'ma40aCollectionPoint4709',
        'Location Near': 2419,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 337
    }
    ma41aCollectionPoint4710 = {
        '$id': '4710colle_ma41a_f077',
        'Name': 'ma40aCollectionPoint4710',
        'Location Near': 2419,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 338
    }
    ma41aCollectionPoint4711 = {
        '$id': '4711colle_ma41a_f078',
        'Name': 'ma40aCollectionPoint4711',
        'Location Near': 2422,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 339
    }
    ma41aCollectionPoint4712 = {
        '$id': '4712colle_ma41a_f079',
        'Name': 'ma40aCollectionPoint4712',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 340
    }
    ma41aCollectionPoint4713 = {
        '$id': '4713colle_ma41a_f081',
        'Name': 'ma40aCollectionPoint4713',
        'Location Near': 2422,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [1564],
        'Rarity': 0,
        'CollectionTableID': 341
    }
    ma41aCollectionPoint4714 = {
        '$id': '4714colle_ma41a_f082',
        'Name': 'ma40aCollectionPoint4714',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 342
    }
    ma41aCollectionPoint4715 = {
        '$id': '4715colle_ma41a_f083',
        'Name': 'ma40aCollectionPoint4715',
        'Location Near': 2417,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 343
    }
    ma41aCollectionPoint4716 = {
        '$id': '4716colle_ma41a_f085',
        'Name': 'ma40aCollectionPoint4716',
        'Location Near': 2419,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 344
    }
    ma41aCollectionPoint4717 = {
        '$id': '4717colle_ma41a_f086',
        'Name': 'ma40aCollectionPoint4717',
        'Location Near': 2419,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 345
    }
    ma41aCollectionPoint4718 = {
        '$id': '4718colle_ma41a_f087',
        'Name': 'ma40aCollectionPoint4718',
        'Location Near': 2417,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 346
    }
    ma41aCollectionPoint4719 = {
        '$id': '4719colle_ma41a_f088',
        'Name': 'ma40aCollectionPoint4719',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 347
    }
    ma41aCollectionPoint4720 = {
        '$id': '4720colle_ma41a_f089',
        'Name': 'ma40aCollectionPoint4720',
        'Location Near': 2406,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 348
    }
    ma41aCollectionPoint4721 = {
        '$id': '4721colle_ma41a_f090',
        'Name': 'ma40aCollectionPoint4721',
        'Location Near': 2405,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 349
    }
    ma41aCollectionPoint4722 = {
        '$id': '4722colle_ma41a_f091',
        'Name': 'ma40aCollectionPoint4722',
        'Location Near': 2411,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 350
    }
    ma41aCollectionPoint4723 = {
        '$id': '4723colle_ma41a_f092',
        'Name': 'ma40aCollectionPoint4723',
        'Location Near': 2405,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 351
    }
    ma41aCollectionPoint4724 = {
        '$id': '4724colle_ma41a_f093',
        'Name': 'ma40aCollectionPoint4724',
        'Location Near': 2411,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 352
    }
    ma41aCollectionPoint4725 = {
        '$id': '4725colle_ma41a_f094',
        'Name': 'ma40aCollectionPoint4725',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 353
    }
    ma41aCollectionPoint4726 = {
        '$id': '4726colle_ma41a_f097',
        'Name': 'ma40aCollectionPoint4726',
        'Location Near': 2428,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 354
    }
    ma41aCollectionPoint4727 = {
        '$id': '4727colle_ma41a_f098',
        'Name': 'ma40aCollectionPoint4727',
        'Location Near': 2411,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 355
    }
    ma41aCollectionPoint4728 = {
        '$id': '4728colle_ma41a_f099',
        'Name': 'ma40aCollectionPoint4728',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 356
    }
    ma41aCollectionPoint4729 = {
        '$id': '4729colle_ma41a_f100',
        'Name': 'ma40aCollectionPoint4729',
        'Location Near': 2409,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 357
    }
    ma41aCollectionPoint4730 = {
        '$id': '4730colle_ma41a_f101',
        'Name': 'ma40aCollectionPoint4730',
        'Location Near': 2420,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 358
    }
    ma41aCollectionPoint4731 = {
        '$id': '4731colle_ma41a_f102',
        'Name': 'ma40aCollectionPoint4731',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 359
    }
    ma41aCollectionPoint4732 = {
        '$id': '4732colle_ma41a_f104',
        'Name': 'ma40aCollectionPoint4732',
        'Location Near': 2418,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 360
    }
    ma41aCollectionPoint4733 = {
        '$id': '4733colle_ma41a_f106',
        'Name': 'ma40aCollectionPoint4733',
        'Location Near': 2417,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 361
    }
    ma41aCollectionPoint4734 = {
        '$id': '4734colle_ma41a_f111',
        'Name': 'ma40aCollectionPoint4734',
        'Location Near': 2425,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 362
    }
    ma41aCollectionPoint4735 = {
        '$id': '4735colle_ma41a_f112',
        'Name': 'ma40aCollectionPoint4735',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 363
    }
    ma41aCollectionPoint4736 = {
        '$id': '4736colle_ma41a_f113',
        'Name': 'ma40aCollectionPoint4736',
        'Location Near': 2403,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 364
    }
    ma41aCollectionPoint4737 = {
        '$id': '4737colle_ma41a_f114',
        'Name': 'ma40aCollectionPoint4737',
        'Location Near': 2414,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 365
    }
    ma41aCollectionPoint4738 = {
        '$id': '4738colle_ma41a_f115',
        'Name': 'ma40aCollectionPoint4738',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 366
    }
    ma41aCollectionPoint4739 = {
        '$id': '4739colle_ma41a_f116',
        'Name': 'ma40aCollectionPoint4739',
        'Location Near': 2406,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 367
    }
    ma41aCollectionPoint4740 = {
        '$id': '4740colle_ma41a_f117',
        'Name': 'ma40aCollectionPoint4740',
        'Location Near': 2417,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 368
    }
    ma41aCollectionPoint4741 = {
        '$id': '4741colle_ma41a_f118',
        'Name': 'ma40aCollectionPoint4741',
        'Location Near': 2416,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 369
    }
    ma41aCollectionPoint4742 = {
        '$id': '4742colle_ma41a_f119',
        'Name': 'ma40aCollectionPoint4742',
        'Location Near': 2416,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 370
    }
    ma41aCollectionPoint4743 = {
        '$id': '4743colle_ma41a_f120',
        'Name': 'ma40aCollectionPoint4743',
        'Location Near': 2428,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 371
    }
    ma41aCollectionPoint4744 = {
        '$id': '4744colle_ma41a_f128',
        'Name': 'ma40aCollectionPoint4744',
        'Location Near': 2408,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 372
    }
    ma41aCollectionPoint4745 = {
        '$id': '4745colle_ma41a_f129',
        'Name': 'ma40aCollectionPoint4745',
        'Location Near': 2420,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 373
    }
    ma41aCollectionPoint4746 = {
        '$id': '4746colle_ma41a_f130',
        'Name': 'ma40aCollectionPoint4746',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 374
    }
    ma41aCollectionPoint4747 = {
        '$id': '4747colle_ma41a_f131',
        'Name': 'ma40aCollectionPoint4747',
        'Location Near': 2421,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 375
    }
    ma41aCollectionPoint4748 = {
        '$id': '4748colle_ma41a_f132',
        'Name': 'ma40aCollectionPoint4748',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 376
    }
    ma41aCollectionPoint4749 = {
        '$id': '4749colle_ma41a_f133',
        'Name': 'ma40aCollectionPoint4749',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 377
    }
    ma41aCollectionPoint4750 = {
        '$id': '4750colle_ma41a_f134',
        'Name': 'ma40aCollectionPoint4750',
        'Location Near': 2416,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 378
    }
    ma41aCollectionPoint4751 = {
        '$id': '4751colle_ma41a_f135',
        'Name': 'ma40aCollectionPoint4751',
        'Location Near': 2425,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 379
    }
    ma41aCollectionPoint4752 = {
        '$id': '4752colle_ma41a_f136',
        'Name': 'ma40aCollectionPoint4752',
        'Location Near': 2421,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 380
    }
    ma41aCollectionPoint4753 = {
        '$id': '4753colle_ma41a_f137',
        'Name': 'ma40aCollectionPoint4753',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 381
    }
    ma41aCollectionPoint4754 = {
        '$id': '4754colle_ma41a_f143',
        'Name': 'ma40aCollectionPoint4754',
        'Location Near': 2428,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 382
    }
    ma41aCollectionPoint4755 = {
        '$id': '4755colle_ma41a_f144',
        'Name': 'ma40aCollectionPoint4755',
        'Location Near': 2416,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 383
    }
    ma41aCollectionPoint4756 = {
        '$id': '4756colle_ma41a_f156',
        'Name': 'ma40aCollectionPoint4756',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 384
    }
    ma41aCollectionPoint4757 = {
        '$id': '4757colle_ma41a_f157',
        'Name': 'ma40aCollectionPoint4757',
        'Location Near': 2406,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 385
    }
    ma41aCollectionPoint4758 = {
        '$id': '4758colle_ma41a_f178',
        'Name': 'ma40aCollectionPoint4758',
        'Location Near': 2416,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 386
    }
    ma41aCollectionPoint4759 = {
        '$id': '4759colle_ma41a_f180',
        'Name': 'ma40aCollectionPoint4759',
        'Location Near': 2428,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 387
    }
    ma41aCollectionPoint4760 = {
        '$id': '4760colle_ma41a_f181',
        'Name': 'ma40aCollectionPoint4760',
        'Location Near': 2412,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 388
    }
    ma41aCollectionPoint4761 = {
        '$id': '4761colle_ma41a_f182',
        'Name': 'ma40aCollectionPoint4761',
        'Location Near': 2402,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 389
    }
    ma41aCollectionPoint4762 = {
        '$id': '4762colle_ma41a_f183',
        'Name': 'ma40aCollectionPoint4762',
        'Location Near': 2416,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 390
    }
    ma41aCollectionPoint4763 = {
        '$id': '4763colle_ma41a_f184',
        'Name': 'ma40aCollectionPoint4763',
        'Location Near': 2407,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 391
    }
    ma41aCollectionPoint4764 = {
        '$id': '4764colle_ma41a_f185',
        'Name': 'ma40aCollectionPoint4764',
        'Location Near': 2416,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 392
    }
    ma41aCollectionPoint4765 = {
        '$id': '4765colle_ma41a_f186',
        'Name': 'ma40aCollectionPoint4765',
        'Location Near': 2428,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 393
    }
    ma41aCollectionPoint4766 = {
        '$id': '4766colle_ma41a_f187',
        'Name': 'ma40aCollectionPoint4766',
        'Location Near': 2428,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 394
    }
    ma41aCollectionPoint4767 = {
        '$id': '4767colle_ma41a_f191',
        'Name': 'ma40aCollectionPoint4767',
        'Location Near': 2428,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 395
    }
    ma41aCollectionPoint4768 = {
        '$id': '4768colle_ma41a_f192',
        'Name': 'ma40aCollectionPoint4768',
        'Location Near': 2421,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 396
    }
    ma41aCollectionPoint4769 = {
        '$id': '4769colle_ma41a_f193',
        'Name': 'ma40aCollectionPoint4769',
        'Location Near': 2417,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 397
    }
    ma41aCollectionPoint4770 = {
        '$id': '4770colle_ma41a_f194',
        'Name': 'ma40aCollectionPoint4770',
        'Location Near': 2425,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 398
    }
    ma41aCollectionPoint4771 = {
        '$id': '4771colle_ma41a_f198',
        'Name': 'ma40aCollectionPoint4771',
        'Location Near': 2406,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 399
    }
    ma41aCollectionPoint4772 = {
        '$id': '4772colle_ma41a_f201',
        'Name': 'ma40aCollectionPoint4772',
        'Location Near': 2406,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 400
    }
    ma41aCollectionPoint4773 = {
        '$id': '4773colle_ma41a_f202',
        'Name': 'ma40aCollectionPoint4773',
        'Location Near': 2421,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 401
    }
    ma41aCollectionPoint4774 = {
        '$id': '4774colle_ma41a_f203',
        'Name': 'ma40aCollectionPoint4774',
        'Location Near': 2420,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 402
    }
    ma41aCollectionPoint4775 = {
        '$id': '4775colle_ma41a_f204',
        'Name': 'ma40aCollectionPoint4775',
        'Location Near': 2425,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 403
    }
    ma41aCollectionPoint4776 = {
        '$id': '4776colle_ma41a_f205',
        'Name': 'ma40aCollectionPoint4776',
        'Location Near': 2425,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 404
    }
    ma41aCollectionPoint4777 = {
        '$id': '4777colle_ma41a_f206',
        'Name': 'ma40aCollectionPoint4777',
        'Location Near': 2421,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 405
    }
    ma41aCollectionPoint4778 = {
        '$id': '4778colle_ma41a_f207',
        'Name': 'ma40aCollectionPoint4778',
        'Location Near': 2428,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 406
    }
    ma41aCollectionPoint4779 = {
        '$id': '4779colle_ma41a_f208',
        'Name': 'ma40aCollectionPoint4779',
        'Location Near': 2415,
        'Story Pre-Req': [16],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 407
    }
    ma41aCollectionPoint4780 = {
        '$id': '4780colle_ma41a_f209',
        'Name': 'ma40aCollectionPoint4780',
        'Location Near': 2416,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 408
    }
    ma41aCollectionPoint4781 = {
        '$id': '4781colle_ma41a_f210',
        'Name': 'ma40aCollectionPoint4781',
        'Location Near': 2408,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 409
    }
    ma41aCollectionPoint4782 = {
        '$id': '4782colle_ma41a_f211',
        'Name': 'ma40aCollectionPoint4782',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 410
    }
    ma41aCollectionPoint4783 = {
        '$id': '4783colle_ma41a_f212',
        'Name': 'ma40aCollectionPoint4783',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 411
    }
    ma41aCollectionPoint4784 = {
        '$id': '4784colle_ma41a_f213',
        'Name': 'ma40aCollectionPoint4784',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 412
    }
    ma41aCollectionPoint4785 = {
        '$id': '4785colle_ma41a_f214',
        'Name': 'ma40aCollectionPoint4785',
        'Location Near': 2411,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 413
    }
    ma41aCollectionPoint4786 = {
        '$id': '4786colle_ma41a_f215',
        'Name': 'ma40aCollectionPoint4786',
        'Location Near': 2407,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 414
    }
    ma41aCollectionPoint4787 = {
        '$id': '4787colle_ma41a_f216',
        'Name': 'ma40aCollectionPoint4787',
        'Location Near': 2417,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 415
    }
    ma41aCollectionPoint4788 = {
        '$id': '4788colle_ma41a_f217',
        'Name': 'ma40aCollectionPoint4788',
        'Location Near': 2417,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 416
    }
    ma41aCollectionPoint4789 = {
        '$id': '4789colle_ma41a_f218',
        'Name': 'ma40aCollectionPoint4789',
        'Location Near': 2420,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 417
    }
    ma41aCollectionPoint4790 = {
        '$id': '4790colle_ma41a_f219',
        'Name': 'ma40aCollectionPoint4790',
        'Location Near': 2409,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 418
    }
    ma41aCollectionPoint4791 = {
        '$id': '4791colle_ma41a_f220',
        'Name': 'ma40aCollectionPoint4791',
        'Location Near': 2420,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 419
    }
    ma41aCollectionPoint4792 = {
        '$id': '4792colle_ma41a_f221',
        'Name': 'ma40aCollectionPoint4792',
        'Location Near': 2414,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 420
    }
    ma41aCollectionPoint4793 = {
        '$id': '4793colle_ma41a_f222',
        'Name': 'ma40aCollectionPoint4793',
        'Location Near': 2414,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 421
    }
    ma41aCollectionPoint4794 = {
        '$id': '4794colle_ma41a_f223',
        'Name': 'ma40aCollectionPoint4794',
        'Location Near': 2420,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 422
    }
    ma41aCollectionPoint4795 = {
        '$id': '4795colle_ma41a_f224',
        'Name': 'ma40aCollectionPoint4795',
        'Location Near': 2428,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 423
    }
    ma41aCollectionPoint4796 = {
        '$id': '4796colle_ma41a_f225',
        'Name': 'ma40aCollectionPoint4796',
        'Location Near': 2420,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 424
    }
    ma41aCollectionPoint4797 = {
        '$id': '4797colle_ma41a_f226',
        'Name': 'ma40aCollectionPoint4797',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 425
    }
    ma41aCollectionPoint4798 = {
        '$id': '4798colle_ma41a_f227',
        'Name': 'ma40aCollectionPoint4798',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 426
    }
    ma41aCollectionPoint4799 = {
        '$id': '4799colle_ma41a_f228',
        'Name': 'ma40aCollectionPoint4799',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 427
    }
    ma41aCollectionPoint4800 = {
        '$id': '4800colle_ma41a_f229',
        'Name': 'ma40aCollectionPoint4800',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 428
    }
    ma41aCollectionPoint4801 = {
        '$id': '4801colle_ma41a_f230',
        'Name': 'ma40aCollectionPoint4801',
        'Location Near': 2402,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 429
    }
    ma41aCollectionPoint4802 = {
        '$id': '4802colle_ma41a_f232',
        'Name': 'ma40aCollectionPoint4802',
        'Location Near': 2406,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 430
    }
    ma41aCollectionPoint4803 = {
        '$id': '4803colle_ma41a_f233',
        'Name': 'ma40aCollectionPoint4803',
        'Location Near': 2408,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 431
    }
    ma41aCollectionPoint4804 = {
        '$id': '4804colle_ma41a_f234',
        'Name': 'ma40aCollectionPoint4804',
        'Location Near': 2405,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 432
    }
    ma41aCollectionPoint4805 = {
        '$id': '4805colle_ma41a_f235',
        'Name': 'ma40aCollectionPoint4805',
        'Location Near': 2408,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 433
    }
    ma41aCollectionPoint4806 = {
        '$id': '4806colle_ma41a_f236',
        'Name': 'ma40aCollectionPoint4806',
        'Location Near': 2401,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 434
    }
    ma41aCollectionPoint4807 = {
        '$id': '4807colle_ma41a_f237',
        'Name': 'ma40aCollectionPoint4807',
        'Location Near': 2414,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 435
    }
    ma41aCollectionPoint4808 = {
        '$id': '4808colle_ma41a_f238',
        'Name': 'ma40aCollectionPoint4808',
        'Location Near': 2414,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 436
    }
    ma41aCollectionPoint4809 = {
        '$id': '4809colle_ma41a_f239',
        'Name': 'ma40aCollectionPoint4809',
        'Location Near': 2414,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 437
    }
    ma41aCollectionPoint4810 = {
        '$id': '4810colle_ma41a_f240',
        'Name': 'ma40aCollectionPoint4810',
        'Location Near': 2417,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 438
    }
    ma41aCollectionPoint4811 = {
        '$id': '4811colle_ma41a_f241',
        'Name': 'ma40aCollectionPoint4811',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 439
    }
    ma41aCollectionPoint4812 = {
        '$id': '4812colle_ma41a_f301',
        'Name': 'ma40aCollectionPoint4812',
        'Location Near': 2401,
        'Story Pre-Req': [12],
        'Required Items': [30387,30411,30421,30360,30444],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 440
    }
    ma41aCollectionPoint4813 = {
        '$id': '4813colle_ma41a_f302',
        'Name': 'ma40aCollectionPoint4813',
        'Location Near': 2402,
        'Story Pre-Req': [12],
        'Required Items': [30387,30411,30421,30360,30444],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 441
    }
    ma41aCollectionPoint4814 = {
        '$id': '4814colle_ma41a_f303',
        'Name': 'ma40aCollectionPoint4814',
        'Location Near': 2414,
        'Story Pre-Req': [12],
        'Required Items': [30378,30428,30372,30388,30436],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 442
    }
    ma41aCollectionPoint4815 = {
        '$id': '4815colle_ma41a_f304',
        'Name': 'ma40aCollectionPoint4815',
        'Location Near': 2414,
        'Story Pre-Req': [12],
        'Required Items': [30387,30411,30421,30360,30444],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 443
    }
    ma41aCollectionPoint4816 = {
        '$id': '4816colle_ma41a_f305',
        'Name': 'ma40aCollectionPoint4816',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [30387,30411,30421,30360,30444],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 444
    }
    ma41aCollectionPoint4817 = {
        '$id': '4817colle_ma41a_f306',
        'Name': 'ma40aCollectionPoint4817',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [30387,30411,30421,30360,30444],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 445
    }
    ma41aCollectionPoint4818 = {
        '$id': '4818colle_ma41a_f307',
        'Name': 'ma40aCollectionPoint4818',
        'Location Near': 2421,
        'Story Pre-Req': [12],
        'Required Items': [30387,30411,30421,30360,30444],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 446
    }
    ma41aCollectionPoint4819 = {
        '$id': '4819colle_ma41a_f308',
        'Name': 'ma40aCollectionPoint4819',
        'Location Near': 2418,
        'Story Pre-Req': [12],
        'Required Items': [30378,30428,30372,30388,30436],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 447
    }
    ma41aCollectionPoint4820 = {
        '$id': '4820colle_ma41a_f309',
        'Name': 'ma40aCollectionPoint4820',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [30378,30428,30372,30388,30436],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 448
    }
    ma41aCollectionPoint4821 = {
        '$id': '4821colle_ma41a_shouki_1',
        'Name': 'ma40aCollectionPoint4821',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [HazeKey, [ManipEtherKey[0]], [HazeAff[0]] , MythraKey, [LightKey[0]]],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 449
    }
    ma41aCollectionPoint4822 = {
        '$id': '4822colle_ma41a_shouki_2',
        'Name': 'ma40aCollectionPoint4822',
        'Location Near': 2407,
        'Story Pre-Req': [12],
        'Required Items': [HazeKey, [ManipEtherKey[0]], [HazeAff[0]] , MythraKey, [LightKey[0]]],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 450
    }
    ma41aCollectionPoint4823 = {
        '$id': '4823colle_ma41a_shouki_3',
        'Name': 'ma40aCollectionPoint4823',
        'Location Near': 2428,
        'Story Pre-Req': [12],
        'Required Items': [HazeKey, ManipEtherKey[:1], HazeAff[:1] , MythraKey, LightKey[:1], MythraAff[:1]],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 451
    }
    ma41aCollectionPoint4824 = {
        '$id': '4824colle_ma41a_shouki_4',
        'Name': 'ma40aCollectionPoint4824',
        'Location Near': 2422,
        'Story Pre-Req': [12],
        'Required Items': [HazeKey, ManipEtherKey, HazeAff[:2] , MythraKey, LightKey, MythraAff],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 452
    }
    ma41aCollectionPoint4825 = {
        '$id': '4825colle_ma41a_shouki_5',
        'Name': 'ma40aCollectionPoint4825',
        'Location Near': 2421,
        'Story Pre-Req': [12],
        'Required Items': [HazeKey, ManipEtherKey, HazeAff[:2] , MythraKey, LightKey, MythraAff],
        'Must Defeat Enemy IDs': [],
        'Rarity': 2,
        'CollectionTableID': 453
    }
    ma41aCollectionPoint4826 = {
        '$id': '4826colle_ma41a_f310',
        'Name': 'ma40aCollectionPoint4826',
        'Location Near': 2401,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 454
    }
    ma41aCollectionPoint4827 = {
        '$id': '4827colle_ma41a_f311',
        'Name': 'ma40aCollectionPoint4827',
        'Location Near': 2408,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 455
    }
    ma41aCollectionPoint4828 = {
        '$id': '4828colle_ma41a_f312',
        'Name': 'ma40aCollectionPoint4828',
        'Location Near': 2415,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 456
    }
    ma41aCollectionPoint4829 = {
        '$id': '4829colle_ma41a_f313',
        'Name': 'ma40aCollectionPoint4829',
        'Location Near': 2409,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 457
    }
    ma41aCollectionPoint4830 = {
        '$id': '4830colle_ma41a_f314',
        'Name': 'ma40aCollectionPoint4830',
        'Location Near': 2409,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 458
    }
    ma41aCollectionPoint4831 = {
        '$id': '4831colle_ma41a_f315',
        'Name': 'ma40aCollectionPoint4831',
        'Location Near': 2409,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 459
    }
    ma41aCollectionPoint4832 = {
        '$id': '4832colle_ma41a_f316',
        'Name': 'ma40aCollectionPoint4832',
        'Location Near': 2409,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 460
    }
    ma41aCollectionPoint4833 = {
        '$id': '4833colle_ma41a_f317',
        'Name': 'ma40aCollectionPoint4833',
        'Location Near': 2425,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 461
    }
    ma41aCollectionPoint4834 = {
        '$id': '4834colle_ma41a_f318',
        'Name': 'ma40aCollectionPoint4834',
        'Location Near': 2409,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 462
    }
    ma41aCollectionPoint4835 = {
        '$id': '4835colle_ma41a_f319',
        'Name': 'ma40aCollectionPoint4835',
        'Location Near': 2418,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 463
    }
    ma41aCollectionPoint4836 = {
        '$id': '4836colle_ma41a_f320',
        'Name': 'ma40aCollectionPoint4836',
        'Location Near': 2418,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 464
    }
    ma41aCollectionPoint4837 = {
        '$id': '4837colle_ma41a_f321',
        'Name': 'ma40aCollectionPoint4837',
        'Location Near': 2418,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 465
    }
    ma41aCollectionPoint4838 = {
        '$id': '4838colle_ma41a_f322',
        'Name': 'ma40aCollectionPoint4838',
        'Location Near': 2410,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 466
    }
    ma41aCollectionPoint4839 = {
        '$id': '4839colle_ma41a_f323',
        'Name': 'ma40aCollectionPoint4839',
        'Location Near': 2410,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 467
    }
    ma41aCollectionPoint4840 = {
        '$id': '4840colle_ma41a_f324',
        'Name': 'ma40aCollectionPoint4840',
        'Location Near': 2410,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 468
    }
    ma41aCollectionPoint4841 = {
        '$id': '4841colle_ma41a_f325',
        'Name': 'ma40aCollectionPoint4841',
        'Location Near': 2425,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 469
    }
    ma41aCollectionPoint4842 = {
        '$id': '4842colle_ma41a_f326',
        'Name': 'ma40aCollectionPoint4842',
        'Location Near': 2425,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 470
    }
    ma41aCollectionPoint4843 = {
        '$id': '4843colle_ma41a_f327',
        'Name': 'ma40aCollectionPoint4843',
        'Location Near': 2425,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 471
    }
    ma41aCollectionPoint4844 = {
        '$id': '4844colle_ma41a_f328',
        'Name': 'ma40aCollectionPoint4844',
        'Location Near': 2419,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 472
    }
    ma41aCollectionPoint4845 = {
        '$id': '4845colle_ma41a_f329',
        'Name': 'ma40aCollectionPoint4845',
        'Location Near': 2422,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 473
    }
    ma41aCollectionPoint4846 = {
        '$id': '4846colle_ma41a_f330',
        'Name': 'ma40aCollectionPoint4846',
        'Location Near': 2422,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 474
    }
    ma41aCollectionPoint4847 = {
        '$id': '4847colle_ma41a_f331',
        'Name': 'ma40aCollectionPoint4847',
        'Location Near': 2425,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 475
    }
    ma41aCollectionPoint4848 = {
        '$id': '4848colle_ma41a_f332',
        'Name': 'ma40aCollectionPoint4848',
        'Location Near': 2417,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 476
    }
    ma41aCollectionPoint4849 = {
        '$id': '4849colle_ma41a_f333',
        'Name': 'ma40aCollectionPoint4849',
        'Location Near': 2417,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 477
    }
    ma41aCollectionPoint4850 = {
        '$id': '4850colle_ma41a_f334',
        'Name': 'ma40aCollectionPoint4850',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 478
    }
    ma41aCollectionPoint4851 = {
        '$id': '4851colle_ma41a_f335',
        'Name': 'ma40aCollectionPoint4851',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 479
    }
    ma41aCollectionPoint4852 = {
        '$id': '4852colle_ma41a_f336',
        'Name': 'ma40aCollectionPoint4852',
        'Location Near': 2422,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 480
    }
    ma41aCollectionPoint4853 = {
        '$id': '4853colle_ma41a_f337',
        'Name': 'ma40aCollectionPoint4853',
        'Location Near': 2422,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 481
    }
    ma41aCollectionPoint4854 = {
        '$id': '4854colle_ma41a_f338',
        'Name': 'ma40aCollectionPoint4854',
        'Location Near': 2417,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 482
    }
    ma41aCollectionPoint4855 = {
        '$id': '4855colle_ma41a_f339',
        'Name': 'ma40aCollectionPoint4855',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 483
    }
    ma41aCollectionPoint4856 = {
        '$id': '4856colle_ma41a_f340',
        'Name': 'ma40aCollectionPoint4856',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 484
    }
    ma41aCollectionPoint4857 = {
        '$id': '4857colle_ma41a_f341',
        'Name': 'ma40aCollectionPoint4857',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 485
    }
    ma41aCollectionPoint4858 = {
        '$id': '4858colle_ma41a_f342',
        'Name': 'ma40aCollectionPoint4858',
        'Location Near': 2423,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 486
    }
    ma41aCollectionPoint4859 = {
        '$id': '4859colle_ma41a_f343',
        'Name': 'ma40aCollectionPoint4859',
        'Location Near': 2420,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 487
    }
    ma41aCollectionPoint4860 = {
        '$id': '4860colle_ma41a_f344',
        'Name': 'ma40aCollectionPoint4860',
        'Location Near': 2425,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 488
    }
    ma41aCollectionPoint4861 = {
        '$id': '4861colle_ma41a_f345',
        'Name': 'ma40aCollectionPoint4861',
        'Location Near': 2414,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 489
    }
    ma41aCollectionPoint4862 = {
        '$id': '4862colle_ma41a_f346',
        'Name': 'ma40aCollectionPoint4862',
        'Location Near': 2415,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 490
    }
    ma41aCollectionPoint4863 = {
        '$id': '4863colle_ma41a_f347',
        'Name': 'ma40aCollectionPoint4863',
        'Location Near': 2415,
        'Story Pre-Req': [16],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 491
    }
    ma41aCollectionPoint4864 = {
        '$id': '4864colle_ma41a_f348',
        'Name': 'ma40aCollectionPoint4864',
        'Location Near': 2408,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 492
    }
    ma41aCollectionPoint4865 = {
        '$id': '4865colle_ma41a_f349',
        'Name': 'ma40aCollectionPoint4865',
        'Location Near': 2401,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 493
    }
    ma41aCollectionPoint4866 = {
        '$id': '4866colle_ma41a_f350',
        'Name': 'ma40aCollectionPoint4866',
        'Location Near': 2407,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 494
    }
    ma41aCollectionPoint4867 = {
        '$id': '4867colle_ma41a_f351',
        'Name': 'ma40aCollectionPoint4867',
        'Location Near': 2407,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 495
    }
    ma41aCollectionPoint4868 = {
        '$id': '4868colle_ma41a_f352',
        'Name': 'ma40aCollectionPoint4868',
        'Location Near': 2407,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 496
    }
    ma41aCollectionPoint4869 = {
        '$id': '4869colle_ma41a_f353',
        'Name': 'ma40aCollectionPoint4869',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 497
    }
    ma41aCollectionPoint4870 = {
        '$id': '4870colle_ma41a_f354',
        'Name': 'ma40aCollectionPoint4870',
        'Location Near': 2402,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 498
    }
    ma41aCollectionPoint4871 = {
        '$id': '4871colle_ma41a_f355',
        'Name': 'ma40aCollectionPoint4871',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 499
    }
    ma41aCollectionPoint4872 = {
        '$id': '4872colle_ma41a_f356',
        'Name': 'ma40aCollectionPoint4872',
        'Location Near': 2413,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 1,
        'CollectionTableID': 500
    }
    ma41aCollectionPoint4873 = {
        '$id': '4873',
        'Name': 'ma40aCollectionPoint4873',
        'Location Near': 2410,
        'Story Pre-Req': [12],
        'Required Items': [],
        'Must Defeat Enemy IDs': [],
        'Rarity': 0,
        'CollectionTableID': 501
    }
    TornaCollectionDict = [ma40aCollectionPoint4401, ma40aCollectionPoint4402, ma40aCollectionPoint4403, ma40aCollectionPoint4404, ma40aCollectionPoint4405, ma40aCollectionPoint4406, ma40aCollectionPoint4407, ma40aCollectionPoint4408, ma40aCollectionPoint4409, ma40aCollectionPoint4410, ma40aCollectionPoint4411, ma40aCollectionPoint4413, ma40aCollectionPoint4414, ma40aCollectionPoint4415, ma40aCollectionPoint4416, ma40aCollectionPoint4417, ma40aCollectionPoint4418, ma40aCollectionPoint4419, ma40aCollectionPoint4420, ma40aCollectionPoint4421, ma40aCollectionPoint4422, ma40aCollectionPoint4423, ma40aCollectionPoint4424, ma40aCollectionPoint4425, ma40aCollectionPoint4426, ma40aCollectionPoint4427, ma40aCollectionPoint4428, ma40aCollectionPoint4429, ma40aCollectionPoint4430, ma40aCollectionPoint4431, ma40aCollectionPoint4432, ma40aCollectionPoint4433, ma40aCollectionPoint4434, ma40aCollectionPoint4435, ma40aCollectionPoint4436, ma40aCollectionPoint4437, ma40aCollectionPoint4438, ma40aCollectionPoint4439, ma40aCollectionPoint4440, ma40aCollectionPoint4441, ma40aCollectionPoint4442, ma40aCollectionPoint4443, ma40aCollectionPoint4444, ma40aCollectionPoint4445, ma40aCollectionPoint4446, ma40aCollectionPoint4447, ma40aCollectionPoint4448, ma40aCollectionPoint4449, ma40aCollectionPoint4450, ma40aCollectionPoint4451, ma40aCollectionPoint4452, ma40aCollectionPoint4453, ma40aCollectionPoint4454, ma40aCollectionPoint4455, ma40aCollectionPoint4456, ma40aCollectionPoint4457, ma40aCollectionPoint4458, ma40aCollectionPoint4459, ma40aCollectionPoint4460, ma40aCollectionPoint4461, ma40aCollectionPoint4462, ma40aCollectionPoint4463, ma40aCollectionPoint4464, ma40aCollectionPoint4465, ma40aCollectionPoint4466, ma40aCollectionPoint4467, ma40aCollectionPoint4468, ma40aCollectionPoint4469, ma40aCollectionPoint4470, ma40aCollectionPoint4471, ma40aCollectionPoint4472, ma40aCollectionPoint4473, ma40aCollectionPoint4474, ma40aCollectionPoint4475, ma40aCollectionPoint4476, ma40aCollectionPoint4477, ma40aCollectionPoint4478, ma40aCollectionPoint4479, ma40aCollectionPoint4480, ma40aCollectionPoint4481, ma40aCollectionPoint4482, ma40aCollectionPoint4483, ma40aCollectionPoint4484, ma40aCollectionPoint4485, ma40aCollectionPoint4486, ma40aCollectionPoint4487, ma40aCollectionPoint4488, ma40aCollectionPoint4489, ma40aCollectionPoint4490, ma40aCollectionPoint4491, ma40aCollectionPoint4492, ma40aCollectionPoint4493, ma40aCollectionPoint4494, ma40aCollectionPoint4495, ma40aCollectionPoint4496, ma40aCollectionPoint4497, ma40aCollectionPoint4498, ma40aCollectionPoint4499, ma40aCollectionPoint4500, ma40aCollectionPoint4501, ma40aCollectionPoint4502, ma40aCollectionPoint4503, ma40aCollectionPoint4504, ma40aCollectionPoint4505, ma40aCollectionPoint4506, ma40aCollectionPoint4507, ma40aCollectionPoint4508, ma40aCollectionPoint4509, ma40aCollectionPoint4510, ma40aCollectionPoint4511, ma40aCollectionPoint4512, ma40aCollectionPoint4513, ma40aCollectionPoint4514, ma40aCollectionPoint4515, ma40aCollectionPoint4516, ma40aCollectionPoint4517, ma40aCollectionPoint4518, ma40aCollectionPoint4519, ma40aCollectionPoint4520, ma40aCollectionPoint4521, ma40aCollectionPoint4522, ma40aCollectionPoint4523, ma40aCollectionPoint4525, ma40aCollectionPoint4526, ma40aCollectionPoint4527, ma40aCollectionPoint4528, ma40aCollectionPoint4529, ma40aCollectionPoint4530, ma40aCollectionPoint4531, ma40aCollectionPoint4532, ma40aCollectionPoint4533, ma40aCollectionPoint4534, ma40aCollectionPoint4535, ma40aCollectionPoint4536, ma40aCollectionPoint4537, ma40aCollectionPoint4538, ma40aCollectionPoint4539, ma40aCollectionPoint4540, ma40aCollectionPoint4541, ma40aCollectionPoint4542, ma40aCollectionPoint4543, ma40aCollectionPoint4544, ma40aCollectionPoint4545, ma40aCollectionPoint4546, ma40aCollectionPoint4547, ma40aCollectionPoint4548, ma40aCollectionPoint4549, ma40aCollectionPoint4550, ma40aCollectionPoint4551, ma40aCollectionPoint4552, ma40aCollectionPoint4553, ma40aCollectionPoint4554, ma40aCollectionPoint4555, ma40aCollectionPoint4556, ma40aCollectionPoint4557, ma40aCollectionPoint4558, ma40aCollectionPoint4559, ma40aCollectionPoint4560, ma40aCollectionPoint4561, ma40aCollectionPoint4562, ma40aCollectionPoint4563, ma40aCollectionPoint4564, ma40aCollectionPoint4565, ma40aCollectionPoint4566, ma40aCollectionPoint4567, ma40aCollectionPoint4568, ma40aCollectionPoint4569, ma40aCollectionPoint4570, ma40aCollectionPoint4571, ma40aCollectionPoint4572, ma40aCollectionPoint4573, ma40aCollectionPoint4574, ma40aCollectionPoint4575, ma40aCollectionPoint4576, ma40aCollectionPoint4577, ma40aCollectionPoint4578, ma40aCollectionPoint4579, ma40aCollectionPoint4580, ma40aCollectionPoint4581, ma40aCollectionPoint4582, ma40aCollectionPoint4583, ma40aCollectionPoint4584, ma40aCollectionPoint4585, ma40aCollectionPoint4586, ma40aCollectionPoint4587, ma40aCollectionPoint4588, ma40aCollectionPoint4589, ma40aCollectionPoint4590, ma40aCollectionPoint4591, ma40aCollectionPoint4592, ma40aCollectionPoint4593, ma40aCollectionPoint4594, ma40aCollectionPoint4595, ma40aCollectionPoint4596, ma40aCollectionPoint4597, ma40aCollectionPoint4598, ma40aCollectionPoint4599, ma40aCollectionPoint4601, ma40aCollectionPoint4602, ma40aCollectionPoint4603, ma40aCollectionPoint4604, ma40aCollectionPoint4605, ma40aCollectionPoint4606, ma40aCollectionPoint4607, ma40aCollectionPoint4608, ma40aCollectionPoint4609, ma40aCollectionPoint4610, ma40aCollectionPoint4611, ma40aCollectionPoint4612, ma40aCollectionPoint4613, ma40aCollectionPoint4614, ma40aCollectionPoint4615, ma40aCollectionPoint4616, ma40aCollectionPoint4617, ma40aCollectionPoint4618, ma40aCollectionPoint4619, ma40aCollectionPoint4620, ma40aCollectionPoint4621, ma40aCollectionPoint4622, ma40aCollectionPoint4623, ma40aCollectionPoint4624, ma40aCollectionPoint4625, ma40aCollectionPoint4626, ma40aCollectionPoint4627, ma40aCollectionPoint4628, ma40aCollectionPoint4629, ma40aCollectionPoint4630, ma40aCollectionPoint4631, ma40aCollectionPoint4632, ma40aCollectionPoint4633, ma40aCollectionPoint4634, ma40aCollectionPoint4635, ma40aCollectionPoint4636, ma40aCollectionPoint4637, ma40aCollectionPoint4638, ma40aCollectionPoint4640, ma40aCollectionPoint4641, ma40aCollectionPoint4642, ma40aCollectionPoint4643, ma40aCollectionPoint4644, ma40aCollectionPoint4646, ma40aCollectionPoint4647, ma40aCollectionPoint4648, ma40aCollectionPoint4649, ma40aCollectionPoint4650, ma40aCollectionPoint4651, ma40aCollectionPoint4652, ma40aCollectionPoint4653, ma40aCollectionPoint4654, ma40aCollectionPoint4655, ma40aCollectionPoint4656, ma40aCollectionPoint4657, ma40aCollectionPoint4658, ma40aCollectionPoint4659, ma40aCollectionPoint4660, ma40aCollectionPoint4661, ma40aCollectionPoint4662, ma40aCollectionPoint4663, ma40aCollectionPoint4664, ma40aCollectionPoint4666, ma40aCollectionPoint4667, ma40aCollectionPoint4668, ma40aCollectionPoint4669, ma40aCollectionPoint4670, ma40aCollectionPoint4671, ma40aCollectionPoint4672, ma40aCollectionPoint4673]    
    GormottCollectionDict = [ma41aCollectionPoint4651, ma41aCollectionPoint4652, ma41aCollectionPoint4653, ma41aCollectionPoint4654, ma41aCollectionPoint4655, ma41aCollectionPoint4656, ma41aCollectionPoint4657, ma41aCollectionPoint4658, ma41aCollectionPoint4659, ma41aCollectionPoint4660, ma41aCollectionPoint4661, ma41aCollectionPoint4662, ma41aCollectionPoint4663, ma41aCollectionPoint4664, ma41aCollectionPoint4665, ma41aCollectionPoint4666, ma41aCollectionPoint4667, ma41aCollectionPoint4668, ma41aCollectionPoint4669, ma41aCollectionPoint4670, ma41aCollectionPoint4671, ma41aCollectionPoint4672, ma41aCollectionPoint4673, ma41aCollectionPoint4674, ma41aCollectionPoint4675, ma41aCollectionPoint4676, ma41aCollectionPoint4677, ma41aCollectionPoint4678, ma41aCollectionPoint4679, ma41aCollectionPoint4680, ma41aCollectionPoint4681, ma41aCollectionPoint4682, ma41aCollectionPoint4683, ma41aCollectionPoint4684, ma41aCollectionPoint4685, ma41aCollectionPoint4686, ma41aCollectionPoint4687, ma41aCollectionPoint4688, ma41aCollectionPoint4689, ma41aCollectionPoint4690, ma41aCollectionPoint4691, ma41aCollectionPoint4692, ma41aCollectionPoint4693, ma41aCollectionPoint4694, ma41aCollectionPoint4695, ma41aCollectionPoint4696, ma41aCollectionPoint4697, ma41aCollectionPoint4698, ma41aCollectionPoint4699, ma41aCollectionPoint4700, ma41aCollectionPoint4701, ma41aCollectionPoint4702, ma41aCollectionPoint4703, ma41aCollectionPoint4704, ma41aCollectionPoint4705, ma41aCollectionPoint4706, ma41aCollectionPoint4707, ma41aCollectionPoint4708, ma41aCollectionPoint4709, ma41aCollectionPoint4710, ma41aCollectionPoint4711, ma41aCollectionPoint4712, ma41aCollectionPoint4713, ma41aCollectionPoint4714, ma41aCollectionPoint4715, ma41aCollectionPoint4716, ma41aCollectionPoint4717, ma41aCollectionPoint4718, ma41aCollectionPoint4719, ma41aCollectionPoint4720, ma41aCollectionPoint4721, ma41aCollectionPoint4722, ma41aCollectionPoint4723, ma41aCollectionPoint4724, ma41aCollectionPoint4725, ma41aCollectionPoint4726, ma41aCollectionPoint4727, ma41aCollectionPoint4728, ma41aCollectionPoint4729, ma41aCollectionPoint4730, ma41aCollectionPoint4731, ma41aCollectionPoint4732, ma41aCollectionPoint4733, ma41aCollectionPoint4734, ma41aCollectionPoint4735, ma41aCollectionPoint4736, ma41aCollectionPoint4737, ma41aCollectionPoint4738, ma41aCollectionPoint4739, ma41aCollectionPoint4740, ma41aCollectionPoint4741, ma41aCollectionPoint4742, ma41aCollectionPoint4743, ma41aCollectionPoint4744, ma41aCollectionPoint4745, ma41aCollectionPoint4746, ma41aCollectionPoint4747, ma41aCollectionPoint4748, ma41aCollectionPoint4749, ma41aCollectionPoint4750, ma41aCollectionPoint4751, ma41aCollectionPoint4752, ma41aCollectionPoint4753, ma41aCollectionPoint4754, ma41aCollectionPoint4755, ma41aCollectionPoint4756, ma41aCollectionPoint4757, ma41aCollectionPoint4758, ma41aCollectionPoint4759, ma41aCollectionPoint4760, ma41aCollectionPoint4761, ma41aCollectionPoint4762, ma41aCollectionPoint4763, ma41aCollectionPoint4764, ma41aCollectionPoint4765, ma41aCollectionPoint4766, ma41aCollectionPoint4767, ma41aCollectionPoint4768, ma41aCollectionPoint4769, ma41aCollectionPoint4770, ma41aCollectionPoint4771, ma41aCollectionPoint4772, ma41aCollectionPoint4773, ma41aCollectionPoint4774, ma41aCollectionPoint4775, ma41aCollectionPoint4776, ma41aCollectionPoint4777, ma41aCollectionPoint4778, ma41aCollectionPoint4779, ma41aCollectionPoint4780, ma41aCollectionPoint4781, ma41aCollectionPoint4782, ma41aCollectionPoint4783, ma41aCollectionPoint4784, ma41aCollectionPoint4785, ma41aCollectionPoint4786, ma41aCollectionPoint4787, ma41aCollectionPoint4788, ma41aCollectionPoint4789, ma41aCollectionPoint4790, ma41aCollectionPoint4791, ma41aCollectionPoint4792, ma41aCollectionPoint4793, ma41aCollectionPoint4794, ma41aCollectionPoint4795, ma41aCollectionPoint4796, ma41aCollectionPoint4797, ma41aCollectionPoint4798, ma41aCollectionPoint4799, ma41aCollectionPoint4800, ma41aCollectionPoint4801, ma41aCollectionPoint4802, ma41aCollectionPoint4803, ma41aCollectionPoint4804, ma41aCollectionPoint4805, ma41aCollectionPoint4806, ma41aCollectionPoint4807, ma41aCollectionPoint4808, ma41aCollectionPoint4809, ma41aCollectionPoint4810, ma41aCollectionPoint4811, ma41aCollectionPoint4812, ma41aCollectionPoint4813, ma41aCollectionPoint4814, ma41aCollectionPoint4815, ma41aCollectionPoint4816, ma41aCollectionPoint4817, ma41aCollectionPoint4818, ma41aCollectionPoint4819, ma41aCollectionPoint4820, ma41aCollectionPoint4821, ma41aCollectionPoint4822, ma41aCollectionPoint4823, ma41aCollectionPoint4824, ma41aCollectionPoint4825, ma41aCollectionPoint4826, ma41aCollectionPoint4827, ma41aCollectionPoint4828, ma41aCollectionPoint4829, ma41aCollectionPoint4830, ma41aCollectionPoint4831, ma41aCollectionPoint4832, ma41aCollectionPoint4833, ma41aCollectionPoint4834, ma41aCollectionPoint4835, ma41aCollectionPoint4836, ma41aCollectionPoint4837, ma41aCollectionPoint4838, ma41aCollectionPoint4839, ma41aCollectionPoint4840, ma41aCollectionPoint4841, ma41aCollectionPoint4842, ma41aCollectionPoint4843, ma41aCollectionPoint4844, ma41aCollectionPoint4845, ma41aCollectionPoint4846, ma41aCollectionPoint4847, ma41aCollectionPoint4848, ma41aCollectionPoint4849, ma41aCollectionPoint4850, ma41aCollectionPoint4851, ma41aCollectionPoint4852, ma41aCollectionPoint4853, ma41aCollectionPoint4854, ma41aCollectionPoint4855, ma41aCollectionPoint4856, ma41aCollectionPoint4857, ma41aCollectionPoint4858, ma41aCollectionPoint4859, ma41aCollectionPoint4860, ma41aCollectionPoint4861, ma41aCollectionPoint4862, ma41aCollectionPoint4863, ma41aCollectionPoint4864, ma41aCollectionPoint4865, ma41aCollectionPoint4866, ma41aCollectionPoint4867, ma41aCollectionPoint4868, ma41aCollectionPoint4869, ma41aCollectionPoint4870, ma41aCollectionPoint4871, ma41aCollectionPoint4872, ma41aCollectionPoint4873]
    global TornaCollection, GormottCollection
    TornaCollection, GormottCollection = [], []

    for collection in TornaCollectionDict:
        TornaCollectionPoint(collection, TornaCollection, CollectionRewardQty)

    for collection in TornaCollection:
        if collection.id == "4413":
            pass
        if collection.mainreq != []:
            collection.itemreqs.extend(Mainquests[collection.mainreq - 1].itemreqs) # adds main story req
            collection.itemreqs = Helper.MultiLevelListToSingleLevelList(collection.itemreqs)
            collection.itemreqs = list(set(collection.itemreqs))
            collection.itemreqs.sort()
        for area in Areas: # adds the area reach requirements
            if collection.nearloc == area.id:
                collection.itemreqs.extend(area.itemreqs)
                break
        if collection.enemyreqs != []:
            for collectionenemyreq in collection.enemyreqs:
                for enemy in Enemies:
                    if enemy.id == collectionenemyreq:
                        collection.itemreqs.extend(enemy.itemreqs)
                        break
        collection.type = "tornacollectionpoint"

    for collection in GormottCollectionDict:
        TornaCollectionPoint(collection, GormottCollection, CollectionRewardQty)

    for collection in GormottCollection:
        if collection.mainreq != []:
            collection.itemreqs.extend(Mainquests[collection.mainreq - 1].itemreqs) # adds main story req
            collection.itemreqs = Helper.MultiLevelListToSingleLevelList(collection.itemreqs)
            collection.itemreqs = list(set(collection.itemreqs))
            collection.itemreqs.sort()
        for area in Areas: # adds the area reach requirements
            if collection.nearloc == area.id:
                collection.itemreqs.extend(area.itemreqs)
                break
        if collection.enemyreqs != []:
            for collectionenemyreq in collection.enemyreqs:
                for enemy in Enemies:
                    if enemy.id == collectionenemyreq:
                        collection.itemreqs.extend(enemy.itemreqs)
                        break
        collection.type = "gormottcollectionpoint"
    return TornaCollection, GormottCollection
    