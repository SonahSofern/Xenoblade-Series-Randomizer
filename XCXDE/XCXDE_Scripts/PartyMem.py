import json
from XCXDE.XCXDE_Scripts import IDs, Options

from scripts import JSONParser, Helper

def Members():
    # charFile = JSONParser.File("XCXDE/JsonOutputs/common/DEF_PcList.json")
    test = Helper.InclRange(1, 252)
    testf = [x for x in test if x not in IDs.PartyMembersIDs]
    # [x for x in test if x not in IDs.PartyMembersIDs]
    Helper.FileShuffle("XCXDE/JsonOutputs/common/DEF_PcList.json", ["$id", "Lv", "InitBp"], testf, lambda e: e["$id"] in [50])