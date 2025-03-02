# https://xenobladedata.github.io/xb1de/bdat/bdat_common/BTL_skilllist.html
import json, random, Options

class Gem:
    def __init__(self):
        pass

def Gems():
    with open("./XCDE/_internal/JsonOutputs/bdat_common/BTL_skilllist.json", 'r+', encoding='utf-8') as gemFile:
        gemData = json.load(gemFile)
        isNotCapped = Options.GemOption_NoCap.GetState()
        isFreeEquip = Options.GemOption_FreeEquip.GetState()
        for gem in gemData["rows"]:
            if isNotCapped:
                gem["max"] = 10000
            if isFreeEquip:
                gem["attach"] = 0
            
        gemFile.seek(0)
        gemFile.truncate()
        json.dump(gemData, gemFile, indent=2, ensure_ascii=False)
        
# 0 Equip to anything
# 1 Equip to weapon
# 2 Equip to armor