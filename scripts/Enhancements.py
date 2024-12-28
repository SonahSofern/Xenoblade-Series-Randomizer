import JSONParser, Helper, random

EnhanceEffectsList = []
class EnhanceEff:
    def __init__(self, ID, Enhancement, Param1, Param2, Caption):
        EnhanceEffectsDict = {
            "$id": ID,
            "EnhanceEffect": Enhancement,
            "Param1": random.randrange(Param1[0],Param1[1]),
            "Param2": random.randrange(Param2[0], Param2[1]),
            "Caption": Caption,
            "Caption2": Caption
        }
        EnhanceEffectsList.append([EnhanceEffectsDict])

  


def IncreaseEffectCaps(NewCap):
    JSONParser.ChangeJSONFile(["common/BTL_EnhanceEff.json"],["Param"], [Helper.InclRange(1,1000)], [NewCap])
    
    
def CreateEnhanceObjects():
    if len(EnhanceEffectsList) == 0:
        CombatMovementSpeed = EnhanceEff(3896 , 211, [1500,1501], [0,1], 309)

def StandardEnhanceRun():
    IncreaseEffectCaps(100000)
    CreateEnhanceObjects()
    JSONParser.ExtendJSONFile("common/BTL_Enhance.json",  EnhanceEffectsList)