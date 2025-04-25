# https://xenobladedata.github.io/xb1de/bdat/bdat_common/BTL_skilllist.html
import json, random, Options
import scripts.PopupDescriptions, scripts.JSONParser
# https://xenobladedata.github.io/xb1de/bdat/bdat_common/BTL_bufflist.html#87 will be similar to enhancement in xc2 i can create gems with new effects and add back gems that dont get put in the game but already exist like cooldown reduc (cast quicken)
# Cant extend gems, the descriptions wont load will have to replace old ones

class Gem:
    def __init__(self, name = "", atr_type = 0, status = 0, rvs_type = 0, attach = 0, max = 0, val_type = 0, power = [0,0], percentPower = [0,0], money = 20, category = 1, rvs_caption = "", menuCaption = ""):
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
            

attributes = {
    0 : (0, "NULL"),
    4 : (4,"Fire"),
    5 : (5, "Water"),
    6 : (6, "Electric"),
    7 : (7, "Ice"),
    8 : (8, "Wind"),
    9 : (9, "Earth")
}

     
def StandardGems(gemData, gemMSData, gemHelpMSData):    
    for gem in gemData["rows"]:
        # Find name
        for name in gemMSData["rows"]:
            if gem["name"] == name["$id"]:
                newName = name["name"]
                break
        for helpName in gemMSData["rows"]:
            if gem["rvs_caption"] == helpName["$id"]:
                newHelpName = helpName["name"]
                break
        
        Gem(newName, attributes[gem["atr_type"]], gem["rvs_status"], gem["rvs_type"], gem["attach"], gem["max"], gem["val_type"], [gem["lower_E"], gem["upper_S"]], [gem["percent_E"], gem["percent_S"]], gem["money"], gem["category"], newHelpName, newHelpName)

    

def UnusedGems(gemData, gemMSData, gemHelpMSData):
    pass
    # QuickRecast = Gem("Cast Quicken", attributes[6], 44, 3,2, 90, 0, [90,100], [0,0], 1000, 4, "\\[Passive\\][XENO:n ] Reduces cast time by $1.") Doesnt seem to work
    

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
                if isEffect:
                    StandardGems(gemData, gemMSData, gemHelpMSData)
                
                if isUnusedGems:
                    UnusedGems(gemData, gemMSData, gemHelpMSData)
                
                if isEffect or isUnusedGems:
                    Effects(gemData, gemMSData, gemHelpMSData)
                
                for gem in gemData["rows"]:
                    if isNotCapped:
                        gem["max"] = 10000
                    if isFreeEquip:
                        gem["attach"] = 0                # 0 Equip to anything                # 1 Equip to weapon                # 2 Equip to armor
                    if isPower:
                        RankPower(gem, ranks)
                        
                
                if isPower or isEffect or isUnusedGems:
                    ItemPower(gemData["rows"], ranks)
                    
                GemList.clear() # Clear the global list
                
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
    # maxGems = 92
    
    # Keep track of what ids to put things in
    idCount = 1
    skillMSCount = 1
    
    
    # Clear for repopulation
    gemData["rows"].clear()
    gemMSData["rows"].clear()
    gemHelpMSData["rows"].clear()
    
    # Loop and generate our new gems
    for i in range(len(GemList)):
    
        if (len(GemList) == 0):
            break
        
        gem = random.choice(GemList)
        
            
        GemList.remove(gem)
        
        incr = max(int((gem.power[-1] - gem.power[0])/12),1)
        pPowIncr = int(gem.pPower[-1]/6)
        
        
        gemData["rows"].append(
            {
                "$id": idCount,
                "name": skillMSCount,
                "cylinder_name": skillMSCount + 1,
                "atr_type": gem.atr_type[0],
                "rvs_status": gem.status,
                "rvs_type": gem.rvstype,
                "attach": gem.attach,
                "accum": gem.accum,
                "max": gem.max,
                "val_type": gem.val_type,
                "lower_E": gem.power[0],
                "upper_E": gem.power[0] + incr,
                "lower_D": gem.power[0] + incr*2,
                "upper_D": gem.power[0] + incr*3,
                "lower_C": gem.power[0] + incr*4,
                "upper_C": gem.power[0] + incr*5,
                "lower_B": gem.power[0] + incr*6,
                "upper_B": gem.power[0] + incr*7,
                "lower_A": gem.power[0] + incr*8,
                "upper_A": gem.power[0] + incr*9,
                "lower_S": gem.power[0] + incr*10,
                "upper_S": gem.power[0] + incr*11,
                "percent_E": gem.pPower[0],
                "percent_D": pPowIncr*2,
                "percent_C": pPowIncr*3,
                "percent_B": pPowIncr*4,
                "percent_A": pPowIncr*5,
                "percent_S": gem.pPower[-1],
                "money": gem.money,
                "category": gem.category,
                "rvs_caption": skillMSCount + 2
                            
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
    mult = random.choice([0.1, 0.2, 0.3, 0.4, 0.6, 0.8, 1.2, 1.3, 1.4, 1.5, 1.7, 2.0, 2.5, 3.0])
    for r in ranks:
        gem[f"lower_{r}"] = min(max(int(gem[f"lower_{r}"] * mult), 1), 254) # Lotta of annoying math here to make sure that lower is smaller than upper but also between 0 and 255
        gem[f"upper_{r}"] = min(int(gem[f"upper_{r}"] * mult), 253) + 2
        
# Changes gems that are already items given out during the story
def ItemPower(gemData, ranks):
    with open("./XCDE/_internal/JsonOutputs/bdat_common/ITM_itemlist.json", 'r+', encoding='utf-8') as gemItemFile: 
        gemItemData = json.load(gemItemFile)
        for gem in gemItemData["rows"]:
            if gem["itemType"] != 3: # If item is not a gem continue
                continue
            rank = gem["rankType"]
            newGem = random.choice(gemData)
            gem["itemID"] = newGem["$id"]
            gem["percent"] = random.randrange(newGem[f"lower_{ranks[rank-1]}"], newGem[f"upper_{ranks[rank-1]}"])
        scripts.JSONParser.CloseFile(gemItemData, gemItemFile)

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