import json, random, Options

TalentArts = [102,101,100,44,99,43,98,42,62,97,154,1,2,19,36,41,61,79,96,119,120,121,122,123,124,125,126,127,153,171,152] # Need to shuffle these seperately for various reasons
DLCArts = [155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187]
GuestArts = [144,145,146,147,148,149]
PonspectorDLCArts = [188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254]
ShulkMonadoArts = [3,4,5,6,7,8,9,10]
DunbanMonadoArts = [150,151]
MeliaSummons = [113,103,109,112,104,105,111]

class ArtGroup:
    def __init__(self, _group):
        self.group = _group
        ArtGroups.append(self)
    def chooseChar(self):
        self.chosenChar = random.choice(CharacterList)
ArtGroups:list[ArtGroup] = []
GaleSlashGroup = ArtGroup([45,46,48,54])
StarlightKickGroup = ArtGroup([115,107])


# Setting that just shuffles arts
def RandomizePcArts():
    keepMeliaSummons = Options.PlayerArtsOption_Summons.GetState()
    earlyArts = Options.PlayerArtsOption_EarlyArtsUnlock.GetState()
    cooldowns = Options.PlayerArtsOption_Cooldown.GetState()
    isArtGroups = Options.PlayerArtsOption_ArtGroups.GetState()
    isGuestArts = Options.PlayerArtsOption_GuestArts.GetState()
    
    for group in ArtGroups:
        group.chooseChar()
    invalidArtIds = TalentArts + DunbanMonadoArts + ShulkMonadoArts + PonspectorDLCArts + DLCArts
    
    if not isGuestArts:
        invalidArtIds.extend(GuestArts)
        
    if keepMeliaSummons:
        invalidArtIds.extend(MeliaSummons)
        
    with open("./XCDE/_internal/JsonOutputs/bdat_common/pc_arts.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        for art in artData["rows"]:
            
            id = art["$id"]
            if id in invalidArtIds: # Ignores invalid/ weird arts
                continue
            
            DetermineArtType(art, random.choice(CharacterList)) # Random choice
            
            if art["pc"] == SharlaActs.pcID: # Ensures sharlas arts still increment the cooldown talent art
                art["tp"] = random.randrange(-25,-1)
            elif art["tp"] < 0: # If sdharlas arts go on someone else it shouldnt buff their talent gauge
                art["tp"] = 0
                
            if isArtGroups:
                for artGroup in ArtGroups: # Ensures grouped arts stay grouped
                    if id in artGroup.group:
                        DetermineArtType(art, artGroup.chosenChar)
                        break
                
            if cooldowns:
                Cooldown(art)
                
            if earlyArts: # Early arts option
                art["get_lv"] = 0
                
        artFile.seek(0)
        artFile.truncate()
        json.dump(artData, artFile, indent=2, ensure_ascii=False)
        
# Setting to make arts all cost tp instead of having cooldowns basically auto attack recharging arts
# Setting to tie arts to weapon https://xenobladedata.github.io/xb1de/bdat/bdat_common/ITM_wpnlist.html#137 
# Setting that randomizes effects of arts

# Summon Flare had War Swing for reyn
# Sharlas talent art is imporved since other char arts dont increase it
# Melias conditional arts are strong because they ignore the condition when not on melia
class ActMatch: # A class so that when arts get randomized their animation somewhat matches their effects by changing pc_arts act_idx
    def __init__(self, _pcID, _SingleAttack, _AOEAttack, _Buff):
        self.pcID = _pcID
        self.SingleAttack = _SingleAttack
        self.AOEAttack = _AOEAttack
        self.Buff = _Buff
        CharacterList.append(self)
CharacterList:list[ActMatch] = []

def BalanceArtUnlockLevels():
    with open("./XCDE/_internal/JsonOutputs/bdat_common/pc_arts.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        for i in range(1,9): # Loop through the characters
            unlockLv = 0 # Starting level to unlock arts
            stepLv = [1,2,3,4] # How many levels for the next unlock 
            for art in artData["rows"]:
                if art["pc"] == i: # Find arts for a character
                    art["get_lv"] = unlockLv
                    unlockLv += random.choice(stepLv)
                    print(unlockLv)

            
        artFile.seek(0)
        artFile.truncate()
        json.dump(artData, artFile, indent=2, ensure_ascii=False)
    

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

def Cooldown(art): # Controls how hard arts are to recharge
    Cooldown = random.randrange(10,60)
    CooldownStep = Cooldown//random.randrange(5,10)
    art["recast"] = Cooldown
    art["glow_recast"]= CooldownStep

def Damage():
    pass

def TargetType():
    types= {
        "Single": 1,
        "Self": 2,
        "Ally": 3
        
    }
    rangeType={
        "Party": 7
    }
    pass

def Effect(): # st_type status type
    pass

   
# Loop through the file and create a list of the attacks and their names for easy handling usese act_idx NOT IDS
ShulkActs = ActMatch(1, _SingleAttack=[1,0,4,8,9,11,12],_AOEAttack=[5,7,15],_Buff=[3,2,6,10,13,14])
ReynActs = ActMatch(2, _SingleAttack=[0,1,4,6,11,12],_AOEAttack=[3,13,15],_Buff=[0,2,3,5,7,8,9,10,14])
FioraActs = ActMatch(3,  _SingleAttack=[3,2,1,0],_AOEAttack=[3,2,1,0],_Buff=[3,2,1,0])
DunbanActs = ActMatch(4,  _SingleAttack=[0,1,3,5,9,14],_AOEAttack=[12,13,14],_Buff=[2,4,6,7,8,10,11,15])
SharlaActs = ActMatch(5,  _SingleAttack=[0,1,7,11,14],_AOEAttack=[6,8,15],_Buff=[0,2,3,4,5,6,9,10,12,13])
RikiActs = ActMatch(6,  _SingleAttack=[1,2,6,11,12,14,15],_AOEAttack=[0,4,6,7,9,10,13,15],_Buff=[0,3,5,8,10,13])
MeliaActs = ActMatch(7,  _SingleAttack=[4,12],_AOEAttack=[5,14,15],_Buff=[0,1,2,3,6,7,8,9,10,11,13])
SevenActs = ActMatch(8,  _SingleAttack=[0,2,3,10,11],_AOEAttack=[5,7,8,9,12,15],_Buff=[1,4,6,13,14])
# DunbanActs = ActMatch(9,  _SingleAttack=[],_AOEAttack=[],_Buff=[])
# art["arts_type"] = 1 This just make the art activate your talent art
