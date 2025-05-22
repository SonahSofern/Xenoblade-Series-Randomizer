import json, random, Options
import scripts.JSONParser
import scripts.PopupDescriptions 
TalentArts = [102,101,100,44,99,43,98,42,62,97,154,1,2,19,36,41,61,79,96,119,120,121,122,123,124,125,126,127,153,171,152] # Need to shuffle these seperately for various reasons
DLCArts = [155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187]
GuestArts = [144,145,146,147,148,149]
PonspectorDLCArts = [188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254]
ShulkMonadoArts = [3,4,5,6,7,8,9,10]
DunbanMonadoArts = [150,151]
MeliaSummonsNames = [205, 207, 209, 217, 221, 223, 225, 231]
ReynGuardShift = [22] # Wont work on other characters

# Setting to make arts all cost tp instead of having cooldowns basically auto attack recharging arts
# Setting to tie arts to weapon https://xenobladedata.github.io/xb1de/bdat/bdat_common/ITM_wpnlist.html#137 
# Setting that randomizes effects of arts

class ActMatch: # A class so that when arts get randomized their animation somewhat matches their effects by changing pc_arts act_idx
    def __init__(self, _pcID, _SingleAttack, _AOEAttack, _Buff, startLv = 1, weight = 0):
        self.pcID = _pcID
        self.SingleAttack = _SingleAttack
        self.AOEAttack = _AOEAttack
        self.Buff = _Buff
        self.startLv = startLv
        self.weight = weight
        CharacterList.append(self)
        
CharacterList:list[ActMatch] = []


ShulkActs = ActMatch(1, _SingleAttack=[0,4,8,9,11,12],_AOEAttack=[5,7,15],_Buff=[1,3,2,6,10,13,14], weight=15)
ReynActs = ActMatch(2, _SingleAttack=[0,1,4,6,11,12],_AOEAttack=[3,13,15],_Buff=[0,2,5,7,8,9,10,14], weight=15)
FioraActs = ActMatch(3,  _SingleAttack=[3,2,1,0],_AOEAttack=[3,2,1,0],_Buff=[3,2,1,0], weight = 3)
DunbanActs = ActMatch(4,  _SingleAttack=[0,1,3,5,9,14],_AOEAttack=[12,13,14],_Buff=[2,4,6,7,8,10,11,15], startLv=20, weight= 15)
SharlaActs = ActMatch(5,  _SingleAttack=[0,1,7,11,14],_AOEAttack=[6,8,15],_Buff=[0,2,3,4,5,6,9,10,12,13], startLv=10, weight= 15)
RikiActs = ActMatch(6,  _SingleAttack=[1,2,6,11,12,14,15],_AOEAttack=[0,4,6,7,9,10,13,15],_Buff=[0,3,5,8,10,13], startLv=22, weight=15)
MeliaActs = ActMatch(7,  _SingleAttack=[4,12],_AOEAttack=[5,14,15],_Buff=[0,1,2,3,6,7,8,9,10,11,13], startLv=23, weight=15)
SevenActs = ActMatch(8,  _SingleAttack=[0,2,3,10,11],_AOEAttack=[5,7,8,9,12,15],_Buff=[1,4,6,13,14], startLv=40, weight= 15)
KinoActs = ActMatch(14,[0],[0],[0])
NeneActs = ActMatch(15,[0],[0],[0])

# Groups for the option to keep arts together
class ArtGroup:
    def __init__(self, _group):
        self.group = _group # Group of name iDS
        ArtGroups.append(self)
    def chooseChar(self, charList):
        self.chosenChar = random.choice(charList)
        
ArtGroups:list[ArtGroup] = []
GaleSlashGroup = ArtGroup([107,91,89,95])
StarlightKickGroup = ArtGroup([229,213])

