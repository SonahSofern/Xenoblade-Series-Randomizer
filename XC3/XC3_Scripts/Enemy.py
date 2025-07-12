
import json, random, copy, traceback, math
from scripts import Helper, JSONParser, PopupDescriptions

# def Enemies():
#     with open(f"XC3/JsonOutputs/btl/BTL_Enemy.json", 'r+', encoding='utf-8') as eneFile: # This file swap method doesnt swap names is probably not better
       
# To fix: 
# Water Enemies instantly dying on land
# Land Enemies falling beneath water
# Land enemies falling in the sky          
# Too many agnus/keves soldier enemies dillutes the pool of intereszting enemies                                                                                                                                                                                                                                                                                                                                          
def Enemies():
    with open(f"XC3/JsonOutputs/fld/FLD_EnemyData.json", 'r+', encoding='utf-8') as eneFile:
        eneData = json.load(eneFile)
        enGroup = []
        ignoreKeys = ["$id", "ID", "Level", "IdMove", "NamedFlag", "IdDropPrecious", "FlgKeepSword", "FlgNoVanish", "FlgDmgFloor", "FlgMoveFloor", "FlgLevAttack", "FlgLevBattleOff", "FlgFixed", "FlgColonyReleased", "FlgNoDead", "FlgNoTarget", "FlgNoFalling"]
        # Make keys list
        keysList = []
        testList = []
        for en in eneData["rows"]:

            for key in en.keys():
                if key in ignoreKeys:
                    continue
                keysList.append(key)
            break
            
        for en in eneData["rows"]:
            if en["FlgSerious"] == 1:
                testList.append(en["$id"])
            enGroup.append(en.copy())
        print(testList)
        for en in eneData["rows"]:
            newEn = random.choice(enGroup)
            enGroup.remove(newEn)
            for key in keysList:
                en[key] = newEn[key]
        JSONParser.CloseFile(eneData, eneFile)
        
   
# https://xenobladedata.github.io/xb3_130/SYS_GimmickLocation.html#25513 useful file has enemy xyz and probably how fights dteremine where try again places you
