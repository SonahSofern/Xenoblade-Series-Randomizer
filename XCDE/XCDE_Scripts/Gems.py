# https://xenobladedata.github.io/xb1de/bdat/bdat_common/BTL_skilllist.html
import json, random, Options
import scripts.PopupDescriptions
# https://xenobladedata.github.io/xb1de/bdat/bdat_common/BTL_bufflist.html#87 will be similar to enhancement in xc2 i can create gems with new effects and add back gems that dont get put in the game but already exist like cooldown reduc (cast quicken)
# Cant extend gems, the descriptions wont load will have to replace old ones

class Gem:
    def __init__(self, name = "", atr_type = 0, status = 0, rvs_type = 0, attach = 0, max = 0, val_type = 0, power = [0,0], percentPower = [0,0], money = 20, category = 1, rvs_caption = "", menuCaption = "", isUnused = False):
        self.name = name # Gen the ID from launch
        self.atr_type = atr_type
        self.status = status
        self.rvstype = rvs_type # A number that represents how the value of this gem in XC1 is input to its status (e.g. added vs multiplied).
        self.attach = attach
        self.accum = 1
        self.max = max
        self.val_type = val_type # 1 for stats 0 for else
        self.power = power
        self.pPower = percentPower
        self.money = money 
        self.category = category
        self.rvs_caption = rvs_caption
        self.menuCaption = menuCaption
        GemList.append(self)
GemList:list[Gem] = []
            
  
Red = (4, "Fire")
Blue = (5, "Water")
Yellow = (6, "Electric")
Teal = (7, "Ice")
Green = (8, "Wind")
Orange = (9, "Earth")
       
def StandardGems():
    StrengthUp = Gem("Strength Up", Red, 88, 1, 0, 150, 1, [5,100], [0,0], 200, 1, "\\[Passive\\][XENO:n ]\nIncreases strength by $1.", "\\[Strength Up\\][XENO:n ]\nIncreases strength.")
    ChillDef = Gem("Chill Defence", Red, 138, 3, 2, 100, 0, [2,75], [0,0], 400, 3, "\\[Passive\\] Decreases Chill damage[XENO:n ]\ntaken by $1.", "\\[Chill Defence\\][XENO:n ]\nDecreases Chill damage received.")
    # SleepResist = Gem("Sleep Resist", Red, 26, 3, 2, 100, 0, [4,100], [0,0], 350, 3, "", "")

def UnusedGems():
    QuickRecast = Gem("Cast Quicken", Yellow, 44, 3,2, 90, 0, [10,50], [0,0], 1000, 4, "\[Passive\][XENO:n ] Reduces cast time by $1.")

def Gems():
    ranks = ["E", "D", "C", "B", "A", "S"] # Calculate proper gem amount based on rank
    with open("./XCDE/_internal/JsonOutputs/bdat_common/BTL_skilllist.json", 'r+', encoding='utf-8') as gemFile:
        with open("./XCDE/_internal/JsonOutputs/bdat_common_ms/BTL_skilllist_ms.json", 'r+', encoding='utf-8') as gemMSFile: 
            with open("./XCDE/_internal/JsonOutputs/bdat_menu_mes_ms/MNU_skill_ms.json", 'r+', encoding='utf-8') as gemHelpMSFile: 
                gemHelpMSData = json.load(gemHelpMSFile)
                gemMSData = json.load(gemMSFile)
                gemData = json.load(gemFile)
                
                isNotCapped = Options.GemOption_NoCap.GetState()
                isFreeEquip = Options.GemOption_FreeEquip.GetState()
                isPower = Options.GemOption_Power.GetState()
                isEffect = Options.GemOption_Effect.GetState()
                isUnusedGems = Options.GemOption_Unused.GetState()
                
                # Might move this into isEffect
                StandardGems()
                
                if isUnusedGems:
                    UnusedGems()
                
                
                for gem in gemData["rows"]:
                    if isNotCapped:
                        gem["max"] = 10000
                    if isFreeEquip:
                        gem["attach"] = 0                # 0 Equip to anything                # 1 Equip to weapon                # 2 Equip to armor
                    if isPower:
                        RankPower(gem, ranks)
                        
                if isEffect:
                    Effects(gemData, gemMSData, gemHelpMSData)
                
                if isPower:
                    ItemPower(gemData["rows"], ranks)
                    
                gemFile.seek(0)
                gemFile.truncate()
                json.dump(gemData, gemFile, indent=2, ensure_ascii=False)
                
                gemHelpMSFile.seek(0)
                gemHelpMSFile.truncate()
                json.dump(gemHelpMSData, gemHelpMSFile, indent=2, ensure_ascii=False) 
                
                gemMSFile.seek(0)
                gemMSFile.truncate()
                json.dump(gemMSData, gemMSFile, indent=2, ensure_ascii=False)


    
def Effects(gemData, gemMSData, gemHelpMSData):
    
    # Number of gems that the game will allow in a single file
    maxGems = 92
    
    # Keep track of what ids to put things in
    idCount = 1
    skillMSCount = 1
    
    
    # Clear for repopulation
    gemData["rows"].clear()
    gemMSData["rows"].clear()
    gemHelpMSData["rows"].clear()
    
    # Loop and generate our new gems
    for i in range(maxGems):
        gem = random.choice(GemList)
        
        if (len(GemList) > 1):
            GemList.remove(gem)
        
        incr = int(gem.power[-1]/12)
        pPowIncr = int(gem.pPower[-1]/6)
        
        
        gemData["rows"].append(
            {
                "$id": idCount,
                "name": idCount,
                "cylinder_name": idCount + 1,
                "atr_type": gem.atr_type[0],
                "rvs_status": gem.status,
                "rvs_type": gem.rvstype,
                "attach": gem.attach,
                "accum": gem.accum,
                "max": gem.max,
                "val_type": gem.val_type,
                "lower_E": gem.power[0],
                "upper_E": incr*2,
                "lower_D": incr*3,
                "upper_D": incr*4,
                "lower_C": incr*5,
                "upper_C": incr*6,
                "lower_B": incr*7,
                "upper_B": incr*8,
                "lower_A": incr*9,
                "upper_A": incr*10,
                "lower_S": incr*11,
                "upper_S": gem.power[-1],
                "percent_E": gem.pPower[0],
                "percent_D": pPowIncr*2,
                "percent_C": pPowIncr*3,
                "percent_B": pPowIncr*4,
                "percent_A": pPowIncr*5,
                "percent_S": gem.pPower[-1],
                "money": gem.money,
                "category": gem.category,
                "rvs_caption": idCount + 2
                            
            }
        )
        
        gemMSData["rows"].extend(
            [{
            "$id": skillMSCount,
            "style": 9,
            "name": gem.name
            },
            {
            "$id": skillMSCount + 1,
            "style": 5,
            "name": gem.atr_type[-1]
            },
            {
            "$id": skillMSCount + 2,
            "style": 51,
            "name": gem.rvs_caption
            }  ]
        )
        
        gemHelpMSData["rows"].append(
            {
            "$id": idCount,
            "style": 117,
            "name": gem.menuCaption
            },
        )
        
        idCount += 1
        skillMSCount += 3
    


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