import json, random

TalentArts = [] # Need to shuffle these seperately for various reasons


def RandomizePcArts():
    with open("./XCDE/_internal/JsonOutputs/bdat_common/pc_arts.json", 'r+', encoding='utf-8') as artFile:
        artData = json.load(artFile)
        for art in artData["rows"]:
            # art["pc"] = random.randrange(1,9)
            
            art["recast"] = 1
            art["tp"] = 100
            # art["arts_type"] = 1 This just make the art activate your talent art
        artFile.seek(0)
        artFile.truncate()
        json.dump(artData, artFile, indent=2, ensure_ascii=False)
        
# Setting to make arts all cost tp instead of having cooldowns basically auto attack recharging arts
# Setting to tie arts to weapon https://xenobladedata.github.io/xb1de/bdat/bdat_common/ITM_wpnlist.html#137 
# Setting that just shuffles arts
# Setting that randomizes effects of arts


class ActMatch: # A class so that when arts get randomized their animation somewhat matches their effects by changing pc_arts act_idx
    def __init__(self, _pcID, _SingleAttack, _AOEAttack, _Buff):
        self.pcID = _pcID
        self.SingleAttack = _SingleAttack
        self.AOEAttack = _AOEAttack
        self.Buff = _Buff
        
def RechargeType(): # Controls how arts recharge
    pass

def Cooldown(art): # Controls how hard arts are to recharge
    art[""]
    pass

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

   
# Loop through the file and create a list of the attacks and their names for easy handling
ShulkActs = ActMatch(1, _SingleAttack=[1,0,4,8,9,10,11,12],_AOEAttack=[5,7,13,15],_Buff=[3,2,6,7,10,13,14])
ReynActs = ActMatch(2, _SingleAttack=[0,1,4,6,11,12],_AOEAttack=[3,13,15],_Buff=[0,2,3,5,7,8,9,10,14])
FioraActs = ActMatch(3,  _SingleAttack=[3,2,1,0],_AOEAttack=[3,2,1,0],_Buff=[3,2,1,0])
DunbanActs = ActMatch(4,  _SingleAttack=[0,1,3,5,9,14],_AOEAttack=[2,12,13,14],_Buff=[2,4,6,7,8,10,11,15])
SharlaActs = ActMatch(5,  _SingleAttack=[0,1,7,11,14],_AOEAttack=[6,8,15],_Buff=[0,2,3,4,5,6,9,10,12,13])
RikiActs = ActMatch(6,  _SingleAttack=[],_AOEAttack=[],_Buff=[])
MeliaActs = ActMatch(7,  _SingleAttack=[],_AOEAttack=[],_Buff=[])
SevenActs = ActMatch(8,  _SingleAttack=[],_AOEAttack=[],_Buff=[])
# DunbanActs = ActMatch(9,  _SingleAttack=[],_AOEAttack=[],_Buff=[])
