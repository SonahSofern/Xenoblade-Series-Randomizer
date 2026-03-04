import json
from scripts import JSONParser

def TutorialSkip():
    with open("XCXDE/JsonOutputs/common/MNU_Tutorial.json", 'r+', encoding='utf-8') as eneFile:
        pass
    
def InfoRangeIncrease():
    infoIDs = [1001,1101,1201,1301,1401,1501,1601,1701,2001,2201]
    for info in infoIDs:
        infoFile = JSONParser.JFile(f"XCXDE/JsonOutputs/common/FLD_TownInfo{info}.json")
        for info in infoFile.rows:
            info["Radius"] = 20
        infoFile.Close()