# https://xenobladedata.github.io/xb1de/bdat/bdat_common/BTL_skilllist.html
from scripts import JSONParser, PopupDescriptions, StatRand
import json, random
from XCDE.XCDE_Scripts import Options, IDs
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
        if menuCaption == "":
            self.menuCaption = rvs_caption
        else:
            self.menuCaption = menuCaption
        GemList.append(self)
GemList:list[Gem] = []
            
     
def StandardGems(gemData:JSONParser.File, gemMSData:JSONParser.File, gemHelpMSData:JSONParser.File):    
    badEffects = [60, 0, 83, 84, 87, 82, 44, 61, 194, 231, 161]
    for gem in gemData.rows:
        if gem["rvs_status"] in badEffects:
            continue
        # Find name
        for name in gemMSData.rows:
            if gem["name"] == name["$id"]:
                newName = name["name"]
                break
        for helpName in gemMSData.rows:
            if gem["rvs_caption"] == helpName["$id"]:
                newHelpName = helpName["name"]
                break
        for gemDesc in gemHelpMSData.rows:
            if gemDesc["$id"] == gem["$id"]:
                help = gemDesc["name"]
                break
        
        Gem(newName, attributes[gem["atr_type"]], gem["rvs_status"], gem["rvs_type"], gem["attach"], gem["max"], gem["val_type"], [gem["lower_E"], gem["upper_S"]], [gem["percent_E"], gem["percent_S"]], gem["money"], gem["category"], newHelpName, help)

attributes = {
    0 : (0, "NULL"),
    4 : (4,"Fire"),
    5 : (5, "Water"),
    6 : (6, "Electric"),
    7 : (7, "Ice"),
    8 : (8, "Wind"),
    9 : (9, "Earth")
}

def UnusedGems():
    Gem("Cast Quicken", attributes[6], 45, 3,2, 90, 0, [10,30], [0,0], 1000, 4, "\\[Passive\\][XENO:n ] Reduces cast time by $1.", "\\[Passive\\][XENO:n ] Reduces cast time.")
    Gem("Reactive Heal", attributes[5], 54, 1, 2, 90, 0, [30,255], [0,0], 1500, 1, "\\[Passive\\][XENO:n ] On damage taken restore $1 health.", "\\[Passive\\][XENO:n ] On damage taken restore health.")
    Gem("Monado Enchant", attributes[7], 208, 1, 1, 90, 0, [100,200], [0,0], 2000, 1, "\\[Passive\\][XENO:n ] Your attacks pierce mechon armor [XENO:n ]\nand inflict $1 bonus damage.", "\\[Passive\\][XENO:n ] Your attacks pierce mechon armor and inflict bonus damage.")
    Gem("Cursed Regen", attributes[8], 53, 1, 2, 1000, 0, [100,100], [1,2], 6500, 1, "\\[Passive\\][XENO:n ] Disables automatic regeneration.")
    # Gem("Recovery Down 0", attributes[8], 142, 1, 0, 1000, 0, [20,20], [100,100], 6500, 1, "\\[Passive\\][XENO:n ] Disables automatic regeneration.")
    # Gem("Recovery Down 1", attributes[8], 142, 0, 0, 1000, 0, [20,20], [100,100], 6500, 1, "\\[Passive\\][XENO:n ] Disables automatic regeneration.")
    
    
    # 94 is accuracy up might add here if it works
    if Options.MovespeedOption.GetState():
        Gem("Quickstep", attributes[8], 3, 3, 2, 25, 0, [2,25], [0,0], 500, 5, "\\[Passive\\][XENO:n ] Increases movement speed by $1.", "\\[Passive\\][XENO:n ] Increases movement speed.")

# Dont work 
# Gem("Regenerate", attributes[5], 52, 1, 2, 1000, 0, [40,200], [1,2], 2999, 1, "Test", "Test")
# Gem("Fall", attributes[8], 58, 0, 2, 1000, 0, [100,100], [100,100], 6500, 1, "\\[Passive\\][XENO:n ] Disables automatic regeneration.")
# Gem("Recovery Down 1", attributes[8], 142, 0, 0, 1000, 0, [20,20], [100,100], 6500, 1, "\\[Passive\\][XENO:n ] Disables automatic regeneration.")

                 
def Gems():
    ranks = ["E", "D", "C", "B", "A", "S"] # Calculate proper gem amount based on rank
    gemFile = JSONParser.File("XCDE/JsonOutputs/bdat_common/BTL_skilllist.json")
    gemMSFile = JSONParser.File("XCDE/JsonOutputs/bdat_common_ms/BTL_skilllist_ms.json")
    gemHelpMSFile = JSONParser.File("XCDE/JsonOutputs/bdat_menu_mes_ms/MNU_skill_ms.json")
    
    isNotCapped = Options.GemOption_NoCap.GetState()
    isFreeEquip = Options.GemOption_FreeEquip.GetState()
    isPower = Options.GemOption_Power.GetState()
    isEffect = Options.GemOption_Effect.GetState()
    isUnusedGems = Options.GemOption_Unused.GetState()
    
    if isEffect:
        StandardGems(gemFile, gemMSFile, gemHelpMSFile)
    
    if isUnusedGems:
        UnusedGems()
    
    if isEffect or isUnusedGems:
        Effects(gemFile, gemMSFile, gemHelpMSFile)
    
    
    for gem in gemFile.rows:
        if isNotCapped:
            if gem["rvs_status"] not in [146, 45]:
                gem["max"] = int(gem["max"] * random.choice([0.2,0.4,0.6,0.8,1.2,1.4,1.6,1.8,2.2,3,3,4]))
        if isFreeEquip:
            gem["attach"] = 0                # 0 Equip to anything                # 1 Equip to weapon                # 2 Equip to armor
        if isPower:
            RankPower(gem, ranks)
            
    
    if isPower or isEffect or isUnusedGems:
        ItemPower(gemFile.rows, ranks)
                    
    GemList.clear() # Clear the global list
                
    gemFile.Close()
    gemMSFile.Close()
    gemHelpMSFile.Close()


    
