
import json, random, copy, traceback, math
from XC3.XC3_Scripts import IDs, Options
from scripts import Helper, JSONParser, PopupDescriptions, Enemies as Enemy

# https://xenobladedata.github.io/xb3_130/SYS_GimmickLocation.html#25513 useful file has enemy xyz and probably how fights dteremine where try again places you

# To fix:         
# Too many agnus/keves soldier enemies dillutes the pool of intereszting enemies         
# Keves Queen is unkillable (its not the NoKill (its named slightly different) Flag on enemy)    

StaticEnemyData:list[Enemy.EnemyGroup] = []

                                                                                                                                                                                                                                                                                                                
def Enemies(targetGroup, isNormal, isUnique, isBoss, isSuperboss, isEnemies):
    global StaticEnemyData
    GroupFightViolations = GetGroupFightViolations()
    GroupFightIDs = GetGroupFightIDs()
    RetryBattleLandmark = "<9A220E4D>"
    ignoreKeys = ["$id", "ID", "Level", "Scale", "EliteScale", "IdMove", "IdDropPrecious", "FlgLevAttack", "FlgLevBattleOff", "FlgDmgFloor", "IdMove", "FlgNoVanish", "FlgSerious", RetryBattleLandmark, "<3CEBD0A4>", "<C6717CFE>", "FlgKeepSword", "FlgColonyReleased", "FlgNoDead", "FlgNoTarget", "ExpRate", "GoldRate", "FlgNoFalling"]
    actKeys = ["ActType", "FlyHeight", "SwimHeight"]
    with open("XC3/JsonOutputs/fld/FLD_EnemyData.json", 'r+', encoding='utf-8') as eneFile:
        with open("XC3/JsonOutputs/btl/BTL_Enemy.json", 'r+', encoding='utf-8') as paramFile:
            with open("XC3/JsonOutputs/btl/BTL_EnRsc.json", 'r+', encoding='utf-8') as rscFile:
                paramData = json.load(paramFile)
                rscData = json.load(rscFile)
                eneData = json.load(eneFile)
                
                eRando = Enemy.EnemyRandomizer(IDs.NormalMonsters, IDs.UniqueMonsters, IDs.BossMonsters, IDs.SuperbossMonsters, isEnemies, isNormal, isUnique, isBoss, isSuperboss, "Resource", "IdBattleEnemy", eneData, paramData, rscData, actKeys=actKeys)
                
                if StaticEnemyData == []:
                    StaticEnemyData = eRando.GenEnemyData()
                
                for en in eneData["rows"]:
                    if eRando.FilterEnemies(en, targetGroup):
                        continue 
                    
                    newEn = eRando.CreateRandomEnemy(StaticEnemyData)
                
                    eRando.ActTypeFix(newEn, en)
                    
                    if Options.BossEnemyOption_GroupFights.GetState():
                        eRando.BalanceFight(en, newEn, GroupFightIDs, GroupFightViolations)
                        
                    EnemySizeHelper(en, newEn, eRando)
                    
                    eRando.CopyKeys(en, newEn, ignoreKeys)
                        
                for group in StaticEnemyData:
                    group.RefreshCurrentGroup()
                
                Bandaids(isBoss, eRando)
                
                JSONParser.CloseFile(eneData, eneFile)
                JSONParser.CloseFile(paramData, paramFile)
                JSONParser.CloseFile(rscData, rscFile)

def EnemySizeHelper(oldEn, newEn, eRando:Enemy.EnemyRandomizer):
    Massive = 3
    Large = 2
    Normal = 1
    Small = 0
    
    multDict = {
        (Massive, Large): 3,
        (Massive, Normal): 6,
        (Massive, Small): 9,
        (Large, Normal): 3,
        (Large, Small): 4,
        (Normal, Small): 1.5,
    }
    keys = ["Scale", "EliteScale", "WeaponScale"]
    eRando.EnemySizeMatch(oldEn, newEn, keys, multDict)

def GetGroupFightViolations():
    return []

def GetGroupFightIDs():
    return []

def IntroFightBalances(eRando:Enemy.EnemyRandomizer):
    introFights = [449, 450, 451, 452, 453, 454, 455]
    bossIntroFights = [456]
    eRando.ChangeStats(introFights, [("StRevHp", 5)])
    eRando.ChangeStats(bossIntroFights, [("StRevHp", 10)])

def Bandaids(isBoss, eRando):
    IntroFightBalances(eRando)
    
def EnemyDesc(name):
    pass