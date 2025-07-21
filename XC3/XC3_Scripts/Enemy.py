
import json, random, copy, traceback, math
from XC3.XC3_Scripts import IDs
from XC2.XC2_Scripts import Enemy
from scripts import Helper, JSONParser, PopupDescriptions

# https://xenobladedata.github.io/xb3_130/SYS_GimmickLocation.html#25513 useful file has enemy xyz and probably how fights dteremine where try again places you

# To fix:         
# Too many agnus/keves soldier enemies dillutes the pool of intereszting enemies         
# Keves Queen is unkillable (its not the NoKill (its named slightly different) Flag on enemy)    

NormalGroup = Enemy.EnemyGroup()
UniqueGroup = Enemy.EnemyGroup()
BossGroup = Enemy.EnemyGroup()
SuperbossGroup = Enemy.EnemyGroup()
StaticEnemyData = [NormalGroup, UniqueGroup, BossGroup, SuperbossGroup]
                                                                                                                                                                                                                                                                                                                
def Enemies(targetGroup, isNormal, isUnique, isBoss, isSuperboss, mainOption):
    with open("XC3/JsonOutputs/fld/FLD_EnemyData.json", 'r+', encoding='utf-8') as eneFile:
    
        eneData = json.load(eneFile)
        
        firstGen = Enemy.GenEnemyData(eneData, IDs.NormalMonsters, IDs.UniqueMonsters, IDs.BossMonsters, IDs.SuperbossMonsters)
        
        ignoreKeys = ["$id", "ID", "Level", "Scale", "EliteScale", "IdMove", "IdDropPrecious", "FlgLevAttack", "FlgLevBattleOff", "FlgDmgFloor", "FlgNoVanish", "FlgSerious", "<3CEBD0A4>", "FlgKeepSword", "FlgColonyReleased", "GetRatio", "GetEnArts", "GetEnSkill", "FlgNoDead", "FlgNoTarget", "ExpRate", "GoldRate", "FlgNoFalling"]
        Enemy.RandomAssignment(eneData, targetGroup, Enemy.GenWeights(isNormal, isUnique, isBoss, isSuperboss), mainOption, ignoreKeys, "XC3/JsonOutputs/btl/BTL_Enemy.json", "XC3/JsonOutputs/btl/BTL_EnRsc.json" )

        if firstGen:
            Bandaids(eneData)
        
        JSONParser.CloseFile(eneData, eneFile)

def Bandaids(eneData):
    pass
    
def EnemyDesc(name):
    pass