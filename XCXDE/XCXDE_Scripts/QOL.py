import json
from scripts import JSONParser

def TutorialSkip():
    with open("XCXDE/JsonOutputs/common/MNU_Tutorial.json", 'r+', encoding='utf-8') as eneFile:
        pass
    
def InfoRangeIncrease():
    infoIDs = [1001,1101,1201,1301,1401,1501,1601,1701,2001,2201]
    for info in infoIDs:
        infoFile = JSONParser.File(f"XCXDE/JsonOutputs/common/FLD_TownInfo{info}.json")
        for info in infoFile.rows:
            info["radius"] = 20
        infoFile.Close()
        
def EasyStoryPrerequisites():
    qstFile = JSONParser.File("XCXDE/JsonOutputs/common/FLD_questlist.json")
    chapterPrereqIDs = [15, 20, 26, 32, 42, 47, 54, 62, 68, 73, 81, 2465, 2477, 2503]
    for qst in qstFile.rows:
        if qst["$id"] in chapterPrereqIDs:
            qst["HexCondition"] = 1
    qstFile.Close()
        
def OpWep():
    with open("XCXDE/JsonOutputs/common/WPN_PcList.json", 'r+', encoding='utf-8') as wpFile:
        wpData = json.load(wpFile)
        for wep in wpData["rows"]:
            if wep["$id"] in [1584]:
                wep["Damage"] = 1500
                wep["Magazine"] = 100
                wep["DMRatio"] = 1500
                wep["Recast"] = 1
                
                
        JSONParser.CloseFile(wpData, wpFile)