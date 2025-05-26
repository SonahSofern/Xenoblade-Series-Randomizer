from scripts import Helper, JSONParser, PopupDescriptions
import json
import random
import time
from IDs import *

class TornaMiscItem: # created to allow me to pass these objects easier
    def __init__(self, input, addtolist, rewardnumber):
        self.fldadditemid = input['FLD_AddItem $id']
        self.name = input["Name"]
        self.mainreq = input['Story Pre-Req']
        self.itemreqs = Helper.MultiLevelListToSingleLevelList(input['Required Items'])
        if rewardnumber > 0:
            self.randomizeditems = [-1]
            self.hasprogression = True
        else:
            self.randomizeditems = [0]
            self.hasprogression = False
        self.nearloc = input['Location Near']
        self.type = "misc"
        addtolist.append(self)

def CreateMiscItems(Mainquests, Areas, MiscOn): # Currently only for massive melee mythra NPC, but wasn't sure how to classify it
    
    NamelessWanderponItem = {
        'FLD_AddItem $id': 258,
        'Name': 'Nameless Wanderpon Gift Item',
        'Location Near': 2303,
        'Story Pre-Req': 8,
        'Required Items': []
    }

    global TornaMiscItems # holds the TornaMainQuest class objects
    TornaMiscItems = []
    TornaMiscItemDict = [NamelessWanderponItem]

    for item in TornaMiscItemDict:
        TornaMiscItem(item, TornaMiscItems, MiscOn)
    
    for item in TornaMiscItems:
        if item.mainreq != []:
            item.itemreqs.extend(Mainquests[item.mainreq - 1].itemreqs) # adds main story req
            item.itemreqs = Helper.MultiLevelListToSingleLevelList(item.itemreqs)
            item.itemreqs = list(set(item.itemreqs))
            item.itemreqs.sort()
        for area in Areas: # adds the area reach requirements
            if item.nearloc == area.id:
                item.itemreqs.extend(area.itemreqs)
                break

    return TornaMiscItems
