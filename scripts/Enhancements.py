import JSONParser, Helper, random

EnhanceEffectsList = []
class EnhanceEff:
    def __init__(self, ID, Enhancement, Param1, Param2, Caption):
        if Param1 == []:
            Param1Val = 0
        else:
            Param1Val = random.randrange(Param1[0],Param1[1])
            
        if Param2 == []:
            Param2Val = 0
        else:
            Param2Val = random.randrange(Param2[0], Param2[1])    
        
        EnhanceEffectsDict = {
            "$id": ID,
            "EnhanceEffect": Enhancement,
            "Param1":  Param1Val,
            "Param2": Param2Val,
            "Caption": Caption,
            "Caption2": Caption
        }
        EnhanceEffectsList.append([EnhanceEffectsDict])

  


def IncreaseEffectCaps(NewCap):
    JSONParser.ChangeJSONFile(["common/BTL_EnhanceEff.json"],["Param"], [Helper.InclRange(1,1000)], [NewCap])
    
    
def CreateEnhanceObjects():     # update the ids when i make more they only go to 4000
    if len(EnhanceEffectsList) == 0:
        CombatMovementSpeed = EnhanceEff(3896 , 211, [40,500], [], 309)
        HPBoost = EnhanceEff(3897, 1, [1,100], [], 1)
        
        

def StandardEnhanceRun():
    IncreaseEffectCaps(100000)
    CreateEnhanceObjects()
    JSONParser.ExtendJSONFile("common/BTL_Enhance.json",  EnhanceEffectsList)
    
    
