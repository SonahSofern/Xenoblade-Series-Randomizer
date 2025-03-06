# https://xenobladedata.github.io/xb1de/bdat/bdat_common/BTL_skilllist.html
import json, random, Options
from scripts.PopupDescriptions import Description
import scripts.PopupDescriptions
# https://xenobladedata.github.io/xb1de/bdat/bdat_common/BTL_bufflist.html#87 will be similar to enhancement in xc2 i can create gems with new effects and add back gems that dont get put in the game but already exist like cooldown reduc (cast quicken)
class Gem:
    def __init__(self,_name, _cyl_name, _atr_type, _status, _rvs_type, _attach, _accum, _power, _percentPower, _money = 20, _category = 1):
        self.status = _status
        self.power = _power
        self.pPower = _percentPower
        self.money = _money 
        self.category = _category

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


GemDescription = Description("Gems")
GemDescription.Text("This allows any gem to be equipped to weapons and armor. \nDouble attack in the vanilla game could only be equipped to your weapon for example.")
GemDescription.Image("./XCDE/_internal/Images/GemsFreeEquipped.png", 500)