def Effects(gemData:JSONParser.File, gemMSData:JSONParser.File, gemHelpMSData:JSONParser.File):
    
    # Number of gems that the game will allow in a single file
    maxGems = 98
    
    # Keep track of what ids to put things in
    idCount = 1
    skillMSCount = 1
    
    # Clear for repopulation
    gemData.rows.clear()
    gemMSData.rows.clear()
    gemHelpMSData.rows.clear()
    
    isQuickstepIn = False
    # Loop and generate our new gems
    for i in range(maxGems):
    
        if len(GemList) == 0: 
            break
        
        gem = random.choice(GemList)
        
        if not isQuickstepIn:
            for rangem in GemList: # Ensure that quickstep is always in the gems list for the QOL option
                if rangem.status == 3:
                    isQuickstepIn = True
                    gem = rangem
                    break
        
        GemList.remove(gem)
        
        incr = max(int((gem.power[-1] - gem.power[0])/12),1)
        pPowIncr = int(gem.pPower[-1]/6)
        
        gemData.rows.append(
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
        
        gemMSData.rows.extend(
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
        
        gemHelpMSData.rows.append(
            {
            "$id": idCount,
            "style": 117,
            "name": gem.menuCaption
            },
        )
        
        idCount += 1
        skillMSCount += 3
        
    CrystalFix(len(gemData.rows))

def CrystalFix(gemLength): # 
    '''Because the gems list is recreated references to the vanilla IDs can be too high for the new valid list this goes through and edits crystals that have values outside the current population of skills'''
    with open("XCDE/JsonOutputs/bdat_common/ITM_dropcrystallist.json", 'r+', encoding='utf-8') as crystalFile: 
        cryData = json.load(crystalFile)
        for crystal in cryData["rows"]:
            for i in range(1,3):
                if crystal[f"skill{i}"] > gemLength:
                    crystal[f"skill{i}"] = random.randrange(1, gemLength+1)
        JSONParser.CloseFile(cryData, crystalFile)
    
    futureConnectedAreas = [2501]
    for area in IDs.areaFileListNumbers:
        
        if area in futureConnectedAreas: # FC uses diffferent names and slightly different implementation
            name = "gemMineList"
            gemrange = 9
        else:
            name = "minelist"
            gemrange = 5
            
        areaMineFile = JSONParser.File(f"XCDE/JsonOutputs/bdat_ma{area}/{name}{area}.json")
        if not areaMineFile.isOpen: continue
        for mine in areaMineFile.rows:
            for i in range(1,gemrange):
                if mine[f"skill{i}"] > gemLength:
                    mine[f"skill{i}"] = random.randrange(1, gemLength+1)
        areaMineFile.Close()
    
    
            
def RankPower(gem, ranks):
    statR = StatRand.Stat(3, 100)
    mult = statR.RollBalancedMult()
    for r in ranks:
        statR.ApplyMult(gem, f"lower_{r}", mult, 253, 1)
        statR.ApplyMult(gem, f"upper_{r}", mult, 255, 1)
        
def ItemPower(gemData, ranks):
    '''Balances premade gems given thorughout the story for their level and new effect'''
    gemType = 3
    with open("./XCDE/JsonOutputs/bdat_common/ITM_itemlist.json", 'r+', encoding='utf-8') as gemItemFile: 
        gemItemData = json.load(gemItemFile)
        for gem in gemItemData["rows"]:
            if gem["itemType"] != gemType: continue
            rank = gem["rankType"]
            newGem = random.choice(gemData)
            gem["itemID"] = newGem["$id"]
            newMin = newGem[f"lower_{ranks[rank-1]}"]
            newMax = newGem[f"upper_{ranks[rank-1]}"]
            if newMin == newMax:
                newVal = newMin
            else:
                newVal = random.randrange(newMin, newMax)
            gem["percent"] = min(newVal, 255)
        JSONParser.CloseFile(gemItemData, gemItemFile)

def GemDescriptions():
    GemDescription = PopupDescriptions.Description()
    GemDescription.Header(Options.GemOption_Power.name)
    GemDescription.Text("This randomizes the power level of crafted and premade gems.")
    GemDescription.Header(f"{Options.GemOption_Effect.name}/{Options.GemOption_Unused.name}")
    GemDescription.Text("This randomizes what each gems effect is. Essentially shuffling the gems. Armors or weapons with unique gems will be randomized as well as any gems given throughout the story, this will also affect crystals.")
    GemDescription.Text("Unused effects will add gems that don't exist in the vanilla game. For example, cooldown reduction gems, or gems infused with monado enchant.")
    GemDescription.Image("crazygems.png", "XCDE", 800)
    GemDescription.Header(Options.GemOption_FreeEquip.name)
    GemDescription.Text("This allows any gem to be equipped to weapons and armor.")
    GemDescription.Image("GemsFreeEquipped.png","XCDE", 500)
    GemDescription.Text("Double Attack on armor and HP Up on weapons.", anchor="center")
    GemDescription.Header(Options.GemOption_NoCap.name)
    GemDescription.Text("This randomizes the % and regular cap for all gems when you equip them.")
    GemDescription.Image("GemCap.png","XCDE", 500)
    GemDescription.Text("Double Attack and Haste above their vanilla 50% cap.", anchor="center")
    return GemDescription