def namePrint(artList):
    with open("./XCDE/_internal/JsonOutputs/bdat_common/pc_arts.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        nameList = []
        for art in artData["rows"]:
            if art["$id"] in artList:
                nameList.append(art["name"])
        print(nameList)

def RemakeArtList():    
    with open("./XCDE/_internal/JsonOutputs/bdat_common/pc_arts.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        # isDupes = Options.PlayerArtsOption_Duplicates.GetState()
        artList = []
        keyList = ["name", "pc", "cast", "recast", "tp", "dex", "rate1", "rate2", "arts_type", "atk_type", "chain_type", "elem", "dmg_type", "dmg_time", "tgt", "range_type", "range", "range_val", "hate", "flag", "st_type", "st_val", "st_val2", "st_time", "st_itv", "sp_cnd", "sp_proc", "sp_val1", "sp_val2", "kb_type", "kb_lv", "grow_powl", "grow_powh", "grow_st_time", "grow_st_val", "glow_recast", "icon", "icon_base", "act_idx", "idx", "list_idx", "get_type", "get_lv", "melia_lv", "melia_slot_idx", "help"]
        
        badReplacementArts = PonspectorDLCArts + GuestArts + DunbanMonadoArts + TalentArts + DLCArts
        for art in artData["rows"]: # Build our list
            if art["$id"] in badReplacementArts:
                continue
            artList.append(art)
        
        badReplacedArts =  PonspectorDLCArts + GuestArts + DunbanMonadoArts + TalentArts + DLCArts
        for art in artData["rows"]: # Replace the old list with random choices from the new list
            if art["$id"] in badReplacedArts:
                continue
            
            newArt = random.choice(artList) # Choose a new art for that slot
            # if isDupes:
            #     artList.remove(newArt)
            
            for key in keyList: # Replace everything
                art[key] = newArt[key]
        scripts.JSONParser.CloseFile(artData, artFile)
        
        
        # Edit the new data

# Setting that just shuffles arts
def RandomizePcArts():
    # RemakeArtList()
    
    keepMeliaSummons = Options.PlayerArtsOption_Summons.GetState()
    isBalancedLv = Options.PlayerArtsOption_BalancedUnlockLevels.GetState()
    isArtGroups = Options.PlayerArtsOption_ArtGroups.GetState()
    
    charList = CharacterList.copy()
    charWeights = []
    
    if keepMeliaSummons: # If melia keeps her summons we should reduce her weights a bit
        MeliaActs.weight = 5
    else:
        MeliaActs.weight = 15
    
    for chr in charList: # Create the weights list
        charWeights.append(chr.weight)
    
    
    # Dole out the special art groups
    for group in ArtGroups:
        group.chooseChar(charList)
    invalidArtIds = TalentArts + DunbanMonadoArts + ShulkMonadoArts + PonspectorDLCArts + DLCArts + GuestArts
    
        
    with open("./XCDE/_internal/JsonOutputs/bdat_common/pc_arts.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        for art in artData["rows"]:
    
            if art["$id"] in invalidArtIds: # Ignores invalid/ weird arts
                continue
            
            if keepMeliaSummons and (art["name"] in MeliaSummonsNames): # Dont change the melias summons if we want her to keep em
                continue
            
            # Choose a character if they have reached their max arts remove them
            char = random.choices(charList,charWeights,k=1)[0]

            
            DetermineArtType(art, char) # Random choice
            FixSharlasNewArts(art)
            ArtGroupManager(isArtGroups, art)


        if isBalancedLv:
            BalanceArtUnlockLevels(artData)
        
        MatchArtBooks(artData)
        scripts.JSONParser.CloseFile(artData, artFile)
        

def ArtGroupManager(isArtGroups, art):
    if isArtGroups:
        for artGroup in ArtGroups: # Ensures theres exists one set of grouped arts staying grouped
            if art["name"] in artGroup.group:
                DetermineArtType(art, artGroup.chosenChar)
                break

def FixSharlasNewArts(art): # Fixes the talent gauge working with her new arts
    if art["pc"] in [SharlaActs.pcID, KinoActs.pcID]: # Ensures former healer's new arts still increment the cooldown talent art
        art["tp"] = random.randrange(-25,-1)
    elif art["tp"] < 0: # If healer arts go on someone else it shouldnt buff their talent gauge
        art["tp"] = 0

def BalanceArtUnlockLevels(artData):
    for char in CharacterList: # Loop through the characters
        unlockLv = char.startLv - 3 # Starting level to unlock arts
        stepLv = [2,3,4,5,6] # How many levels for the next unlock 
        for art in artData["rows"]:
            # print(unlockLv)
            if art["$id"] in ShulkMonadoArts + TalentArts + DunbanMonadoArts + PonspectorDLCArts + DLCArts:
                continue
            if art["pc"] == char.pcID: # Find arts for a character
                getlv = min(max(unlockLv,0),80) # Max to frontload the arts a little bit so you get them early
                if char.pcID == 3:
                    print(f"ID: {art["$id"]} Lv: {getlv}")
                art["get_lv"] = getlv
                art["get_type"] = 1
                unlockLv += random.choice(stepLv)

# Fixes art books
def MatchArtBooks(artData):
    with open("./XCDE/_internal/JsonOutputs/bdat_common/ITM_artslist.json", 'r+', encoding='utf-8') as artBookFile:
        artBookData = json.load(artBookFile)
        for book in artBookData["rows"]:
            for art in artData["rows"]:
                if art["$id"] == book["get_arts"]:
                    book["pc_type"] = art["pc"]
                    break
                
def DetermineArtType(art, char:ActMatch):
    if art["pc"] == char.pcID: # If they get a vanilla art dont change the act no
        return
    
    art["pc"] = char.pcID
    
    if art["tgt"] in [2,3] or art["atk_type"] in [3]:
        art["act_idx"] = random.choice(char.Buff)
    elif art["range_type"] == 0:
        art["act_idx"] = random.choice(char.SingleAttack)
    else:
        art["act_idx"] = random.choice(char.AOEAttack)      
        
CooldownStartRange = (10,60)
CooldownStepRange = (5,10)
def Cooldown(art): # Controls how hard arts are to recharge
    Cooldown = random.randrange(CooldownStartRange[0],CooldownStartRange[1])
    CooldownStep = Cooldown//random.randrange(CooldownStepRange[0],CooldownStepRange[1])
    art["recast"] = Cooldown
    art["glow_recast"]= CooldownStep

def ArtsDescriptions():
    ArtDesc = scripts.PopupDescriptions.Description()
    ArtDesc.Header(Options.PlayerArtsOption_BalancedUnlockLevels.name)
    ArtDesc.Text("Ensures that your arts unlock consistently as your level up.\nOtherwise your might get really high levels arts and be stuck with nothing for most of the game.\nOn average your will unlock a new art every 2-3 levels.")
    ArtDesc.Header(Options.PlayerArtsOption_ArtGroups.name)
    ArtDesc.Text("Keep arts that have combos randomized to the same character.")
    ArtDesc.Tag("Gale Slash, Worldly Slash, Electric Gutbuster, Tempest Kick", pady=3, anchor="center")
    ArtDesc.Tag("Spear Break, Starlight Kick", pady=3, anchor="center")
    ArtDesc.Header(Options.PlayerArtsOption_Summons.name)
    ArtDesc.Text("Keeps Melia's summon arts on her, so that her talent art is not useless.")
    ArtDesc.Tag("Summon Wind, Summon Earth, Summon Ice, Summon Aqua, Summon Flare, Summon Bolt, Summon Copy and Power Effect", pady=3, anchor="center")
    # ArtDesc.Header(Options.PlayerArtsOption_Cooldown.name)
    # ArtDesc.Text(f"Chooses a random cooldown between {CooldownStartRange[0]}-{CooldownStartRange[1]}s then each level up reduces that cooldown by the original cooldown / {CooldownStepRange[0]}-{CooldownStepRange[1]}")
    return ArtDesc