# https://xenobladedata.github.io/xb1de/bdat/bdat_common/BTL_skilllist.html
import json, random, Options
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
    ranks = ["E", "D", "C", "B", "A", "S"] # Calculate proper gem amount based on rank
    with open("./XCDE/_internal/JsonOutputs/bdat_common/BTL_skilllist.json", 'r+', encoding='utf-8') as gemFile:
        gemData = json.load(gemFile)
        isNotCapped = Options.GemOption_NoCap.GetState()
        isFreeEquip = Options.GemOption_FreeEquip.GetState()
        isPower = Options.GemOption_Power.GetState()
        for gem in gemData["rows"]:
            if isNotCapped:
                gem["max"] = 10000
            if isFreeEquip:
                gem["attach"] = 0                # 0 Equip to anything                # 1 Equip to weapon                # 2 Equip to armor
            if isPower:
                RankPower(gem, ranks)
        if isPower:
             ItemPower(gemData["rows"], ranks)
        gemFile.seek(0)
        gemFile.truncate()
        json.dump(gemData, gemFile, indent=2, ensure_ascii=False)
        

def RankPower(gem, ranks):
    mult = random.choice([0.1,0.2, 0.3, 0.4, 0.6, 0.8, 1.2, 1.3, 1.4, 1.5, 1.7, 2.0, 2.5, 3.0])
    for r in ranks:
        gem[f"lower_{r}"] = min(max(int(gem[f"lower_{r}"] * mult), 1), 254) # Lotta of annoying math here to make sure that lower is smaller than upper but also between 0 and 255
        gem[f"upper_{r}"] = min(int(gem[f"upper_{r}"] * mult), 253) + 2
        
# Changes gems that are already items given out during the story
def ItemPower(gemData, ranks):
    with open("./XCDE/_internal/JsonOutputs/bdat_common/ITM_itemlist.json", 'r+', encoding='utf-8') as gemItemFile: 
        gemItemData = json.load(gemItemFile)
        for gem in gemItemData["rows"]:
            if gem["itemType"] != 3: # If item is a gem
                continue
            rank = gem["rankType"]
            for g in gemData:
                if g["$id"] == gem["itemID"]:
                    gem["percent"] = random.randrange(g[f"lower_{ranks[rank-1]}"], g[f"upper_{ranks[rank-1]}"])
                    break
        gemItemFile.seek(0)
        gemItemFile.truncate()
        json.dump(gemItemData, gemItemFile, indent=2, ensure_ascii=False)

def GemDescriptions():
    GemDescription = scripts.PopupDescriptions.Description()
    GemDescription.Header(Options.GemOption_Power.name)
    GemDescription.Text("This randomizes the power level of crafted and premade gems")
    GemDescription.Header(Options.GemOption_FreeEquip.name)
    GemDescription.Text("This allows any gem to be equipped to weapons and armor.")
    GemDescription.Image("GemsFreeEquipped.png","XCDE", 500)
    GemDescription.Text("Double Attack on armor and HP Up on weapons.")
    GemDescription.Header(Options.GemOption_NoCap.name)
    GemDescription.Text("This removes the % and regular cap for all gems when you equip them.")
    GemDescription.Image("GemCap.png","XCDE", 500)
    GemDescription.Text("Double Attack and Haste above their vanilla 50% cap.")
    return GemDescription